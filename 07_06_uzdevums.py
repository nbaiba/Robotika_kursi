import datetime

# ###
# # 1st task
# ###
year_now = datetime.datetime.now().year

# # ask name
name = input("Whats your name? => ")

# # ask age, asign to int
age = int(input(f"Nice to meet you {name} how old are you? => "))

# # print with calculations 
print(f"{name}, after {100 - age} years you will be 100 years old, and that will be in year {100 - age + year_now}")

# ###
# # 2nd task
# ###

# # ask measurements
width = int(input("What is width of room? => "))
height = int(input("What is height of room? => "))
length = int(input("What is length of room? => "))

# calculate and print volums

print(f"Total volume is {width * height * length}")


###
# 3rd task
###

# ask temperature, asign to variable
temperature = int(input("Whats temperature right now in Celsius? => "))

# print farenheits with calculation
print(f"In Farenheit that will be {32 + temperature * (9/5)}")