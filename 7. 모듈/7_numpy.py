# numpy
# 행렬, 벡터 만들기
import numpy as np

A = np.mat([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
B = np.mat([[1], [0], [0]])
print(A)
print(B)


# 행렬과 벡터의 연산
import numpy as np

A = np.mat([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
B = np.mat([[1], [0], [0]])
print(A + A)
print(A - A)
print(A * A)
print(B + B)
print(B - B)


# 역행렬 구하기
import numpy as np

A = np.mat([[2, 1, 1], [3, 2, 1], [2, 1, 1]])
inv_A = np.linalg.inv(A)
print(A * inv_A)


# 행렬에서 요소 접근하기
import numpy as np

A = np.mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(A[1, 1])
A[1, 1] = 0
print(A)
A[0, 0] = A[1, 0] + A[2, 0]
print(A)
A[4, 4] = 0
print(A)


# 행렬에서 행 또는 열 추출하기
import numpy as np

A = np.mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(A[0, 0])
print(A[1, 2])
print(A[0:3, 0])
print(A[0, 1:3])
print(A[0, :])
print(A[:, 1])


# 행렬을 텍스트 파일로 저장
import os

os.makedirs("C:/textfiles")

import numpy as np

A = np.mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.savetxt('C:/textfiles/sample1.txt', A, fmt='%d')


# 텍스트파일로부터 행렬 읽기
import numpy as np

data = np.loadtxt('C:/textfiles/sample1.txt')

print(type(data))
print(data)

data = np.mat(data)

print(type(data))
print(data)