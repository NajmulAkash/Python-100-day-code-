# class person:
#     def __init__(self,name,skill):
#     #    print("Hay I am a person")
#        self.name=name
#        self.skill=skill
#     def info(self):
#      print(f"{self.name}is a {self.skill}")
# a=person("Najmul Balghari","Sofware developer")
# b=person("tajwar shaheen","Ai developer")
# c=person("yaseen","web-developer")
# a.info()
# b.info()
# c.info()

class person:
    def __init__(self,name,skill):
        print("Hay I am a person")
        self.name=name
        self.skill=skill
    def info(dets):
        print(f"{dets.name} is a {dets.skill}")
a=person("najmul","developer")
b=person("tajwar","ai developers")
a.info()
b.info()



