from email.policy import default
from datetime import timedelta, datetime
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class ShowTime(models.Model):
    _name = "cinema.show.time"
    _description = "This is table for show time"

    name = fields.Text(compute='_compute_name')
    begin_time = fields.Datetime(string = 'Giờ bắt đầu',  default=fields.Datetime.now)
    movie_id = fields.Many2one('cinema.movie', string='Phim')
    movie_name = fields.Char(related = 'movie_id.name')
    thoi_luong = fields.Integer(related='movie_id.length', string = 'Thời lượng (phút)')
    end_time = fields.Datetime(compute='_compute_end_time', string = 'Giờ kết thúc', store=True)
    room_id = fields.Many2one('cinema.room', string='Phòng')
    room_name = fields.Char(related='room_id.name')
    product_id = fields.Many2one('product.template', string='San pham')
    sale_order_ids = fields.One2many('sale.order.line', 'show_time_id')

    @api.depends("begin_time", "thoi_luong")
    def _compute_end_time(self):
        for record in self:
            if record.begin_time and record.thoi_luong:
                record.end_time = record.begin_time + timedelta(minutes=record.thoi_luong)
            else:
                record.end_time = False

    @api.constrains('begin_time', 'end_time', 'room_id')
    def _check_room_availability(self):
        for record in self:
            if not record.begin_time or not record.end_time:
                continue  # Bỏ qua kiểm tra ràng buộc nếu begin_time hoặc end_time chưa được thiết lập

            # Lấy phần ngày của thời gian bắt đầu
            begin_date = record.begin_time.date()

            # Tìm các showtime có trùng thời gian chiếu
            overlapping_showtimes = self.env['cinema.show.time'].search([
                ('room_id', '=', record.room_id.id),
                ('id', '!=', record.id),  # Bỏ qua bản ghi hiện tại
                ('begin_time', '<', record.end_time),
                ('end_time', '>', record.begin_time),
            ])

            # Kiểm tra nếu có bất kỳ showtime nào trùng ngày
            for overlap in overlapping_showtimes:
                if overlap.begin_time.date() == begin_date:
                    raise ValidationError(
                        "Phòng này đã được đặt cho một bộ phim khác trong thời gian này trong cùng một ngày.")

    @api.depends("room_id", "movie_id")
    def _compute_name(self):
        for record in self:
            if record.room_id and record.movie_id:
                record.name = record.movie_name +" "+ record.room_name
            else:
                record.name = 'show time'
