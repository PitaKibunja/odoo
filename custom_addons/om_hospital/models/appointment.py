from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread']
    _description = 'Hospital Appointment'
    _rec_name  = 'patient_id'

    # Model fields
    reference = fields.Char(string="Reference", default='New', tracking=True)
    patient_id = fields.Many2one('hospital.patient', string="Patient")
    date_appointment = fields.Date(string="Date")
    note = fields.Text(string="Note")
    state = fields.Selection([
        ('draft', 'Draft'), ('confirmed', 'Confirmed'),
        ('ongoing', 'Ongoing'), ('done', 'Done'), ('cancel', 'Canceled')
    ], default='draft', tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # Check for 'reference' field existence and assign a new value if it's 'New' or not present
            if not vals.get('reference') or vals['reference'] == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or 'New'
        return super(HospitalAppointment, self).create(vals_list)

    def action_confirm(self):
        for rec in self:
            rec.state='confirmed'
    def action_ongoing(self):
        for rec in self:
            rec.state='ongoing'
    def action_done(self):
        for rec in self:
            rec.state='done'
    def action_cancel(self):
        for rec in self:
            rec.state='cancel'


class HospitalAppointmentLine(models.Model):
    _name = 'hospital.appointment_line'
    _description = 'Hospital Appointment Line'

    appointment_id=fields.Many2one('hospital.appointment', string='Appointment')
    product_id=fields.Many2one('product.product', string='Product')
    qty=fields.Float(string='Quantity')



