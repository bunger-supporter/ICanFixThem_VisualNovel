﻿#script file yipppeeeee, all text goes here
#if you're in VSCode I'd recommend pressing Alt+Z to have lines wrap around so you dont have to scroll sideways
#images are just for ref (obv)


#below is creating variables for the characters. Theres more info that can be put in the Character() function but thats a problem for later.
define Goo = Character("Goo")
define J = Character("Jess")
define x = Character("???")


#code taken from online for a player naming themselves, dw about it
define yn = Character("[yname]")
default yname = "Beb Brisk"
image poem  = Movie(play="cg_poem.av1", size=(1920,1080), loop=False, xalign=0.5, yalign=0.5)
# The game starts here, labels separate sections of the story + 
label start:

    #below is the background. Its simple, if you have image (ex. slimulation.png) you type "scene slimulation" without including file type, or can type a generic colour
    scene black



    #line below is dialogue, character variable + "dialogue"
    #appears like:
    #???
    #sigh... I said siggghhhhh......
    #in game
    #cps effects speed that text appears, you can also do {b} for bold and {i} for italics, you can even change text size with {size}, {w} adds a break in one message so you have to press enter again
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


    scene mug with fade
    show text "{color=#000001}{size=+20}[yname]{/size}{/color}"
        

    
    "You know what? Screw this, you’re raw dogging it today." 
    "You rub your eyes and leave for your chore-packed day." 

    yn "I’ll start with the grocery store. Call it chore warmups if you will."
#grocery store!!
    scene grocery
    "You bumble around the store picking up this and that, and before you know it, the majority of morning has gone out the window (time flies when you’re 'having fun')."
    "After some tough grocerying, you pick a comfy-looking shelf and lean up against it to relax for a minute." 
    "Unfortunately, minutes seem to have been experiencing shrinkflation as well, since not even 5 seconds pass before the entire shelf, your sole haven in this grocery hell, violently tumbles over with a deafening crash."
    scene bg_fallen with fade
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
    "You tenderly (not really) wipe as many beans off of him as you can. Except he’s like 1,000 feet tall, so there’s a lot of him to wipe beans off of.wIt didn’t occur to you before you started this endeavor, but this is gonna be an awkward amount of standing here wiping beans off some guy you don’t know. Might as well introduce yourself."

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
    show jhandssigh
    J "Hi um, sorry I'm a little lost, can you help me?" 
    hide jhandssigh
    show j
    yn "Oh uh sure, where are you headed?" 
    hide j
    show jsmile
    "You just hope it isn’t across the building." 
    hide jsmile
    show jfacesigh
    J "I’m supposed to be at the children’s sector, but this place is worse than a mirror maze. I’ve been roaming around for like half an hour." 
    "It's across the building." 
    hide jfacesigh
    show j
    yn "Yeah I think I know the way there, I can help. I’m [yname], by the way." 
    hide j
    show jhandshappy
    J "Oh, I’m Jess, nice to meet you." 
    "She puts her hand out to shake, but as soon as you grab it, you feel something nip at your fingers."
    yn "Youch!!" 
    hide jhandshappy
    show jhandssad
    J "AHH"  
    "The perpetrator quickly reveals itself as a beak pokes out from her sleeve. The dove squirms out of their shirt and flies down the hall, disappearing around the corner." 
    J "Yip-" 
    yn "huhhh?? What’s going on?" 
    J "Gosh, I’m so sorry, I guess she got bored waiting for the magic show." 
    J "But hurry!! We gotta get her back!!!" 
    yn "I guess this is my life now..." 
    hide jhandssad
    "You both run down the hallway after the bird, each step revealing a deep regret over improper time management."
    show jsigh
    J "Poor Toodaloo must’ve been woken up by the handshake." 
    yn "Are you sure she’s not a swift??" 
    hide jsigh
    scene windowdove with fade
    "Each step becomes harder than the last, but the dove keeps moving forward. It makes a sharp turn into an empty office, fear hits as both you and jess notice the open window."
    "Just as it reaches the opening, hands fly up to catch Toodaloo, and you feel the feathers between your fingers as you grasp them."
    yn "I got her!!" 
    J "Oh yes!" 
    scene hospital with fade
    "You step down and wrap the dove in your sweater while Jess brings out bird feed to calm it down. Both of you sit down together, soothing the dove. While waiting for Toodaloo to drowse off, there’s a slightly awkward air to the room.{p} Suddenly, she yawns and leans her head against your shoulder.{p} Her head up against your cheek, you can’t help but think about how warm she feels." 
    yn "uh-" 
    "Jess scrambles away."
    show jhandssad
    J "OH! I am so sorry I slept really poorly last night-" 
    hide jhandssad
    show jhandssigh
    J "Please don’t be mad-" 
    yn "Hey its fine I get it; I barely woke up this morning." 
    hide jhandssigh
    show jhandsblush
    J "..." 
    J "I’m really sorry about putting you through this [yname].. You didn’t deserve this, you were just close to my chaotic mess." 
    yn "Ah, no it’s fine... It was-" 
    yn "Interesting, that’s for sure." 
    hide jhandsblush
    show jsmile
    J "No, let me make it up to you, please. How about I buy you a coffee? Oh, no pressure, you just really helped out and I deeply appreciate it." 
    yn "Well, sure I’ll think about it." 
    yn "Plus..." 
    yn "It would be nice to spend some more time together." 
    hide jsmile
    show jfaceblush
    "Jess blushes a little." 
    J "Well, here’s my phone number. Call me if you want to see each other again." 
    hide jfaceblush
    "Before you could even say bye, Jess runs off with Toodaloo on her shoulder."  
    yn "Huh, what a strange person." 
    "..."
    yn "Wait, I never gave her directions!" 

