
listdata = []
while True:
    print('''
    ======================== 리스트 데이타 관리 ======================
    1. 리스트에 추가 2. 리스트 데이타 수정 3. 리스트 데이터 삭제 4. 종료
    =================================================================
    ''')
    meun = int(input("메뉴를 선택하세요: "))

    if meun == 4:
        break
    elif meun == 1:
        data = input("추가 할 데이터를 입력하세요: ")
        listdata.append(data)
        print(listdata)
    elif meun == 2:
        print(listdata)
        indexNum = int(input("수정 할 데이터 인덱스 값을 선택하세요: "))
        if indexNum >= len(listdata):
            print("데이터가 없는 번호 입니다.")
        else:
            data = input("수정 할 데이터를 입력하세요: ")
            listdata[indexNum] = data
            print(listdata)
    elif meun == 3:
        print(listdata)
        indexNum = int(input("삭제 할 데이터 인덱스 값을 선택하세요: "))
        if indexNum >= len(listdata):            
            print("데이터가 없는 번호 입니다.")
        else:
            del listdata[indexNum]
            print(listdata)
    else:
        print("메뉴에 있는 번호를 선택해주세요")
        continue