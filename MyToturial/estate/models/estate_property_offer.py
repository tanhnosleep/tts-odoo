from odoo import fields, models


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