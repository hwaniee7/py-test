a = 12
b = 3

print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print(a % b)    # 0
print(a ** b)   # 1728
print(a // b)   # 4

a = 17
b = 3
print(a / b)    # 5.666666666666667


def add_numbers(x: int, y: int) -> int:
    return x + y


result1 = add_numbers(10, 5)
print(result1)  # 15
print(add_numbers(20, 20))  # 40

a = 20
b = 10.5
c = 5j
print(type(a))
print(type(b))
print(type(c))

# casting - int()
a1 = int(a)
a2 = int(b)
a3 = int("3")
#a4 = int(c) # c의 타입이 complex여서 불가
print(a1)
print(a2)
print(a3+1)
print()

# casting - float()
b1 = float(a)
b2 = float(b)
b3 = float("3")
print(b1)
print(b2)
print(b3)
print()

# casting - str()
c1 = str("가")
c2 = str(a)
c3 = str(b+1)
c4 = str(c) #가능!
print(c1)
print(c2)
print(c3)
print(c4)

