from odoo import models, fields, api

class HrDepartment(models.Model):
    _inherit = "hr.department"

    department_key = fields.Char( string="Department Description" )

