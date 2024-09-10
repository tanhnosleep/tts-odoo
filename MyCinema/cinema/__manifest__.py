{
    'name': "Cinema",
    'version': '1.0',
    'depends': ['base', 'product', 'sale'],
    'author': "Author Name",
    'category': 'CRM/Cinema',
    'description': """
    Description text
    """,

    'data': [
        'security/ir.model.access.csv',
        'views/cinema_movie_views.xml',
        'views/cinema_foods_views.xml',
        'views/cinema_sale_off_views.xml',
        'views/cinema_show_time_views.xml',
        'views/cinema_room_views.xml',
        'views/cinema_seat_views.xml',
        'views/cinema_ticket_views.xml',
        'views/cinema_sale_order_views.xml',
        'views/cinema_menus.xml',

    ],
}
