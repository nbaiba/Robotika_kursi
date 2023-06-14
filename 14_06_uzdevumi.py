##################
# 1st task
##################

is_input_correct = None
while not is_input_correct:
    user_name = str(input("Whats your name? => "))
    if user_name.isalpha() and not user_name.isspace():
        is_input_correct = True
        print(user_name[::-1].title())
    else:
        print("Wrong input, only letters allowed with no spaces")

##################
# 2nd task
##################

while True:
    user_input = str(input("Enter some name or more names: "))
    guess = str(input("Enter alphabet character: "))

    if (user_input.replace(" ", "").isalpha() and not user_input.isdigit()) and (guess.isalpha() and not guess.isdigit() and len(guess) == 1):
        masked = ''
        for i in user_input:
            if i.isspace():
                masked += ' '
            elif i == guess:
                masked += i
            else:
                masked += '*'
        print(masked)
        break
    else:
        print("Something went wrong")
        continue

##################
# 3rd task
##################


while True:
     user_input = str(input("Enter text: ")) 
     if (user_input.replace(" ", "").isalpha() and not user_input.isdigit()):
        indexes = []

        indexes.insert(0, user_input.find("nav"))
        indexes.insert(1, user_input.find("slikts"))
        if indexes[0] > 0 and indexes[1] > 0:
            replacable_text = user_input[indexes[0]:indexes[1] + len('slikts')]
            print(user_input.replace(replacable_text, "ir labs"))
            break
     else:
        print("Something went wrong")
        continue
