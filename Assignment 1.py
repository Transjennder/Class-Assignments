# -*- coding: utf-8 -*-
"""
@author: Quintan Seyfert

Created on Thu Aug 27 16:17:39 2020

Title: Assignment 1
"""

#testing this to see how it works
br = "\n"

#this section is to ask the user for their first and last name
print("Please enter your first and last name")
first_name = input("First Name: ")
last_name = input("Last Name: ")
#next line of code concatenates their name with a greeting
print(br+"Hello "+ first_name +" "+ last_name +"! Let's do some math for the fun of it!")

#the next two sections are setup to convert temperatures
fahrenheit = float(input("""First Fahrenheit to Celsius.
Please enter a temperature in Fahrenheit: """ ))
celsius = (fahrenheit-32)/1.8
print(br+str(fahrenheit)+"F is "+str(celsius)+"C")

celsius = float(input("""Now let's convert Celsius to Fahrenheit.
Please enter a temperature in Celsius: """ ))
fahrenheit = (celsius*1.8)+32
print(br+str(celsius)+"C is "+str(fahrenheit)+"F")

#these two sections are for converting different speeds
mph = float(input("""Next let's try miles per hour to knots and vice versa.
Please enter a speed in mph: """ ))
knots = mph/1.15078
print(br+str(mph)+" mph is "+str(knots)+" knots")

knots = float(input("Now enter a different speed in knots: "))
mph = knots*1.15078
print(br+str(knots)+" knots is "+str(mph)+" mph")

#now for the section to get an average
print("Let's try to get an average of three numbers.")
number_1 = float(input("First number: "))
number_2 = float(input("Second number: "))
number_3 = float(input("Third number: "))
average = (number_1+number_2+number_3)/3
print(br+"And the average of "+str(number_1)+", "+str(number_2)+", and "+str(number_3)+" is "+str(average)+"!")

#finally the section on board feet followed by an exit message
print("Finally, let's calculate board feet")
board_width = float(input("Width in inches: "))
board_length = float(input("Length in inches: "))
board_thickness = float(input("Thickness in inches: "))
board_length_feet = board_length/12
board_feet = board_length_feet*board_width*board_thickness/12
board_feet_inches = board_feet*12
print("That is "+str(board_feet)+" board feet. In inches that is "+str(board_feet_inches)+"in.")

print(br+"That's all we have time for now! So long and thanks for all the fish!")