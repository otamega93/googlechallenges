#You have n cases
n = int(input())
#loop for n cases
for cases in range(n):
    #You have a credit c
    c = int(input())
    #You have a list of l items
    l = int(input())
    #Price of each item
    p = [int(positions) for positions in input().split()]
    for iterations in range(l-1):
        for pointer in range(iterations+1, l):
            if p[iterations] + p[pointer] == c:
                print("Case #" + str(cases + 1) + ": " + str(iterations + 1) + " " + str(pointer + 1))
                #test
