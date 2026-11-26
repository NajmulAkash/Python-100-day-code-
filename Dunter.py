class emplopye:
    name = "najmul"
    def __len__(self):
      i=0
      for c in self.name:
         i=i +1
         return i
e=emplopye()
print(e.name)
print(len(e))