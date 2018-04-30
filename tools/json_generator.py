# -*- coding: utf-8 -*-

# @Time  :2018/4/30 16:27
# @File  : json_generator.py
# @Author: LI Jiawei

import json

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
BORDER = 50

dict = {
    'cars':
        [
            {
                'initialize_position' : [300, 300],
                'mass' : 10,
                'radius' : 10,
                'color' : 'yellowgreen'
             },
        ],

    'walls':
        [
            {
                'initialize_position' : [300, 300],
                'start_endpoint' : [0, -75],
                'end_endpoint' : [0, 75],
                'radius' : 1
            },
            {
                'initialize_position' : [100, 100],
                'start_endpoint' : [0, -75],
                'end_endpoint' : [0, 75],
                'radius' : 1
            }
        ],

    'stones':
        [
            {
                'mass' : 999999,
                'moment' : [60, 60],
                'initialize_position' : [500, 100],
                'size' : [60, 60],
                'inner_radius' : 0,
                'color' : 'darkgray'
            }
        ],

    'cats':
        [
            {
                'initialize_position' : [100, 500],
                'mass' : 1,
                'radius' : 15,
                'color' : 'orange'
            }
        ]
}

with open('../config.json', 'w') as file:
    json.dump(dict, file)
    print('Done!')