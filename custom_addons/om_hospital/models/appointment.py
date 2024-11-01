# define a model inside odoo
from odoo import fields, models


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread']
    _description = 'Hospital Appointment'


    patient_id = fields.Many2one('hospital.patient', string="Patient")
    date_appointment = fields.Date(string="Date")
    note = fields.Text(string="Note")
