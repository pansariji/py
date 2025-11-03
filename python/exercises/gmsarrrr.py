# import os  # Example: importing the 'os' module
import time  
timestamp= time.strftime('%H:%M:%S')
print(timestamp) 
timestamp= time.strftime('%H')
print(timestamp)
if int(timestamp) < 12:
    print("Good Morning")
elif int(timestamp) < 18:
    print("Good Afternoon")
else:
    print("Good Evening")

    
