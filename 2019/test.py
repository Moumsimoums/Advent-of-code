import tsp 


mat = [[1000, 15, 21, 16, 3, 5, 7, 5, 7, 9],
[1000, 1000, 6, 1, 14, 12, 10, 16, 14, 12],
[1000, 6, 1000, 5, 20, 18, 16, 22, 20, 18],
[1000, 1, 5, 1000, 15, 13, 11, 17, 15, 13],
[1000, 14, 20, 15, 1000, 4, 6, 2, 6, 8],
[1000, 12, 18, 13, 4, 1000, 4, 6, 2, 6],
[1000, 10, 16, 11, 6, 4, 1000, 8, 6, 2],
[1000, 16, 22, 17, 2, 6, 8, 1000, 8, 10],
[1000, 14, 20, 15, 6, 2, 6, 8, 1000, 8],
[1000, 12, 18, 13, 8, 6, 2, 10, 8, 1000]]  # Distance Matrix
r = range(len(mat))
# Dictionary of distance
dist = {(i, j): mat[i][j] for i in r for j in r}
print(tsp.tsp(r, dist))