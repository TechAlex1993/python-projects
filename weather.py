unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C" or unit == "c":
    temp = temp * 9 / 5 + 32
    print(f'Temperature in Fahrenheit: {temp}')
elif unit == "F" or unit == "f":
    temp = (temp - 32) * 5 / 9
    print(f'Temperature in Celsius: {temp}')
else:
    print("Invalid unit")

