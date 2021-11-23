from odoo import models, fields

class orderStatus(models.Model):
    _name = "order.status"
    _description = "Order status table"

    key = fields.Char()
    name = fields.Char(string="Status")
    # orders = fields.Many2one("food.order")