from datetime import timedelta
from email.policy import default

from odoo import fields, models


class RecurringPlan(models.Model):
    _name = "estate.property"
    _description = "This is demo for estate_property"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default= lambda self: fields.Date.today() + timedelta(days=3*30), string = 'Available From')
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Direction',
        selection=[('North', 'North'), ('South', 'South'), ('East', 'East'), ('West', 'West')],
        help="Type is used to separate Leads and Opportunities")
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='State Selection',
        selection=[('New', 'New'), ('Offer Received', 'Offer Received'), ('Offer Received', 'Offer Received'), ('Sold', 'Sold'), ('Canceled', 'Canceled')],
        help="Type is used to separate Leads and Opportunities", required=True, copy=False, default='New')
    property_type_id = fields.Many2one('estate.property.type', string = 'Property Type')
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy = False)
    salesperson_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
    tag_ids = fields.Many2many('estate.property.tag')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string = 'Offer ID', required = True)
