tup = (1,2,3,4 ,342)
print(type(tup),tup)
print(len(tup),tup)
print(tup[0])
print(tup[-1])
print(tup[2])
print(tup[3])

if 342 in tup:
    print("yes 342 is present in this tuple")

tup2 =tup[1:5]
print(tup2)

