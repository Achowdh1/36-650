def printNumTriangle(n):
    if not (isinstance(n, int) and n >= 0): 
        print('Invalid Input')
        return 
    c = 0 
    for i in range(1, n + 1):
        for j in range(i):
            c += 1
            print(str(c) + " ", end = "")
        print("")


printNumTriangle(3)
printNumTriangle(6)