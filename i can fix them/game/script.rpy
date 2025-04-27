#script file yipppeeeee, all text goes here
#if you're in VSCode I'd recommend pressing Alt+Z to have lines wrap around so you dont have to scroll sideways
#images are just for ref (obv)


#below is creating variables for the characters. Theres more info that can be put in the Character() function but thats a problem for later.
define Goo = Character("Goo")
define J = Character("Jess")
define x = Character("???")


#code taken from online for a player naming themselves, dw about it
define yn = Character("[yname]")
default povname = "Beb Brisk"


# The game starts here, labels separate sections of the story + 
label start:

    #below is the background. Its simple, if you have image (ex. slimulation.png) you type "scene slimulation" without including file type, or can type a generic colour
    scene black


    #line below is dialogue, character variable + "dialogue"
    #appears like:
    #???
    #sigh... I said siggghhhhh?
    #in game
    #cps effects speed that text appears, you can also do {b} for bold and {i} for italics, you can even change text size with {size}, {p} adds a break in one message so you have to press enter again
    x "sigh... I said siggghhhhh......"
    x "I hate errands. It’s the weekend, I should be playing video games, not running around town." 
    "You open your eyes to stare out to the world that has forsaken you. The birds chirp, the sun shines, but you can barely get yourself out of bed."
    x "I guess I can’t sit around moping forever." 
    "With a heavy heart, you pick yourself up and head downstairs. You figure a cuppa Joe would do nicely right now. You reach into the cupboard and grab a random mug, too tired to look up and pick one."
    "You look down at your expertly chosen mug."
    x "Man." 
    "You grabbed the stupid one with your name printed on it in giant letters. Thanks mom."
#name pick!!!
    $ yname = renpy.input("What's the name on the mug?")
    $ yname = yname.strip()

    if not yname:
        $yname = "Beb Brisk"


    scene mug
    show text "{color=#000001}{size=+20}[yname]{/size}{/color}"
        

    
    "You know what? Screw this, you’re raw dogging it today." 
    "You rub your eyes and leave for your chore-packed day." 

    yn "I’ll start with the grocery store. Call it chore warmups if you will."
#grocery store!!
    scene grocery
    "You bumble around the store picking up this and that, and before you know it, the majority of morning has gone out the window (time flies when you’re 'having fun')."
    "After some tough grocerying, you pick a comfy-looking shelf and lean up against it to relax for a minute." 
    "Unfortunately, minutes seem to have been experiencing shrinkflation as well, since not even 5 seconds pass before the entire shelf, your sole haven in this grocery hell, violently tumbles over with a deafening crash."
    scene bg_fallen
    "..."
    "From the rubble that was only moments ago recognizable as a canned bean shelf, you hear a faint, wimpy little squeak."
    "UH OH." 
    "Last you checked, beans don’t make that sound."
    "You scramble over to the next isle to rescue the mystery squeaker."
    yn "Oh my god I’m so sorry!! Are you alright?!"
    "You start digging, chucking cans in every direction." 
    "A fluffy figure rises from the collapsed shelf. Well, he doesn’t look too flattened at least. Good lord, this guy’s tall. And kinda cute..." 
    #line below is a sprite, if you have file (ex. gbeans1.png) instead of "show gbeans1.png" you just go "show gbeans1"
    #once you switch sprites type "hide gbeans1" so no sprites overlap
    show gbeans1
    "Somehow, the impact managed to shatter some of the bean cans (how???) and the poor guy has beans of every kind all over him." 
    yn "I’m really sorry, I didn’t mean to do that! Stay right here, I’ll go get you some paper towels."
    hide gbeans1

    menu:
        "You dash to the paper towel isle, fill your arms with rolls (you don’t have time to think about how much you need, you’re in a rush here!)."

        "Be a respectable member of society and pay for them.":

            "You hustle to the cash, thinking about how proud your parents would be that you didn’t chose to be evil today." 
            yn "I’ll take these please!!"
            "Congratulations! You just bought an absurd amount of paper towel."

        "Hurry!! Back to the cute guy!! No time to pay for these!!":
            #put variable name in square brackets
            "[yname] 1, capitalism 0."

    "You rush back to your maiden in distress."

    yn "I got you some paper towel! Here, I’ll clean you up." 
    show gbeans2
    "You tenderly (not really) wipe as many beans off of him as you can. Except he’s like 1,000 feet tall, so there’s a lot of him to wipe beans off of.{p}It didn’t occur to you before you started this endeavor, but this is gonna be an awkward amount of standing here wiping beans off some guy you don’t know. Might as well introduce yourself."

    yn "I’m yname by the way. I, uh..." 

    menu:
        "Say something cool":
            yn "I do groceries sometimes..." 
        "Say something attractive":
            yn "I do groceries sometimes..." 

    "Why the hell would you say that what is wrong with you what are you doing wh" 
    Goo "I’m Goo, nice to meet you." 
    hide gbeans2
    show gbeans3and5
    "He licks a whole buncha beans off his face. With his stupendously long tongue." 
    Goo "I’m the postman around here. I deliver your mail! So I actually sorta... knew your name already..." 
    yn "Huh?? But I’ve never seen you." 
    Goo "Yeah... I run kinda fast. I saw you once, though. I thought you looked really cool and I wished I had a reason to talk to you. That’s why I remembered your name." 
    yn "Oh! Damn! Well, it’s a pleasure to meet you too. Again, I’m so sorry for all of this. I know! Let’s exchange numbers. I’d love to make it up to you sometime." 
    "You each take a piece of paper towel. You take a pen from your pocket. Goo tears his number into the paper with his claws."
    yn "Great! I’ve gotta skedaddle now, though. Or else I’ll be late to my doctor’s appointment. Goodbye for now!" 
    Goo "Oh! Uh... get better soon!" 
    hide gbeans3and5
    "What? No, it’s a checku- whatever, you’ve gotta get moving." 

