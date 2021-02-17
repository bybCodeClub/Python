#
# problem 12
# Chapter 6 exersice 5 

# take the followiing python code that stores a string, 
# use find and string slicing to extract the portion of the string after the colen character,
# then use the float function to convert the extracted string into a float number.


original_string = "X-DSPAM-Confidence:0.8475"
find_colen = original_string.find(":")
print(find_colen)

part_to_convert = float(original_string[19:])
print(part_to_convert)

checkingWork = (part_to_convert + 99) # which should equal 99.8475
print(checkingWork) 

