#Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds?( k or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "kgs."    
else:
    print(f"{unit} is not valid") 

print(f"Your weight is: {weight}{unit}")    
# print(f"Your weight is: {round(weight, 1)}{unit}")    rounded t 1