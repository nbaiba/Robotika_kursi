import datetime

# ###
# # 1st task
# ###
year_now = datetime.datetime.now().year

# # ask name
name = input("Whats your name? => ")

# # ask age, asign to int
age = int(float(input(f"Nice to meet you {name} how old are you? => ")))

# # print with calculations 
print(f"{name}, after {100 - age} years you will be 100 years old, and that will be in year {100 - age + year_now}")

# ###
# # 2nd task
# ###

# # ask measurements
width = float(input("What is width of room? => "))
height = float(input("What is height of room? => "))
length = float(input("What is length of room? => "))

# calculate and print volums
print(f"Total volume is {round(width * height * length, 2)}")


###
# 3rd task
###

# ask temperature, asign to variable
temperature = float(input("Whats temperature right now in Celsius? => "))

# print farenheits with calculation
print(f"In Farenheit that will be {round(32 + temperature * (9/5), 2)}")