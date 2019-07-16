import random

arr = [0,0,0,0,0,0]
num = random.randint(1, 45)

for i in range(0,5):
    for j in range(0,6):        
        while num in arr:
            print(num)          
            num = random.randint(1, 45)            
        arr[j] = num    
    arr.sort()
    print(arr)
    



