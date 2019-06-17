import os

from utils.utils import AttrDict


def config(debug, cache={}):
    d = lambda _debug, _prod: _debug if debug else os.environ[_prod]
    if cache:
        return cache['config']
    else:
        cache['config'] = AttrDict.from_data(
            {
                'DB': {
                    'name': d('sourandperky', 'DB.name'),
                    'user': d('sourandperky', 'DB.user'),
                    'password': d('sourandperky', 'DB.password'),
                    'host': d('127.0.0.1', 'DB.host'),
                    'port': d('5432', 'DB.port'),
                },
                'SECRET_KEY': d('SECRET_KEY', 'SECRET_KEY')
            }
        )
        return cache['config']