#rush
    scene bg_town
    "You stagger out of the store, trying to process the strange encounter you just had. What a mess. You almost killed someone! What did he say his name was... Goo? What kind of a name is Goo?? Your face reddens with embarrassment, what an awful first impression."
    "Still, for the moment, that doesn’t matter. You check your watch and realize its already 1 pm"
    yn "1 pm!!?!? Crap!!!" 
    "You hop on forward, dashing past every pedestrian, even a few cool dogs you would’ve loved to pet. You tap into a speed you didn’t know existed, the buildings around you blend together, the cars get lost in your dust, nothing seems to slow you down, not even the fact you missed your stop a few blocks ago."
    yn "Wait... I missed my stop?!??" 
    "A quick and abrupt halt helps you course correct, making the jog back. Finally, the hospital stood in front of you."  
    yn "Surely now the tough part is over, right??" 

#hopital
    scene hospital 

    "As you walk through the hallway, your spontaneous marathon started to hit you. Your legs wobbled like never before, making you finally sympathetic towards poor Jello."
    "Yet, your attention is suddenly drawn by a strange clown wandering towards you." 
    J "Hi um, sorry I'm a little lost, can you help me?" 
    yn "Oh uh sure, where are you headed?" 
    "You just hope it isn’t across the building." 
    J "I’m supposed to be at the children’s sector, but this place is worse than a mirror maze. I’ve been roaming around for like half an hour." 
    "It's across the building." 
    yn "yeah i think i know the way there, i can help. I’m [yname], by the way." 
    J "Oh, I’m Jess, nice to meet you." 
    "She puts her hand out to shake, but as soon as you grab it, you feel something nip at your fingers."
    yn "Youch!!" 
    J "AHH"  
    "The perpetrator quickly reveals itself as a beak pokes out from her sleeve. The dove squirms out of their shirt and flies down the hall, disappearing around the corner." 
    J "Yip-" 
    yn "huhhh?? What’s going on?" 
    J "Gosh, I’m so sorry, I guess she got bored waiting for the magic show." 
    J "But hurry!! We gotta get her back!!!" 
    yn "I guess this is my life now..." 
    "You both run down the hallway after the bird, each step revealing a deep regret over improper time management."
    J "Poor Toodaloo must’ve been woken up by the handshake." 
    yn "Are you sure she’s not a swift??" 
    "Each step becomes harder than the last, but the dove keeps moving forward. It makes a sharp turn into an empty office, fear hits as both you and jess notice the open window."
    "Just as it reaches the opening, hands fly up to catch Toodaloo, and you feel the feathers between your fingers as you grasp them."
    yn "I got her!!" 
    J "Oh yes!" 
    "You step down and wrap the dove in your sweater while Jess brings out bird feed to calm it down. Both of you sit down together, soothing the dove. While waiting for Toodaloo to drowse off, there’s a slightly awkward air to the room. Suddenly, she yawns and leans her head against your shoulder. Her head up against your cheek, you can’t help but think about how warm she feels." 
    yn "uh-" 
    "Jess scrambles away."
    J "OH! I am so sorry I slept really poorly last night-" 
    J "Please don’t be mad-" 
    yn "Hey its fine I get it; I barely woke up this morning." 
    J "..." 
    J "I’m really sorry about putting you through this yname.. You didn’t deserve this, you were just close to my chaotic mess." 
    yn "Ah, no it’s fine... It was-" 
    yn "Interesting, that’s for sure." 
    J "No, let me make it up to you, please. How about I buy you a coffee? Oh, no pressure, you just really helped out and I deeply appreciate it." 
    yn "Well, sure I’ll think about it." 
    yn "Plus..." 
    yn "It would be nice to spend some more time together." 
    "Jess blushes a little." 
    J "Well, here’s my phone number. Call me if you want to see each other again." 
    "Before you could even say bye, Jess runs off with Toodaloo on her shoulder."  
    yn "Huh, what a strange person." 
    "..."
    yn "Wait, I never gave her directions!" 

