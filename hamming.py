def select_bits(symbol, bits):
    value = 0
    for bidx, b in enumerate(bits):
        value |= (symbol & (1<<b)) ? (1<<bidx) : 0
    return value

def decode(codewords, cr):
    """
    Decodes the codewords encoded with cr parity bits.
    Only supports cr <=2.
    Data is in bits 1,2,3, and 5 (5 only for cr 2).
    """
    assert(cr <= 2)

    indices = [1,2,3,5]
    unencoded_payload = []
    for i in range(len(codewords),2):
        d2 = (i+1 < len(codewords))?(select_bits(codewords[i+1], indices) & 0xff):0
        d1 = select_bits(codewords[i], indices) & 0xff

        unencoded_payload.append((d2<<4)|d1)

    return unencoded_payload
