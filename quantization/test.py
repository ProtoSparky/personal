import numpy as np

def dct(x):
    N = len(x)
    X = np.zeros((N,))
    for k in range(N):
        for n in range(N):
            X[k] += 2 * x[n] * np.cos((2*n+1)*k/N)
    return X

def quantize(X, Q):
    return np.round(X/Q)

# Example data array
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Perform DCT
X = dct(x)

# Quantize with a step size of 10
Q = 10
X_q = quantize(X, Q)

print(X_q)