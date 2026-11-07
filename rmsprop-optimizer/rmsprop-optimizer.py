import numpy as np

def rmsprop_step(
    w: list,
    g: list,
    s: list,
    lr: float = 0.001,
    beta: float = 0.9,
    eps: float = 1e-8,
) -> tuple[list, list]:
    """
    Returns (new_w, new_s) with the same shapes as the inputs.
    """
    # Write code here
    W = np.array(w, dtype=float)
    G = np.array(g, dtype=float)
    S = np.array(s, dtype=float)
    
    S = S * beta + (1 - beta) * G**2
    
    W = W - lr * (1/np.sqrt(S + eps)) * G

    return tuple([W.tolist(), S.tolist()])
    pass