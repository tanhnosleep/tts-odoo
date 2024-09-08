from odoo import fields, models


class SaleOrder(models.Model):
    _description = "day la sale order"

    _inherit = 'sale.order.line'
    movie_id = fields.Many2one('cinema.movie')
    show_time_id = fields.Many2one('cinema.show.time', domain="[('movie_id', '=', movie_id)]")
    phong = fields.Char(related='show_time_id.room_name')
    seat_id = fields.Many2one('cinema.seat', domain="[('room_id', '=', phong)]")
    ticket_id = fields.Many2one('cinema.ticket', domain="[('seat_id', '=', seat_id), ('show_time_id', '=', show_time_id)]")
