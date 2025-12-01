# Please write a program which asks the user for a number of days.
# The program then prints out the number of seconds in the amount of days given.


number_of_days = int(input("How many days? "))

seconds_to_days = number_of_days * 86400

print(f"Seconds in that many days: {seconds_to_days}")
