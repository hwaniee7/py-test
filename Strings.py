
name = "이순신"
age = 30
addr = "서울시"

print("Hello, My Name is", name, "and I'm", age,".\n I live in ", addr)


def introduce(name: str, age:int, addr:str) -> str:
    return 'Hello, My Name is ' + name + ' and I\'m ' + str(age) +  '.\n I live in ' + addr


print(introduce("홍길동", 25, "부산시"))


sentence = "Hello World! What a beautiful World!"
print(sentence[0])
print(sentence[10])
print(sentence[-1])
print(sentence[:5])
print(sentence[6:12])
print(sentence[-6:])
print(sentence[0:6] + sentence[-6:])

#Python strings cannot be changed — they are immutable.
#sentence[0] = "A"   # Class 'str' does not define '__setitem__', so the '[]' operator cannot be used on its instances

print("Oh!", sentence[6:12])
print(len(sentence))
print(sentence.lower())
print(sentence.upper())

sentence = "  Hello World!   "
print(sentence.strip())


