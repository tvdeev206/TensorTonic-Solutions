import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    temp = np.asarray(A, dtype=float)
    final = np.zeros((temp.shape[1], temp.shape[0]))
    for i in range(temp.shape[0]):
        for j in range(temp.shape[1]):
            final[j][i] = temp[i][j]
    return final    
    pass
