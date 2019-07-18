# f = open('basic/test.txt', 'w',encoding="utf8")

# for i in range(1,11):
#     data = "%d번째 줄입니다.. \n"%i
#     f.write(data)


# f.close()



tajalist = ["멸치","돼지","개","소","타조","책","잠","문","전등","말"]

f = open('word.txt','w',encoding='utf8')
for i in tajalist:
    data = "%s\n"%i  
    line = f.write(data)
f.close()