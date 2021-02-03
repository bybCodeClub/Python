# Chapter 3:  exercise 2

# Simple try / except Error handling.
# Re-write the pay computation from problem 3 or 6 using try and except to handle potential non-numeric input by printing a graceful message to the user.


while True:
    try:
        work_hours = int(input("How many hours did you work this week? "))
        break

    except:
        print("Oops, Please only use numbers 1-9")



while True:
    try:
        pay_rate   = float(input("How much do you make an hour? "))
        break
    
    except:
        print("Oops, Please only use numbers 1-9")


paycheck = (work_hours * pay_rate)

if work_hours <= 40:
    print(f"Your weekly pay is ${paycheck} dollars")

elif work_hours > 40:
    overtime = ((work_hours - 40) * pay_rate * 1.5) + paycheck
    print(f"Your weekly check is ${overtime} dollars") 



# notes
# 
# The only difference between problem 6 and problem 7  is the try / except block to prevent users from typing in string when asked for their hour or pay rate 
# abd crashing the python program.    
