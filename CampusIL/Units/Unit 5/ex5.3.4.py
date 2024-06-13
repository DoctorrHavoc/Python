def last_early(my_str):
    print(my_str[-1:].lower() in my_str[:-1].lower())


last_early("happy birthday")
last_early("best of luck")
last_early("Wow")
last_early("X")
