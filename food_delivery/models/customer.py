from odoo import models, fields

class customer(models.Model):
    _name = "customer"
    _description = "Customer table"

    name = fields.Char(required = True, string="Customer Name")
    address = fields.Text(required = True)
    address_longlat = fields.Char(required = True, string="Long Lat")
    email = fields.Char(required = True)
    contact_number = fields.Char(required = True)