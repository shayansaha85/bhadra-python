# koyekta data ekloge thakbo
# jekunu data
# jodi, same type er data ekloge thake, taile oita array, R naile list
# sob array list, kintu sob list array na
# # list lekha hoy [e1,e2]

# list
l1 = [1,2,3,4,5]


# finding element
# [ 1   2   3   4   5 ]
#   0   1   2   3   4 --> front index
#  -5  -4  -3  -2  -1 --> back index

# to print 4 from l1
print(l1[3])
print(l1[-2])

# slicing - sub list print koron
print(l1[1:4])

# length of list - list e koyta element ase
print(len(l1))

# list e jodi sob integer hoy, taile tarar summation
sum_result = sum(l1)
print(sum_result)

# avergae
avg_ans = sum_result / len(l1)
print(avg_ans)

# join all elements
# [1,2,3,4,5]
# "1-2-3-4-5" --> string
l2 = ['1','2','3','4']
output = '**'.join(l2)
print(output)

# printing last element
last_el1 = l1[len(l1)-1]
last_el2 = l1[-1]
print(last_el1,last_el2)

# maximum and minimum numbers
max = max(l1)
min = min(l1)
print(max,min)

# element add
names = ["shayan", "bhadra", "prasanta"]
print("name",names)
names.append("supratim")
print("name",names)

# remove elements
names.remove("shayan")
print(names)

# last element remove
names.pop()
print(names)