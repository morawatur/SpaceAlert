directions = {'r':0, 'rru':1, 'ru':2, 'ruu':3, 'u':4, 'luu':5, 'lu':6, 'llu':7, 'l':8, 'lld':9, 'ld':10, 'ldd':11, 'd':12, 'rdd':13, 'rd':14, 'rrd':15}
unit_speeds = []

def frange(x, y, jump):
    while x < y:
        yield x
        x += jump