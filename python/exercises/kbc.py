q=[
    ("0",23,45,76,78,3),["1",56,34,50,23,4],["2",12,32,43,65,2],["3",98,45555,3433,434,1],["4",23434,45555556,7567,45234,4],["5",15,1611,65161,1616,1],["6",1684,646,684,6846,3],
    ["7",14,541,54,44,2],["8",3484,8364,34444448,48,84,1],["9",18,8634,8413,3484,4]
]
s=[100,1000,5000,10000,50000,100000,500000,1000000,5000000,10000000]

print("Welcome to KBC")

def money(j):
    if j%2!=0:
         print("Your take home money is: ",s[j])
    elif j==0:
         print("Your take home money is: 0")
    else:
         print("Your take home money is: ",s[j-1])

for j in range(0,len(q)):
            ques=q[j]
            print(f"\n\nQuestion no.{j+1}:\n",ques[0])
            print(f"option 1: {ques[1]}    option 2: {ques[2]}")
            print(f"option 3: {ques[3]}    option 4: {ques[4]}")
            c=int(input("enter your answer(1-4): "))
            if c<0 and c>4:
                raise ValueError("Enter value between 1 and 4")
            elif c==ques[-1]:
                print("correct answer")
                print("you won",s[j])
            else:
                print("wrong answer")
                money(j)
                break
            if j >= len(q) - 1:
                print("quiz completed")
            else:
                continue