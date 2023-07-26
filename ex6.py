# A variable holds the value of 2 but in binary 
types_of_people = 10
# A variable that holds an f-string that will insert the value of the 'types_of_people' variable
x = f"There are {types_of_people} types of people."

# A variable that holds the string "binary" 
binary = "binary"
# A variable that holds the string "don't"
do_not = "don't"
# A variable that holds an f-string that will insert the values of the string variables'binary' and 'do_not'
y = f"Those who know {binary} and those who {do_not}."

# Print the f-string contained in the variable 'x'
print(x)
# Print the f-string contained in the variable 'y'
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
