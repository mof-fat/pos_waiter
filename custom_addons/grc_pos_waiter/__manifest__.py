# _*_ conding: utf-8 _*_

{
    "name": "POS Waiter",
    "version": "1.0",
    "description": "Add a waiter on pos order and PoSticket",
    "summary": "Add a waiter on pos order and PoS ticket",
    "category": "Point Of Sale",
    "sequence": 20,
    'license': 'LGPL-3',
    "author": "Gracias Kasongo",
    "website": "https//gracias.zeslap.com",
    "depends": ["base", "point_of_sale", "hr", "web"],
    "data": ['views/grc_pos_view.xml', 'views/hr_employee.xml', 'views/pos_order.xml', 'views/pos_waiter.xml'],
    "assets": {
        'point_of_sale.assets': [
            'grc_pos_waiter/static/src/css/waiter.css',
            'grc_pos_waiter/static/src/js/waiter.js',
        ],
    },
    # "qweb": ['static/src/xml/waiter.xml'],
    "installable": True,
    "application": True,
    "auto_install": False,
    "maintainer": "graciaskas96@gmail.com",
    "support": "graciaskas96@gmail.com",
    'images': ['images/icon_screenshot.png'],
    "currency": "USD"
}
