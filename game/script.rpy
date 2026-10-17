# The script of the game goes in this file.
init python:
    import random 

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define randnum = renpy.random.random
#define randfloat = 0.[randnum]

#define randpos = Position(xalign=randnum, yalign=randnum)

define pos = Position(xalign=0.2, yalign=0.5)
#define scenelist = [scene1, scene2, scene3]


# The game starts here.

label start:

    $ rand = random.randint(0,100)
    $ floatrand = renpy.random.random

    $ countyes = 0
    $ countno = 0 
    $ count = 1

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # THIS IS THE BACKGROUND
    scene skrivbord

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #INTRO TEXT HERE


    jump handler
  
    
    # This ends the game.

    return


label handler: 
    
    while count <= 6:
        jump expression "scene"+str(count)

    "You played all the scenes"
    #jump to the end scene
    return 

label scene1:
    $ count += 1
    show sweden at pos
    "Adopt me please!"

    "I really can't adopt any animals."
    "No, I can't adopt you."

    "The Moose looks at you confused."

    "Ah, maybe I need to say it in their native language. Hmmm What was it again."
 
    menu: 
            "Ja":
                $ countyes += 1
                "You adopted the Moose!" 

            "Nej":
                "The Moose left."
    hide sweden
    jump handler

    return

label scene2: 
    $ count += 1
    show brazil at pos

    "Adopt me please!"

    menu: 
        "Não":
            "The Jaguar left."

        "Sim":
            $ countyes += 1
            "You adopted the Jaguar!" 
            
    hide brazil 
    jump handler

    return

label scene3: 
    $ count += 1

    "This is scene 3"

    jump handler

    return

label scene4: 
    $ count += 1

    "This is scene 4"

    jump handler

    return

label scene5: 
    $ count += 1

    "This is scene 5"

    jump handler

    return

label scene6: 
    $ count += 1

    "This is scene 6"

    jump handler

    return

label scene7: 
    $ count += 1

    "This is scene 7"

    jump handler

    return

label scene8: 
    $ count += 1

    "This is scene 8"

    jump handler

    return

label scene9: 
    $ count += 1

    "This is scene 9"

    jump handler

    return

label scene10: 
    $ count += 1

    "This is scene 10"

    jump handler

    return

label scene11: 
    $ count += 1

    "This is scene 11"

    jump handler

    return


label scene12: 
    $ count += 1

    "This is scene 12"

    jump handler

    return


label scene13: 
    $ count += 1

    "This is scene 13"

    jump handler

    return

label scene14: 
    $ count += 1

    "This is scene 14"

    jump handler

    return

label scene15: 
    $ count += 1

    "This is scene 15"

    jump handler

    return

label scene16: 
    $ count += 1

    "This is scene 16"

    jump handler

    return

label scene17: 
    $ count += 1

    "This is scene 17"

    jump handler

    return

label scene18: 
    $ count += 1

    "This is scene 18"

    jump handler

    return

label scene19: 
    $ count += 1

    "This is scene 19"

    jump handler

    return

label scene20: 
    $ count += 1

    "This is scene 20"

    jump handler

    return

label scene21: 
    $ count += 1

    "This is scene 21"

    jump handler

    return