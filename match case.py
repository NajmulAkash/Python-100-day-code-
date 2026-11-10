a=int(input("Enter your total number : "))
match a:
    case _ if 0>10:
        print(a)
    case _ if 10>=40:
        print("3th Position")
    case _ if 40>=80:
        print("2th position")
    case _:
        print("1th Position")