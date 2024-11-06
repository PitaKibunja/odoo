# define a model inside odoo
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'

    name = fields.Char(string="Name", required=True )
