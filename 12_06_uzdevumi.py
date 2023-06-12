############
# Task Nr.1
############

for n in range(101):
    text = ''
    if(n % 7 == 0 and n % 5 == 0):
        text += 'FizzBuzz'
    elif(n % 5 == 0):
        text += 'Fizz'
    elif(n % 7 == 0):
        text += 'Buzz'
    else:
        text += str(n)
    print(text, end=", ")
print('\n')

############
# Task Nr.2
############

is_valid = False
while not is_valid:
    try:
        height = int(input("Enter height (Number) of a tree: "))
        is_valid = True
    except ValueError:
        print("Enter NUMBER")

line_width = 1

if is_valid:
    for n in range(height):
        spaces = height - n - 1
        print(" " * spaces + "*" * line_width + " " * spaces)
        line_width += 2

############
# Task Nr.3
############

for n in range(1, 16):
    if (n != 1) and ((n % 2 != 0 and n % 3 != 0) or n == 2 or n == 3):
        print(f"{n} is prime number")
    else:
        print(f"{n} is NOT prime number")