from odoo import fields, models


class SaleOrder(models.Model):
    _description = "This is table for sale order"

    _inherit = 'product.product'