#home!!
    scene black with fade
    "You get back home and lay down."
    "Despite the botched shopping trip and missed appointment, today’s encounters really stuck out."
    show garmupskirt at left
    "Goo..."
    show j at right
    "Jess..."
    yn "They both seem so strange, but I can’t stop thinking about them." 


    #choice!!!!!
    menu:
        #the question
        yn "But, one really sticks out."

        #answer one
        "Goo":
            hide garmupskirt
            hide j
            show garmupskirt
            yn "Goo."
            yn "He was real nice, his sincerity really makes him easy to talk to."
            yn "Maybe hanging out will be fun, maybe we can get closer.."
            hide garmupskirt
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
            hide garmupskirt
            hide j
            show j
            yn "Jess." 
            yn "She’s real sweet, I can’t help but want to spend time with her." 
            yn "Maybe the coffee date won’t be the end, maybe it’ll even lead to something more.."
            hide j 
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




    # Chapter 2 

    scene apartment

    "You get up with a spring in your step."

    "You’re gonna ask Goo out on a date today!"

    "You try to wait and call at a reasonable time, but nerves get the better of you. You’ve got all your courage gathered already, and waiting would be torture." 

    "You pick up your phone and dial his number, which you can barely make out from the scratches in the paper towel that spent a whole day (including a bird chase) in your pocket."

    "..." 

    "..."

    "..."  

    Goo "Hello?"

    yn "Hey, it’s [yname]! Are you busy?"

    Goo "Not really. Just, uh... practicing my awesome skateboard tricks! Oh yeah." 

    menu:
        "Pretend like you believe him.":
            "There’s pretty much no way that’s true, but you’ll humour him because you can tell he tried really hard to come up with that one."

            yn "Wow! Cool!"

        "Hmm...":

            "He couldn’t sound less convincing if he tried."

            yn "... Skateboard tricks? Really?" 

            Goo "Y- Yup!" 

            "He then proceeded to hold his phone a little farther from his face and make what you can only assume are 'skateboard noises' with his mouth. "


    yn "Anyway, I was wondering if maybe you’d like to hang out sometime?"
    yn "I feel like I made a pretty awful first impression yesterday, considering I almost killed you and stuff."
    yn "I’d like to try making a better one, if you’d let me. So whaddya say?"

    Goo "Wh-!! Me??? Hang out with-??" 

    "You hear him hold the phone aside and stammer a little more to himself before composing himself and replying."
    "Adorable."

    Goo "Yeah, we could do that."
    Goo "How about we meet up today at noon for co-" 

    "And then you hear what sounds like a phone falling down a well, followed by a distant 'Oh no!'. Finally, you hear it hit the water and the call terminates."

    "Huh."
    "Welp."
    "Alright then."

    yn "WAIT."
    yn "NOON IS IN 45 MINUTES."
    yn "Guess I’m hauling ass this morning." 

    scene bg_town

    "You hastily get to the only coffee shop in town (you estimate that the chances he was gonna say 'coffee' are pretty strong)."

    scene cafe

    "You make it with a couple minutes to spare! Hooray!"
    "You have a seat and pretend like you’re not glancing at the door every 10 seconds."
    "..."
    "..."
    "Okay, so he’s a few minutes late."
    "That’s alright. Maybe he doesn’t know where the only coffee shop in town is..."
    "..."
    "..."
    "..."
    "Ok, it’s been 20 minutes now."
    "Maybe he really was doing sick skateboard tricks and he broke a bone."
    "..."
    "..."
    "..."

    yn "Hmmm..." 

    "Alright, it’s been two hours and the shop owner is giving you the stink eye."  
    "Well..."
    "You’d never been stood up before."
    "It doesn’t feel great."

    "You get up to leave."
    "Outside, there’s an unusual smell adrift on the wind."
    "You definitely know it, but you can’t quite put your finger on it."
    "You look around to see where it’s coming from, and that’s when you notice the pop-up corn stand."

    scene bg_town

    "Ah, of course."
    "Boiled corn smell."
    "Wait a minute..."

    yn "Is that...?" 

    "IT’S GOO!!!"
    "Standing at... a corn... stand..."

    scene apartment
    Goo "How about we meet up today at noon for co-"
    scene bg_town

    yn "..."

    yn "Good grief." 

    scene bg_corn

    "You catch his eye and his face lights up, and..."
    "IS HIS TAIL WAGGING??"
    "THAT’S ADORABLE!!!!!"

    show gcornhappy

    "You go meet up with him and apologize a thousand times."
    "It seems like he hadn’t at all noticed two hours had passed."

    Goo "Hi there! :D" 

    "He hands you a corn cob. It’s covered in dog hair."

    Goo "Wanna go for a walk?" 

    yn "I- of course!" 

    Goo "Yay!"
    hide gcornhappy
    show gcornsad
    Goo "We can’t go very far, though."
    Goo "I’m my boss’ only employee, so he’s very good at noticing when I go over my lunch break time." 
    hide gcornsad
    "Ok... and with that said, you go for a walk."

    scene bg_town

    "You’re not terribly familiar with this part of town, so Goo leads the way."

    "It occurs to you that you’ve never been on a date before, and, well, you don’t know anything about this guy, really."
    "Gotta find something interesting and sustainable to talk about."
    "Thousands of brilliant conversation topics flash through your head."
    "You’ve been training your whole life for this."
    "Conversation is one of your greatest attributes."
    "You’re about to win his entire heart over simply by impressing him with your judicious and witty choice of topic." 

    "Just kidding, you start talking about the weather."

    yn "Weather’s nice." 

    show gcornhope
    Goo "Yup." 

    yn "I guess you probably hear the ol’ 'How’s the weather up there?' bit pretty often, huh?" 
    hide gcornhope
    show gcornsad
    Goo "Not really... no one talks to me..." 

    "Gulp. How do you even respond to that??"
    hide gcornsad
    show gcorn
    Goo "Oh wait, yes actually, my boss says that to me every single morning when I walk into work."
    Goo "And then, when I trip on the banana peel he places in front of my mailbag every day, he goes 'How’s the weather down there?'" 

    yn "He- You- Every day????" 
    hide gcorn
    show gcornhope
    Goo "Oh don’t worry, it’s alright, he lets me eat the banana peel after, if I ask nicely."
    Goo "They’re my favourite!" 

    "His gaze drifts off to the skyline and he licks his chops."
    "..."
    "Is he just thinking about banana peels?"
    "You feel a profound desire to introduce him to a new favourite food that isn’t banana peels."

    yn "I like your skirt, by the way." 
    hide gcornhope
    show gcornslightblush
    Goo "Oh... thanks..."
    hide gcornslightblush
    show gcornsad
    Goo "My boss makes fun of me a lot for always wearing skirts, but I have to, because no pants in the world fit me." 

    "Does... does he know people can sew their own pants?"
    hide gcornsad
    show gcornhope
    Goo "You know, I’ve never told this to anyone, but my greatest dream is to someday own my very own pants."
    Goo "And they would fit me just right and I could wear them all around town."
    Goo "And my boss would say 'Wowie! Those are some beautiful pants, Goo! I might even consider making you employee of the month!'"
    Goo "Sigh..." 

    yn "Aren’t you his only employee?" 
    hide gcornhope
    show gcorn
    Goo "Yeah..."
    hide gcorn
    show gcornsad
    Goo "But he always makes himself employee of the month anyway." 

    "Wow..."
    hide gcornsad
    show gcorn
    "His gaze drifts off again."
    "Guess he’s the pensive type."
    "If he’s actually thinking, that is."
    "Which you have no proof of."

    "Well, you’re pretty conversationally warmed up now."
    "Time to really get to know him!"

