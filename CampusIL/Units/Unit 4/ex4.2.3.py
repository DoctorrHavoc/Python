temperature = str(input("Insert the temperature you would like to convert: ")).lower()
num = int(temperature[:-1])
if temperature[-1:] == "c":
    print(int((9 * num + (32 * 5)) / 5), "F", sep='')
else:
    print(int((5 * num - 160) / 9), "C", sep='')
