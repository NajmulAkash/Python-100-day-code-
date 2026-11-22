# Map function
def cube(x):
    return x*x*x
print(cube(2))

l = [1,2,3,4,5,6]
# newl=[]
# for item in l:
#     newl.append(cube(item))
# print(newl)
newl = list(map(cube,l))
print(newl)

# Filter 
def filter_function(a):
    return a>=3
newnewl = list(filter(filter_function,l))
print(newnewl)