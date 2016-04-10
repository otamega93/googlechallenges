while 1:
    #dumb test :v
    number = input("put a number here: ")
    if float(number) % 3 == 0:
        print("Fizz!")
    elif float(number) % 5 == 0:
        print("Buzz!")
    else:
        print("Nothing")
