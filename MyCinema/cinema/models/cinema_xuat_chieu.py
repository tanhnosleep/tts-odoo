from email.policy import default

from odoo import fields, models


class XuatChieu(models.Model):
    _name = "cinema.xuat.chieu"
    _description = "This is table for xuat chieu"

    name = fields.Char(required=True, string= 'Xuất chiếu', default='Xuất chiếu')
    room_id = fields.Many2one('cinema.room', string='Phòng')
    show_time_id = fields.Many2one('cinema.show.time')
    start_time = fields.Datetime(related = 'show_time_id.begin_time', string='Giờ chiếu')
    room_name = fields.Char(related = 'room_id.name')