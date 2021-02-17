# problem 12
# Chapter 6 exersice 5 

# take the followiing python code that stores a string, 
# use find and string slicing to extract the portion of the string after the colen character,
# then use the float function to convert the extracted string into a float number.


original_string = "X-DSPAM-Confidence:0.8475"            
find_colen = original_string.find(":")            # this gives us the index location of the colen within this string which is at 18 
print(find_colen)

part_to_convert = float(original_string[19:])     # Here we are taking everything after the colen and converting it into a float
print(part_to_convert)

checkingWork = (part_to_convert + 99) # This is just to make sure that we can add/ subtract from this variable, It should equal 99.8475
print(checkingWork) 

