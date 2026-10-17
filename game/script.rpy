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

    "Landlord: Congradutions on your new home! I hope you will be very happy here! Just three little rules: no smoking, no pets, and no funny business."
    "Of course, I am a very boring and responsible person."
    "(Finally, a place where my biggest problem will only be paying rent!)"

    jump handler
  
    
    # This ends the game.

    return


label handler: 
    
    while count <= 21:
        jump expression "scene"+str(count)

    #jump to the end scene
    if countyes == 0:
        jump scene_all_no_result
    elif countyes <= 3:
        jump scene_up_to_3_result
    else:
        jump scene_more_than_3_result

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
    show kenya at pos

    "Adopt me please!"

    menu: 
        "Hapana":
            "The Lion left."

        "Ndiyo":
            $ countyes += 1
            "You adopted the Lion!" 
            
    hide kenya 
    jump handler

    return

label scene4: 
    $ count += 1
    show turkey at pos

    "Adopt me please!"

    menu: 
        "Evet":
            $ countyes += 1
            "You adopted the Grey wolf!" 

        "Hayır":
            "The Grey wolf left."

    hide turkey 
    jump handler

    return

label scene5: 
    $ count += 1
    show samoa at pos

    "Adopt me please!"

    menu: 
        "Leai":
            "The Tooth-billed pigeon left."

        "Ioe":
            $ countyes += 1
            "You adopted the Tooth-billed pigeon!" 
            
    hide samoa 
    jump handler

    return

label scene6: 
    $ count += 1
    show germany at pos

    "Adopt me please!"

    menu: 
        "Ja":
            $ countyes += 1
            "You adopted the Eagle!" 

        "Nein":
            "The Eagle left."
            
    hide germany 
    jump handler

    return

label scene7: 
    $ count += 1
    show slovakia at pos

    "Adopt me please!"

    menu: 
        "Nie":
            "The Tatra chamois left."

        "Áno":
            $ countyes += 1
            "You adopted the Tatra chamois!" 
            
    hide slovakia
    jump handler

    return

label scene8: 
    $ count += 1
    show spain at pos

    "Adopt me please!"

    menu: 
        "No":
            "The Bull left."

        "Sí":
            $ countyes += 1
            "You adopted the Bull!" 
            
    hide spain 
    jump handler

    return

label scene9: 
    $ count += 1
    show south africa at pos

    "Adopt me please!"

    menu: 
        "Cha":
            "The Springbok left."

        "Yebo":
            $ countyes += 1
            "You adopted the Springbok!" 
            
    hide south africa 
    jump handler

    return

label scene10: 
    $ count += 1
    show france at pos

    "Adopt me please!"

    menu: 
        "Non":
            "The Gallic rooster left."

        "Oui":
            $ countyes += 1
            "You adopted the Gallic rooster!" 
            
    hide france 
    jump handler

    return

label scene11: 
    $ count += 1
    show japan at pos

    "Adopt me please!"

    menu: 
        "いいえ":
            "The Green pheasant left."

        "はい":
            $ countyes += 1
            "You adopted the Green pheasant!" 
            
    hide japan 
    jump handler

    return


label scene12: 
    $ count += 1
    show uzbekistan at pos

    "Adopt me please!"

    menu: 
        "Yoʻq":
            "The Sand cat left."

        "Ha":
            $ countyes += 1
            "You adopted the Sand cat!" 
            
    hide uzbekistan 
    jump handler

    return


label scene13: 
    $ count += 1
    show greece at pos

    "Adopt me please!"

    menu: 
        "Όχι":
            "The Dolphin left."

        "Ναι":
            $ countyes += 1
            "You adopted the Dolphin!" 
            
    hide greece 
    jump handler

    return

label scene14: 
    $ count += 1
    show philippines at pos

    "Adopt me please!"

    menu: 
        "Oo":
            $ countyes += 1
            "You adopted the Philippine eagle!" 
            
        "Hindi":
            "The Philippine eagle left."

    hide philippines 
    jump handler

    return

label scene15: 
    $ count += 1
    show pakistan at pos

    "Adopt me please!"

    menu: 
        "ہاں":
            $ countyes += 1
            "You adopted the Markhor!" 

        "نہیں":
            "The Markhor left."

            
    hide pakistan 
    jump handler

    return

label scene16: 
    $ count += 1
    show eritrea at pos

    "Adopt me please!"

    menu: 
        "ኣይፋል":
            "The Dromedary camel left."

        "እወ":
            $ countyes += 1
            "You adopted the Dromedary camel!" 
            
    hide eritrea 
    jump handler

    return

label scene17: 
    $ count += 1
    show nepal at pos

    "Adopt me please!"

    menu: 
        "होइन":
            "The Cow left."

        "हो":
            $ countyes += 1
            "You adopted the Cow!" 
            
    hide nepal 
    jump handler

    return

label scene18: 
    $ count += 1
    show thailand at pos

    "Adopt me please!"

    menu: 
        "ไม่":
            "The Asian elephant left."

        "ใช่ ":
            $ countyes += 1
            "You adopted the Asian elephant!" 
            
    hide thailand 
    jump handler

    return

label scene19: 
    $ count += 1
    show myanmar at pos

    "Adopt me please!"

    menu: 
        "ဟုတ်ကဲ့":
            $ countyes += 1
            "You adopted the Green peafowl!" 
        
        "မဟုတ်ဘူး":
            "The Green peafowl left."
            
    hide myanmar 
    jump handler

    return

label scene20: 
    $ count += 1
    show south korea at pos

    "Adopt me please!"

    menu: 
        "아니요":
            "The Siberian tiger left."

        "네":
            $ countyes += 1
            "You adopted the Siberian tiger!" 
            
    hide south korea
    jump handler

    return

label scene21: 
    $ count += 1
    show china at pos

    "Adopt me please!"

    menu: 
        "不":
            "The Giant panda left."

        "是":
            $ countyes += 1
            "You adopted the Giant panda!" 
            
    hide china
    jump handler

    return

label scene_all_no_result: 
    show scene_all_no_result at pos

    "Crisis resolved! I still have a roof over my head!"
    "And absolutly no one to talk to!"
    "Maybe I should get some plants?"
    "Wait. Do plants count as animals?"
            
    hide scene_all_no_result

    return

label scene_up_to_3_result: 
    show scene_up_to_3_result at pos

    "Three animals. That's managable! Nobody will ever know!"
            
    hide scene_up_to_3_result

    return

label scene_more_than_3_result: 
    show scene_more_than_3_result at pos

    "Well, I am homeless now."
    "Animals: So... can you adopt us now?"
    "I AM LIVING IN A SMALL TENT!"
    "Animals: is it pet friendly?"
    "I guess I am going to need a bigger tent! "
            
    hide scene_more_than_3_result

    return