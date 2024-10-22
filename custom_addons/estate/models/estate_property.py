from odoo import api, fields, models


class RealEstateProperty(models.Model):
    __name='estate.property'
    __description='Real Estate Property'

    name=fields.Char('Property Name', required='True')
    description=fields.Text(string='Description')
    postcode=fields.Char(string='Postcode')
    date_availability=fields.Date(string='Available From')
    expected_price=fields.Float(string='Selling Price')
    bedrooms=fields.Integer(string='Number of Bedrooms')
    living_area=fields.Integer(string='Living Area (sqm)')
    facades=fields.Integer(string='Number of Facades')
    garage=fields.Boolean(string='Garage Available')
    garden=fields.Boolean(string='Garden Available')
    garden_area=fields.Integer(string='Garden Area (sqm)')
    garden_orientation=fields.Selection(
        [
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West')
        ], string='Garden Orientation'
    )