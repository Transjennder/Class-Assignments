# -*- coding: utf-8 -*-
"""
@author: Quintan Seyfert

Created on Thu Aug 27 16:17:39 2020

Title: Assignment 1
"""






def main() :
    
    # This is the main function to call other functions and/or to run code
    
    # Lines 21-23 print the start of the program, run the name function, and prints the results
    
    print("Time for some more math! Let's get your name again and also where you are from.")
    name, location = name_function()
    print("\nAwesome! Thank you "+name+" from "+location+"!")
    
    # Lines 27-31 sends information to the first triangle function and prints the answer
    
    print("\n\nFirst let's calculate the areas of some triangles. The first two I will provide the numbers")
    x = 6.0
    y = 12.0
    result = AreaOfTriangle_a(x, y)    
    print("\nIf triangle A has a base of 12 units and a height of 6 units the area of triangle A is "+str(result)+" units.")
    
    # Lines 35-37 sends information to the second triangle function which prints the answer
    
    x = 2.0
    y = 3.0
    AreaOfTriangle_b(x, y)
    
    # Lines 41-43 starts the third triangle function and prints the answer
    
    print("\nOk, now it's your turn to input the values. ")
    ans, x, y = AreaOfTriangle_c()
    print("\nIf triangle C has a base of "+str(x)+" units and a height of "+str(y)+" units the area of triangle C is "+str(ans)+" units.")
    
    # Line 47 runs the fourth triangle function which handles the variables and prints the results
    
    AreaOfTriangle_d()
    
    # Lines 51-53 asks the user for the variables, runs the miles to knots function, and prints the results
    
    mph = float(input("\n\nNext let's try miles per hour to knots and vice versa. Please enter a speed in mph: " ))
    result = miles_to_knots(mph)
    print("\n"+str(mph)+" mph is "+str(result)+" knots")
    
    # Lines 57-59 asks the user for the variables, runs the knots to miles function, and prints the results
    
    knots = float(input("\nNow enter a different speed in knots: "))
    result = knots_to_miles(knots)
    print("\n"+str(knots)+" knots is "+str(result)+" mph")
    
    # Lines 63-68 asks the user for the variables, runs the averages function, and prints the results
    
    print("\n\nLet's try to get an average of three numbers.")    
    x = float(input("First number: "))
    y = float(input("Second number: "))
    z = float(input("Third number: "))
    result = three_number_average(x, y, z)
    print("And the average of "+str(x)+", "+str(y)+", and "+str(z)+" is "+str(result)+"!")
    
    # Line 72 runs the salary function which handles the variables and prints the results
    
    gross_salary()
    
    # Line 76 runs the fahrenheit to celsius function which handles the variables and prints the results
    
    farhenheit_to_celsius()
    
    ## Line 80 runs the celsius to fahrenheit function which handles the variables and prints the results
    
    celsius_to_farhenheit()
    
    # Line 84 prints the exit message using variables given by the name function earlier
    
    print("\nThanks again "+name+"! That's all for now")
    
# Lines 88-96 are the name function. This asks for the variables required and returns the results

def name_function() :

    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    location = input("Where are you from? : ")

    name = first_name+" "+last_name

    return name, location

# Lines 100-106 are the first triangle function. This receives the variables required from the main funtion and returns the results

def AreaOfTriangle_a(num1, num2) :
    
    ans = 0.0
    
    ans = 0.5*num1*num2
    
    return ans

# Lines 110-115 are the second triangle function. This receives the variables required from the main funtion and prints the results
    
def AreaOfTriangle_b(num1, num2) :
    
    ans = 0.0
    ans = 0.5*num1*num2
    
    print("\nIf triangle B has a base of 3 units and a height of 2 units the area of triangle B is "+str(ans)+" units.")
 
# Lines 119-128 are the thrid triangle function. This asks for the variables required and returns the results

def AreaOfTriangle_c() :
   
    ans = 0.0
   
    x = float(input("Please enter the base of Triangle C: "))
    y = float(input("Please enter the height of Triangle C: "))
             
    ans = 0.5*x*y
    
    return ans, x, y
    
# Lines 132-141 are the fourth triangle function. This asks for the variables required and prints the results

def AreaOfTriangle_d() :
    
    ans = 0.0
   
    x = float(input("Please enter the base of Triangle D: "))
    y = float(input("Please enter the height of Triangle D: "))
    
    ans = 0.5*x*y
    
    print("\nIf triangle D has a base of "+str(x)+" units and a height of "+str(y)+" units the area of triangle D is "+str(ans)+" units.")

# Lines 145-150 are the miles to knots function. This receives the variables required from the main funtion and returns the results 

def miles_to_knots (mph):
 
    knots = 0.0
    knots = mph/1.15078

    return knots

# Lines 154-159 are the knots to miles function. This receives the variables required from the main funtion and returns the results

def knots_to_miles (knots):
    
    mph = 0.0
    mph = knots*1.15078

    return mph

# Lines 163-167 are the average of three numbers function. This receives the variables required from the main funtion and returns the results

def three_number_average (num1, num2, num3):
   
    average = (num1+num2+num3)/3
    
    return average

# Lines 171-177 are the gross salary function. This asks for the variables required and prints the results

def gross_salary ():
    
    print("\n\nNext let's calculate your gross salary in a certain amount of months.")
    monthly_salary = float(input("\nPlease enter what you make in a month: "))
    months = float(input("\nPlease enter how many months: "))
    gross = months*monthly_salary
    print("\nIn "+str(months)+" months you made $"+str(gross))
    
# Lines 181-186 are the fahrenheit to celsius function. This asks for the variables required and prints the results

def farhenheit_to_celsius ():
    
    print("\n\nFinally, let's convert temperature measurements.")
    fahrenheit = float(input("First Fahrenheit to Celsius. Please enter a temperature in Fahrenheit: " ))
    celsius = (fahrenheit-32)/1.8
    print("\n"+str(fahrenheit)+"F is "+str(celsius)+"C")

# Lines 190-194 are the celsius to fahrenheit function. This asks for the variables required and prints the results

def celsius_to_farhenheit ():
    
    celsius = float(input("Now let's convert Celsius to Fahrenheit. Please enter a temperature in Celsius: "))
    fahrenheit = (celsius*1.8)+32
    print("\n"+str(celsius)+"C is "+str(fahrenheit)+"F")



main ()

