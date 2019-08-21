# directions = {'u':0, 'luu':1, 'lu':2, 'llu':3, 'l':4, 'lld':5, 'ld':6, 'ldd':7, 'd':8, 'rdd':9, 'rd':10, 'rrd':11, 'r':12, 'rru':13, 'ru':14, 'ruu':15}
directions = {'u':0, 'lu':1, 'l':2, 'ld':3, 'd':4, 'rd':5, 'r':6, 'ru':7}
unit_speeds = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))

def frange(x, y, jump):
    while x < y:
        yield x
        x += jump