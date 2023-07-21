animals = ['dog', 'cat', 'lion', 'tiger', 'monkey']

for animal in animals:
    print(animal)

print()

for i in range(5):
    print(i)

print()

numList = list(range(5, 10))
print(numList)  # [5, 6, 7, 8, 9]
print(range(5, 10))  # range(5, 10)
numList = list(range(5, 20, 3))
print(numList)  # [5, 8, 11, 14, 17]
print()
for i in range(len(animals)):
    print(i, animals[i])

print(sum(range(5, 20, 3))) # 55
