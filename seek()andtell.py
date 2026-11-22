# with open('najmul.txt','r')as f:
#     print(type(f))
   
#     f.seek(10) # f.seek dusara file masa jetana line code ha wo is ma sa deya huwa number a ga sa read kara ga
#     print(f.tell())
#     data = f.read(5)# f.seek pecha sa read kara ga
#     print(data)

# Example good
with open('najmul.txt','w') as f:
    f.write('Hello World!')
    f.truncate(5) # ya trucate file dusara file masa delete karta ha number ka hasab sa

with open('najmul.txt','r') as f:
    print(f.read())