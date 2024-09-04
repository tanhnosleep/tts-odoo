from odoo import fields, models, api


class Foods(models.Model):
    _name = "cinema.room"
    _description = "This is table for room"

    name = fields.Char(required=True, string= 'Tên phòng')
    seat_counts = fields.Integer(compute='_compute_seat_counts', store=True, string= 'Số ghế')

    seat_ids = fields.One2many('cinema.seat', 'room_id', string='Ghế')

    @api.depends('seat_ids')
    def _compute_seat_counts(self):
        for record in self:
            record.seat_counts = len(record.seat_ids)