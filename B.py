

a = 10
print(a)
b = '문자'
print(b)
print()

a, b, c = "이순신", "홍길동", "강감찬"
print(a + ", " + b + ", " + c)
print()

d = e = f = "30세"
print(d)
print(e)
print(f)

h = "member variable"
def m():
    #h = "local variable"
    #global h
    #print(h)

    global h   # global은 함수 내의 지역 변수를 멤버 변수로 만들어준다
    h = "What is this?"

m()
print(h)  #member variable


def m1():
    global a
    a = "유관순"
m1()
print(a)