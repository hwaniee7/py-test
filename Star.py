"""
기본적으로 print() 함수는 출력된 내용 끝에 개행 문자를 추가하여 커서를 다음 줄로 이동시킨다.
end 매개변수를 지정함으로써 이 기본 동작을 변경할 수 있다.
end는 print() 함수의 선택적 매개변수로서 출력 결과의 끝에 기본적으로 추가되는 개행 문자인 \n 대신에 어떤 문자(들)를 추가할지를 결정한다.
여기서는 star 또는 blank를 출력한 후 커서를 같은 줄에 그대로 두고 다음 문자를 바로 뒤에 출력하게 한다.

"""

star: str = "* "
blank: str = "  "

for i in range(4):
    for j in range(4):
        if i >= j:
            print(star, end="")
        else:
            print(blank, end="")
    print()
print()
for i in range(4):
    for j in range(4):
        if i <= j:
            print(star, end="")
        else:
            print(blank, end="")
    print()
print()
'''
for i in range(4):
    print(i,"",end="")
print()
for j in range(3,-1,-1):
    print(j, "", end="")
print()
'''
for i in range(4):
    for j in range(3,-1, -1):
        if i <= j:
            print(star, end="")
        else:
            print(blank, end="")
    print()
print()
for i in range(3,-1,-1):
    for j in range(4):
        if i <= j:
            print(star, end="")
        else:
            print(blank, end="")
    print()
print()



