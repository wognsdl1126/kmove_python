import re, pickle, os
custlist=[]
page=-1

def insertData():
    global page
    print("고객 정보 입력")
    customer = {'name':'','sex':'',"email":'',"birthyear":''}
    name = input('이름을 입력하세요: ')
    customer["name"] = name        
    while True:
        sex = input('성별을 입력하세요(M or F)').upper()
        print(sex)
        
        if sex == 'F' or sex == 'M':                
            customer["sex"] = sex
        else:
            print("다시입력하세요.")
            continue
        break
    while True:
        regex = re.compile('^[a-z][a-z0-9]{4,10}@[a-zA-Z]{2,6}[.][a-zA-Z]{2,3}$')
        while True:
            email = input('이메일을 입력하세요: ')
            golbang = regex.search(email)
            if golbang:
                customer["email"]=email
                break
            else:
                print("이메일 형식에 맞춰서 입력해주세요")
                continue
        check = 0
        for i in custlist:                
            if i['email'] == customer['email']:
                check = 1        
        if check == 0:
            break
    while True:
        birthyear = input('생년을 입력하세요/ex(1994): ')
        if len(birthyear) == 4 and birthyear.isdigit():
            customer["birthyear"] = birthyear
        else:
            print("형식에 맞춰서 입력해주세요")
            continue 
        break      
    print(customer)
    custlist.append(customer)
    print(custlist)       
    page = (len(custlist)-1)
    print(page)
def curSearch():
    global page
    print("현재 고객 정보 조회")
    print(custlist[page])
    print(page + 1, "페이지 입니다.")  
def preSearch():
    global page
    print("이전 고객 정보 조회")
    page -= 1
    if page < 0:
        print("첫페이지 입니다.")
        page += 1
        print(custlist[page])
    else:
        print(page + 1, "페이지 입니다.")            
        print(custlist[page])
def nextSearch():
    global page
    print("다음 고객 정보 조회")
    page += 1        
    if page >= len(custlist):            
        print("마지막 페이지 입니다.")
        page -= 1
        print(custlist[page]) 
    else:
        print(page + 1, "페이지 입니다.")         
        print(custlist[page])
def updateData():
    while True:
        print("고객 정보 수정")
        print(custlist)
        choice1 = input("수정할 고객의 이메일을 입력해 주세요: ")
        idx = -1
        for i in range(0,len(custlist)):
            if custlist[i]['email'] == choice1:
                idx = i
                break
        if idx ==-1:
            print("등록되지 않은 이메일입니다.")
            break
        choice2 = input('''
        다음중 수정하실 정보를 골라주세요
        name, sex, birthyear
        수정할 정보가 없으면 'exit'입력
        ''')
        if choice2 in ('name', 'sex', 'birthyear'):
            custlist[idx][choice2]=input('수정할 {}을 입력하세요'.format(choice2))
            break
        elif choice2 =='exit':
            break
        else:
            print("존재하지않는 정보입니다.")
            break 
def deleteData():
    print("고객 정보 삭제")
    print(custlist)
    email = input("삭제할 이메일을 입력해 주세요: ")   
    for i in range(0,len(custlist)):                
        if custlist[i]['email'] == email:         
            del custlist[i]
            print("삭제완료")
            break
        else:
            print("등록되어있지 않는 이메일입니다.")      
    print(custlist)
def saveData():
    with open('basic/data.txt','wb') as f:
        pickle.dump(custlist,f)
def loadData():
    global page, custlist
    if os.path.exists('basic/data.txt'):
        with open('basic/data.txt','rb') as f:
            custlist = pickle.load(f)
            page=len(custlist)-1
def exe(choice):
        if choice=='I':
            insertData()
        
        elif choice=='C':
            curSearch()
        
        elif choice=='P':
            preSearch()

        elif choice=='N':
            nextSearch()

        elif choice=='U':
            print(page)
            updateData()
        
        elif choice=='D':
            deleteData()
        
        elif choice=='Q':
            saveData()
            quit()
            
