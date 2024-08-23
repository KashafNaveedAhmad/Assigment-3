
import math
import time

# Assignment-03
print("Let's start the assignment!!")

# Calculate your age based on the current year and your birth year.
# Age 
print("\nWe are going to calculate your age.\nBelow:")
birth_year=int(input("Enter your birth year:"))
current_year=int(time.strftime('%Y'))
age=current_year-birth_year
print("Your age based on your birth year is:",age,"years old.")


# Write a program that calculates the area of a rectangle using length and width variables.
# Area of a recatangle(length*width)
print("\nLet's calculates the 'Area of a rectangle'.\nBelow:")
length=float(input("Enter the lenght:"))
width=float(input("Enter the width:"))
area=length*width
print("The area of rectangle is:",area)


# Write a program that calculates the area of a circle.
# Area of a circle (Formula:(math.pi)*(radius**2))
print("\nLet's calculate the 'Area of Circle'.\nBelow:")
radius_of_circle=float(input("Enter the radius:"))
area_of_circle=((math.pi)*(radius_of_circle**2))
print("The area of circle is:",area_of_circle)


# Write a program that calculates the area of the cube.
# Area of a circle (Formula:6(a^2))
print("\nLet's calculate the 'Area of Cube'.\nBelow:")
side_of_cube=int(input("Enter the it's side:"))
area_of_cube=(6*(side_of_cube**2))
print("The area of cube is:",area_of_cube)


# Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.
# Fahrenheit to Celsius (Formula:(5/9)*(F-32))
print("\nWe are going to convert 'Fahrenheit' into 'Celsius': \nBelow:")
input_fahrenheit=float(input("Enter the temperature in 'Fahrenheit':"))
celsius=float((5/9)*(input_fahrenheit-32))
print("The converted temperature in 'Celsius' is:",celsius,"°C")


# Celsius to Fahrenheit (Formula:((9/5)*C)+32))
print("\nWe are going to convert 'Celsius' into 'Fahrenheit': \nBelow:")
input_celsius=float(input("Enter the temperature in 'Celsius':"))
fahrenheit=(((9/5)*input_celsius)+32)
print("The converted temperature in 'Fahrenheit' is:",fahrenheit,"°F")


# Convert a given number of seconds into minutes and minutes into seconds using variables.
# Seconds into Minutes (Formula:seconds/60)
print("\nTo calculate number of seconds into minutes.\nEnter values below:")
sec=int(input("Enter the seconds to be converted into minutes:"))
min=float(sec/60)
print("Based on the seconds the minutes are :",min)

# Minutes into Seconds (Formula:minutes*60)
print("\nTo calculate number of minutes into seconds.\nEnter values below:")
min=float(input("Enter the minutes to be converted into seconds:"))
sec=float(min*60)
print("Based on the minutes the seconds are :",sec)
 
 
# Write a program that calculates the percentage.
# Percentge calculation
print("\nLet's calculate the percentage.\nBelow:")
num1=int(input("Enter the obtained number:"))
num2=int(input("Enter the total number:"))
percentage=(num1/num2)*100
print("The percentage is:",percentage,'%')


# Write a program that calculates the BMI using height (in meters) and weight (in kilograms) variables.
# BMI using height (in meters) and weight (in kilograms) variables.(Formula:weight/height^2)
print("\nLet's calculate BMI (Body mass index).\nBelow:")
Bmi_height=float(input("Enter the height(m):"))
Bmi_weight=float(input("Enter the weight(Kg):"))
# BMI_Formula=weight/height^2
BMI_result=Bmi_weight/Bmi_height**2
print("The calculated BMI is:",BMI_result)


# Write a program that calculates the volume of a cylinder using the formula.
# Area of a cylinder (Formula:A=2π*(r^2)+2πrh)
print("\nWe are going to calculate the 'Area of Cylinder' :\nBelow:")
height_cylinder=float(input("Enter the height:"))
radius_cylinder=float(input("Enter the radius:"))
cy1=2*math.pi*(radius_cylinder**2)
cy2=2*math.pi*radius_cylinder*height_cylinder
area_of_cylinder=print("The area of cylinder is:",cy1+cy2)
