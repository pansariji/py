def average(a, b):
    average = (a + b) / 2
    print("The average is",average)

def isgreater(a, b):
    if a > b:
        print(f"{a} is greater than {b}")
    elif a < b:
        print(f"{a} is less than {b}")
    else:
        print(f"{a} is equal to {b}")

a=20
b=67
average(76, 23)
isgreater(90, 100)



# def average(*numbers):
#     sum=0
#     for i in numbers:
#         sum+=i
#     print("the average is",sum/len(numbers))

# average(78,89,754,902784581628)
