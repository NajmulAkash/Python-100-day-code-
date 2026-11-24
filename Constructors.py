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
    def __init__(self,name,skill): # is function ma name or skill banaya ha
        print("Hay I am a person")
        self.name=name # self.name=name ya name function wala name ma jaya ga
        self.skill=skill # sef.skill=skill ya skill function wala skill ma jaya ga
    def info(dets):
        print(f"{dets.name} is a {dets.skill}")
a=person("najmul","developer") #  a=person keya ha is ka matlab class function ko call keya ha najmul name ma jaya ga or developer skill ma jaya ga
b=person("tajwar","ai developers") # ouper wala ko dakho
a.info() # info ko call keya ha to show hoga
b.info()



