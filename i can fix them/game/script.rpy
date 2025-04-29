#script file yipppeeeee, all text goes here
#if you're in VSCode I'd recommend pressing Alt+Z to have lines wrap around so you dont have to scroll sideways
#images are just for ref (obv)


#below is creating variables for the characters. Theres more info that can be put in the Character() function but thats a problem for later.
define Goo = Character("Goo")
define J = Character("Jess")
define x = Character("???")


#code taken from online for a player naming themselves, dw about it
define yn = Character("[yname]")
default yname = "Beb Brisk"


# The game starts here, labels separate sections of the story + 
label start:

    #below is the background. Its simple, if you have image (ex. slimulation.png) you type "scene slimulation" without including file type, or can type a generic colour
    scene black



    #line below is dialogue, character variable + "dialogue"
    #appears like:
    #???
    #sigh... I said siggghhhhh......
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
        "You dash to the paper towel isle and fill your arms with rolls (you don’t have time to think about how much you need, you’re in a rush here!)."

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

    yn "I’m [yname] by the way. I, uh..." 

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
    "Still, for the moment, that doesn’t matter. You check your watch and realize its already 1 pm."
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
    yn "Yeah I think I know the way there, I can help. I’m [yname], by the way." 
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
    J "I’m really sorry about putting you through this [yname].. You didn’t deserve this, you were just close to my chaotic mess." 
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

            jump jessbeginning


#start of new section of the story
label goobert:

    #general black screen
    scene black
    #this is added to changes in visuals for a more smooth experience
    #just fancy scene transitions
    with fade

    #if you want variable in text put it in square brackets
    #text
    

    # This ends the game, place it after endings.
    return


label jessbeginning:
    
    scene apartment 

    "You open your eyes to welcome another day. Unlike the previous, there’s an excitement that helps you hop out of bed. The morning routine suddenly takes too long, you dress while making breakfast, you brush your teeth while drinking your morning coffee. All of this finally brings you to the phone call." 
    "*Ring  ring*"
    "*Ring ring*"
    "*Ri-"
    "The ringing is interrupted by what seems to be circus music, the sounds of bells and horns make it difficult to truly hear the person beginning to speak."
    J "Hello this is Jess!" 
    "Despite it being eight in the morning, she’s still decked out in full clown makeup."
    yn "Oh, hi Jess, this is [yname], sorry if I woke you." 
    J "[yname]?? Gosh does this mean you really want to hang out??" 
    J "Don’t worry about me, my boss makes me wake up at 4 am sharp to start work." 
    yn "What? That sounds..." 
    yn "Anyway yes let’s meet up." 
    yn "So... when and where can we meet up for coffee?" 
    J "Oh, i know this great place near where we met, it’d be perfect!!" 
    J "I can meet you in an hour." 
    J "I- if you want of course..." 
    yn "Sounds perfect actually!!" 
    J "Really?" 
    yn "Yup, see you soon." 
    J "So its a date!" 
    yn "What?" 
    J "Um ah oh i mean uh w-well you see..." 
    J "BYE." 
    "*Click*"
    "The confusion is quickly replaced by excitement. You cannot contain yourself. You start to jump up and down and all around. You knock over your terrible mug. For a second you regret it, but you quickly remember how much you hated it and move on." 
    yn "A date eh? I like the sound of that." 
    yn "But... did she really mean it like that? It’s also a turn of phrase, right?" 
    yn "Something about the way she reacted though..." 
    "The train of thought kept moving around in circles, endless possibilities flooded through that simple sentence."
    yn "Yikes, look at the time!" 
    "You decided that it was better to think while walking than to miss the date."
    jump jesscoffeepart1

