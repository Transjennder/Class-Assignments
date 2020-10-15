# -*- coding: utf-8 -*-
"""
@author: Quintan Seyfert

Created on Sun Sep 13 14:25:17 2020

Title: 
"""

import sys

# Function takes a string and reverses it
def word_reverse():
       
    word = input("\nPlease enter a word or sentence and I will reverse "\
                 "it: ")

    # Creating a blank string variable to write into
    reverse = ""
    
    print()
    
    # This loop looks at each character and places it into the reverse 
    # variable. The order of the placement puts the character before the last
    # character reversing the string
    for char in word:
        reverse = char + reverse      

    print("Whatever you typed in reverse is...\n"+reverse)
    
    # Sending a number to the restart function so if the user wants to try
    # again the restart funtion knows which function to return to 
    code = 1
    restart(code)    
    
# This function will show which numbers between 1 and 100 is divisble by three
# using modulo     
def divisible():
    
    print("\nThis will show you all numbers divisible by 3 between 1 and 100!")
    
    for num in range(1,100):
        
        if (num%3 == 0):
            
            print("\n"+str(num)+" ")
            
    print("Neat!")
   
    # Sending a number to the restart function so if the user wants to try
    # again the restart funtion knows which function to return to
    code = 2
    restart(code)

# This function will compare characters and sort them       
def compare():
    
    # 65-90 capital letters
    # 97-122 lowercase letters
    
    string = input("Enter whatever you want and I will tell you what is a "
                  "letter and what isn't: ")
    
    # Blank variables to put the characters
    good = ""
    bad = ""
    
    # Loop will run through the string and compare the characters ascii number
    # to a set "good" or "bad" value
    for c in string:
        
        # This compares the ascii value of the character to the values of
        # capital letters and adds them to the good string variable
        if (65 <= ord(c) <= 90):
            
            good += c + ", "
        
        # This compares the ascii value of the character to the values of
        # lower case letters and adds them to the good string variable
        elif (97 <= ord(c) <= 122):
            
            good += c + ", "
            
        # This compares the ascii value of the character to the values of
        # space and skips them so there isn't any spaces in the variables
        elif (ord(c) == 32):
            
            continue
        
        # The characters that don't fit into the previous comparison go into
        # the bad string variable
        else:
            
            bad += c + ", "
            
    print("The letters are: "+good)
    print("Everything else: "+bad)

    # Sending a number to the restart function so if the user wants to try
    # again the restart funtion knows which function to return to
    code = 3
    restart(code)
    
# This function collects a value from a user and passes it to the calendar
# funciton
def move_value():
    
    # Try/except catches non ints and else catches incorrect ints
    try:
        move = int(input("Please enter a number between 0 and 7: "))
        
        if 0 <= move <= 7:
            calendar(move)
            
        else:
            print("\nNot a number between 0 and 7. Please try again")
            move_value()
    
    except ValueError:
        print("\nPlease make sure your number is a whole number.")
        move_value()

def calendar(move):
    
    # Variables for following loops
    rows = 5       # Number of rows for the calendar
    columns = 7    # Number of columns for the calendar
    d = 0          # Day count
    last = 31      # End of month
    days = ["S", "M", "T", "W", "R", "F", "S"]  # List of day titles for 
                                                # calendar
    print()        
    
    # Used to format and print each day letter for the calendar
    # '{:^3s}' creates a centered group of 3 spaces for the format
    print('{:^3s}''{:^3s}''{:^3s}''{:^3s}''{:^3s}''{:^3s}''{:^3s}'.format(\
          days[0],days[1],days[2],days[3],days[4],days[5],days[6]))
    print()
    
    # Start of loop to create calendar
    for r in range(rows):          # Loops starts by creating the rows
              
        for c in range(columns):   # Then creates columns with following rules
            
            # If the user enters a move value it will minus one and put a 
            # space instead of the day number until move = 0
            if (move > 0):
                move -=1
                sys.stdout.write('{:^3s}'.format(" "))   # Same format as days
            
            # once it has finished with the move variable it will start
            # printing the days starting with 1
            elif (d < last):
                d+=1
                sys.stdout.write('{:^3s}'.format(str(d)))# Same format as days
            
            # Once d = 31 it will stop printing even if there is still space
            # on the row
            elif (d == last):
                break
            
        print()
     
    # Sending a number to the restart function so if the user wants to try
    # again the restart funtion knows which function to return to   
    code = 4
    restart(code)

# Functions to restart the functions
def restart(code):
    
    # Usual try/except and else logic
    try:
        
        ans = float(input("\n\nWould you like to do that again? "\
                          "\n1. Yes\n2. No\n3. Exit\n"))
            
        # This is used when the user wants to try again. It will check the 
        # code sent by the funtion to restart the correct function
        if (ans == 1):
            
            if (code == 1):
                word_reverse()
                
            elif (code == 2):
                divisible()
                
            elif (code == 3):
                compare()
                
            elif (code == 4):
                move_value()
            
        elif (ans == 2):
            menu()
            
        elif (ans == 3):
            sys.exit()
            
        else:
            print("\nThat was not a choice. Please try again :)")
            menu()
        
    except ValueError:
        
        print("\nThat was not actually a number. Please try again :)")
        menu() 
   
# Menu function
def menu():
    
    # Usual try/except and else logic
    try:
        
        ans = int(input("Hello. In this program there are several small "\
                          "things you can do. Which would you like to start "\
                          "with?\n1. Word Reverse\n2. Divisible\n3. Character"\
                          " Compare\n4. Calendar\n5. Exit the program.\n"))
        
        if (ans == 1):
            word_reverse()
            
        elif (ans == 2):
            divisible()
            
        elif (ans == 3):
            compare()
             
        elif (ans == 4):
            move_value()
                 
        elif (ans == 5):
            sys.exit()
            
        else:
            print("\nThat was not a choice. Please try again :)")
            menu()
        
    except ValueError:
        
        print("\nThat was not actually a number. Please try again :)")
        menu()       
      
def main():
    
    menu()

main()