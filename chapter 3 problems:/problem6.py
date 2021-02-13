# Chapter 3:  exercise 1

# Re-write the pay computation from problem 3 to give the employee an hourly rate for hours worked above 40 hours.

work_hours = int(input("How many hours did you work this week? "))
pay_rate   = float(input("How much do you make an hour? "))
paycheck = (work_hours * pay_rate)



if work_hours <= 40:
    print(f"Your weekly pay is ${paycheck} dollars")

elif work_hours > 40:
    overtime = ((work_hours - 40) * pay_rate * 1.5) + paycheck
    print(f"Your weekly check is ${overtime} dollars") 
    


# Logic  

# Step 1: I just copied and pasted the same problem from exercise 3 and modified the code
#         I added a simple if statement to set the regular weekly work hours to 40  

# Step 2: then used the elif statement to calculate the overtime.
