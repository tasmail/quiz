from settings.base import *

DATABASE['data'] = {
    'users': [
        {
            'login': 'admin',
            'password': 'admin',
            'is_admin': True
        },
        {
            'login': 'user1',
            'password': 'user1',
            'is_admin': False
        },
    ]
}
