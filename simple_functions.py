# python code 

# Exercise 1 : create a function that checks two numbers and returnes true if one of the numbers is 100
#              or if the sum of the two numbers is 100.



def keepin_it_100(num1, num2):


    if num1 == 100 or num2 == 100:
        return True 
    elif num1 + num2 == 100 :
        return True
    else:
        return False  




print(keepin_it_100(100, 3))
print(keepin_it_100(28, 100))

print(keepin_it_100(12, 16))
print(keepin_it_100(825, 1345))

print(keepin_it_100(30, 70))
print(keepin_it_100(50, 50))


# the solution should print ture(twice), false(twice), then true(twice) agian.

