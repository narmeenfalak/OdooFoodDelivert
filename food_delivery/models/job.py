from odoo import models, fields, api

class HrJob(models.Model):
    _inherit = "hr.job"

    # emp_description = fields.Char( string="EMployee Description" )