alian_0 = {'color': 'green', 'points': 5}
print(alian_0['color'])
print(str(alian_0['points']))
new_points = alian_0['points']
print("You just earned " + str(new_points) + " points!")
print(alian_0)

alian_0['x_position'] = 0
alian_0['y_position'] = 10

print(alian_0)

alian_0['color'] = 'yellow'
print(alian_0)

alian_0['speed'] = 'medium'
if alian_0['speed'] == 'slow':
    x_increment = 1
elif alian_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alian_0['x_position'] = alian_0['x_position'] + x_increment
print("New x-postion: " + str(alian_0['x_position']))

alian_0['speed'] = 'fast'
if alian_0['speed'] == 'slow':
    x_increment = 1
elif alian_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alian_0['x_position'] = alian_0['x_position'] + x_increment
print("New x-postion: " + str(alian_0['x_position']))

del alian_0['points']
print(alian_0)
print("===================================================")
wife = {
    'first_name': 'bao',
    'last_name': 'rongrong',
    'age': '30',
    'city': 'shanghai',
}

print(wife)

for key, value in wife.items():
    print("\nKey: " + key)
    print("\nValue: " + value)

favorite_languages = {
    'joe': 'python',
    'joyce': 'c',
    'joey': 'c++',
    'sarah': 'java',
    'Phil': 'python',
}

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
            language.title())

print("==============6.3.2=====================")
print("\n")

for name in favorite_languages.keys():
    print(name.title())

print("\n")

friends = ['joe', 'joyce']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() + ", I see your favorite language is "
                + favorite_languages[name].title())

print("\n")
print("==============6.3.2=====================")
print("\n")

for name in sorted(favorite_languages.keys()):
    print(name.title())

for language in favorite_languages.values():
    print(language)
print("\n")

for language in set(favorite_languages.values()):
    print(language)

for item in favorite_languages.items():
    print(item)

print("\n")
print("==============6-5 test=====================")
print("\n")

rivers = {'nile': 'egypt',
          'changjiang': 'china',
          'amazon': 'brazil',}
for key, value in rivers.items():
    print("The " + key.title() + " runs through " + value.title())

for key in rivers.keys():
    print(key)

for value in rivers.values():
    print(value)

print("\n")
print("==============6-6 test=====================")
print("\n")

friends = ['joe', 'joyce']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() + ", thanks for your investigation.")
    else:
        print("Hi " + name.title() + ", can I invite you to take an investigation?")