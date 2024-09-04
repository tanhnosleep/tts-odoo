from email.policy import default

from odoo import fields, models, api


class Ticket(models.Model):
    _name = "cinema.ticket"
    _description = "This is table for ticket"

    name = fields.Char(default= 'Nguyễn Văn A')
    # movie_id = fields.Many2one('cinema.movie', string='Vé xem phim')
    show_time_id = fields.Many2one('cinema.show.time', string='Xuất chiếu')
    movie_name = fields.Char(related='show_time_id.movie_name')
    seat_id = fields.Many2one('cinema.seat', string='Ghế')

    phong = fields.Char(related = 'show_time_id.room_name')
    gio_bat_dau = fields.Datetime(related = 'show_time_id.begin_time')
    # thoi_luong = fields.Integer(related = 'movie_id.length')
    seat_name = fields.Char(related = 'seat_id.seat_name')

    seat_price = fields.Float(related = 'seat_id.seat_price')
    total_price = fields.Float(compute='_compute_total_price', string='Thành tiền')

    @api.depends("seat_price")
    def _compute_total_price(self):
        for record in self:
            record.total_price = record.seat_price