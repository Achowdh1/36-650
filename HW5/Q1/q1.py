def T(X):
    res = [[0 for i in range(len(X))] for j in range(len(X[0]))]
    for i in range(len(X)):
        for j in range(len(X[0])):
            res[j][i] = X[i][j] 
    for row in res: print(row)
    return res

X = [[10,8],
 [2 ,4],
 [1 ,7]]
T(X)