label jesscoffeepart1:  
    "You pull up to the cafe, filled with hope and anxiety. You check the time, despite your elongated route, you still arrive 10 minutes early. Still, there’s only so many circles someone can walk without drawing suspicion." 
    yn "huh?" 
    "Suddenly, you see her. Jess, more early than you, sitting at one of the tables. She awkwardly waves to you and you head over."
    yn "I guess we’re both early then." 
    J "Looks like it, heheh." 
    J "..." 
    yn "..." 
    J "..." 
    "Before you sat down, all sorts of ideas ran through your mind as to how this chat would go. Now that you’re here though, it seems as if none of them would come true. You forgot you really didn’t know anything about Jess."
    yn "So... what do you do for a living?" 
    "As soon as the words come out of your mouth, you can’t help but be embarrassed at the obviousness of the answer."
    "Jess giggles."
    J "well, I don’t just dress like this for fun," 
    yn "(just?)" 
    J "I’m a professional clown." 

label clownquestions:
    menu clowning:

        "Is it tough?" if not renpy.seen_label("hard"):
            jump hard

        "How long have you been a clown?" if not renpy.seen_label("clown"): 
            jump clown

        "Did you always want to be one?" if not renpy.seen_label("childhood"):
            jump childhood

        "What do clowns even do?" if not renpy.seen_label("what"):
            jump what

    jump jesscoffeepart2

label hard:
    J "... it can be, but I’ve been in the biz so long that I’m used to the hard parts." 
    J "Although I can’t really handle group performances." 
    jump clownquestions
label clown:
    J "Ough, as long as I can remember." 
    yn "Did you start as a kid?" 
    J "I think I was around 15 when I started." 
    J "I’m 28 by the way, I’ve been told i have kind of a young face." 
    "You wonder if it's her face or the layers of makeup over it." 
    jump clownquestions
label childhood:
    J "I don’t think so." 
    J "Don’t get me wrong I love the genre, but sometimes it feels like I’m more clown than Jess." 
    jump clownquestions
label what:
    J "some different things." 
    J "My favourite job is cheering up some of the child patients at the hospital, but I also do birthday parties and some clown shows." 
    J "We’re actually hosting one soon if you want to check it out." 
    jump clownquestions

label jesscoffeepart2:
    yn "Do you make a lot being a clown?" 
    J "Haha, no" 
    yn "Maybe I should buy your coffee then *chuckles*" 
    J "Wha- Wh- But I wanted to thank you!!" 
    "Jess takes a deep breath. Her voice slows."
    J "Genuinely. Like I caused such a mess, and i really appreciate your help. Toodaloo does too, she’s doing much better now. Especially since she’s on break from magic tricks." 
    yn "Hey, there’s no need to get so hung up on it. Would you believe that I almost pancaked a guy beforehand at the grocery store?" 
    J "What??? Are you the one that dropped the shelf!?" 
    yn "How did you know????" 
    J "It was on the local news!" 
    "You both snicker at the events that transpired the day before. Whatever awkwardness that was there at the beginning had disappeared. Rather than a stranger, you saw before you a friend."
    yn "Hey, why was the clown’s bag so full?" 
    "Jess stares for a moment."
    J "Well, why don’t I check?" 
    "She picks up her purse from under the table, its just as colourful as she was. She pulls out her wallet, then a scarf, then another scarf, and another."
    "Not too long and she’s covered head to toe in scarves all tied together."  
    J "Well, seems we have our answer." 
    "She muffles out from the inside of her tent." 
    yn "Well, i was gonna say ‘because it had to carry their emotional baggage,’ but that works too." 
    J "pft." 
    J "HAHAHAHAHAHAHAHHAHAHAH!!!" 
    "You’re caught off guard, uncertain if she truly thought you were that funny, or if she’s overcompensating."
    "Her voice, hoarse, almost reassured your worries."
    J "Ah shucks, between the two of us, you should’ve been the clown!" 
    yn "Thanks!" 
    J "You should meet my buddy, Binko, he’s got some good ones too." 
    yn "Well, you want to hear another?" 
    "The date went on. Laughs were thrown around as jokes were passed. Eventually, the poor workers had to ask you to leave as you raised the decibel level in the room by at least 30. Before separating, you agreed to another date. Well, not quite an official date yet, but Jess flushed face, even through makeup, seemed to want to say it."
    "Just, for the moment, you appreciate the one you already had."
    scene black
    jump jesspark
    
