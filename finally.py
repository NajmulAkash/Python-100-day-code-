def fun():
   try:# finally function importance ha funciton ka andar
    l=[1,2,3,4]
    a=int(input("Enter your value :"))
    print(l[a])
   except:
    print("Inviled value ")
   finally:
    print("I am always excute !")
x=fun()