import sys

print(f"The name of this Python file is '{sys.argv[0]}'")
print(f"The first argument passed in to my script was: '{sys.argv[1]}'")
print(f"The second argument passed in to my script was: '{sys.argv[2]}'")
print(f"The third argument passed in to my script was: '{sys.argv[3]}'")


# in console type: python3 collect_input.py apples pears oranges 
# will display
# The name of this Python file is 'collect_input.py'
# The first argument passed in to my script was: 'apples'
# The second argument passed in to my script was: 'pears'
# The third argument passed in to my script was: 'oranges'