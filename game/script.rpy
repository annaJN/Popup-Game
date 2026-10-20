# The script of the game goes in this file.
init python:
    import random 

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define randnum = renpy.random.random
#define randfloat = 0.[randnum]

#define randpos = Position(xalign=randnum, yalign=randnum)

define pos = Position(xalign=0.5, ypos=-0.1)
#define scenelist = [scene1, scene2, scene3]

#define NotoSansJP = "/fonts/NotoSansJP.ttf"


# The game starts here.

#CHARACTERS 
define land = Character("Landlord")
define t = Character(what_font="Montserrat.ttf")

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
    scene background
    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #INTRO TEXT HERE

    play music "andriih-chill-chill-music-614318.mp3"

    land "Congradutions on your new home! I hope you will be very happy here! Just three little rules: no smoking, no pets, and no funny business."
    "Of course, I am a very boring and responsible person."
    t "Finally, a place where my biggest problem will only be paying rent!"

    scene knocking
    play sound "soundreality-door-knocking-175163.mp3"
    "Knock knock"
    "Oh, someone is knocking on the door. Is the landlord back?"
    "Oh!!"
    "Where did all of these animals come from?"
    play music "andriih-cute-cats-pets-music-613347.mp3"

    scene dooropen 
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
    elif countyes == 21:
        jump adopt_all_result
    else:
        jump scene_more_than_3_result

    return 

label scene1:
    $ count += 1
    show sweden at pos:
        zoom 1.5
    "Adopt me please!"

    t "I really can't adopt any animals. The land lord will evict me."
    "No, I'm sorry I can't adopt you."

    t "The Moose looks at you confused."

    t"Ah, maybe I need to say it in their native language. Hmmm What was it again."
 
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
    show brazil at pos:
        zoom 1.5

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
    show kenya at pos:
        zoom 1.5

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
    show turkey at pos:
        zoom 1.5

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
    show samoa at pos:
        zoom 1.5

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
    show germany at pos:
        zoom 1.5

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
    show slovakia at pos:
        zoom 1.5

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
    show spain at pos:
        zoom 1.5

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
    show southafrica at pos:
        zoom 1.5

    "Adopt me please!"

    menu: 
        "Cha":
            "The Springbok left."

        "Yebo":
            $ countyes += 1
            "You adopted the Springbok!" 
            
    hide southafrica 
    jump handler

    return

label scene10: 
    $ count += 1
    show france at pos:
        zoom 1.5

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
    show japan at pos:
        zoom 1.5

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
    show uzbekistan at pos:
        zoom 1.5

    "Adopt me please!"

    menu: 

        "Ha":
            $ countyes += 1
            "You adopted the Sand cat!" 
        "Yoʻq":
            "The Sand cat left."

        
            
    hide uzbekistan 
    jump handler

    return


label scene13: 
    $ count += 1
    show greece at pos:
        zoom 1.5

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
    show philippines at pos:
        zoom 1.5

    "Adopt me please!"

    menu: 
        "Oo":
            $ countyes += 1
            "You adopted the Carabao buffalo!" 
            
        "Hindi":
            "The Philippine Carabao buffalo left."

    hide philippines 
    jump handler

    return

label scene15: 
    $ count += 1
    show pakistan at pos:
        zoom 1.5

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
    show eritrea at pos:
        zoom 1.5

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
    show nepal at pos:
        zoom 1.5

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
    show thailand at pos:
        zoom 1.5

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
    show myanmar at pos:
        zoom 1.5

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
    show southkorea at pos:
        zoom 1.5

    "Adopt me please!"

    menu: 
        "아니요":
            "The Siberian tiger left."

        "네":
            $ countyes += 1
            "You adopted the Siberian tiger!" 
            
    hide southkorea
    jump handler

    return

label scene21: 
    $ count += 1
    show china at pos:
        zoom 1.5

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
    scene background

    "Crisis resolved! I still have a roof over my head!"
    "And absolutly no one to talk to!"
    "Maybe I should get some plants?"
    "Wait. Do plants count as animals?"
    return

label scene_up_to_3_result: 
    scene hiddenanimals
    play music "andriih-funny-funny-music-585934.mp3"
    

    "A few animals. That's managable! Nobody will ever know!"
    "Right?"
            

    return

label scene_more_than_3_result: 
    scene homeless
    play music "andriih-sad-sad-music-601661.mp3"

    "Well, I am homeless now."
    "Animals: So... can you adopt us now?"
    "I AM LIVING IN A SMALL TENT!"
    "Animals: is it pet friendly?"
    "I guess I am going to need a bigger tent! "

    return

label adopt_all_result:
    scene allanimals
    "You ended up adopting all the animals. It was hard to say no to allt these cuties."
    "To your suprise, the landlord did not kick you out!"
    "They helped you turn the appartment into a zoo and now you do not even have to worry about paying rent. The Zoo covers it."
    "And on top of that, now the entire building is pet friendly!"

    return