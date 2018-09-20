#Sequence! Code reads from left to right and top to bottom like English.
#The compiler reads your code a bit like a person would read a book, unless
#we are using Selection! or Iteration!


#We use import statements to access code from other code modules. This one
#will give us random numbers.

import random

#Our first variables. Variables are the building blocks of our program. We are
#resrving blocks in the computers memory to store the current health of our
#Pokemon, so that we can keep score. We are also assigning each space with a
#starting integer value. 

pikachuHealthPoints = 100
snorlaxHealthPoints = 100

print("A wild snorlax has appeared!")

while True:
    print("snorlax's health:",snorlaxHealthPoints)
    print("pikachu's health:",pikachuHealthPoints)

    pikachuAttack = random.randint(7,12)
    pikachuHeal = random.randint(5,15)
    snorlaxAttack = random.randint(7,12)
    snorlaxHeal = random.randint(5,15)

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
            if snorlaxHealthPoints > 100:
                snorlaxHealthPoints = 100

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
            print("YOU HEAL YOURSELF FOR",pikachuHeal,"POINTS!")
            pikachuHealthPoints = pikachuHealthPoints + pikachuHeal
            if pikachuHealthPoints > 100:
                pikachuHealthPoints = 100
    
