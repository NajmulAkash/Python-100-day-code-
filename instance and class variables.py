class employe:
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02
    def showdetails(self):
        print(f"the name of the employee is {self.name}")
employe =employe("najmul")
employe.showdetails()
emp1=employe("balghari")
emp1.showdetails()