f = open('basic/test.txt','a',encoding='utf8')
for i in range(11,21):
    data = "%d번째 줄입니다..\n"%i
    line = f.write(data)
f.close()

f = open('basic/test.txt','r',encoding='utf8')
line = f.readline().replace('\n','')
print(line)
print(type(line))
f.close()

f = open('basic/test.txt','r',encoding='utf8')
line = f.readlines()
print(line)
print(type(line))
for i in line:
    print(i.replace('\n',''))        
f.close()

