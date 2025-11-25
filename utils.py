import numpy as np

def generate_random_sales(min_val, max_val, size, seed=None):
    if seed is not None:
        np.random.seed(seed)
    return np.random.randint(min_val, max_val + 1, size=size)

