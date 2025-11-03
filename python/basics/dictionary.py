dic = {
    "25BCE": "Madhav",
    "25BAI": "Yahswant"
 } 
print(dic["25BAI"])

# print(dic[434])       #throws error
# print(dic.get(434))     #print none


# print(dic.keys())
# print(dic.values())


# for key in dic.keys():
#   print(f"the value corresponding to the key {key} is {dic[key]}")


# for key, value in dic.items():
#     print(f"the value corresponding to the key {key} is {value}")


#-----------Dictionary Methods--------------
ep1 = {
    122: 45, 123: 89, 124: 69, 125: 69
}
ep2 = {
    222: 67, 897: 99
}

ep1.update(ep2)
ep1.clear()     
ep1.pop(122)
ep1.popitem()     #pop last key value pair in dictionary
del ep1  #delete ep1
del ep1[122]   #delete particular key value pair
print(ep1)