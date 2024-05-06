received = str(input("Enter a word: ")).lower().replace(" ", "")
if received == received[::-1]:
    print("OK")
else:
    print("NOT")
