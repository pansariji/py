subjects = ("Math", "Science", "History", "English")
temp = list(subjects)
temp.append("Art") 
subjects = tuple(temp)
print(subjects)

scores = (95, 88, 76, 89, 92)
temp2 = subjects + scores
print(temp2)