label jesspark:
    "A week later, it was finally time for the second ‘date.’"

    scene park 
    "This time, it’s going to be a pleasant stroll through the park. Once again you arrive early and still are beaten out by Jess."
    J "Hi! Nice day, isn’t it?" 
    "You’re starting to wonder if the makeup is just actually her skin."
    yn "Yeah definitely, why did you want to be here?" 
    J "Well, it’s always good to get fresh air. The atmosphere at the rehearsal hall is like mildew." 
    yn "Right, you gotta practice for that show soon." 
    J "Yup, and my boss is a bit of a perfectionist so it’s pretty draining." 
    yn "Well, at least you get a little break from clown stuff right now (as much as you can in full costume)." 
    J "Oh yes! Just got to enjoy the suuuuunnnnnnnn-" 
    "Jess slides forward as she steps on a banana peel, pushing her several meters down the path. She waves her arms as she attempts to stabilize, only bumping into those around her. They fall and launch their possessions up, which Jess struggles to catch. It started simple, a dog’s rubber ball, then a hat, and soon she was juggling a bowling pin, chainsaw, squirrel, and who knows what else."
    J "AHHHH HELP!!!" 
    "She screams as the banana continues forward. You chase after her, trying to keep all of your limbs intact. It seems impossible, everything bounced and moved at alarming speeds, but eventually the laws of physics caught up to her as the sliding slows and Jess could get a hold of the situation." 
    "She hands you the ball, drops the pin, throws the chainsaw, and eventually puts the squirrel down." 
    J "Sigh, gosh... What a mess." 
    yn "Are you alright? That was crazy!!" 
    J "Sadly not too different from the training exercises we got to do." 
    yn "So, it looks like you can’t really get a break from the clowning." 
    J "Looks like it..." 
    J "You know what? Honk this, I just want some rest." 
    yn "Well maybe then you can come over to my place." 
    "You could feel your heartbeat. Where you being too forward?"
    yn "T-to relax that is...." 
    J "Sure, that sounds nice." 
    "So, off you went to your apartment. Despite trying to act cool, you couldn’t help but panic. Did you clean your room earlier? What if she hates the style? What if the building collapsed and you took her there for nothing? But, as you round the corner, you confirm that your apartment did not collapse and head up together."
    jump jessapartment

label jessapartment:
    scene apartment 
    "Awkwardly, you let Jess inside. Her face is struck with some strange awe."
    J "Wow, it’s so spacious in here! You live like this?" 
    "You look at your studio apartment, a little confused."
    J "Oh, sorry haha... I live with roommates, so my place seems way packed in comparison." 
    yn "That makes sense. Are you at least close?" 
    J "Not really, they’re kinda my colleagues so it feels weird to talk to them." 
    yn "Well, I don’t have roommates, so feel free to make yourself at home." 
    J "Thanks!" 
    "Jess looks around nervously. Despite the circumstances, your apartment wasn’t decorated with the idea of guests in mind. She plops down in a corner."
    yn "Oh, you can go on the sofa if you want-" 
    J "N-no its fine, it’s good for back, I think.." 
    J "But man it must feel great to wake up in here." 
    J "Your own space... You can just lay down on the floor and think." 
    yn "Yeah, I guess I take it for granted, but it is nice." 
    J "Woah what’s in that picture frame over there?" 
    
    menu:
        "My family": 
            yn "It's a picture of my family. I don’t live with them anymore, but it feels nice to see them." 
            J "That’s beautiful, you all look so happy in it." 
            yn "What’s your family like?" 
            J "Well, I never had one growing up. Right now, the rest of the clowns are kinda like my family, even if we don’t get along much." 
            J "Oh, but i hope that changes!! I really want kids in the future." 
            J "It’s just kind of hard in my current living situation and job." 

        "Travel photos":
            J "God it’s gorgeous there!" 
            yn "You ever went anywhere exciting?" 
            J "No not really, clowning is a full-time job, not much space for breaks." 
            J "Plus I don’t think my boss would let me have the time off." 
            yn "... Your boss sounds bad." 

    yn "Then why are you working at that place?" 
    J "It’s a job, [yname], I can’t just stop working." 
    yn "Why don’t you look for another? I’ve heard you talk a lot about it, but never really anything positive. What makes you glued to that place?" 
    J "I- I" 
    J "..." 
    J "It’s kind of all I’ve ever known. I can’t just give up on the only thing I’ve ever done with my life." 
    J "Plus- I have a show in four days. It would be a shame to give up on all that work." 
    yn "Okay." 
    yn "..." 
    J "I should get going." 
    J "It was nice seeing you [yname]." 
    yn "You too." 
    J "..." 
    J "It would make me happy if you checked out the show. You don’t have to of course, but still..." 
    yn "I’ll come around." 
    J "Thanks." 
    "Jess leaves." 
    yn "Maybe i shouldn’t have pushed..." 
    "But you did."

    scene black 
    jump jesscircus

