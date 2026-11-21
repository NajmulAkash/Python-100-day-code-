# Reading to a file
f=open('najmul.txt','r')
# print(f)
text = f.read()
print(text)

# Writing a file
with open('najmul.txt2','a')as f:
  f.write("Hello najmul balghari")