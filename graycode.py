decimal_to_gray = {
        0:0,
        1:1,
        2:3,
        3:2,
        4:6,
        5:7,
        6:5,
        7:4,
        8:12,
        9:13,
        10:15,
        11:14,
        12:10,
        13:11,
        14:9,
        15:8}

gray_to_decimal = {
        0:0,
        1:1,
        3:2,
        2:3,
        6:4,
        7:5,
        5:6,
        4:7,
        12:8,
        13:9,
        15:10,
        14:11,
        10:12,
        11:13,
        9:14,
        8:15
        }

def encode(symbol):
    return symbol ^ (symbol >> 1)

def decode(symbol):
    mask = symbol >> 1
    out = symbol
    while mask > 0:
        out = out ^ mask
        mask = mask >> 1
    return out
