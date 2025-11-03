x= 90
match x:
    case 1:
          print("x is 1")
    case 2:
          print("x is 2")
    case 100:
          print("x is 100")   
    case _ if x>0:
          print("x is greater than 0")  
    case _ if x<0:  
          print("x is less than 0")
    case _ if x == 0:
          print("x is zero")
    case _:
          print(x)
