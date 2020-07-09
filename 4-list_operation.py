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

digits = [1, 2, 3, 5, 99, 65, 85, 48, 65]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1, 11)]
print(squares)

for value in range(1, 21):
    print(value)

number = list(range(1, 1000001))

# for value in range(1, 1000001):
#    print(value)

print(min(number))
print(max(number))
print(sum(number))

odd = []
for value in range(1, 20, 2):
    odd.append(value)
print(odd)

number = list(range(3, 30, 3))
print(number)

cubes = []
for value in range(1, 11):
    cube = value**3
    cubes.append(cube)
print(cubes)

cubes = [value**3 for value in range(1, 11)]
print(cubes)

players = ['aaron', 'brian', 'charles', 'dright', 'elian', 'fox', 'grey']
print(players[1:4])
print(players[3:])
print(players[-3:])
friends = players[:]
friends.append('haro')
print(friends)

print("The first items in this list are:")
print(players[:3])

print("Three items from the middle of the list are:")
print(players[2:5])

print("The last items in this list are:")
print(players[-3:])

food = ("rice", "fish", "crab", "pork", "beef")
for f in food:
    print(f)

food = ("muton", "fish", "crab", "pork", "beef")
for f in food:
    print(f)