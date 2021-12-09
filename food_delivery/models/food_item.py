from odoo import models, fields

class foodItem(models.Model):
    _name = "food.item"
    _description = "Food item table"

    name = fields.Char( string="Title")
    description = fields.Text()
    price = fields.Float(required = True)
    in_stock = fields.Boolean(required = True)
    category = fields.Many2one("food.item.category")
    image = fields.Binary(string = "Product Image")
    preparation_time = fields.Integer( string="Preparation Time (in minutes)" , required=True)