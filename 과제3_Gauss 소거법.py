# a = [
#     [1, 1, 1],
#     [1, -2, -1],
#     [3, 2, 4]
#     ]
# b = [5, 0, 3]

# a = [
#     [1, 2, 3],
#     [1, 3, 6],
#     [2, 6, 13]
#     ]
# b = [1, 1, 5]

# a = [
#     [2, 5, 6],
#     [1, 2, 4],
#     [1, 7, 3]
#     ]
# b = [2, 3, 7]

# x = [0, 0, 0]
# s = [0, 0, 0]

# a = [
#     [2, 4, 1, 3, 2],
#     [1, 6, 3, 2, 3],
#     [1, 2, 2, 3, 5],
#     [3, 5, 1, 2, 8],
#     [2, 2, 6, 3, 2]
#     ]
# b = [1, 6, 9, 4, 11]

# a = [
#     [3, 2, 1, 1, -2],
#     [2, 3, 2, -1, 4],
#     [1, 4, 1, 3, 5],
#     [-1, 3, -3, 2, 2],
#     [2, 1, 5, 4, 3]
#     ]
# b = [5, -4, 9, -1, 6]

a = [
    [-5, 4, 1, 1, 9],
    [7, 1, 2, 3, -1],
    [-2, 1, 4, 5, 3],
    [1, 1, 8, 6, 2],
    [2, 4, 7, 4, 7]
    ]
b = [4, 0, 10, -5, 15]

x = [0, 0, 0, 0, 0]
s = [0, 0, 0, 0, 0]

def Pivot(a, b, s, n, k):
    p = k
    big = abs(a[k][k] / s[k])

    for ii in range(k, n):
        dummy = abs(a[ii][k] / s[ii])
        if dummy > big:
            big = dummy
            p = ii
    
    if p != k:
        for jj in range(k, n):
            a[p][jj], a[k][jj] = a[k][jj], a[p][jj]

        b[p], b[k] = b[k], b[p]
        s[p], s[k] = s[k], s[p]


def Eliminate(a, s, n, b, tol, er):
    print("<전진소거>")
    for k in range(n - 1):
        Pivot(a, b, s, n, k)
        if abs(a[k][k] / s[k]) < tol:
            er = -1

        for i in range(k + 1, n):
            factor = a[i][k] / a[k][k]
            for j in range(k + 1, n):
                a[i][j] = a[i][j] - factor * a[k][j]
            b[i] = b[i] - factor * b[k]
        
        for i in range(len(a)):
            print(a[i])
        print()
    
    if abs(a[n-1][n-1] / s[n-1]) < tol:
        er = -1

def Substitute(a, n, b, x):
    x[n-1] = b[n-1] / a[n-1][n-1]
    for i in range(n - 1, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum = sum + a[i][j] * x[j]

        x[i] = (b[i] - sum) / a[i][i]

def Gauss(a, b, n, x, tol, er):
    er = 0
    for i in range(n):
        s[i] = abs(a[i][0])
        for j in range(1, n):
            if abs(a[i][j] > s[i]):
                s[i] = abs(a[i][j])
    
    Eliminate(a, s, n, b, tol, er)

    if er != -1:
        Substitute(a, n, b, x)

Gauss(a, b, len(a), x, 1e9, 0)
for i in range(len(x)):
    print(i + 1, ":", round(x[i], 8))