# Sequence! Text based code reads from left to right and top to bottom like
# English. The compiler reads your code a bit like a person would read a book,
# unless we are using Selection! or Iteration!


# We use import statements to access code from other code modules. This one
# will give us random numbers.

import random

# Our first variables. Variables are the building blocks of our program. Here
# we are reserving blocks in the memory to store the current health of our
# Pokemon, so that we can keep score. We are also assigning each space with a
# starting integer value. An integer is a whole number that can't have a decimal
# point.

pikachuHealthPoints = 60
snorlaxHealthPoints = 60

# An output (or print) to console statement. Here we are passing the built in
# Python print() function a string of characters to print to the console.
# The string will be all the characters within the quotation marks "".  

print("A wild snorlax has appeared!")

# Our first Iteration! or loop. All the code indented underneath the statement
# while True: will go back to the top when it is finished and repeat. It will
# continue to do that forever until reaches a break condition.

while True:
    
    # We print out to the console, the variables we just created at the top
    # that are storing our Pokemon current health points. This will show us a
    # running tally.
    
    print("snorlax's health:",snorlaxHealthPoints)
    print("pikachu's health:",pikachuHealthPoints)

    
    # We now need to create some more variables to store the values attached
    # to our actions. In future, every time we ask for the variable pikachuAttack
    # in this example, we are requesting it to be assigned a random integer
    # (whole number) between 7 and 12.
    
    pikachuAttack = random.randint(7,12)
    pikachuHeal = random.randint(5,15)
    snorlaxAttack = random.randint(7,12)
    snorlaxHeal = random.randint(5,15)

    # Our first Selection! statements. Before we do anything else we need to
    # check if either of our characters has reached 0 health points,
    # which would mean the end of the game. We use the operator <= (less than
    # or equal to) to compare our health point variables to zero.
    # If either meets the condition the game is over and we break out of the
    # loop(and the program).

    if pikachuHealthPoints <= 0 or snorlaxHealthPoints <= 0:
        print("GAME OVER")
        break

    # If the game is not over, our snorlax will take his turn. to
    # do this we create a variable that will have a random chance
    # of scoring either 1 or 2 to decide whether he wants to
    # attack or heal. 
    
    else:
        snorlaxMove = random.randint(1,2)

        # If we get a 1, he will attack pikachu and we subtract the value
        # of his random attack variable from pikachu's health points variable. 
        
        if snorlaxMove == 1:
            print("snorlax ATTACKS FOR",snorlaxAttack,"POINTS!")
            pikachuHealthPoints = pikachuHealthPoints - snorlaxAttack

        # If we get a 2, snorlax will heal himself. We add the value of his
        # random heal variable onto his health points variable.
        
        elif snorlaxMove == 2:
            print("snorlax HEALS FOR",snorlaxHeal,"POINTS!")
            snorlaxHealthPoints = snorlaxHealthPoints + snorlaxHeal

            # Let's also make sure that snorlax cannot heal himself past the
            # amount he started with.
            
            if snorlaxHealthPoints > 60:
                snorlaxHealthPoints = 60

        print("snorlax's health:",snorlaxHealthPoints)
        print("pikachu health:",pikachuHealthPoints)
        
    # We use selection to again check if the game is over and end the game
    # loop if that is the case. 
    
    if pikachuHealthPoints <= 0 or snorlaxHealthPoints <= 0:
        print("GAME OVER")
        break

    # If it isn't game over it is pikachu's turn.
    
    else:
        print("pikachu moves:")
        print("1: Attack. Attacks the snorlax for 7 to 12 damage")
        print("2: Heal. Heals us for 5 to 15 points")
        
        # Our first input statement. The line of code below 
        # passes a string of text to the console (our question) and stores
        # the next value entered by the user at the memory address of
        # the new variable pikachuMove.
        
        pikachuMove = eval(input("What would you like to do? Press 1 or 2."))

        # If the player entered 1, pikachu attacks and we subtract his
        # random attack variable from the health points variable for snorlax.

        if pikachuMove == 1:
            print("YOU ATTACK FOR",pikachuAttack,"POINTS!")
            snorlaxHealthPoints = snorlaxHealthPoints - pikachuAttack

        # If the player entered 2, we heal pikachu by adding his random
        # heal variable onto his health points total.
        
        elif pikachuMove == 2:
            print("YOU HEAL FOR",pikachuHeal,"POINTS!")
            pikachuHealthPoints = pikachuHealthPoints + pikachuHeal

            # Pikachu probably shouldn't be allowed to heal himself past the
            # amount he started with either.
            
            if pikachuHealthPoints > 60:
                pikachuHealthPoints = 60
    
            # Remember our Iteration! ? We are still in a loop.
            # When we get to this point we will jump back to the code
            # directly underneath the while True: statement.



