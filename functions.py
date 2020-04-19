def gen(key):
    a = []
    for i in range(97, 122):
        a.append(chr(i))
    return dict(zip(a, "".join(a[key:] + a[:key])))


def enc_dec(origin, map, type):
    if type == 2:
        map = {val: key for (key, val) in map.items()}
    new = ""
    for i in range(0, len(origin)):
        if origin[i] in map:
            new = new + map[origin[i]]
        else:
            new = new + origin[i]
    return new


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
