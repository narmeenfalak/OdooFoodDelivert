from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    emp_description = fields.Char( string="EMployee Description" )