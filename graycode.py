import numpy as np
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

def generate_n_bit_gray(n):
    """
    Generate an n-bit Gray code.
    Starts with 1 bit code and generates
    recursively.
    """
    crt_code = np.array([[0],[1]])
    crt_bits = 1
    while crt_bits < n:
        # Reflect the current one
        new_code = np.flip(crt_code, 0)
        # Prefix old code with 0
        old_code = np.concatenate((np.zeros((len(crt_code),1)), crt_code), axis=1)
        # Prefix new code with 1
        new_code = np.concatenate((np.ones((len(new_code),1)), new_code), axis=1)
        # Concatenate old with new
        crt_code = np.concatenate((old_code, new_code), axis=0)
        crt_bits += 1
    return crt_code
        
