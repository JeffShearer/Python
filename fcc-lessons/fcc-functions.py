# Max will look for most advanced letter in the alphabet when used on a string.

big = max('hiya')
print(big)

# Defining your own functions
def thing() :
    print('it\'s a thing!')
thing()

# custom functions with arguments and user input
lang = input('what language?')
name = input('name')
def greet(lang) :
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet(lang),name)

