from email.policy import default

from odoo import fields, models, api


class Ticket(models.Model):
    _name = "cinema.ticket"
    _description = "This is table for ticket"

    name = fields.Char(required=True, string= 'Vé xem phim')
    movie_id = fields.Many2one('cinema.movie', string='Vé xem phim')
    xuat_chieu_id = fields.Many2one('cinema.xuat.chieu', string='Xuất chiếu')
    seat_id = fields.Many2one('cinema.seat', string='Ghế')

    phong = fields.Char(related = 'xuat_chieu_id.room_name')
    gio_bat_dau = fields.Datetime(related = 'xuat_chieu_id.start_time')
    thoi_luong = fields.Integer(related = 'movie_id.length')
    seat_name = fields.Char(related = 'seat_id.seat_name')

    seat_price = fields.Float(related = 'seat_id.seat_price')
    total_price = fields.Float(compute='_compute_total_price', string='Tổng giá vé')

    @api.depends("seat_price")
    def _compute_total_price(self):
        for record in self:
            record.total_price = record.seat_price