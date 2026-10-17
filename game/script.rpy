# The script of the game goes in this file.
init python:
    import random 

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define randnum = renpy.random.random
#define randfloat = 0.[randnum]

#define randpos = Position(xalign=randnum, yalign=randnum)

define randpos = Position(xalign=0.2, yalign=0.5)


# The game starts here.

label start:

    $ rand = random.randint(0,100)
    $ floatrand = renpy.random.random

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene skrivbord

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show box at randpos

  
    # These display lines of dialogue.

    e "Hello! I'm a QR box!!! [floatrand]"

    e "Will you scan me? Random nummer [rand]"

    menu: 
        "Yes":
            jump pressed_yes 

        "No":
            jump pressed_no 
    

    # This ends the game.

    return

    label pressed_yes:

        "You pressed yes"

        return

    label pressed_no:

        "You pressed no"

        return
