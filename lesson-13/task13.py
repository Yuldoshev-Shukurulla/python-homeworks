# # 1. Create a vector with values ranging from 10 to 49.
import numpy as np
a = np.arange(10, 49)
# # 2. Create a 3x3 matrix with values ranging from 0 to 8.
b = np.arange(9).reshape(3, 3)
# # 3. Create a 3x3 identity matrix.
c = np.eye(3)
# # 4. Create a 3x3x3 array with random values.
d = np.random.randint(1, 50, size=(3, 3, 3))
# # 5. Create a 10x10 array with random values and find the minimum and maximum values.
e = np.random.randint(1, 50, size=(10, 10))
print(e.max())
print(e.min())
# # 6. Create a random vector of size 30 and find the mean value.
f = np.random.randint(1, 100, size=(30))
print(f.mean())
# # 7. Normalize a 5x5 random matrix.
g = np.random.randint(1, 100, size=(5, 5))
normalized_g = (g - g.min()) / (g.max() - g.min())
print(normalized_g)
# # 8. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product).
h = np.random.randint(1, 20, size=(5, 3))
i = np.random.randint(1, 20, size=(3, 2))
j = h @ i
print(j)
# # 9. Create two 3x3 matrices and compute their dot product.  
k = np.random.randint(1, 20, size=(3, 3))
l = np.random.randint(1, 20, size=(3, 3))
m = np.dot(k, l)
print(m)
# # 10. Given a 4x4 matrix, find its transpose.  
n = np.array([[19, 6, 8, 18],
            [17, 9, 16, 3],
            [10, 4, 12, 1],
            [17, 7, 5, 1]])
n_transpozed = n.transpose()
print(n_transpozed)
# # 11. Create a 3x3 matrix and calculate its determinant.  
o = np.random.randint(1, 20, size=(3, 3))
det_o = np.linalg.det(o)
print(det_o)
# # 12. Create two matrices \( A \) (3x4) and \( B \) (4x3), and compute the matrix product \( A \cdot B \).  
A = np.random.randint(1, 20, size=(3, 4))
B = np.random.randint(1, 20, size=(4, 3))
C = np.dot(A, B)
print(C)
# # 13. Create a 3x3 random matrix and a 3-element column vector. Compute the matrix-vector product.  
p = np.random.randint(1, 20, size=(3, 3))
q = np.array([1, 2, 3])
r = p * q
print(r) 
# # 14. Solve the linear system \( Ax = b \) where \( A \) is a 3x3 matrix, and \( b \) is a 3x1 column vector.
A = np.array([[5, 3, 1],
              [4, 1, 2],
              [3, 2, 5]])

b = np.array([1, 2, 3]).reshape(3, 1)
x = np.linalg.solve(A, b)
print(x)
# # 15. Given a 5x5 matrix, find the row-wise and column-wise sums.
matrix = np.random.randint(1, 10, size=(5, 5))
print("Asosiy matritsa:\n", matrix)

row_sums = np.sum(matrix, axis=1)

col_sums = np.sum(matrix, axis=0)

print("\nHar bir qator yig'indisi (Row-wise):", row_sums)
print("Har bir ustun yig'indisi (Column-wise):", col_sums)