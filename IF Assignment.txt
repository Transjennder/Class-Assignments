# -*- coding: utf-8 -*-
"""
@author: Quintan Seyfert

Created on Sun Sep 13 15:25:43 2020

Title: 
"""

import sys

# This function is used to calculate taxes.
# It will calculate tax and net income and print the results
def tax_calc(gross,taxrate):
    
        tax = gross * taxrate
        net = gross - tax
        taxrate = round(taxrate*100,1) # This is used to change the taxrate
        # to a percentage. Round used due to float issues during printing
        
        # These format the numbers to have two decimal points and adds commas
        # every thousands to make it look more accurate
        gross = ("{:,.2f}".format(gross))
        tax = ("{:,.2f}".format(tax))
        net = ("{:,.2f}".format(net))
       
        print("\nSince you make $"+gross+", that means your tax rate is "+\
              str(taxrate)+"%. You will pay $"+tax+" with a net"\
              " income of $"+net)
        
        print("\nThanks for playing!")
        
        # Returning to a function to handle trying again or going to the menu
        restart_taxes()
        
# This function allows the user to try another number for taxes or go to 
# the menu      
def restart_taxes():        
        
        # Using try/except to catch inputs that aren't ints
        try:
        
            again = int(input("Would you like to try a different number?"\
                              "\n1. Yes\n2. No\n"))
            
            # This is to catch other ints that aren't an option
            if(again == 1):
                taxes()
                
            elif(again == 2):
                print("\nThen back to the main menu with you!")
                menu()
                            
            else:
                print("\nThat was not a valid answer. Please try again :)")
                taxes()
            
        except ValueError:
            
           print("\nThat was not an actual number. Please try again :)")
           taxes()

# This function collects the tax input from the user and decides which bracket
# the user is in. Then it sends that data to the calculator
def taxes():
    
    # Using try/except to catch inputs that aren't floats
    try:
        
        # .replace catches if the user uses commas to separate thousands
        gross = float(input("Please enter your gross annual income: ")
                      .replace(",",""))

        # Sorts the answer into the correct tax bracket
        if (0 <= gross <= 9275):
            taxrate = 0.1
            tax_calc(gross, taxrate)
                      
                    
        elif (9275 < gross <= 37650):
            taxrate = 0.15
            tax_calc(gross, taxrate)
            
            
        elif (37650 < gross <= 91150):
            taxrate = 0.25
            tax_calc(gross, taxrate)
            
            
        elif (91150 < gross <= 190150):
            taxrate = 0.28
            tax_calc(gross, taxrate)
            
            
        elif (190150 < gross <= 413350):
            taxrate = 0.33
            tax_calc(gross, taxrate)
            
            
        elif (413350 < gross <= 415050):
            taxrate = 0.35
            tax_calc(gross, taxrate)
            
            
        elif (415050 < gross):
            taxrate = 0.396
            tax_calc(gross, taxrate)
        
        # Not too neccessary but can catch negative floats
        else:
            print("\nThat was not a valid number. Please try again :)")
            taxes()
            
    except ValueError:
        
       print("\nThat was not actually a number. Please try again :)")
       taxes()
            
# This will restart the game after the user is done
def restart_game():
    
    # Usual try/except and else reasoning
    try:
        
        ans = int(input("\nDo you want to play again?\n1. Yes\n2. No\n"))
        
        if(ans == 1):
            game()
            
        elif(ans == 2):
            print("\nThen back to the main menu with you!")
            menu()
        
        else:
            print("\nThat was not a valid number. Please try again :)")
            restart_game()
            
    except ValueError:
        
        print("\nThat was not actually a number. Please try again :)")
        restart_game()

# Start of game
def game():
    
    print("\nYou are stranded on top of a mountain with no memory of how you"\
          " got there. Looking around you see a cave and a meandering path"\
              " along a cliff.")
    
    # Usual try/except and else reasoning
    try:
    
        choice = int(input("Do you go down the path or into the cave?"\
                           "\n1. Path\n2. Cave\n"))
        
        # Choice sends to new functions
        if(choice == 1):
            game_path_branch()
            
        elif(choice == 2):
            game_cave_branch()
            
        else:
            print("\nI guess you decided to just jump off the cliff? You"\
                  " have to start over.")
            game()
            
    except ValueError:
        
        print("\nThat was not actually a number. Please try again :)")
        game()

