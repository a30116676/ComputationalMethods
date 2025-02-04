import numpy as np

M = np.array([[1, 2, 3, 4 ,5], [6, 8, 10, 12, 14]])

print(M[0, :3]) # a

print(M[0, 2:4]) # b

print(M[:, 0]) # c

print(M[:, 1:4]) # d

print(M[0, 1:4], M[1, :2]) # e

print(M[M > 4]) # f

print(M[np.where((M > 4) & (M < 10))]) # g

print(M[np.where((M > 4) & (M % 2 == 0))]) # h

M[np.where(M % 2 == 1)] = 0 # i

print(M)
