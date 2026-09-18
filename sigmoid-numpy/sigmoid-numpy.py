import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    def func(x: float):
        return 1/(1+np.exp(-x))
    temp = np.asarray(x, dtype=float)
    # Write code here
    if type(temp) != list:
        return func(temp)
    else:
        temp[:, :] = func(x[:][:])
        return temp
    pass