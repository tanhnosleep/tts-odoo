from odoo import fields, models


class Foods(models.Model):
    _name = "room"
    _description = "This is table for room"

    name = fields.Char(required=True, string= 'Tên phòng')
    seat_counts = fields.Integer(required=True, string= 'Số ghế')