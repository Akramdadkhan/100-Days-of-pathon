def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)


def isGreater(a, b):
    if (a > b):
        print("First Number is Greater")
    else:
        print("Second Number is greater")


def isLesser(a, b):
    pass
# We can pass the function by passing pass in function


a = 10
b = 9
isGreater(a, b)
calculateGmean(a, b)

c = 45
d = 85
isGreater(c, d)
calculateGmean(c, d)
