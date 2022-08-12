# some basic loops in python 


# the basic for loop structure in python.
for number_of_prints in range(5):
    print("please print 5 imes", number_of_prints )

# So basically if you want a action printed a certain number of times this simple code block can achive that goal. 




# nested for loop syntax 
for i in range(3):
    for j in range(2):
        print(i,j)
        

# To explain this 'i' is the first and outer loop, as long as 'i' is under the range(3) the loop will proceed to the interior loop.

# here, as long a 'j' is under 2 the loop will continue, so with the way this is coded there will always be 2 operations within the interior loop
# because 0 is less then 2 and so is 1, once it gets out of range it will trigger the outer loop again and the process will repeate.

# the inner loop "j" will finish all of its iterations before fininshing one of the "outer loop i"




# This nested loop makes a 2D array.

myArray = []

for i in range (5, 0):
    myArray.push(i)
    print("watch the numbers go down")
    i = i - 1


# using loops to create shapes 
rows    = int(input("how many rows:"))
columns = int(input("how many columns:"))
symbol  = input("enter a shape")


for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()    

# quick simple explanation to really help you get whats going on, the first loop "i" get excuted once,
# while the second loop "j" get excuted until completion, which is the range() you set.
# so if "i" is 12 and "j"  is 3 ,  you will have 12 rows of 3. 
