import datetime

# ###
# # 1st task
# ###
year_now = datetime.datetime.now().year

# ask name
name = input("Whats your name? => ")

# ask age, asign to int
age = int(float(input(f"Nice to meet you {name} how old are you? => ")))

# print with calculations 
print(f"{name}, after {100 - age} years you will be 100 years old, and that will be in year {100 - age + year_now}")

# ###
# # 2nd task
# ###

# ask measurements
width = float(input("What is width of room? => "))
height = float(input("What is height of room? => "))
length = float(input("What is length of room? => "))

# calculate and print volums
print(f"Total volume is {round(width * height * length, 2)}")


# ###
# # 3rd task
# ###

# ask temperature, asign to variable
temperature = float(input("Whats temperature right now in Celsius? => "))

# print farenheits with calculation
print(f"In Farenheit that will be {round(32 + temperature * (9/5), 2)}")

# ###
# # 4th task
# ###

# ask body temperature
temperature = float(input("Whats your body temperature? => "))
 
# check temperature and give feedback
if temperature < 35:
    print("Isn't it too cold?")
elif temperature >= 35 and temperature <= 37:
    print("You are ok")
else:
    print("You might be sick")

# ###
# 5th task
# ###

# ask for salary amount and years worked
monthly_salary = float(input("What is your salary? => "))
years_worked = int(input("How many years have you worked in company? => "))

# calculate bonus
bonus = round((years_worked - 2) * (15/100) * monthly_salary, 2)

# print message using if else
if years_worked > 2:
    print(f"Tour bonus: {bonus}")
else:
    print("Not enought work done in this company")
