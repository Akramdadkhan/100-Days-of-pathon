# Function Argument in Python

# default arguments

# def average(a=9, b=1):
#     print("Average will be :", (a+b)/2)


# average(1)

# # Keyword Argument

# average(b=5, a=8)


# How we can pass direct argument to number

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        # print(sum/len(numbers))
    return sum/len(numbers)


a = average(5, 6, 7, 1)
print("Value is", a)