label gooquestions:
    menu gooping:

        "Ask about home.":
            jump home

        "Ask about languages.": 
            jump languages

        "Ask about pets.":
            jump pets

        "Ask about corn.":
            jump corn

        "Ask about music.":
            jump pinkfloyd

        "Ok, that's enough conversation.":
            jump done

label home:
    yn "So where are you from?" 
    hide gcorn
    show gcornhope
    Goo "Oh, I’m from a really nice city."
    hide gcornhope
    show gcorn
    Goo "You’ve probably never heard of it, though..."
    Goo "It’s called Montreal." 
    "Huh. Never heard of it."
    jump gooquestions

label languages:
    yn "Do you speak any other languages?" 
    Goo "Woof."    
    jump gooquestions

label pets:
    yn "Got any pets?"
    hide gcorn
    show gcornhope
    Goo "I had a goldfish once."
    Goo "I got it at a fair, and it cost me my whole month’s pay worth of coins trying to win it over and over again..."
    hide gcornhope
    show gcornsad
    Goo "But a bird snatched it on my way home." 
    "Why does the world hate this guy..."
    yn "Your whole month’s worth of pay??"
    yn "How long ago was this?" 
    Goo "Last week..."
    hide gcornsad
    show gcorn
    jump gooquestions

label corn:
    yn "Big fan of corn?"
    Goo "It has its moments."
    "What in the world does that mean??"
    jump gooquestions

label pinkfloyd:
    yn "What kind of music do you like?"
    hide gcorn
    show gcornhope
    Goo "There’s a Pink Floyd song I really enjoy."
    Goo "It’s the one that’s 17 minutes long."
    hide gcornhope
    show gcorn
    Goo "Can’t remember what it’s called, though..." 
    "Approved. That’s a good one."
    jump gooquestions