#home!!
    scene black
    "You get back home and lay down."
    "Despite the botched shopping trip and missed appointment, today’s encounters really stuck out."
    show garmupskirt at left
    "Goo..."
    "Jess..."
    yn "They both seem so strange, but I can’t stop thinking about them." 


    #choice!!!!!
    menu:
        #the question
        yn "But, one really sticks out."

        #answer one
        "Goo":
            yn "Goo."
            yn "He was real nice, his sincerity really makes him easy to talk to."
            yn "Maybe hanging out will be fun, maybe we can get closer.."
            yn "!!?"
            yn "What am I thinking?? I could've killed him, who forgives someone so easily after that???"
            yn "Goo, he seems like such a pushover, I wonder if there's anything going on in his head."
            yn "Yet, his bluntness and simplicity make him so endearing, maybe I should take a chance with him."
            yn "Maybe I can help him out."
            yn "Yeah, maybe..."
            yn "I can fix him!!"
            "And with that final thought, you drift off to sleep, excited for the future ahead."
            
            #goes to goo's section of the story
            jump goobert

        #answer two
        "Jess":
            yn "Jess." 
            yn "She’s real sweet, I can’t help but want to spend time with her." 
            yn "Maybe the coffee date won’t be the end, maybe it’ll even lead to something more.." 
            yn "!!?" 
            yn "What am I thinking?? We went on a literal wild dove chase, who even keeps a dove in their sleeve??" 
            yn "Jess, she seems so nervous, barely able to function within normal interactions." 
            yn "Yet, there’s something so mesmerizing about her, maybe I should take a chance with her." 
            yn "Maybe I can help her out." 
            yn "Yeah, maybe..." 
            yn "I can fix her!!" 
            "And with that final thought, you drift off to sleep, excited for the future ahead."

            jump jessica


#start of new section of the story
label goobert:

    #general black screen
    scene black
    #this is added to changes in visuals for a more smooth experience
    #just fancy scene transitions
    with fade

    #if you want variable in text put it in square brackets
    #text
    g"Oh well hi there [yname] :)"

    # This ends the game, place it after endings.
    return


label jessica:
    scene white
    with dissolve

    show wally

    g"Youchers why?"
    "Felt like it."
    g"ah okay"

    # This ends the game, place it after endings.
    return