def game_cave_branch():
    
    print("\nYou start moving along through the cave and come across"\
          " two items. One is a shiny ring with a strange inscription"\
          " along the inside of the ring. The second item is a"\
          " book with the words 'Don't Panic' in large friendly"\
          " letters. Because you are in a hurry you only pick one"\
          " item.")
    
    # Usual try/except and else reasoning             
    try:
        item = int(input("Do you choose the ring or the book?"\
                      "\n1. Ring\n2. Book\n"))
        
        # Both results will send to another function to handle the next choice
        # Will pass the item along to the next choice
        if(0 <= item <= 2):
            
            # Changes the int value of the item to a string to use in print
            if(item == 1):
                item = "ring"
                        
            elif(item == 2):
                item = "book"

            print("\nAfter picking up the "+item+", you notice the cave "\
                  "splits with one opening just large enough for you "\
                  "to fit through while the other opening is plenty "\
                  "wide.")
        
            game_cave_item_branch(item)
                
        else:
            print("\nDespite you being in a hurry you decided to take a "\
              "nap before you decide. To your horror your mind gets stuck "\
              "in an infinite loop and you die. As you approach the light "\
              "you find... ")
        
            game_cave_branch()
        
    except ValueError:
        print("\nDespite you being in a hurry you decided to take a "\
              "minute to decide. To your horror your mind gets stuck in an "\
              "infinite loop and you die. As you approach the light you "\
              "find... ")
        
        game_cave_branch()

def game_cave_item_branch(item):
    
    # Usual try/except and else reasoning
    try:
        choice = int(input("Do you choose the narrow or wide opening?"\
              "\n1. Narrow\n2. Wide\n"))
       
        # Item passed through this function to the next as it has no use yet
        if(choice == 1):
            game_narrow_branch(item)
        
        elif(choice == 2):
            game_wide_branch(item)
            
        else:
            print("\nYou sit and have a good hard think about it and then "\
                  "finally...")
            game_cave_item_branch(item)
        
    except ValueError:
        print("\nYou sit and have a good think about it and then finally...")
        game_cave_item_branch(item)

def game_narrow_branch(item):
    
    print("\nSucking in your belly you squeeze into the narrow passage "\
          "hoping that you chose correctly. You continue for what feels "\
          "like hours before finally spilling into a small cavern. At the "\
          "you see the exit! As you walk towards the exit, suddenly, a "\
          "barrier comes down and a voice drones, 'Papers please.' "\
          "You look over to see a hideous creature peering out at you "\
          "from what looks like a toll booth in the wall. Investigating "\
          "the area you realize you are trapped and the creature is your "\
          "only way out. You argue, beg, and plead with him to no avail. "\
          "Your only way out is to have the correct paper work.")
    
    # Different results based on the item pass through from two functions
    if(item == "book"):
        print("\nYou panic. You don't even understand what's going on, so "\
              "how are you supposed to get out? You then remember the book. "\
              "You pull it out and see 'Don't Panic' and you decide to take "\
              "its advice. You open the book and find out it has all the "\
              "answers you were looking for and work your way through the "\
              "bureaucratic nightmare and finally escape the mountain.")
        print("\nYou win!")
        
        # Allows user to try the game again after result
        restart_game()
        
    else:
        print("\nYou panic. You don't even understand what's going on, so "\
              "how are you supposed to get out? You then remember the ring. "\
              "You pull it out and look at it. You can feel it calling to "\
              "you...\n\n\nYou put it on and then...\n\n\n\n...nothing. You "\
              "try to work with the creature, but you can't understand it. "\
              "The rest of your years are spent doing paperwork.")
        print("\nYou died!")
        
        # Allows user to try the game again after result
        restart_game()

def game_wide_branch(item):
    
    print("\nYou decide on the wide path as it looks more comfortable and "\
          "easier to manage. You stroll along at a brisk pace. Gradually, "\
          "you hear a croaky voice drift towards you. It seems to be singing.")
    
    # Different results based on the item pass through from two functions
    if(item == "book"):
        print("\nYou begin to fiddle with the book as you head towards the "\
              "singing. At some point, you trigger the auto read feature and "\
              "the book starts reciting a random entry about toadstools. The "\
              "creature hears the noise and rushes towards it and you. It "\
              "screeches something about you being filthy before pouncing at "\
              "you. You hear a crunch and the world goes dark. ")
        print("\nYou died!")
        
        # Allows user to try the game again after result
        restart_game()
        
    else:
        print("\nYou begin to fiddle with the ring as you head towards the "\
              "singing. At some point, it slips on your finger, rendering "\
              "you invisible. This allows you to move right up on the "\
              "ghastly creature and watch it. After a few minutes, the "\
              "creature crawls along his way. You follow him as he "\
              "unknowingly leads you to the exit.")
        print("\nYou win!")
        
        # Allows user to try the game again after result
        restart_game()


