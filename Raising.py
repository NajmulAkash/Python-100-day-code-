a=int(input("Enter your value of 4 to 9 : "))
if(a<4 or a>9):
    raise ValueError("unexcepted value")
else:
    print("Value is >4 or <9")