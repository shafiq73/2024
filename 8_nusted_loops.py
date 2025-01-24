# nusted loops ka matlab loop ke andar loop
# 1- nusted for loop


# colors = ['red','green','blue']
# items = ['book','pen','copy']

# for color in colors:
#     for item in items:
#         print(color,item)

# 1- nusted while loop

i = 0
while i < 3:
    j = 0
    while j < 3:
        print(i,j)
        j += 1
    i +=1
# clt c press in terminal for stoping for loop infinate positionig

# for loop inside while loop

i = 1
while i < 4:
    for j in range(3):
        print(i ,j)
    i += 1

# assignment while loop inside for loop

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
i = 0
while i < len(fruits):
    for j in range(3):
        print(f"fruit = {fruits[i]}, j = {j}")
    i += 1
