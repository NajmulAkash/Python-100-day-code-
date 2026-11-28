class animal:
    def __init__(self,name,species):
        self.name=self.name
        self.species=species

    def make_sound(self):
        print("Sound made by the animal")

class dog (animal):
    def __init__(self, name, bread):
        animal.__init__(self,name,species="dog")
        self.bread=bread
    def make_sound(self):
        print("Bark!")

d=dog("Dog","Doggment")
d.make_sound()

a=animal("Dog","Dog")
a.make_sound()