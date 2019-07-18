import random

end = True
s = random.sample(range(1,10),3)
print("야구게임을 시작 합니다")
print(s)
while end:
    strike = 0
    ball = 0 
    arr = list(map(int,input("세 자리 숫자를 입력하세요 (0, 공백제외) : ")))
    print(arr)
    for i in range(0,3):
        while arr[i] in s:        
            if arr[i] == s[i]:
                strike += 1            
            else:
                ball += 1
            break
    print(strike,"스트라이크",ball,"볼") 
    if strike == 3:
        print("성공하셨습니다.")
        end = False  
