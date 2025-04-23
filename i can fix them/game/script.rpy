#script file yipppeeeee, all text goes here
#if you're in VSCode I'd recommend pressing Alt+Z to have lines wrap around so you dont have to scroll sideways
#images are just for ref (obv)


#below is creating variables for the characters. Theres more info that can be put in the Character() function but thats a problem for later.
define g = Character("Goo")
define j = Character("Jess")
define x = Character("???")


# The game starts here, labels separate sections of the story + 
label start:

    #below is the background. Its simple, if you have image (ex. slimulation.png) you type "scene slimulation" without including file type.

    scene slimulation

    #line below is a sprite, if you have file (ex. wally.png) instead of "show wally.png" you just go "show wally"
    #once you switch sprites type "hide wally" so no sprites overlap
    show wally

    #line below is dialogue, character variable + "dialogue"
    #appears like:
    #???
    #who are you?
    #in game
    x "who are you?"

    hide wally
    show toebeans

    #appears like:
    #Goo
    #Goo, but my full name is actually Goober.
    g "Goo, but my full name is actually Goober."

    #choice!!!!!
    menu:
        #the question
        "How do you respond?"

        #answer one
        "Say hi":
            #jumps to label hi's section
            jump hi

        #answer two
        "Punch him in face":

            jump punch


#start of new section of the story
label hi:

    #general black screen
    scene black
    #this is added to changes in visuals for a more smooth experience
    #just fancy scene transitions
    with fade

    g"Oh well hi there :)"

    # This ends the game, place it after endings.
    return


label punch:
    scene white
    with dissolve

    show wally

    g"Youchers why?"
    "Felt like it."
    g"ah okay"

    # This ends the game, place it after endings.
    return
