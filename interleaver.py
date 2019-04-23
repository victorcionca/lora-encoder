import numpy as np

def deinterleave(symbol_matrix, sf, cr):
    """
    De-interleaves a set of 4+cr symbols each of sf bits.
    Based on the de-interleaver by Robyns et al
    In and out numpy matrices
    """
    # First reverse the order of the columns in the symbol matrix
    A = symbol_matrix
    B = np.flip(A, 1)
    B = B.transpose()
    # Now build the codeword matrix by parsing it upwards, end to start
    cw_matrix = []
    for j in range(0, sf):
        # Codeword j = B[(j+k)%sf, k], where 0<=k<=4-cr-1
        cw_j = [B[(j+k)%sf][4+cr-1-k] for k in range(4+cr)]
        cw_matrix.append(cw_j)
    return cw_matrix

def interleave(cw_matrix, sf, cr):
    sym_matrix = []
    for k in range(4+cr):
        sym_matrix.append([cw_matrix[(m-k)%sf][k] for m in range(sf)])
    return np.flip(np.flip(sym_matrix,0),1)
