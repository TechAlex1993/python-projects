# Python weight convertor

weight = float(input("Weight: "))  # Weight in pounds
unit = input("(K)g or (L)bs: ")  # Unit of weight

if unit == "K" or unit == "k":
    weight = weight * 2.205
    unit = "Lbs"
elif unit == "L" or unit == "l":
    weight = weight / 2.205
    unit = "Kg"
else:
    print("Invalid unit")

print("Weight in", unit, ":", weight)
