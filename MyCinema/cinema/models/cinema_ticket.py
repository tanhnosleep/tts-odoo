from email.policy import default

from odoo import fields, models, api
from odoo.exceptions import ValidationError
from odoo.tools.populate import compute


class Ticket(models.Model):
    _name = "cinema.ticket"
    _description = "This is table for ticket"

    name = fields.Char(compute='_compute_name')
    sold_status = fields.Char(compute='_compute_sold_status', string='Trạng thái vé')
    customer_id = fields.Many2one('res.partner', string = 'Khách hàng')
    show_time_id = fields.Many2one('cinema.show.time', string='Xuất chiếu')
    show_time_name = fields.Text(related='show_time_id.name')
    phong = fields.Char(related='show_time_id.room_name')
    seat_id = fields.Many2one('cinema.seat', string='Ghế', domain="[('room_id', '=', phong)]")
    gio_bat_dau = fields.Datetime(related = 'show_time_id.begin_time')
    # thoi_luong = fields.Integer(related = 'movie_id.length')
    seat_name = fields.Char(related = 'seat_id.seat_name')

    seat_price = fields.Float(related = 'seat_id.seat_price')
    total_price = fields.Float(compute='_compute_total_price', string='Thành tiền')

    @api.depends("seat_price")
    def _compute_total_price(self):
        for record in self:
            record.total_price = record.seat_price

    @api.depends("show_time_id", "seat_id")
    def _compute_name(self):
        for record in self:
            if record.show_time_id and record.seat_id:
                record.name = record.show_time_name + " " + record.seat_name
            else:
                record.name = 'ticket'

    @api.depends("customer_id")
    def _compute_sold_status(self):
        for record in self:
            if record.customer_id:
                record.sold_status = 'Sold'
            else:
                record.sold_status = 'On Sale'

    @api.constrains('seat_id', 'phong')
    def _check_unique_seat(self):
        for record in self:
            if record.seat_id:
                # Check if there's any other ticket with the same seat in the same room and show time
                existing_ticket = self.search([
                    ('seat_id', '=', record.seat_id.id),
                    ('show_time_id', '=', record.show_time_id.id),
                    ('id', '!=', record.id)
                ])
                if existing_ticket:
                    raise ValidationError(
                        f"Ghế {record.seat_name} trong {record.phong} đã được chọn cho xuất chiếu này. Vui lòng chọn ghế khác..")