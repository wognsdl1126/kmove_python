import random, time, pickle



tajalist = []
rank = {}
def sortV(x):
    return x[1]


while True:
    print("1.문제불러오기 2.타자게임 3.등수목록 4.저장하기 5.불러오기 6.문제저장하기 7.문제입력하기")
    menu = input("메뉴를 선택하세요\n")
    if menu =='1':
        f = open('taja_pickle.txt','rb')
        tajalist = tajalist + pickle.load(f)
        f.close()
        print(tajalist)                       
    elif menu =='2':
        choicelist = random.sample(tajalist,5)
        input("준비되시면 enter를 누르세요")
        start = time.time()
        for i in range(5):            
            print(choicelist[i])            
            while True:
                inputdata = input(": ")              
                if inputdata == choicelist[i]:
                   break
                else:
                    print(choicelist[i], "를 다시 입력하세요")
                    continue
        end = time.time()
        et = int(end - start)
        et=format(et,".2f")
        print("타자 시간: ",et,"초")
        name = input("사용자 이름을 입력하세요: ")
        rank[name] = float(et)        
    elif menu =='3':
        ranklist = sorted(rank.items(),key=sortV)
        num = 1
        for k,v in ranklist:
            print("%d등 %s %f"%(num,k,v))
            num = num + 1        
    elif menu =='4':
        f=open('rank_pickle.txt','wb')
        data = rank
        pickle.dump(data,f)
        print(data)        
        f.close()
    elif menu =='5':
        f=open('rank_pickle.txt','rb')
        data = pickle.load(f)
        rank = data        
        print(data)
        f.close()       
    elif menu == '6':
        f = open('taja_pickle.txt', 'wb')
        data = tajalist
        pickle.dump(data,f)
        f.close()
        print(data)
    elif menu == '7':
        word = input("문제를 입력하세요")
        tajalist.append(word)
    else:
        print("메뉴를 잘못 선택하셨습니다.")
    

print("5개의 단어를 입력하는데 걸린시간 %d초"%et)
