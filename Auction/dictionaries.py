programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again."}
# retreive value
programming_dictionary["Bug"]
# add a new key-value pair to the dictionary
programming_dictionary["Loop"] = "A block of code that is repeated until a certain condition is met."

# editting the dictionary
programming_dictionary["Bug"] = "A moth that flies around."
# loop through the dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

# wipe the loop out of the dictionary
programming_dictionary ={}
print(programming_dictionary)
