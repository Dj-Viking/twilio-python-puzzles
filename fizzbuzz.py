import sys

# assign variable to the sys.argv list array
inputs = sys.argv
# clear the sys.argv list item that contains the file name
inputs.pop(0)
# check the inputs list
# print(inputs)



    # if int(item % 15 == 0):
    #   print("fizzbuzz")

# loop through the inputs list and perform an action on each input argument
# print("here are the input numbers")
for index, item in enumerate(inputs, start=1):
# convert the input numbers into integers from string inputs
    if int(item) % 3 == 0 and int(item) % 5 == 0:
        print("fizzbuzz")
    elif int(item) % 5 == 0:
        print("buzz")
    elif int(item) % 3 == 0:
        print("fizz")
    else:
        print(int(item))




