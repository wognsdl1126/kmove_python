import random
arr = [0,0,0,0,0,0]


for i in range(0,5):
    for j in range(0,6):
        while arr[j] != arr [j-1]:
            num = random.randint(1, 45)
            break
        num = random.randint(1, 45)
        arr[j] = num
    arr.sort()
    print(arr)
    


