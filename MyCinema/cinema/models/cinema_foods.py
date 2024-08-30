from odoo import fields, models


class Foods(models.Model):
    _name = "cinema.foods"
    _description = "This is table for foods"

    name = fields.Char(required=True)
    price = fields.Float(string= 'Giá bán (chưa bao gồm khuyến mãi)', required=True)