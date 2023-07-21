squares = [1, 4, 9, 16, 25]
print(squares[0])   # 1
print(squares[2])   # 9
print(squares[-1])  # 25
print(squares[:])   # [1, 4, 9, 16, 25]

squares2 = squares + [36, 49, 64, 81, 100]
print(squares2)     # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']

print(letters)      # ['a', 'b', 'C', 'D', 'E', 'f', 'g']

letters[2:5] = []
print(letters)      # ['a', 'b', 'f', 'g']
print(len(letters))

