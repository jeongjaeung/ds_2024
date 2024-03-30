# A = np.matrix([[1,2],[4,5],[7,8]])
# B = np.matrix([[1,1,0],[0,1,1],[1,0,1]])

# import numpy as np
# A = np.array([[1,2,1],[4,4,5],[6,7,7]])
# B = np.array([[-7,-7,6],[2,1,-1],[4,5,-4]])
# A
# B
# A*B
# (A*B == (B*A)).all() == ((B*A) == np.eye(A.shape[0])).all()

#import numpy as np
# mat = np.vstack([[1,1,1],[1,-1,2],[2,0,3]])
# sol = np.vstack([3,2,1])
# try:
#     npl.solve(mat,sol)
# except:
#     print(np.hstack([mat,sol]))
#     print("Not solveable. Adding rows 1 and 2 contradicts row 3.")


# A = np.matrix([[1,2,3],[3,2,1]])
# B = np.matrix([[0,2],[1,-1],[0,1]])
# print(A)
# print(B)

# #2.4.a.
# import numpy as np
# A = np.matrix([[1,2],[4,5],[7,8]])
# B = np.matrix([[1,1,0],[0,1,1],[1,0,1]])
# print(A*B)

# #2.4.b.
# A = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
# B = np.matrix([[1,1,0],[0,1,1],[1,0,1]])
# print(A*B)

# #2.4.c.
# A = np.matrix([[1,1,0],[0,1,1],[1,0,1]])
# B = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
# print(A*B)

# #2.4.d.
# A = np.matrix([[1,2,1,2],[4,1,-1,-4]])
# B = np.matrix([[0,3],[1,-1],[2,1],[5,2]])
# print(A*B)

# #2.4.e.
# A = np.matrix([[0,3],[1,-1],[2,1],[5,2]])
# B = np.matrix([[1,2,1,2],[4,1,-1,-4]])  
# print(A*B)

# # 2.5.a singular matrix이므로 해를 구할 수 없음
# A = np.array([[1, 1, -1, -1],
#               [2, 5, -7, -5],
#               [2, -1, 1, 3],
#               [5, 2, -4, 2]])
# b = np.array([1, -2, 4, 6])
# A_inv = np.linalg.inv(A)
# x= np.dot(A_inv, B)
# print("Solution x:", x)

# 2.5.b A가 정방행렬이 아니므로 해를 구할 수 없음
# A = np.array([[1, -1, 0, 0, 1],
#               [1, 1, 0, -3, 0],
#               [2, -1, 0, 1, -1],
#               [-1, 2, 0, -2, -1]])
# b = np.array([3, 6, 5, -1])
# x = np.linalg.solve(A, b)
# print("Solution x:", x)

# #2.6
# A = np.array([[0, 1, 0, 0, 1, 0],
#               [0, 0, 0, 1, 1, 0],
#               [0, 1, 0, 0, 0, 1]])

# b = np.array([2, -1, 1])

# C = numpy. concatenate((A,b), axis=1)

# import numpy as np

# A = np.array([[0, 1, 0, 0, 1, 0],
#               [0, 0, 0, 1, 1, 0],
#               [0, 1, 0, 0, 0, 1]])

# b = np.array([2, -1, 1])

# Ab = np.column_stack((A, b))

# # 가우스 소거법을 사용하여 상삼각 행렬로 변환합니다.
# for i in range(len(Ab)):
#     pivot_row = Ab[i]
#     for j in range(i + 1, len(Ab)):
#         factor = Ab[j][i] / pivot_row[i]
#         Ab[j] -= factor * pivot_row

# # 후진 대입을 사용하여 해를 찾습니다.
# x = np.zeros(len(b))
# for i in range(len(b) - 1, -1, -1):
#     x[i] = (Ab[i][-1] - np.dot(Ab[i][:i], x[:i])) / Ab[i][i]

# print("Solution x:", x)

# import numpy as np
# # 주어진 행렬 A
# A = np.array([[6, 4, 3], [6, 0, 9], [0, 8, 0]])

# # 항등 행렬 I3
# I3 = np.eye(3)

# # 행렬 A - 12I3
# A_12I3 = A - 12 * I3

# # A - 12I3의 특잇값 분해 수행
# U, s, V = np.linalg.svd(A_12I3)

# # 특잇값 중 0에 가까운 값은 영공간에 해당
# # 따라서 V의 마지막 행이 영공간의 기저 벡터가 됨
# null_space = V[-1]

# print("Null space of A - 12I3:", null_space)