label done:
    hide gcorn
    "He finishes his corn and then starts taking loud, crunchy bites out of the cob itself. You’re not even surprised."

    "You hear a voice yell from off in the distance."

    x "GOO!! YOUR 15 MINUTE LUNCH BREAK ENDED 2 HOURS AGO!! GET BACK HERE!!" 
    show gcorncob
    Goo "Uh oh!"
    Goo "Gotta run!"
    Goo "Itwasnicetalkingiwithyou okbye!!!!!!" 
    hide gcorncob

    play sound "vroom.mp3"
    #if this doesn't work, try just 'play vroom'

    "And thus, he disappears at a break-neck speed, leaving in his wake a Looney Toons style cloud of dust (and dog hair)."

    "..." 

    play sound "vroom.mp3"

    "About 12 seconds later, he runs past you in the opposite direction, wearing his mailman uniform (which seems to just be a hat) and carrying a mailbag about the size of Santa Claus’ toy bag, and then he disappears into the horizon."

    "..."
    "..." 

    "That was a great date!"

    play sound "fanfare.mp3"

    "Time to head home!"

    scene apartment
    "That Goo guy sure is something..."
    "He’s like..."
    "The man of your dreams..."
    "Sigh..." 

    "Tonight, you fall asleep with a great big smile on your face."

    scene black with fade

    "And you even dream of him..."

    scene bg_fish with fade
    
    scene black with fade


    scene apartment with fade
    "About a week has passed since your date with Goo."
    "You’ve tried reaching him since, but to no avail."
    "Hey, it only took you about 6 calls to remember his phone was in a well somewhere."
    "Ayway, today’s the day you usually get your mail, so you’re patiently waiting by the door."
    "He probably normally just drops it and keeps running, but you have a gut feeling that today, he’s gonna stop to say hello."
    "Any second now..."

    "..."

    "..."

    "..."

    "..."

    "..."

    "..."

    "..."

    "..."

    "..."

    "..."

    "..."

    "..."

    "..."

    "*DING DONG* "

    "You scurry to the door."

    scene hewwooo
    Goo "Helloooo! Helloooo!"
    Goo "Delivery for [yname]!" 

    "You open the door."
    scene apartment
    show gmailarmuphappy
    "You don’t realize it, but you’re blushing ever so slightly."  

    yn "H- hi Goo!"
    yn "Nice to see you again!" 

    menu: 
        "Hug him!":

            "You wrap your arms around him. He smells nice???"
            hide gmailarmuphappy
            show gmailarmupbigblush
            Goo "!!!" 

            "When you let go, he hands you an envelope with your name (written in huge letters) on it."
            hide gmailarmupbigblush
            show gmailarmuphappy

        "Dap him up? (99\% change of failure)":

            "You lift your arm to dap him up and he enthusiastically places an envelope in your hand. Your name is written on it in huge letters."


    Goo "For you! Go ahead, open it!" 

    "Is he just gonna stand there while you open the letter and read it in front of him???"
    "Alright.....?"

    "You tear the envelope and pull out the (surprisingly) tremendously neatly folded letter."
    "You actuallt didn't know it was possible to fold a paper this precisely."
    "Guess he’s got some talent after all."
    hide gmailarmuphappy

    show cg_letter
    "..."
    hide cg_letter
    show gmailarmuphappy

    "You look at him with 'a hint of confusion' (what the hell is happening) in your eyes."

    yn "Ok???? I’ll be there??" 
    Goo "Yaaay! :D"
    hide gmailarmuphappy
    "And then he runs off, at his usual Mach speed."

    "..." 

    "Well alright."

    "Once he’s out of sight (so approximately 3 seconds later), you get right to work."
    "The rest of your day will be spent sewing the biggest pants of all time."

    "..." 

    "..." 

    scene cg_morning
    "Wow! It’s tomorrow already! Isn’t it great how the world works?"

    "You pack your gift and make your way to the corn stand."
    "Huh, it’s gone."
    "Guess corn season’s over already."
    "Too bad."

    "You head what feels like 2 km west, as instructed."
    "You don’t quite know what you expected, but this wasn’t even close."

    scene bg_field

    "It’s the plainest, emptiest, flattest field you’ve seen in your life."
    "Heck, possibly most in the world."
    "But aha!"
    "What’s that in the distance?"

    scene bg_mini_party

    "Time to investigate!"

    "..."

    "Big field, huh?"

    "..." 

    "You made it!"

    scene bg_party

    "There’s an assortment of large rocks and logs strewn about the area."

    "How’d he do that?"

    Goo "Oh hi, you’re right on time!" 

    "Normally, being snuck up on in a field would’ve given you about a dozen heart attacks, but his voice is so inoffensive that you manage to make it out with only half a stroke."

    show gbdayskirthandshappy

    Goo "Thanks for coming! Alright, let’s begin!" 

    "He proceeds to pull out a really crumpled piece of paper."
    "Guess his folding skills are selective."
    hide gbdayskirthandshappy
    show gbdayskirtarmuphope

    Goo "Ok, we’ll start with the gift. I’ve heard that people usually give a gift at birthday parties, so I made this for you!" 

    "He hands you what appears to be a palm-sized bug constructed from bits and bobs that seem to have originated from ye olde junkyarde."
    hide gbdayskirtarmuphope
    show cg_bug

    "A man after your own heart."
    "You think to yourself, 'If this were a dating sim, my hearts would be maxxed out now.'"
    hide cg_bug

    "Wait what??"
    "Why’d he give you a gift????"
    "Does he really not know how birthday parties work??"
    show gbdayskirthandshope
    Goo "Wow, that was fun! Alright what’s next?" 

    "He pulls the list out again, but, not having the most optimal paws for holding little pieces of paper, a mild gust of wind blows it right out of his grasp." 
    hide gbdayskirthandshope
    scene black

    "And into your face."

    "..."

    "You grab the list and read it."
    scene bg_party
    show cg_list_real_real

    "..." 
    yn "... Goo?" 
    hide cg_list_real_real

    show gbdayskirtsad
    Goo "Is it all wrong?"
    Goo "Gosh, I’m really sorry..."
    Goo "I’ve never been to a birthday party before, much less had one myself."
    Goo "But I did read a book with a birthday party in it once, when I was younger."
    Goo "I thought maybe I could recreate it..." 

    "You’re at such a loss for words."
    "Ok, hold on, first things first."

    yn "Okay, Goo."
    yn "I’ve been to many a birthday party in my day, and there’s something really important you should know."
    yn "You’re not the one who gives me a gift."
    yn "Although I appreciate the thought very much." 

    "You take his hand and give him a kind smile."
    hide gbdayskirtsad
    show gbdayskirtarmupbigblush
    "He blushes so hard you can see it through his fur."

    yn "But no."
    yn "I’M the one who’s supposed to give YOU a gift."
    yn "Close your eyes." 
    hide gbdayskirtarmupbigblush
    "You reach into your bag and gingerly pull out the humongous pair of pants you made for your prince charming."
    "You hold them out for him."

    yn "Now open your eyes." 
    show gbdayskirthandshappy
    Goo "!!!!!!" 

    Goo "ARE THOSE??!?!"
    Goo "PANTS!!??!?!?!"
    Goo "FOR ME!?!?!?!?!?!"
    Goo "But... but... there’s no way these are gonna fit, right?" 

    "He puts them on ."
    hide gbdayskirthandshappy
    show gbdaypantshandsbigblush
    "They couldn’t possibly fit any better."

    Goo "WOOOOW!!!!!!" 

    "He jumps up super high, and then takes a big giant lick at the side of your face."

    Goo "I’m so happy I could- I could-" 

    "And then he passes out."

    hide gbdaypantshandsbigblush

    "Luckily..."

    scene cg_he_died
    "You caught him."

    "Wow, this guy weighs like 3 grams."

    "Now what are you gonna do with him?"

    yn "Oh! I got it!"  

    "You’re gonna take him out for a REAL day of birthday fun!"

    yn "Hmm... where to first?" 

    "..." 

    scene black

    "The day went by."
    "You two had... well, just about the most fun you’ve had in years!"  

    "You went roller skating..."

    Goo "Weee!" 

    "You went to a clown show..."

    Goo "Heehee!" 

    "You got ice cream..."

    play sound "splat.mp3"

    Goo "Aw... mine fell on the floor :(" 

    "You played laser tag..."

    Goo "AAAH!!" 

    "You went to see a movie..."

    Goo ":0" 

    "And then you brought him home."

    scene apartment
    show ghandspantshappy
    Goo "That must have been the second best day off my whole life!"
    Goo "It comes really close to that day where my boss let me have TWO banana peels, but, y’know..."
    Goo "There’s just something unbeatable about two banana peels." 

    "Can’t argue with that, I guess..."

    yn "Sit down, make yourself comfy."
    yn "I’m gonna bake you a birthday cake!" 

    Goo "Oh boy!"
    Goo "Can I help?" 

    "You ponder the nutritional value of a dog hair cake..."

    yn "Nah, I got this." 
    hide ghandspantshappy

    "You dust off your mom’s peanut butter cake recipe, take out the ingredients and get to work."

    "While you’re crafting Goo’s cake (and doing so with all the love in your heart, might I add), he rustles about and reveals yet another piece of paper."
    show garmuppantsslightblush
    Goo "Hey..."
    Goo "[yname]?"
    Goo "Would it be OK if I read you my latest poem?"
    Goo "I’m really proud of it..." 

    "HE WRITES POETRY?????"

    yn "Wh-"
    yn "Of course!"
    yn "It would be my pleasure to listen." 

    Goo "Alright then... here goes.."
    Goo "*Ahem*" 
    hide garmuppantsslightblush

