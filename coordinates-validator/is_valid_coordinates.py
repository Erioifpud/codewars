import re
def is_valid_coordinates(coordinates):
    r = re.compile(r'-?0*([0-8]?\d|90)(\.\d+)?, -?0*(180|1[0-7]\d|[0-9]?\d)(\.\d+)?').match(coordinates)
    return False if not r else r.group() == coordinates
