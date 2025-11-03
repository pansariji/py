# num = {1,2,3,4,5,2,2,2,2,2,3,4,5,"madhav", "yashwant", "madhav"}
# print(set)   # it does not print duplicate values
             

# info = {"madhav" , 18 , False , 3.8 , 18}
# print(info) # also order in which a set is printed is random

# madhav = {}
# print(type(madhav))  #class = 'dict' because both set and dict starts with { and ends with }

# megha = set()
# print(type(megha)) # class = set  to make an empty set we have to write set()

#-------------Set methods-------------
s1 = {1,2,5,6}
s2 = {3,6,7}


# s3 = s1.union(s2) #takes union of both sets
# print(s3)


# s1.update(s2)  #add those elements of s2 in s1 which were not present in s1
# print(s1 , s2)

# s4 = s1.intersection(s2)   #takes intersection of both sets
# print(s4) 


# s1.intersection_update(s2)
# print(s1,s2)


# s5 = s1.symmetric_difference(s2)    # universe - intersection
# print(s5)


# s6 = s1.difference(s2)    #A -B
# print(s6)


# print(s1.isdisjoint(s2))    #check wether sets have somthing common or not


#issuperset
#issubset

# s1.add(11)  #add an element in set
# print(s1)


#remove()/discard() to remove the elements from set


# element = s1.pop()  #removes random value
# print(element)


# del s1  #delete entire set


# s1.clear()   #delete all items of set and make it an empty set
# print(s1)




