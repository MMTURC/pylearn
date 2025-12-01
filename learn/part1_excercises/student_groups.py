# Please write a program which asks for the number of students on a course and the desired group size.

import math

students_in_course = float(input("How many students on the course? "))

desired_group_size = float(input("Desired group size? "))

result = students_in_course / desired_group_size

print(f"Number of groups formed: {math.ceil(result)}")


# Notes:
#
# Had to google how to round up a number in python because the excercise expected a rounded number from the calculation
#
# So if we got a 2.6 math.ceil will round the result to 3 and you get the point
# It actually worked so...
