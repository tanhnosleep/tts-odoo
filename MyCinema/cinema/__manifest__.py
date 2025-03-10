{
    'name': "Cinema",
    'version': '1.0',
    'sequence': 1,
    'depends': ['base', 'product', 'sale', 'point_of_sale', 'web', 'website'],
    'author': "Author Name",
    'category': 'CRM/Cinema',
    'description': """
    Description text
    """,

    'data': [

        'security/cinema_security.xml',
        'security/ir.model.access.csv',
        'views/cinema_movie_views.xml',
        'views/cinema_show_time_views.xml',
        'views/cinema_room_views.xml',
        'views/cinema_seat_views.xml',
        'views/cinema_ticket_views.xml',
        'views/cinema_sale_order_views.xml',
        'views/cinema_menus.xml',
        'views/cinema_template.xml',
        'views/cinema_movie_detail_template.xml',
        'views/cinema_booking_views.xml',

    ],

    'assets': {
        'web.assets_frontend': [
            'cinema/static/src/cinema_python_template.xml',
            'cinema/static/src/js/seat_selection.js',
        ]
    }

}
