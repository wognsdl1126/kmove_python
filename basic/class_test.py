import re,sys,pickle,os


class Customer:
    custlist=[]
    page=-1


    def __init__(self):
        self.loadData()
        while True:
            self.exe(self.firstinput())
                

    def insertData(self):    
        print("고객 정보 입력")
        customer = {'name':'','sex':'',"email":'',"birthyear":''}
        name = input('이름을 입력하세요: ')
        customer["name"] = name        
        while True:
            sex = input('성별을 입력하세요(M or F)').upper()                     
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
        self.page = (len(custlist)-1)
        print(page)
    def curSearch(self):
        global page
        print("현재 고객 정보 조회")
        print(custlist[page])
        print(page + 1, "페이지 입니다.")  
    def preSearch(self):
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
    def nextSearch(self):
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
    def updateData(self):
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
    def deleteData(self):
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
    def saveData(self):
        with open('basic/data.txt','wb') as f:
            pickle.dump(custlist,f)
    def loadData(self):
        global page, custlist
        if os.path.exists('basic/data.txt'):
            with open('basic/data.txt','rb') as f:
                custlist = pickle.load(f)
                page=len(custlist)-1
    def quit(self):
        print("프로그램을 종료합니다.")
        sys.exit()
    def exe(self,choice):
            if choice=='I':
                self.insertData()
            
            elif choice=='C':
                self.curSearch()
            
            elif choice=='P':
                self.preSearch()

            elif choice=='N':
                self.nextSearch()

            elif choice=='U':
                print(page)
                self.updateData()
            
            elif choice=='D':
                self.deleteData()
            
            elif choice=='Q':
                self.saveData()
                self.quit()
    def firstinput(self):
        choice=input('''
            다음 중에서 하실 일을 골라주세요 :
            I - 고객 정보 입력
            C - 현재 고객 정보 조회
            P - 이전 고객 정보 조회
            N - 다음 고객 정보 조회
            U - 고객 정보 수정
            D - 고객 정보 삭제
            Q - 프로그램 종료
            ''').upper()  
        return choice              



   
        

