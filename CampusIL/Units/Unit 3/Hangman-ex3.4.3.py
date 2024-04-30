received_string = str(input("Please enter a string: "))
middle_point = int(len(received_string) / 2)
print(received_string[:middle_point].lower() + received_string[middle_point:].upper())
