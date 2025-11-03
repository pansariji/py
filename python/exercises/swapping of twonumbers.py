# a=1
# b=3
# print("before swapping",a,b)
# a,b=b,a
# print("after swapping",a,b)
# print(a)



def is_leap(year):
    leap = False
    
    if year%400==0 and year%4==0:
        leap=True
    elif year%100==0:
         leap=False
    
    return leap

year = int(input())
print(is_leap(year))