def game_path_branch():
       
    print("\nYou meander down the meandering path along the cliffs, "\
          "following it forward to an unknown destination. As you move "\
          "ahead, the path opens onto a wide plateau. You notice an ornate "\
          "wooden box on the ground in the center of the plateau. When you "\
          "open the box you see a letter reading, 'Here lies the Holy Hand "\
          "Grenade of Antioch and a potion. You may only take one or you "\
          "will be cursed by greed.' You toss the letter aside and "\
          "check the box. Sure enough there is a grenade and a bottle with "\
          "a tag that says 'Drink me'")
    
    # Usual try/except and else reasoning             
    try:
        item2 = int(input("Do you choose the grenade or the bottle?"\
                     "\n1. Grenade\n2. Bottle\n"))
            
        # Both results will send to another function to handle the next choice
        # Will pass the item along to the next choice
        if(0 <= item2 <= 2):
            
            # Changes the int value of the item to a string to use in print
            if(item2 == 1):
                item2 = "Holy Hand Grenade"
                        
            elif(item2 == 2):
                item2 = "bottle"

            print("\nAfter picking up the "+item2+", you look around for "\
                  "your next step. To your left you see a canyon decending "\
                  "to the valley below. To your right there seems to be a "\
                  "small path that decending to a rose garden.")
        
            game_path_item_branch(item2)
                
        else:
            print("\nYou are overcome by a sudden surge of greed, rushing "\
                  "forward to grab both items at once. You trip in your "\
                  "haste, face planting before the world goes black and "\
                  "start to recall.... ")
        
            game_path_branch()
        
    except ValueError:
        print("\nFacing an overwhelming sense of greed, you rush "\
              "forward to grab both items at once. You trip in your "\
              "haste, face planting before the world goes black and "\
              "start to recall.... ")
        
        game_path_branch()

def game_path_item_branch(item2):
    
    # Usual try/except and else reasoning
    try:
        choice = int(input("Do you choose the canyon or the garden?"\
             "\n1. Canyon\n2. Garden\n"))
        
        # Item passed through this function to the next as it has no use yet
        if(choice == 1):
            game_canyon_branch(item2)
        
        elif(choice == 2):
            game_garden_branch(item2)
            
        else:
            print("\nYou sit and have a good hard think about it and then "\
                  "finally...")
            game_path_item_branch(item2)
            
    except ValueError:
        print("\nYou sit and have a good think about it and then finally...")
        game_path_item_branch(item2)

def game_canyon_branch(item2):
    
    print("\nAs you walk down the canyon, you start to notice bones "\
          "starting to litter the canyon floor, appearing more often the "\
          "further you go. Suddenly, there is a gap in the canyon floor too "\
          "wide to jump across. At the bottom, in a warren of carcasses and "\
          "bones with a small white rabbit with red stains over its fur and "\
          "face. Scared of what this means you reach into your pocket and "\
          "remember you have the "+item2+".")
    
    # Different results based on the item pass through from two functions
    if(item2 == "Holy Hand Grenade"):
        print("\nThinking on your feet, you pull the grenade from the box "\
              "and count to three, no more, no less, and toss it towards the "\
              "rabbit. It explodes in a holy choir of an explosion, taking "\
              "the bunny with it. It has also blown a nice crack in the wall "\
              "for you to climb out of the gap and out to freedom.")
        print("\nYou win!")
        
        # Allows user to try the game again after result
        restart_game()
        
    else:
        print("\nYou realize there is no time like the present and pull the "\
              "stopper from the vial and downing it in one gulp. You are "\
              "enjoying the pleasant marmalade taste when suddenly you feel "\
              "yourself shrink to the size of a mouse. The rabbit has taken "\
              "notice of you and hops up to you faster than you can cry out. "\
              "You are unable to escape the sharp pointy teeth as it has you "\
              "for a snack.")
        print("\nYou died!")
        
        # Allows user to try the game again after result
        restart_game()
        

def game_garden_branch(item2):

    print("\nClimbing down to the garden you start following the path made "\
          "by the bushes around you. After an hour or so you find youself "\
          "face to face with a dead end. Slowly losing your cool, you start "\
          "desperately looking around for something you must have missed. "\
          "Finally, you look down and see a small door fit for a dormouse. "\
          "When you bend down to look the "+item2+" falls out of your pocket "\
          "and onto the grass.")
    
    # Different results based on the item pass through from two functions
    if(item2 == "bottle"):
        print("\nShrugging your shoulders you pick up the bottle and throw "\
              "it back. There is an overwhelming marmalade taste as you "\
              "find yourself steadily shrinking. You stand in front of the "\
              "door and find it to be perfectly you sized. Not wanting to "\
              "think about it to hard you walk through the door. After "\
              "coming out the other side, you get extremely dizzy and pass "\
              "out. When you come to you are your normal size and just "\
              "outside civilization.")
        print("\nYou win!")
        
        # Allows user to try the game again after result
        restart_game()
        
    else:
        print("\nYou grab the Holy Hand Grenade, pull the pin, and roll it "\
              "towards the door. There is a muffled whump of an explosion "\
              "and the wall falls forward, squishing you underneath.")
        print("\nYou died!")
        
        # Allows user to try the game again after result
        restart_game()


def menu():
    
    # Usual try/except and else reasoning
    try:
        
        ans = int(input("Please choose between taxes, a game, or exiting "\
                          "the program.\n1. Taxes\n2. Game\n3. Exit\n"))
        
        if (ans == 1):
            taxes()
            
        elif (ans == 2):
            game()
        
        # Allows user to exit
        elif (ans == 3):
            sys.exit()
            
        else:
            print("\nThat was not a choice. Please try again :)")
            menu()
        
    except ValueError:
        
        print("\nThat was not actually a number. Please try again :)")
        menu()

# Simple function to call the menu
def main():
    
    print("This program allows you to calculate your taxes and play a game. "\
          "How fun!")
    menu()        

main()
