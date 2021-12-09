from odoo import models, fields, api
from datetime import timedelta
import requests

class FoodOrder(models.Model):
    _name = "food.order"
    _description = "Food order table"

    customer_id = fields.Many2one("customer", string="Customer")
    employee_id = fields.Many2one("hr.employee", string="Delivery Rider")
    delivery_duration = fields.Integer(compute="_gmaps_api", string="Delivery Duration" , store=True) 
    delivery_address = fields.Text(string="Customer Address", compute="_allocate_address")
    status = fields.Many2one("order.status")
    payment_type = fields.Selection(
        required = True,
        selection = [
            ('cash_on_delivery', 'Cash on Delivery')
        ]
    )
    line_item = fields.One2many("line.item", "order_id", store = True)
    time_placed = fields.Datetime( string="Order Date/Time" ,required = True, default= fields.Datetime.add(fields.Datetime.now()))
    time_delivered = fields.Datetime()
    estimated_delivery_time = fields.Integer(compute="_estimare_delivery_time", string="Estimated Order Duration (in minutes)")
    estimated_delivery_distance = fields.Integer(string="Delivery Distance", compute="_estimate_delivery_distance")
    delivery_fees = fields.Float(compute = "_calculate_delivery_fees")
    total_price = fields.Float(compute = "_calculate_total_price", store=True)
    expected_delivery_time = fields.Datetime(required = True, compute="_calculate_delivery_time")
    
    @api.depends('customer_id')
    def _allocate_address(self):
        for record in self:
            record.delivery_address = self.customer_id.address

    @api.depends('line_item','time_placed','delivery_duration')
    def _calculate_delivery_time(self):
        for record in self:
            time = 0
            for product in self.line_item:
                time = time + (product.name.preparation_time)
            record.expected_delivery_time = self.time_placed + timedelta(minutes=time) + timedelta(minutes=self.delivery_duration)

    @api.depends('line_item','time_placed','delivery_duration')
    def _estimare_delivery_time(self):
        for record in self:
            time = 0
            max_time = 40
            base_time = 10
            for product in self.line_item:
                time = time + (product.name.preparation_time)
            if(time > max_time):
                time = max_time
            record.estimated_delivery_time = base_time + time + self.delivery_duration

    @api.depends("estimated_delivery_distance")
    def _calculate_delivery_fees(self):
        for record in self:
            labor_fees = 30
            delivery_rate = 0.001
            if (record.estimated_delivery_distance > 0):
                record.delivery_fees = labor_fees + (delivery_rate*record.estimated_delivery_distance)
            else:
                record.delivery_fees = 0

    @api.depends('line_item', 'delivery_fees')
    def _calculate_total_price(self):
        for record in self:
            price = 0
            for product in self.line_item:
                price = price + (product.name.price * product.quantity)
            record.total_price = price + record.delivery_fees

    @api.depends('customer_id')
    def _gmaps_api(self):
        API_key = "5b3ce3597851110001cf6248a115ac3f860646bc9f8489570277725e"
        url="https://api.openrouteservice.org/v2/directions/driving-car?"
        for record in self:
            origin = "100.50974794289523,13.799011705163643"
            destination = record.customer_id.address_longlat
            if(destination != False):
                destination = destination.replace(" ","%20")
                complete_url= url + 'api_key=' + API_key + '&start=' + origin + '&end=' + destination
                r = requests.get(complete_url , params={'data': ""})
                x = r.json()
                record.delivery_duration = int((x["features"][0]["properties"]["summary"]["duration"])/60)
            else:
                record.delivery_duration = ""

    @api.depends('customer_id')
    def _estimate_delivery_distance(self):
        API_key = "5b3ce3597851110001cf6248a115ac3f860646bc9f8489570277725e"
        url="https://api.openrouteservice.org/v2/directions/driving-car?"
        for record in self:
            origin = "100.50974794289523,13.799011705163643"
            destination = self.customer_id.address_longlat
            if(destination != False):
                destination = destination.replace(" ","%20")
                complete_url= url + 'api_key=' + API_key + '&start=' + origin + '&end=' + destination
                print(complete_url)
                r = requests.get(complete_url , params={'data': ""})
                x = r.json()
                record.estimated_delivery_distance = x["features"][0]["properties"]["summary"]["distance"]
            else:
                record.estimated_delivery_distance = ""


