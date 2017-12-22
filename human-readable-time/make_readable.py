import time
def make_readable(seconds):
    # Do something
    t = time.gmtime(seconds)
    return '{:02}:{:02}:{:02}'.format(24 * (t[2] - 1) + t[3], t[4], t[5])
