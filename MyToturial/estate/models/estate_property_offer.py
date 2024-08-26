from datetime import timedelta

from odoo import fields, models, api
from odoo.tools.populate import compute


class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "This is demo for estate_property_offer"

    price = fields.Float()
    status = fields.Selection(
        string='Status Selection',
        selection=[('Accepted', 'Accepted'), ('Refused', 'Refused')],
        copy=False)
    partner_id = fields.Many2one('res.partner', string = 'Partner', required = True)
    property_id = fields.Many2one('estate.property', string = 'Property', required = True)

    validity = fields.Integer(default=7, string='Validity (days)')
    date_deadline = fields.Date(string='Deadline', compute='_compute_date_deadline', inverse='_inverse_date_deadline')

    @api.depends("validity", "create_date")
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = record.create_date + timedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date.date()).days