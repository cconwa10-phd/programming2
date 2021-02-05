Height = input("Height")
Weight = input("Weight")
BMI = float(Weight)/float(Height)**2
print(BMI)

Height_feet = input("Height (ft)")
Height_inches = input("Height (in)")
Weight_pounds = input("Weight (lbs)")
Height_m = (float(Height_feet)*12 + float(Height_inches))/39.37
Weight_kg = float(Weight_pounds)/2.205
BMI_New = Weight_kg/Height_m**2
print(BMI_New)


