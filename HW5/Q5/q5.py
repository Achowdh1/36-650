# i couldnt tell which of these resembled the picture more, so i put both in just in case
# the first one is the simpler one that i think is closer to what the image looks like, with more
#intuitive spacing. The second is a little challenge to space out the triangle more just in case
def printStarTriangle(n):
    l = [("* " * i)[:-1] for i in range(1, n + 1)]
    for i in range(len(l)):
        print(" "* (len(l) - i- 1) + l[i])

def printBigStarTriangle(n):
    l = [("*   " * i)[:-1] for i in range(1, n + 1)]
    for i in range(len(l)):
        print("  "* (len(l) - i- 1) + l[i])
        if i != len(l) - 1: 
            print('\n')
        

printStarTriangle(5)
printBigStarTriangle(5)
