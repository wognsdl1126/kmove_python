import time
input("엔터를 누르고 20초를 셉니다.:")
strart = time.time()
print("20초 후에 다시 엔터를 누릅니다.")
input('')
end = time.time()
result = end - strart
print("실제시간: ",result, "초")
print("차이",abs(20-result),"초")