#    $ renpy.movie_cutscene("cg_poem.av1")
#    $ renpy.movie_cutscene("cg_poem.avi")
    $ renpy.movie_cutscene("images/cg_poem_webm.webm")


#    image cg_poem  = Movie(play="cg_poem.av1", size=(1920,1080), loop=False, xalign=0.5, yalign=0.5)
#    image cg_poem  = Movie(play="cg_poem.avi", size=(1920,1080), loop=False, xalign=0.5, yalign=0.5)
#    image cg_poem_webm  = Movie(play="images/cg_poem_webm.webm", size=(1920,1080), loop=False, xalign=0.5, yalign=0.5)
#    show cg_poem_webm

    jump ending

label ending:
    scene apartment
    "..."

    yn "Oh, Goo... that was..." 

    show garmuppantsbigblush

    Goo "You know, [yname]..."
    Goo "I had a wonderful time with you today."
    Goo "And I was wondering if maybe..."
    Goo "We could see each other, like, every day?"
    Goo "What I mean is..."
    Goo "Well... it’s... you know..."
    Goo "I-" 

    yn "You want us to date?" 

    Goo "Yes... I think I would like that." 

    "Your heart is practicing its jackhammer impression in your chest."

    yn "Alright."
    yn "I hereby pronounce you: my boyfriend." 

    Goo "Yaaayyy! :D" 

    "You walk over and kiss him on the cheek."
    "Well, more like on the side of his long, long nose."
    hide garmuppantsbigblush
    "You go back to the kitchen to put the cake in the oven, and then you return to the couch and lie in his arms..."
    scene black with fade
    "You’re happier than ever."

    return
