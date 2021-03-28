alien_0 = {'color': 'red', 'points': 5}
favourite_language = {'jen': 'Python',
                      'sarah': 'C',
                      'edward': 'ruby',
                      'wsp': 'Python'}
print("your points is :" + str(alien_0['points']))

for key, value in alien_0.items():
    print(key + ":" + str(value))
print("\n")
for name in favourite_language.keys():
    print(name)
print("\n")
for name in sorted(favourite_language.keys()):
    print(name)
print("\n")
for language in favourite_language.values():
    print(language)
print("\n")
for language in set(favourite_language.values()):
    print(language)

list_test = []
list_test.append(alien_0)
list_test.append(favourite_language)
for test in list_test[:]:
    print(test)

favourite_language_list = {'wsp': ['Java', 'Python'],
                           'mmf': ['C']}
for name, favourite_languages in favourite_language_list.items():
    print(name + "'s favourite language are:")
    for language in favourite_languages:
        print(language)
