def add(a,b):
    return a+b

print(add(5,4))
c = add(5,6)
print(c)

def add_many(*a):
    result = 0
    print(type(a))
    print(a)
    for i in a:
        result=result+i
    return result

total = add_many(1,2,3,4,5,6,7,8,9,10)
print(total)


def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)

def add_and_mul(a,b):
    return a+b, a*b

add,mul = add_and_mul(3,6)
print(type(add))
print(type(mul))
print(add)
print(mul)

def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다."%name)
    print("나이는 %d살입니다."%old)
    if man:
        print("남자입니다")
    else:
        print("여자입니다.")

say_myself("박응용",27)
say_myself("박응용",27,False)
say_myself("박응용",27,True)