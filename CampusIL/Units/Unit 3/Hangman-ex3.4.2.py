received_string = str(input("Please enter a string: "))
first_index = received_string[0:1]
print(first_index + received_string[1:].replace(first_index, "e"))
