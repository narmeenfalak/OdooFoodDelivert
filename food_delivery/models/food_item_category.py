from odoo import models, fields

class foodItemCategory(models.Model):
    _name = "food.item.category"
    _description = "Food Item Category table"

    name = fields.Char(string="Category")