q=[0,1,2,3,4,5,6,7,8,9]
a=["7","8","15","9","10","11","12","13","14","15"]
s=[100,1000,5000,10000,50000,100000,500000,1000000,5000000,10000000]
i=-1
print("Welcome to KBC")
while i < len(q):
    if i >= len(q) - 1:
        print("quiz completed")
        break
    else:
        i += 1
    print(q[i])
    c=input("enter your answer")
    if c == a[i]:
        print("correct answer")
        print("you won", s[i])
    else:
        print("wrong answer")
        break
