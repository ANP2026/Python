import numpy as np
a=np.arange(9, dtype=float).reshape(3,3)
print(a)
b=np.array([10,10,10])
print(b)
print(np.add(a, b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))