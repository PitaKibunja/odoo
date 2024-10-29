#define a model inside odoo
from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = 'hospital.patient'