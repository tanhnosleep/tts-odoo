from email.policy import default

from odoo import fields, models


class ShowTime(models.Model):
    _name = "show.time"
    _description = "This is table for show time"

    name = fields.Selection(
        string='Xuất chiếu',
        selection=[('Xuất sáng', 'Xuất sáng'), ('Xuất trưa', 'Xuất trưa'), ('Xuất tối', 'Xuất tối'), ('Xuất khuy', 'Xuất khuya')],
        required=True, copy=False, default='Xuất sáng')
    begin_time = fields.Datetime(string = 'Giờ bắt đầu', required = True)
    seat_counts = fields.Integer(default = 50, required = True, string= 'Số ghế ')
    adult_ticket_price = fields.Float(required = True, string= 'Giá vé người lớn', default = 80000)
    children_ticket_price = fields.Float(required = True, string= 'Giá vé trẻ em', default = 40000)

    movie_id = fields.Many2one('movie', string = 'Phim')