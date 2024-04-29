all_digit = int(input("Enter three digits (each digit for one pig): "))
digit1 = int(all_digit / 100)
digit2 = int(all_digit % 100 / 10)
digit3 = int(all_digit % 100 - digit2 * 10)
total_bricks = digit1 + digit2 + digit3
print(total_bricks)
print(int(total_bricks / 3))
print(total_bricks % 3 == 0)
