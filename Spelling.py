# You have n cases
n = int(input())
# You have a dictionary so it can translate numbers into keywords
d = {'a': '2', 'b': '22', 'c': '222', 'd': '3', 'e': '33', 'f': '333', 'g': '4', 'h': '44', 'i': '444',
     'j': '5', 'k': '55', 'l': '555', '6': 'm', 'n': '66', 'o': '666', 'p': '7', 'q': '77', 'r': '777',
     's': '7777', 't': '8', 'u': '88', 'v': '888', 'w': '9', 'x': '99', 'y': '999', 'z': '9999', ' ': '0'}
# You have a list of characters
m = []
# You have a function which receive all the characters collected and insert them into m


def insert(i):
    return m.append(i)
# Then, you have n cases
for cases in range(n):
    i = input()
    insert(i)
    print(m)
# split the list
for iterator in range(n):
    # print("pre: " + str(iterator))
    for iterations in m[iterator][0:]:
        print("Case #" + str(cases + 1) + ": " + d[str(iterations)])
        # print("iteration: " + str(iterations))
