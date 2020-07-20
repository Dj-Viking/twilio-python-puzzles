import sys


list_items = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]]

print("These are the items on my grocery list:")
for index, item in enumerate(list_items, start=1):
    string_to_print = f"{index}. {item}"
    print(string_to_print)