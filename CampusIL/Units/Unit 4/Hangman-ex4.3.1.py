guess = str(input("Guess a letter: "))

if len(guess) > 1 and guess.isalpha() != 1:
    print("E3")
elif len(guess) > 1:
    print("E1")
elif guess.isalpha() != 1:
    print("E2")
else:
    print(guess.lower())