# end of goo route!!!!!!!!!!!!








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
    scene cafe with fade
    "You pull up to the cafe, filled with hope and anxiety. You check the time, despite your elongated route, you still arrive 10 minutes early. Still, there’s only so many circles someone can walk without drawing suspicion." 
    yn "huh?" 
    show j
    "Suddenly, you see her. Jess, more early than you, sitting at one of the tables. She awkwardly waves to you and you head over."
    yn "I guess we’re both early then." 
    hide j
    show jhappy
    J "Looks like it, heheh." 
    hide jhappy
    show j
    J "..." 
    yn "..." 
    hide j
    show jhandsblush
    J "..." 
    "Before you sat down, all sorts of ideas ran through your mind as to how this chat would go. Now that you’re here though, it seems as if none of them would come true. You forgot you really didn’t know anything about Jess."
    hide jhandsblush
    show jhands
    yn "So... what do you do for a living?" 
    "As soon as the words come out of your mouth, you can’t help but be embarrassed at the obviousness of the answer."
    hide jhands
    show jhandshappy
    "Jess giggles."
    hide jhandshappy
    show jhandssmile
    J "well, I don’t just dress like this for fun," 
    yn "{size=20}just?{/size}" 
    J "I’m a professional clown." 
    hide jhandssmile

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
    show j
    J "... it can be, but I’ve been in the biz so long that I’m used to the hard parts."
    show jsigh 
    J "Although I can’t really handle group performances." 
    hide jsigh
    jump clownquestions
label clown:
    show jfacesmile
    J "Ough, as long as I can remember." 
    yn "Did you start as a kid?"
    J "I think I was around 15 when I started." 
    hide jfacesmile
    show jhands
    J "I’m 28 by the way, I’ve been told i have kind of a young face." 
    "You wonder if it's her face or the layers of makeup over it."
    hide jhands
    jump clownquestions
label childhood:
    show j
    J "I don’t think so." 
    show jsigh
    J "Don’t get me wrong I love the genre, but sometimes it feels like I’m more clown than Jess." 
    hide jsigh
    jump clownquestions
label what:
    show jhandssmile
    J "some different things." 
    hide jhandssmile
    show jfacehappy
    J "My favourite job is cheering up some of the child patients at the hospital, but I also do birthday parties and some clown shows." 
    hide jfacehappy
    show jsmile
    J "We’re actually hosting one soon if you want to check it out." 
    hide jsmile
    jump clownquestions

label jesscoffeepart2:
    show jhandssmile
    yn "Do you make a lot being a clown?" 
    hide jhandssmile
    show jhandssad
    J "Haha, wno" 
    yn "Maybe I should buy your coffee then *chuckles*" 
    hide jhandssad
    show jsad
    J "Wha- Wh- But I wanted to thank you!!" 
    hide jsad
    show jsigh
    "Jess takes a deep breath. Her voice slows."
    hide jsigh
    show jhandsblush
    J "Genuinely. Like I caused such a mess, and i really appreciate your help. Toodaloo does too, she’s doing much better now. Especially since she’s on break from magic tricks." 
    yn "Hey, there’s no need to get so hung up on it. Would you believe that I almost pancaked a guy beforehand at the grocery store?" 
    hide jhandsblush
    show jfacesmile
    J "What??? Are you the one that dropped the shelf!?" 
    yn "How did you know????" 
    hide jfacesmile
    show jfacehappy
    J "It was on the local news!" 
    "You both snicker at the events that transpired the day before. Whatever awkwardness that was there at the beginning had disappeared. Rather than a stranger, you saw before you a friend."
    hide jfacehappy
    show jface
    yn "Hey, why was the clown’s bag so full?" 
    "Jess stares for a moment."
    hide jface
    show j
    J "Well, why don’t I check?" 
    "She picks up her purse from under the table, its just as colourful as she was. She pulls out her wallet, then a scarf, then another scarf, and another."
    "Not too long and she’s covered head to toe in scarves all tied together." 
    hide j
    show jsmile 
    J "Well, seems we have our answer." 
    "She muffles out from the inside of her tent." 
    yn "Well, i was gonna say ‘because it had to carry their emotional baggage,’ but that works too." 
    hide jsmile
    show jfacesmile
    J "pft." 
    hide jfacesmile
    show jhandshappy
    J "HAHAHAHAHAHAHAHHAHAHAH!!!" 
    "You’re caught off guard, uncertain if she truly thought you were that funny, or if she’s overcompensating."
    "Her voice, hoarse, almost reassured your worries."
    hide jhandshappy
    show jsmile
    J "Ah shucks, between the two of us, you should’ve been the clown!" 
    yn "Thanks!" 
    J "You should meet my buddy, Binko, he’s got some good ones too." 
    yn "Well, you want to hear another?" 
    hide jsmile
    scene black with fade
    "The date went on. Laughs were thrown around as jokes were passed. Eventually, the poor workers had to ask you to leave as you raised the decibel level in the room by at least 30. Before separating, you agreed to another date. Well, not quite an official date yet, but Jess flushed face, even through makeup, seemed to want to say it."
    "Just, for the moment, you appreciate the one you already had."
    jump jesspark
    
