# Please write a program which asks the user for their name and year of birth.
# The program then prints out a message as follows


name = input("What is your name? ")

year_born = int(input("Which year were you born? "))

expected_age = 2021 - year_born # should be 2025 but for the sake of the excercise

print(f"Hi {name}, you will be {expected_age} years old at the end of the year 2021")
