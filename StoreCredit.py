#You have n cases
print("Select number of cases:")
n = int(input())
#loop for n cases
for cases in range(n):
    #You have a credit c
    print("Select your credit:")
    c = int(input())
    #You have a list of l items
    print("Select number of items available:")
    l = int(input())
    #Price of each item
    p = [int(positions) for positions in input().split()]
    print(p)
    for iterations in range(l-1):
        for pointer in range(iterations+1, l-1):
            #TO DO: stop iteration when one match is found
            if p[iterations] + p[pointer] == c:
                print("Case #" + str(cases + 1) + ": " + str(iterations + 1) + " " + str(pointer + 1))
