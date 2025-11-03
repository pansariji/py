def average(*numbers):
    sum=0
    for i in numbers:
     sum+=i
    print("the average is",sum/len(numbers))



# method 1
a= int(input("enter a number"))
b= int(input("enter a number"))

even=[]                                     
for j in range(a, b):                               
    if j%2==0:
        even.append(j)
   
average(*even)

# method 2
# a= int(input("enter a number"))
# b= int(input("enter a number"))

# list=[i for i in range(a,b) if i%2==0]
# print(list)
# average(*list)
