# for loop e 
# 1. ekta iterator, mane ekta variable jar value prottek run e change hoibo
# 2. ekta range, aar difference

# 1 to 10 print koron
# python e upper limit sobsomoy ekta kom jodi ascending order e thake

for i in range(11):
    print(i)

for _ in range(15):
    print("Hello")

l = [5,6,9,8]
# index : 0,1,2,3 --> range(4)
# i <-- range(4) | i = 0,1,2,3
# l[i] = 9

for i in range(len(l)):
    print(l[i])

for x in l:
    print(x)

d = {
    "name" : "shayan",
    "address" : "agartala"
}

keys= []

for k,v in d.items():
    keys.append(k)

print(keys)

# reverse for loop

for i in range(10,-1,-1):
    print(i)