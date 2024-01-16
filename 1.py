import numpy as np

n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
w, v = np.linalg.eig(a)
print(v)