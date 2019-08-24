import numpy as np

sprites_dir = 'sprites/'

disp_width = 1024
disp_height = 768

ship_size = [ 64, 64 ]
ship_oblique_size = [ int(np.round(ship_size[0] * np.sqrt(2))) ] * 2

half_ship_size = [ x // 2 for x in ship_size ]
half_ship_oblique_size = [ x // 2 for x in ship_oblique_size ]

rot_ang_increment = 22.5

ship_speed = 10
ship_max_speed = 25
rot_delay = 2

proj_speed = 20
proj_max_dist = 20
proj_delay = 5

time_delay = 50