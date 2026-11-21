# x=4
# print(x)

# def hello():
#     x=5
#     print(f"the local x is {x}")
#     print(x)
# print(f"the global x is {x}")
# hello()
# print(f"the global x is {x}")

x=10 # global variable
def functi():
    global x
    x=5
    y=5 # local variables
    print(y)

functi()
print(x)
# print(y) 