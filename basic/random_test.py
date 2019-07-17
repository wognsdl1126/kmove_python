import random
import time
count = 0

input("시작하려면 enter 을 누르세요")
start = time.time()
for i in range(0,5):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    a = random.choice(['+','-','*','/'])
    inputdata = int(input("%d %s %d = "%(num1,a,num2)))
    result = int(eval("%d %s %d"%(num1,a,num2)))
    if result == inputdata:
        print("정답입니다.")
        count += 1
    else:
        print("오답입니다. 정답은 %d"%result)    
end = time.time()
et = int(end - start)
print("문제를 푸는데 걸린시간은 ", et,"초 입니다.")
print("맞춘갯수는 %d 개 입니다."%count)
    
