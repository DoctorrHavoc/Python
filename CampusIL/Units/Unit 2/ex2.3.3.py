full_entered_num = int(input("Enter three digits (each digit for one pig): "))
num_first_digit = int(full_entered_num / 100)
num_second_digit = int(full_entered_num % 100 / 10)
num_third_digit = int(full_entered_num % 100 - num_second_digit * 10)
total_bricks = num_first_digit + num_second_digit + num_third_digit
print(total_bricks)
print(int(total_bricks / 3))
print(total_bricks % 3 == 0)
