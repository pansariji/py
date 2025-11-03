d="hi myself madhav aggarwal usually my friends calls me pansariji"
# for charcater in d:
#     print(charcater)
# print(d[0])

# for i in len(d):
#     i-=1
#     print(i)


# Method 1: Using string slicing
print("Reversed string using slicing:")
print(d[::-1])

# Method 2: Using reversed() function
print("\nReversed string using reversed():")
for char in reversed(d):
    print(char, end='')

# Method 3: Using a loop from last index
print("\n\nReversed string using loop:")
for i in range(len(d)-1, -1, -1):
    print(d[i], end='') 