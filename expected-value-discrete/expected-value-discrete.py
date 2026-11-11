import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    x_new = np.array(x)
    p_new = np.array(p)

    return float(x_new.T@p_new)
    pass