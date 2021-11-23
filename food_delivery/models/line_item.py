from odoo import models, fields,api

class lineItem(models.Model):
    _name = "line.item"
    _description = "Line item table"

    name = fields.Many2one("food.item", string="Items")
    order_id = fields.Many2one("food.order", string="Order No.")
    quantity = fields.Integer(default=1)
    unit_price = fields.Float(compute="_unit_price")
    price = fields.Float(compute="_calculate_price")

    @api.depends('name', 'quantity')
    def _calculate_price(self):
        for record in self:
            record.price = self.name.price * self.quantity

    @api.depends('name')
    def _unit_price(self):
        for record in self:
            record.unit_price = self.name.price