################
# 1st Task
################

input_list = []
while True:
    user_input = input("Enter number (or 'q/Q' to quit): ")
    if user_input.lower() == 'q' or user_input.upper() == 'Q':
        break
    try:
        float_input = float(user_input)
        input_list.append(float_input)
        listSum = sum(input_list)
        print(f"Total sum: {listSum}")
        print(f"Average: {listSum / len(input_list)}")
        print(f"List: {input_list}")
        numbers = list(set(input_list))
        print(f"3 largest numbers: {sorted(numbers, reverse=True)[:3]}")
        print(f"3 smallest numbers: {sorted(numbers)[:3]}")
        print("####################################")
    except ValueError:
        print('Invalid input')

################
# 2nd Task
################

try:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    list = []
    for number in range(first_number, second_number + 1):
        list.append(f"{number} cubed: {number ** 3}")
    for text in list:
        print(text)
except ValueError:
    print("Invalid input")

################
# 3rd Task
################

try:
    text = input("Enter text: ")
    sentence = text.split()
    new_list = [word[::-1].lower() for word in sentence]
    new_list[0] = new_list[0].capitalize()
    new_sentence = " ".join(new_list)
    print("New sentence: ", new_sentence)
except ValueError:
    print("Invalid input")