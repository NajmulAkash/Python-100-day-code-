class Employee:
    def __init__(self, name , id):
        self.name=name
        self.id=id
    def showdetails(self):
        print(f"the name of empolyee {self.name} and id is {self.id}")
class programmer(Employee):
        def showlan(self):
             print("The default language is python")

e1 = Employee("najmul ",200)
e1.showdetails()
e2 = programmer("tajwar shaheen" ,400)

e2.showlan()