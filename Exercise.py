
st = input("Enter message : ")
words=st.split("")
coding=True
if(coding):
  nwords=[]
  for word in words:
   if(len(word)>=3):
     r1="naj"
     r2="mul"
     stnew =r1+ word[1:] + word[0] +r2
     nwords.append(stnew)
     print("".join(nwords))
else:
    pass