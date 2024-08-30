from odoo import fields, models


class SaleOff(models.Model):
    _name = "cinema.sale.off"
    _description = "This is table for sale off"

    name = fields.Char(required=True, string= 'Tên khuyến mãi')
    percent_sale_off = fields.Float(string= '% khuyến mãi', required=True)