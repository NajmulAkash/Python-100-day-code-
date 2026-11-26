class parementclass:
    def parent_method(self):
     print("This is the parent method.")
class childclass(parementclass):
   def child_method(self):
      print("This is the child method.")
      super().parent_method()
child_object = childclass()
child_object = classmethod()