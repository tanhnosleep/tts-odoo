from odoo import fields, models


class SaleOrder(models.Model):
    _description = "This is table for sale order"

    _inherit = 'product.template'
    show_time_ids = fields.One2many('cinema.show.time', 'product_id')