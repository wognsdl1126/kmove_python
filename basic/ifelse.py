money = True

if money:
    print("택시")
else:
    print("워킹")


a = int(input("점수를 입력하세요 "))
print("입력한 점수는 %d 입니다."%a)

if a >= 90:
    total = 'A'
elif a >= 80:
    total = 'B'
elif a >= 70:
    total = 'C'
elif a >= 60:
    total = 'D'
else:
    total = 'F'
print("성적은 {} 입니다.".format(total))