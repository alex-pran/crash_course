squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

print("==========1============")

squares = []
for value in range(3, 11, 1):
    square = value ** 2
    squares.append(square)

print(squares)

print("==========2============")

squares = [value ** 2 for value in range(1,11)]
print(squares)