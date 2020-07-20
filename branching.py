import sys
# import decimal

# dinner_name = sys.argv[1]

# if dinner_name == "tacos":
#     print("Tacos for dinner - right on!")
# elif dinner_name == "pizza":
#     print("Pizza - can't go wrong there!")
# else:
#     print("Okay - better than eing hungry amiright?")

# not sure how to do all the decimal numbers..
# this only deals with integers

num_one = float(sys.argv[1])
num_two = float(sys.argv[2])
sum_to_use = num_one + num_two

if sum_to_use <= 0:
    print("You have chosen the path of destitution.")
elif 1 <= sum_to_use <= 100:
    print("You have chosen the path of plenty.")
elif sum_to_use > 100:
    print("You have chosen the path of excess.")

