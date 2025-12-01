# Please write a program which estimated a user's typical food spend


time_week_eating = float(input("How many times a week do you eat at the student cafeteria? "))

lunch_price = float(input("The price of a typical student lunch? "))

weekly_spent_groc = float(input("How much money do you spend on groceries in a week? "))


weekly_spend = time_week_eating * lunch_price + weekly_spent_groc

daily_spend = weekly_spend / 7






print("Average food Expenditure:")
print(f"Daily: {daily_spend} euros")
print(f"Weekly: {weekly_spend} euros")