label jeesscircus:
    "It's the day of the show. You haven’t heard from Jess since your last encounter."
    yn "At this point, should I even go? Things were... awkward before." 
    "No, she wanted you there, you were certain of it. Before you change your mind again, you get ready and head out the door. You’ll worry about this being a mistake afterwards."
    "You wander towards the address. What stands in front of you seems to be a very generic theatre. As you prepare to pay, a clown begins to approach you." 
    J "You actually came." 
    yn "Did... did you not want me here?" 
    J "What? No, I was hoping you would, I just didn’t know if you were going to." 
    J "You don’t need to wait in line, I already bought your ticket, just in case." 
    yn "Oh, thank you." 
    J "It's no problem." 
    J "Quick, the show’s almost started." 
    "You head inside and take your seat, while Jess heads backstage."
    "Soon, the red curtains draw back, to reveal a thin sheet. Lights turn on to reveal the shadowy appearance of clowns on the other side. They start moving immediately. Some dance, some juggle, one’s even balancing on a ball. Silhouetted chaos continues, till eventually one falls and breaks through the screen, Jess."
    "Her head thuds against the floor after the impact, smudging the makeup on her forehead. You start to stand in shock, but the show continues. She wobblily gets up and walks away, her and another clown taking the screen. The clowns return to their show, one Jess less."
    "She never comes back on stage." 
    "After the show, the people begin to file out, but you can’t help but wait. The seats are now empty. You head towards the stage."
    yn "Hello? Jess?" 
    "Another clown points you in the direction."
    x "Oh, she’s in the back." 
    "You enter a room to see a woman. It takes you a second to look past the antennae and blank face, but it’s her."
    yn "Jess are you okay??" 
    J "[yname]??" 
    J "Don’t worry, I’m fine, just a slip-up." 
    J "It happened once or twice during rehearsals too, so I’m used to it." 
    yn "Jess, this isn’t healthy. Not only is your job impeding your happiness, but it’s hurting you physically." 
    J "You know what [yname], you’re right." 
    J "I’ve done a lot of thinking since we last talked, and i really can’t keep doing this." 
    J "But I don’t know what to do!!" 
    J "I’ve done this my whole life, I live here backstage with the other performers, if I leave, where would I go?" 
    "Your chest begins to hurt. You take a deep breath, you know what you have to do now."
    yn "Live with me." 
    J "What?" 
    yn "You heard me, live with me." 
    J "[yname] that’s crazy-" 
    yn "There’s something I need to tell you, Jess." 
    yn "I- I..." 
    menu:
    
        "I love you.":
            "Jess covers her mouth in shock."
            J "God, I thought it was just me..." 
            J "I love you too, [yname]..." 
            "You look into each other's eyes. You reach for her hand, it’s soft."
            yn "Pack your stuff tonight. First thing tomorrow, we’ll move you in." 
            J "Thank you.... [yname].... for everything." 
            "THE END."
    return
