from odoo import models, fields

class foodItemCategory(models.Model):
    _name = "food.item.category"
    _description = "Food Item Category table"

    # key = fields.Char()
    name = fields.Char(string="Category")