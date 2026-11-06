import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))



def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    # Write code here
    m, n = X.shape
    w = np.zeros((n,))
    b = 0.0
    for i in range(0,steps):
        
        z = np.dot(X,w) + b
        p = _sigmoid(z)

        error = p - y
        
        w = w - (lr * (np.dot(X.T, error))/m)
        b = b - (lr * (error.sum(axis=0))/m)

    return w, b
    
    pass