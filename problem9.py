# Chapter 4: exercise 6

# rewrite the pay computation problem from chapter 3 with time and a half overtime and 
# create a function called computepay which takes two paramaters (hour, rate)


def computepay(hours, rate):
    if hours <= 40:
        print(f"Your pay this week is ${hours * rate} dollars")

    elif hours >40:
        print(f"Your weekly check is ${((hours - 40) * rate * 1.5) + (hours * rate)} dollars") 

computepay(40,10)      # this is how you call a function in python
computepay(55,10)
computepay(32,10)


# logic for problem 9

# A function in python is basically a way to break down code into smaller reusable pieces, 
# firstly we named the function and gave it the paramaters hours and rate, 
# because we already defined the paramaters within the brackets of the function we no longer need  a input statement.

# The second line of code only calculates working hours up to 40 hours a week 
# then prints out the weekly pay

# while the elif statement handles the overtime payments

# lastly to call a function, use  the function-name() 
