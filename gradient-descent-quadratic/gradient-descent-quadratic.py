def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # Write code here

    for i in range(steps):
        Jacobi = 2*x0*a + b
        x0 = x0 - lr*Jacobi
    return x0
    pass