label jesspark:
    "A week later, it was finally time for the second ‘date.’"

    scene park 
    "This time, it’s going to be a pleasant stroll through the park. Once again you arrive early and still are beaten out by Jess."
    show jhandssmile
    J "Hi! Nice day, isn’t it?" 
    "You’re starting to wonder if the makeup is just actually her skin."
    yn "Yeah definitely, by the way, why did you pick the park?"
    hide jhandssmile
    show jhands 
    J "Well, it’s always good to get fresh air. The atmosphere at the rehearsal hall is like mildew." 
    yn "Right, you gotta practice for that show soon." 
    hide jhands
    show jhandssigh
    J "Yup, and my boss is a bit of a perfectionist so it’s pretty draining." 
    hide jhandssigh
    show j
    yn "Well, at least you get a little break from clown stuff right now {cps=*2}{size=20}{i}as much as you can in full costume.{/i}{/size}{/cps}" 
    J "Oh yes! Just got to enjoy the {cps=*0.5}suuuuunnnnnnnn-{/cps}"
    hide j 
    scene jugglepark with fade
    "Jess slides forward as she steps on a banana peel, pushing her several meters down the path. She waves her arms as she attempts to stabilize, only bumping into those around her. They fall and launch their possessions up, which Jess struggles to catch.{w} It started simple, a dog’s rubber ball,{w} then a hat,{w} and soon she was juggling a bowling pin, chainsaw, squirrel, and who knows what else."
    J "AHHHH HELP!!!" 
    "She screams as the banana continues forward. You chase after her, trying to keep all of your limbs intact. It seems impossible, everything bounced and moved at alarming speeds, but eventually the laws of physics caught up to her as the sliding slows and Jess could get a hold of the situation." 
    "She hands you the ball, drops the pin, throws the chainsaw, and eventually puts the squirrel down." 
    scene park with fade
    show jfacesigh
    J "Sigh, gosh... What a mess." 
    yn "Are you alright? That was crazy!!" 
    hide jfacesigh
    show jface
    J "Sadly not too different from the training exercises we got to do." 
    yn "So, it looks like you can’t really get a break from the clowning." 
    J "Looks like it..." 
    hide jface
    show jfacesad
    J "You know what? Honk this, I just want some rest." 
    hide jfacesad
    show jblush
    yn "Well maybe then you can come over to my place." 
    "You could feel your heartbeat. Where you being too forward?"
    yn "T-to relax that is...." 
    hide jblush
    show jhandsblush
    J "Sure, that sounds nice." 
    scene black with fade
    hide jhandsblush
    "So, off you went to your apartment. Despite trying to act cool, you couldn’t help but panic. Did you clean your room earlier? What if she hates the style? What if the building collapsed and you took her there for nothing? But, as you round the corner, you confirm that your apartment did not collapse and head up together."
    jump jessapartment

