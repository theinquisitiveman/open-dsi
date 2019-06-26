import sys

CAPITALS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
CAPITAL_SUGGESTIONS = {char.lower(): char for char in CAPITALS}

LOWERS = CAPITALS.lower()
LOWERS_SUGGESTIONS = {char.upper(): char for char in LOWERS}

DIGITS = '0123456789'
DIGITS_SUGGESTIONS = {'e': '3', 'o': '0', 's': '5', 't': '7', 
                      'E': '3', 'O': '0', 'S': '5', 'T': '7',
                      'a': '4', 'l': '1', 'i': '1',
                      'A': '4', 'L': '1', 'i': '1'}

SYMBOLS = '^!#$?-@'
SYMBOLS_SUGGESTIONS = {'a': '@', 'i': '!', 'l': '!', 's': '$',
                       'A': '@', 'I': '!', 'L': '!', 'S': '$',
                       'm': '^^',
                       'M': '^^'}


def check_password(password):
    return (contains_one_of_char(password, CAPITALS) and
            contains_one_of_char(password, LOWERS) and
            contains_one_of_char(password, DIGITS) and
            contains_one_of_char(password, SYMBOLS))

def contains_one_of_char(password, characters):
    for char in characters:
        if char in password:
            return True
    return False

def suggest_password(password, max_iter=5):
    n_iter = 0
    while not check_password(password) and n_iter < max_iter:
        if not contains_one_of_char(password, CAPITALS):
            password = suggest_replacement(password, CAPITAL_SUGGESTIONS)
        if not contains_one_of_char(password, LOWERS):
            password = suggest_replacement(password, LOWERS_SUGGESTIONS)
        if not contains_one_of_char(password, DIGITS):
            password = suggest_replacement(password, DIGITS_SUGGESTIONS)
        if not contains_one_of_char(password, SYMBOLS):
            password = suggest_replacement(password, SYMBOLS_SUGGESTIONS)
        n_iter = n_iter + 1
    return password

def suggest_replacement(password, replacement_dict):
    for char in password:
        if char in replacement_dict:
            replacement = replacement_dict[char]
            password = password.replace(char, replacement, 1)
            break
    return password

if __name__ == '__main__':
    password = sys.argv[1]
    if check_password(password):
        print("Password is OK!")
    else:
        suggestion = suggest_password(password)
        if check_password(suggestion):
            print("How about this: ", suggestion)
        else:
            print("Warning: Could not find a substitution that works!")
