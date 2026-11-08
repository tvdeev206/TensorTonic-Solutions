import math

def gaussian_kernel(size: int, sigma: float) -> list:
    """
    Returns a square two-dimensional list.
    """
    # Write code here
    kernel = []
    offset = int((size/2))
    sum = 0
    for i in range(size):
        row = []
        for j in range(size):
            G = (1/(2*math.pi*sigma**2))*math.exp(-((i-offset)**2 + (j-offset)**2)/(2*sigma**2))
            sum = sum + G
            row.append(G)
        kernel.append(row)
    temp = 0
    for i in range(size):
        for j in range(size):
            kernel[i][j] = kernel[i][j] / sum
            temp += kernel[i][j]
    print(temp)
    return kernel
    pass