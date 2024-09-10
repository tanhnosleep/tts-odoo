from contextlib import nullcontext
from datetime import timedelta
from email.policy import default

from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError
from odoo.tools.populate import compute


class RecurringPlan(models.Model):
    _name = "estate.property"
    _description = "This is demo for estate_property"
    _order = "id desc"
    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default= lambda self: fields.Date.today() + timedelta(days=3*30), string = 'Available From')
    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0)',
         'The expected price must be strictly positive.')
    ]
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
        string='Status',
        selection=[('New', 'New'), ('Offer Received', 'Offer Received'), ('Offer Received', 'Offer Received'), ('Sold', 'Sold'), ('Canceled', 'Canceled')],
        help="Type is used to separate Leads and Opportunities", required=True, copy=False, default='New')
    property_type_id = fields.Many2one('estate.property.type', string = 'Property Type')
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy = False)
    salesperson_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
    tag_ids = fields.Many2many('estate.property.tag')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string = 'Offer ID', required = True)

    total_area = fields.Integer(compute='_compute_total_area', string='Total Area')

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    best_price = fields.Float(compute='_compute_best_price')

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            prices = record.mapped('offer_ids.price')
            record.best_price = max(prices, default=0.0)

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden == True:
            self.garden_area = 10
            self.garden_orientation = 'North'
        else:
            self.garden_area = None
            self.garden_orientation = None

    def action_sold(self):
        for record in self:
            if record.state == "Canceled":
                raise UserError('Canceled properties cannot be sold')
            else:
                record.state = "Sold"
        return True

    def action_cancel(self):
        for record in self:
            if record.state == "Sold":
                raise UserError('Canceled properties cannot be canceled')
            else:
                record.state = "Canceled"
        return True

    @api.constrains('selling_price')
    def _check_selling_price(self):
        for record in self:
            if 0< record.selling_price < record.expected_price *0.9:
                raise ValidationError("The selling price cannot be lower than 90% of the expected price.")