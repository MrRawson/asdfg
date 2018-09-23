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
    
    # We print out the variables we just created that are storing our
    # Pokemon current health points to the console.
    
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
    # or equal to) to compare our health point variables to zero

    if pikachuHealthPoints <= 0 or snorlaxHealthPoints <= 0:
        print("GAME OVER")
        break
    else:
        snorlaxMove = random.randint(1,2)

        if snorlaxMove == 1:
            print("snorlax ATTACKS FOR",snorlaxAttack,"POINTS!")
            pikachuHealthPoints = pikachuHealthPoints - snorlaxAttack
        elif snorlaxMove == 2:
            print("snorlax HEALS FOR",snorlaxHeal,"POINTS!")
            snorlaxHealthPoints = snorlaxHealthPoints + snorlaxHeal
            if snorlaxHealthPoints > 60:
                snorlaxHealthPoints = 60

        print("snorlax's health:",snorlaxHealthPoints)
        print("pikachu health:",pikachuHealthPoints)

    if pikachuHealthPoints <= 0 or snorlaxHealthPoints <= 0:
        print("GAME OVER")
        break
    else:
        print("pikachu moves:")
        print("1: Attack. Attacks the snorlax for 7 to 12 damage")
        print("2: Heal. Heals us for 5 to 15 points")

        pikachuMove = eval(input("What would you like to do? Press 1 or 2."))

        if pikachuMove == 1:
            print("YOU ATTACK FOR",pikachuAttack,"POINTS!")
            snorlaxHealthPoints = snorlaxHealthPoints - pikachuAttack
        elif pikachuMove == 2:
            print("YOU HEAL FOR",pikachuHeal,"POINTS!")
            pikachuHealthPoints = pikachuHealthPoints + pikachuHeal
            if pikachuHealthPoints > 60:
                pikachuHealthPoints = 60
    