label jessapartment:
    scene apartment with fade
    "Awkwardly, you let Jess inside. Her face is struck with some strange awe."
    show jfacehappy
    J "Wow, it’s so spacious in here! You live like this?" 
    "You look at your studio apartment, a little confused."
    hide jfacehappy
    show jfacesmile
    J "Oh, sorry haha... I live with roommates, so my place seems way packed in comparison." 
    yn "That makes sense. Are you at least close?" 
    hide jfacesmile
    show jhands
    J "Not really, they’re kinda my colleagues so it feels weird to talk to them." 
    yn "Well, I don’t have roommates, so feel free to make yourself at home."
    hide jhands
    show jsmile 
    J "Thanks!"
    hide jsmile 
    "Jess looks around nervously. She plops down in a corner."
    yn "Oh, you can go on the sofa if you want-" 
    show j
    J "N-no its fine, it’s good for back, {w}I think.." 
    hide j
    show jfacesmile
    J "But man it must feel great to wake up in here." 
    J "Your own space... You can just lay down on the floor and think." 
    yn "Yeah, I guess I take it for granted, but it is nice." 
    hide jfacesmile
    show jsmile
    J "Woah what’s in that picture frame over there?" 
    
    menu:
        "My family": 
            yn "It's a picture of my family. I don’t live with them anymore, but it feels nice to see them." 
            J "That’s beautiful, you all look so happy in it."
            hide jsmile
            show jhands
            yn "What’s your family like?" 
            J "Well, I never had one growing up. Right now, the rest of the clowns are kinda like my family, even if we don’t get along much." 
            hide jhands
            show jfacesigh
            J "Oh, but i hope that changes!! I really want kids in the future." 
            hide jfacesigh
            show jface
            J "It’s just kind of hard in my current living situation and job." 
            hide jface

        "Travel photos":
            hide jsmile
            show jhandshappy
            J "God it’s gorgeous there!" 
            yn "You ever went anywhere exciting?" 
            hide jhandshappy
            show jhandssmile
            J "No not really, clowning is a full-time job, not much space for breaks." 
            J "Plus I don’t think my boss would let me have the time off." 
            yn "... Your boss sounds bad." 
            hide jhandssmile

    show j
    yn "Then why are you working at that place?" 
    hide j
    show jhands
    J "It’s a job, [yname], I can’t just stop working." 
    yn "Why don’t you look for another? I’ve heard you talk a lot about it, but never really anything positive. What makes you glued to that place?"
    hide jhands
    show jhandsblush
    J "I- I" 
    J "..." 
    hide jhandsblush
    show j
    J "It’s kind of all I’ve ever known. I can’t just give up on the only thing I’ve ever done with my life." 
    hide j
    show jsmile
    J "Plus- I have a show in four days. It would be a shame to give up on all that work." 
    yn "Okay."
    hide jsmile 
    show jhands
    yn "..." 
    J "I should get going." 
    J "It was nice seeing you [yname]." 
    yn "You too." 
    hide jhands
    show jhandsblush
    J "..." 
    hide jhandsblush
    show jsmile
    J "It would make me happy if you checked out the show. You don’t have to of course, but still..." 
    yn "I’ll come around." 
    J "Thanks."
    hide jsmile 
    "Jess leaves." 
    yn "Maybe i shouldn’t have pushed..." 
    "But you did."

    scene black with fade
    jump jesscircus

label jesscircus:
    "It's the day of the show. You haven’t heard from Jess since your last encounter."
    yn "At this point, should I even go? Things were... awkward before." 
    "No, she wanted you there, you were certain of it. Before you change your mind again, you get ready and head out the door. You’ll worry about this being a mistake afterwards."
    scene theatre
    "You wander towards the address. What stands in front of you seems to be a very generic theatre. As you prepare to pay, a clown begins to approach you." 
    show jsmile
    J "You actually came." 
    yn "Did... did you not want me here?" 
    hide jsmile
    show jblush
    J "What? No, I was hoping you would, I just didn’t know if you were going to."
    hide jblush
    show j 
    J "You don’t need to wait in line, I already bought your ticket, just in case." 
    yn "Oh, thank you." 
    hide j
    show jsmile
    J "It's no problem." 
    J "Quick, the show’s almost started." 
    hide jsmile
    scene black
    "You head inside and take your seat, while Jess heads backstage."
    scene shadow with fade
    "Soon, the red curtains draw back, to reveal a thin sheet. Lights turn on to reveal the shadowy appearance of clowns on the other side. They start moving immediately. Some dance, some juggle, one’s even balancing on a ball. Silhouetted chaos continues, till eventually one falls and breaks through the screen,{w} Jess."
    "Her head thuds against the floor after the impact, smudging the makeup on her forehead.{w} You start to stand in shock, but the show continues. She wobblily gets up and walks away, her and another clown taking the screen. The clowns return to their show, one Jess less."
    "She never comes back on stage." 
    scene black
    "After the show, the people begin to file out, but you can’t help but wait. The seats are now empty. You head towards the stage."
    yn "Hello? Jess?" 
    "Another clown points you in the direction."
    x "Oh, she’s in the back." 
    scene bunkapartment
    show jess
    "You enter a room to see a woman. It takes you a second to look past the antennae and blank face, but it’s her."
    yn "Jess are you okay??" 
    J "[yname]??" 
    hide jess
    show jesssmile
    J "Don’t worry, I’m fine, just a slip-up."
    J "It happened once or twice during rehearsals too, so I’m used to it." 
    hide jesssmile
    show jess
    yn "Jess, this isn’t healthy. Not only is your job impeding your happiness, but it’s hurting you physically."
    hide jess 
    show jessangry
    J "You know what [yname], you’re right." 
    J "I’ve done a lot of thinking since we last talked, and i really can’t keep doing this." 
    hide jessangry
    show jesssad
    J "But I don’t know what to do!!"
    hide jesssad
    show jessangry 
    J "I’ve done this my whole life, I live here backstage with the other performers, if I leave, where would I go?" 
    "Your chest begins to hurt. You take a deep breath, you know what you have to do now."
    yn "Live with me." 
    hide jessangry
    show jesssad
    J "What?" 
    yn "You heard me, live with me." 
    J "[yname] that’s crazy-" 
    yn "There’s something I need to tell you, Jess." 
    yn "I- I..." 
    menu:
    
        "I love you.":
            "Jess covers her mouth in shock."
            hide jesssad
            show jesshappy
            J "God, I thought it was just me..." 
            J "I love you too, [yname]..." 
            hide jesshappy
            show jesssmile
            "You look into each other's eyes. You reach for her hand, it’s soft."
            yn "Pack your stuff tonight. First thing tomorrow, we’ll move you in." 
            hide jesssmile
            show jesshappy
            J "Thank you.... [yname].... for everything." 
            scene black with fade
            "THE END."
    return
