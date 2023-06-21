##############
# 1st Task
##############

def get_char_count(string):
    chars = {}
    string = string.replace(" ", "")
    for char in string:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars

try: 
    input = str(input("Enter word or multyple words: "))
    print(get_char_count(input))
except ValueError:
    print("Wrong input")

##############
# 2nd Task
##############

def get_common_elements(seq1, seq2, seq3):
    set1 = set(seq1)
    set2 = set(seq2)
    set3 = set(seq3)
    common = set1.intersection(set2, set3)

    return tuple(common)

print(get_common_elements("abcf",['a','b', 'f'],('b','c', 'f')))

##############
# 3rd Task
##############

def is_pangram(text):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    lower = text.lower()
    mytext_set = set(lower.replace(" ", ""))
    
    return alphabet.issubset(mytext_set)

assert is_pangram('abcdefghijklmnopqrstuvwxyz') == True
assert is_pangram('a') == False

try: 
    text_input = str(input("Enter word or multyple words: "))
    print(is_pangram(text_input))
except ValueError:
    print("Wrong input")