magicians = ['allice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(magician.title() + ", that is a great trick!")

#test

meats = ['pork', 'beef', 'mutton']
for meat in meats:
    print("I like " + meat)
print("I really love them.")

#4.3 create value list
for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(0, 20, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)