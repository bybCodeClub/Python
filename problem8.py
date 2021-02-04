# write a file that prompts for a score between 0 - 100
# if score is out of range print an error message, and convert the numbers to a letter grade
# print grades using the following table 

# >= 90  A+
# >= 80  A
# >= 75  B+
# >= 70  B
# >= 60  c
# >= 50  D
# < 50   F


while True:
    try:
        grades = int(input("Enter grades here: "))
        break

    except:
        print("use 1-9 numbers")    


if grades >= 90:
    print("A+ \nCongradulations on all your great work, keep it up")
elif grades >= 80:
    print("B+ \nWell you not as dumb as you look, but still not smart enough to get an A+, better luck next time")
elif grades >= 75:
    print("B+ \nwith grades like this, your well on your way to the world of middle managment, congrats")
elif grades >= 70:
    print("B \nYou barely made it into the group of kid with a future, If you don't want to be flipping burgers the rest of you life \n we suggest you start studying more") 
elif grades >= 60:
    print("C \nwith grades like this you be lucky if you get into community college.")
elif grades >= 50:
    print("D \nwow you passed, looks like you not a complete retard,")
elif grades < 50:
    print("F+ \nWell Mcdonalds and Wal-mart are always hiring, you might as well apply because you wasting you time here.")
