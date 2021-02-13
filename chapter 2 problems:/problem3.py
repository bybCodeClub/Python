# python for everybody.
# Chaper 2 : Exercises  # 3

# Write a script that prompts a user to input the amount of hours worked in a week along with the hourly rate
# then compute the gross pay.

work_hours = int(input("How many hours did you work this week? "))

pay_rate   = float(input("How much do you make an hour? "))

paycheck = (work_hours * pay_rate)

print(f"You made ${paycheck} dollars this week" )



# logic

# first we need to prompt/ ask the user the amount of hours worked in a week with an input statement then store it in a variable. 
# side note to avoid a syntax error use int first the input 

# Second we need how much money they make an hour and aslo store that number in a variable

# third we multiply the two number together to get the weekly pay

# lastly print out the statement.



