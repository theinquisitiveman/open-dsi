import sys

CAPITALS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
CAPITALS_SUBSTITUTIONS = {char: char.lower() for char in CAPITALS}

LOWERS = 'abcdefghijklmnopqrstuvwxyz'
LOWERS_SUBSTITUTIONS = {char: char.upper() for char in LOWERS}

DIGITS = '0123456789'
DIGITS_SUBSTITUTIONS = {
    'o': '0', 'a': '4', 'e': '3', 's': '3',
    'O': '0', 'A': '4', 'E': '3', 'S': '3'
}

SYMBOLS = '^!#$?-@'
SYMBOLS_SUBSTITUTIONS = {
    'a': '@', 'i': '!', 's': '$', 'm': '^^',
    'A': '@', 'I': '!', 'S': '$', 'M': '^^'
}


def is_valid(password):
    return (has_at_least_one_of(password, CAPITALS) and
            has_at_least_one_of(password, LOWERS) and 
            has_at_least_one_of(password, DIGITS) and 
            has_at_least_one_of(password, SYMBOLS))

def has_at_least_one_of(password, characters):
    for letter in password:
        if letter in characters:
            return True
    return False

def make_substitutions(password, characters, substitution_dictionary):
    if not has_at_least_one_of(password, characters):
        for char in password:
            if char in substitution_dictionary:
                password = password.replace(
                    char, substitution_dictionary[char], 1)
                break
    return password

password = sys.argv[1]
if is_valid(password):
    print("Your password {} is valid.".format(password))
else:
    password = make_substitutions(password, CAPITALS, LOWERS_SUBSTITUTIONS)
    password = make_substitutions(password, LOWERS, CAPITALS_SUBSTITUTIONS)
    password = make_substitutions(password, DIGITS, DIGITS_SUBSTITUTIONS)
    password = make_substitutions(password, SYMBOLS, SYMBOLS_SUBSTITUTIONS)
    if is_valid(password):
        print("How about this: ", password)
    else:
        print("Error: That didn't work!")
