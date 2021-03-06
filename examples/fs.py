# -*- coding: utf-8 -*-

import os
import logging
from rocket import Rocket

if __name__ == '__main__':
    log = logging.getLogger('Rocket.Requests')
    log.setLevel(logging.INFO)
    fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
    h = logging.StreamHandler()
    h.setFormatter(fmt)
    log.addHandler(h)
    
    app_info = dict(document_root=os.getcwd(),
                    display_index=True)
    Rocket(interfaces=('127.0.0.1', 80),
           method='fs',
           app_info=app_info).start()
