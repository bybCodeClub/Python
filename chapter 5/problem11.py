# chapter 5: Exercise 1

# write a program which repeatedly asks the user for a numbers until user enters "done". 
# once done is entered, print out the total, count and average of the numbers. If the user enter anything other then a number,
# detect their mistake using try & except and print an error massage and skip to the next number.

# enter a number
# enter a number
# enter a number: inproper data
# enter a number : done
# total(99) , 8, 33.333

print("Enter any number \nTo exit type exit")
num = [] 

while num != "exit":
    try:
        imput = (input("Enter a number: "))
        number = int(imput)
        num.append(number) 
            
            

    except ValueError:
        if imput == "exit":
            print((sum(num)))
            print(number)
            print(sum(num) / len(num))
            break
        else:
            print("1 - 9 symbols only please")
            


# coding logic: 
# first we set num as an empty list variable outside the while loop 
# Then we create a while loop, setting the condition that if "exit" is entered as in input to exit the loop

# The try block
# The first vairable asks you to input a number... This input was purposfully not made an int to get around the value error in the except block
# The we made another vairable named number, that was in int() to make the input variable a int, without it messing up the except block. Remember if you int the input "exit"
# as the keyword that ends the loop, is going to be a problem because "exit" is a string not a int, which is why we created a secondary vairable. 
# Then lastly any number that is added to the number vairable is appended to the empty list.

# The except block:
# valueerror is the type of error we are accounting for, in case python runs into a valueError then we want python to handle it a certain way 
# In our case if the "exit" is typed in the we want to print out the sum of the list and the average number of that list.

# The the else statement handles any string values entered into a int list.
