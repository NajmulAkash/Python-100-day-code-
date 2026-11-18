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

try:
    b=[2,3,4,5,5]
except:
  print("Inviled value")
finally:
  print("i am always excute !")