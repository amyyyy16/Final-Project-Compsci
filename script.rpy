# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("[name]")
define coffee = Character("Barista")
define secret = Character("???")
define wise2 = Character("Eilyan")
define mon1 = Character("Abysswing")
define mon2 = Character("Shadeling")
define boss = Character("Helltalon")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    define n = Character("[name]")

    python:
        name = renpy.input("What is your name?")
        name = name.strip()

        if not name:
            name = "Y/N"

    "Your name is [name]?"

    menu:
        "Yes":
            jump con

        "No":
            jump again

    label again:
        "Well we are going to continue and call you whatever you wrote, we simply don't have the time for your shenanigans"

        jump reg

    label con:
        "Good, we can continue"

        jump reg

    label reg:

        "This game is about imagining the story that we put you through in a way that is unique to only you"

        "So please sit back, relax, and let your mind drift to the parts of it that you didn't think possible."

        "Of course, remember, have fun"

        jump story

    # These display lines of dialogue.

    #Input a coffeeshop image here, maybe a sound if you're feeling it"

    label story:
        "You are outside of your apartment for some reason, leaving the small place was not the smartest of ideas, but here you are"

        "You walk into a coffeeshop that has a sailors name for some reason to pick up your overpriced coffee"

        e "*This day can't get any worse*"

        coffee "Order for...[name]!?"

        e "Oh, uh that's me, thanks."

        e "*Well, atleast I have my drink*"

        e "ERRGUHH"

        e "Of course they got it wrong"

        e "*this has been the worst day of my entire life*"

        "You walk to the nearest garbage can to throw out your coffee which suspiciously tasted like green tea, when you hear a distant voice"

        secret "I seem to understand that you are not having a good day"

        e "Huh? What?"

        e "Who said that!?!?"

        "A little startled, you turn towards where the voice came from"

        "To your surprise, you see a short man with a long white beard and grey robes on looking up at you"

        show wizard at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

        e "OH?!"

        e "Uh? Hi? Erm? Who are you?"

        wise2 "I'm Eilyan the wizard and you, [name], are the chosen one"

        e "Huh, this can't be happening, this day has been insane."

        wise2 "We're going now"

        hide wizard

        #sparke effect

        "Everything goes white for a milisecond, then your scenery changes to a forest."

        e "WOAH!?!?"

        e "Okay a little warning nex- hey where are you going?!"

        show wizard at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

        "Eilyan started walking towards a table with four glass tubes."

        wise2 "You need to pick your class."

        e "No, I'm not doing anything, I don't know where we are. Take me back home now!"

        wise2 "We don't have time for your nonsense, pick one or the world as you know it will cease."

        e "How do I know I can even believe you?"

        wise2 "If you don't you can leave anytime you want, but then you must understand that when the world ends, that is on you and you alone."

        e "..."

        e "Okay, fine, what are my options?"

        wise2 "You can choose one of the following items, a Hat, Pen, Twig, and a Sweater"

        e "Okay, so it might just be me, but these all seem useless"

        wise2 "..."

        "Eilyan doesn't respond, he just stares at you"

        wise2 "..."

        e "Alright then, uhhh I choose the..."

        hide wizard

        menu:
            "Hat":
                $ classopt = "hat"
                jump hat

            "Pen":
                $ classopt = "pen"
                jump pen

            "Twig":
                $ classopt = "twig"
                jump twig

            "Sweater":
                $ classopt = "sweater"
                jump sweater

        label hat:
            "You grab the green hat and put it on, and out of no where a sword an sheild appear on your body"

            jump h

        label pen:
            "You grab the weirdly futuristic pen with a button on the side"

            jump p

        label twig:
            "You grab the mishapen, yet oddly weighty twig"

            jump t

        label sweater:
            "You grab the sweater that has an English train station on the front"

            jump s

    label h:
        #screen shake
        e "WOAH"

        e "That was unexpected, uhhhh..."

        e "Are the sword and sheild really necessary for the \"great mission\" I've been chosen for?"

        wise2 "Yes, we must go, NOW!"

        hide wizard

        jump ww

    label p:
        "Curiousity gets the best of you and you press the red button"

        #laser sound, screen shake

        "A yellow laser comes out the top and you leap back statled"

        e "OH SHOOT!"

        e "WOAH! Do I get the powers to lift things aswell?"

        wise2 "..."

        wise2 "We don't have time for this, we need to go now!"

        hide wizard

        jump ww

    label t:
        "You turn the twig in your hands, a bit confused as to what you are supposed to do with it?"

        wise2 "You chose what I chose when I was about your age"

        e "Oh? Well forgive me but I am a bit confused as to what I am supposed to do with it"

        wise2 "No time for that, we must go NOW!"

        hide wizard

        jump ww

    label s:
        "You slip on the purple sweater and suddenly, you have a painful headache"

        e "OWW, gosh is my head supposed to hurt this much"

        wise2 "It's just increasing your knowledge, suck it up"

        wise2 "No time to explain, we have to go NOW!"

        hide wizard

        jump ww

    #hat
    label ww:

        "Everything goes white again, and you are back in your city, this time in an alley."

        show wizard at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

        e "Wait, okay so what am I supposed to do?"

        wise2 "Just follow the trail of things that don't seem normal and it'll take you to your first trial."

        hide wizard

        "With that Eilyan disappeared, leaving you to your own devices."

        e "Well that was descriptive."

        "You walk out the alley and immeadiately realize everything was off."

        e "This is definetily not right."

        e "There are straight up snakes slitering down the sidewalk how is no one else noticing this?"

        "You walk up to a person on the street and wave your hand infront of them."

        "Nothing happened, they just walked through it."

        e "So I'm home, but not home, alright cool cool cool."

        e "Maybe...I'm supposed to go back home?"

        e "Yeah well that just sounds like a good idea"

        "You look around and see that there are monsters around you all heading somewhere."

        e "*ohhhhhh crap...*"

        e "*...I have to remain hidden"

        "You make your way back to your apartment building trying to stay as hidden as possible."

        e "*There are more monsters here than there were back where Eilyan left me.*"

        e "Well...here goes nothing."

        "You walked into the building to find that it is crawling with monsters, creatures, and unsuspecting humans alike."

        e "This is crazy, like absolutely crazy."

        secret "So you're [name]? I would've thought you were taller."

        "You turn quickly to see a short humanoid monster."

        e "Who are you and why do you know who I am?"

        mon1 "Haha, my name is Abysswing, and I'm surprised that everyone here doesn't know you, you are [name] the chosen one."

        e "What was it that I'm chosen for exactly?"

        mon1 "Do you not know? Well you are the one who is \"supposedly\" going to overthrow out king, and prevent us from infiltrating the human world."

        e "*why on Earth would you tell me what your plan is, all you did is tell me what I need to do. How dumb are you?*"

        e "Sooooo... about that... you mind taking me to him?"

        mon1 "Sure, but you must go through me first \"chosen one\""

        "Abysswing lifts various objects from around him and smirks devilously"

        mon1 "This will be your end [name]"

        e "oh crap crap crap crap"

        "You freak out tring to think of what to do."

        "You remember what Eilyan had given you to protect yourself."

        if classopt == "hat":
            "You take out your sword and sheild"

            mon1 "You think that will stop me? You clearly underestimate me."

            "Abysswing, is about to throw the various objects he is levitating around him at you."

            "You can either..."

            menu:
                "Protect yourself":
                    jump protect1

                "Attack MONSTER":
                    jump attack1

        if classopt == "pen":
            "You take out your light sword"

            mon1 "You think that will stop me? You clearly underestimate me."

            "Abysswing, is about to throw the various objects he is levitating around him at you."

            "You can either..."

            menu:
                "Protect yourself":
                    jump protect2

                "Attack MONSTER":
                    jump attack2

        elif classopt == "twig":
            "You take out your wand"

            mon1 "You think that will stop me? You clearly underestimate me."

            "Abysswing, is about to throw the various objects he is levitating around him at you."

            "You can either..."

            menu:
                "Protect yourself":
                    jump protect3

                "Attack Abysswing":
                    jump attack3

        if classopt == "sweater":
            "Your eyes glow purple and your hair stars to rise as you levitate of the ground preparing yourself for the attack"

            mon1 "Haha, do you know how to even use your power?"

            e "Well there is a first for everything."

            "Abysswing, is about to throw the various objects he is levitating around him at you."

            "You can either..."

            menu:
                "Protect yourself":
                    jump protect4

                "Attack Abysswing":
                    jump attack4

    label protect1:
        "You put your sheild infront of your body to protect yourself."

        mon1 "Haha what good will that do you?"

        "Abysswing throws a chair at you that deflects of the sheild, but not without causing you to jerk backwards."

        mon1 "That...was not was supposed to happen."

        "You decide that this is as good a time as any to attack Abysswing."

        jump attack1

    label attack1:
        "You run at Abysswing with your sword in hand, effortlessly dodging the various objects that are hurdling at you."

        "You manage to reach him and hold your sword at his neck."

        e "Surrender now, don't make me kill someone."

        mon1 "Hmm, you may have bested me, but you have no idea what is coming."

        "Abysswing dissolves and a blue light evaporated upward."

        e "That was... weird, to say the least."

        jump continue2

    label protect2:
        "You stand guard with your light saber in a defensive position."

        mon1 "Haha what good will that do you?"

        "Abysswing throws a chair at you that you cut through with ease protecting yourself from the projectile."

        mon1 "That...was not was supposed to happen."

        "You decide that this is as good a time as any to attack Abysswing."

        jump attack2

    label attack2:
        "You run at Abysswing with your saber in hand, effortlessly dodging the various objects that are hurdling at you."

        "You manage to reach him and you hold your saber at his neck."

        e "Surrender now, don't make me kill someone."

        mon1 "Hmm, you may have bested me, but you have no idea what is coming."

        "Abysswing dissolves and a blue light evaporated upward."

        e "That was... weird, to say the least."

        jump continue2

    label protect3:
        "You stand guard with your wand in hand, objects hurdling at you."

        "You close your eyes having absolutely no idea of how to use the thing."

        #sound

        "You open your eyes and all the objects have turned into paper birds."

        e "What the?"

        mon1 "Well...that was not supposed to happen."

        "You decide that this is as good a time as any to attack Abysswing."

        jump attack3

    label attack3:
        "You run at Abysswing with your wand in your hand, dodging the objects hurding at you."

        "You manage to reach him and hold you wand at his neck."

        e "Surrender now, don't make me kill someone."

        mon1 "Hmm, you may have bested me, but you have no idea what is coming."

        "Abysswing dissolves and a blue light evaporated upward."

        e "That was... weird, to say the least."

        jump continue2

    label protect4:
        "You watch as the objects hurdling came closer with every milisecond passing."

        "At the last second you create create a sheild around yourself and all the objects fall to the ground."

        e "Woah..."

        mon1 "You are stronger than I thought you were..."

        mon1 "That was not supposed to happen."

        "You decide that this is as good a time as any to attack Abysswing."

        jump attack4

    label attack4:
        "You float higher off the ground and in a split second a ball that resembles a purple electro ball from a game you used to play came flying from your hands."

        "It hits Abysswing and he stumbles back"

        mon1 "Ow, how did you?..."

        mon1 "You're one of \"them\""

        "You prepared for another attack from Abysswing, but he evaporated before you or him could attack again."

        "You lowered and went back to normal, standing on the ground like nothing happened."

        e "That was... weird, to say the least."

        jump continue2

    label continue2:

        "You catch your breath after the battle."

        e "*That wasn't much of a fight, Abysswing kinda just let me best him."

        e "*Well no matter, I have to get to this \"King\" or something."

        e "But first, home."

        "You walk to the elevator that you normally take to your apartment."

        "The moment it opens 6 creatures came bursting out of it, completely ignoring you, excpet for one who remained in the elevator."

        secret "Well, well, well, isn't it [name]."

        "The masked monster said to you as you walked into the elevator."

        e "Let me guess, I'm shorter than you thought I was?"

        secret "That was not what was going to say, but now that you mention it, yes actually."

        e "Oh, well thanks..."

        e "I guess?"

        e "..."

        secret "..."

        e "..."

        e "Okay this is killing me, who are you? When am I fighting you? And where is your \"king\""

        "The masked monster chuckles and shakes their head."

        mon2 "My name is Shadeling and I'm not as stupid as Abysswing I won't just tell you what the plan is."

        e "Worth the shot, so what are your powers?"

        "The elavator dings signaling you reached your floor"

        mon2 "Well...you're about to find out."

        e "Yay, here we go again."

        "Shadeling walks out of the elevator waiting for you to exit it."

        "The second the doors shut behind you, his hands ignite into flames and his eyes had flames reflected in them."

        mon2 "Prepare to meet your end [name]. You stand no chance against me."

        e "Ugh, fire, how cliche."

        mon2 "Call it basic, but it will ulimately be your doom."

        if classopt == "hat":
            "You prepare yourself for an attack pulling out your sword and gripping you sheild."

            mon2 "Ha and you called fire cliche."

            e "Have you never read any fantasy?"

            e "The night in shining armour always defeats the fire breathing dragon."

            "Shadeling scowls at your remark and his flames get bigger."

            "Shadeling throws a ball of fire directly at you"

            "You dodge the ball, which has set fire to the building behind you."

            e "See, that wasn't very nice."

            "You say on one knee behind your sheild."

            "Shadeling prepares to throw another at you, you choose to..."

            menu:
                "Protect yourself":
                    jump protect5

                "Attack Shadeling":
                    jump attack5

        if classopt == "pen":
            "You pull out your light saber, spin it around you and finish in a defensive position"

            mon2 "Fear. Fear attracts the fearful. The strong. The weak. The innocent. The corrupt. Fear. Fear is my ally."

            "You stare at Shadeling taken slightly aback"

            e "That was from Star Wars, well looks like you do have some taste."

            e "Strike me down and I will become more powerful than you could possibly imagine"

            "Shadeling scowls at your nerdy remark and his flames get bigger."

            "Shadeling throws a ball of fire directly at you"

            "You dodge the ball, which has set fire to the building behind you."

            e "See, that wasn't very nice."

            "You say with your saber behind you"

            "Shadeling prepares to throw another at you, you choose to..."

            menu:
                "Protect yourself":
                    jump protect6

                "Attack Shadeling":
                    jump attack6

        if classopt == "twig":
            "You pull out your wand and focus your mind."

            mon2 "There is no good and evil. There is only power... and those too weak to seek it."

            "You stare at Shadeling taken slightly aback"

            e "That was from Harry Potter, well looks like you do have some taste."

            e "It means you know that Harry and his friends win the war."

            e "We’ve all got both light and dark inside us. What matters is the part we choose to act on. That’s who we really are."

            "Shadeling scowls at your nerdy remark and his flames get bigger."

            "Shadeling throws a ball of fire directly at you"

            "You dodge the ball, which has set fire to the building behind you."

            e "See, that wasn't very nice."

            "You say with your wand tight in hand"

            "Shadeling prepares to throw another at you, you choose to..."

            menu:
                "Protect yourself":
                    jump protect7

                "Attack Shadeling":
                    jump attack7

        if classopt == "sweater":
            "You close your eyes and focus your energy."

            "Much like earlier in the day you begin to levitate and when you look up at Shadeling, your eyes are vibrant purple."

            mon2 "..."

            mon2 "You're one of them..."

            e "What? No snarky reaction?"

            "Shadeling scowls at your remark and his flames get bigger."

            "Shadeling throws a ball of fire directly at you"

            "You manifest a sheild which deflects the fire ball away from you."

            e "See, that wasn't very nice."

            "You say disapating your sheild"

            "Shadeling prepares to throw another at you, you choose to..."

            menu:
                "Protect yourself":
                    jump protect8

                "Attack Shadeling":
                    jump attack8

    label protect5:
        "You decide it's best you wait for Shadeling to be caught off guard before you attack."

        "He throws another fireball at you and in a split second thought you put your sword up to touch it"

        "Your sword catches blade catches fire and you chuckle."

        e "Best to fight fire with fire right?"

        "Shadeling looks at the sword confused."

        mon2 "H-how? How did you-"

        "You decide that this is the best time to attack."

        jump attack5

    label attack5:
        "You run at Shadeling sword and sheild in hand."

        "He just laughs and conjours another fireball"

        "You slide under the fireball and immediately get back up to contine running."

        mon2 "How di-"

        "You cut him off by swinging your sword at him and stopping at his neck."

        e "I'm not going to kill you, take me to you king."

        "Shadeling rolls his eyes"

        mon2 "His name is Helltalon, get it right."

        mon2 "And no, you two will meet soon enough."

        e "Wait what do yo-"

        "Shadeling evaporates like Abysswing did."

        e "What the heck?"

        e "Uhh alright then, well atleast I now know who I'm supposed to be heading towards."

        jump continue3

    label protect6:
        "You decide it's best you wait for Shadeling to be caught off guard before you attack."

        "He throws another fireball at you and you dodge it as easily as the first."

        "Shadeling laughs and says evilly."

        mon2 "We could do this all day [name]."

        "You frown at the comment."

        "You remember that you haven't tried using the force yet"

        e "Well this seems that this is as good a time as any."

        e "Hey Shadeling! You missed, try to actually hit me next time."

        "He growled getting angrier, in turn making the flames larger."

        e "This better work."

        "Shadeling throws a bigger fire ball at you and you extend your arm and hand to try to stop it from moving."

        "It slows its speed eventually stopping between the two of you"

        "You both have shocked expressions on your faces, but with a bit more energy you send the ball flying back at him."

        "Shadeling just dodges it which causes him to loose his bearings slightly."

        "You decide that this is the best time to attack."

        jump attack6

    label attack6:
        "You run at Shadeling saber in hand."

        "He gathers himself and conjours another fireball to throw at you."

        mon2 "Oh no you don't!"

        "He yells as he throws it at you, you jump over it, higher than you expected and land infront of Shadeling with your saber up to his neck."

        e "I'm not going to kill you, take me to you king."

        "Shadeling rolls his eyes"

        mon2 "His name is Helltalon, get it right."

        mon2 "And no, you two will meet soon enough."

        e "Wait what do yo-"

        "Shadeling evaporates like Abysswing did."

        e "What the heck?"

        e "Uhh alright then, well atleast I now know who I'm supposed to be heading towards."

        jump continue3

    label protect7:
        "You decide it's best you wait for Shadeling to be caught off guard before you attack."

        "He throws another fireball at you and you dodge it as easily as the first."

        "Shadeling laughs and says evilly."

        mon2 "We could do this all day [name]."

        "You frown at the comment."

        "You think of what you could do to the fire balls so they don't hit you"

        "Shadeling just laughs maniacally"

        mon2 "Haha, you think your wand will help you, you are no match for me."

        "That really got your blood boiling."

        e "Fine have it your way..."

        "You point your wand at his hand and concentrate on the cold."

        "The moment you thought of the cold both his hands froze over with ice."

        mon2 "WHAT! HOW DARE YOU?!"

        "Shadeling screams at you taken aback."

        "The ice begins to melt quickly"

        "You decide now is the time to attack."

        jump attack7

    label attack7:
        "You run at Shadeling wand in hand and mind focussed."

        "Shadeling laughs, and conjours another fireball to throw at you."

        "He launches it at you and you easily dodge it."

        mon2 "No stay away!!"

        "You ignore his yelling and place your wand on his neck"

        e "I'm not going to kill you, take me to you king."

        "Shadeling rolls his eyes"

        mon2 "His name is Helltalon, get it right."

        mon2 "And no, you two will meet soon enough."

        e "Wait what do yo-"

        "Shadeling evaporates like Abysswing did."

        e "What the heck?"

        e "Uhh alright then, well atleast I now know who I'm supposed to be heading towards."

        jump continue3

    label protect8:
        "You decide it's best you wait for Shadeling to be caught off guard before you attack."

        "He throws another fireball at you and you deflect it as you did the first."

        "Shadeling laughs and says evilly."

        mon2 "We could do this all day [name]."

        "You look up at him and smile."

        e "You don't know what I'm capable of..."

        "Shadeling starts to conjour another fireball"

        mon2 "Haha, you say that to me now when you yourself have no idea."

        "He launches it at you, but this time you stop it from moving, it remains stationary between the two of you."

        mon2 "..."

        "You flick your finger towards Shadeling and it goes flying back towards him."

        "He barely dodges it slightly loosing his bearings."

        mon2 "WOAH!!!"

        "You decide this is your time to attack."

    label attack8:
        "You lock eyes with Shadeling which let you invade his brain."

        mon2 "W- What a- are you-?"

        "You just smile and take over his brain controlling his movements."

        "You float over to him and say..."

        e "Don't ever underestimate me, now don't make me kill you."

        e "Take me to your king."

        "You slightly release your grip on his brain allowing him to speak."

        "Shadeling starts to chuckle"

        mon2 "His name is helltalon..."

        mon2 "And for how powerful you are, you are quite dumb."

        e "Wh-"

        "Shadeling evaporates before you could finish"

        e "What the heck?"

        "You relax your powers and float back down returning to normal."

        e "Uhh alright then, well atleast I now know who I'm supposed to be heading towards."

        jump continue3

    label continue3:
        "You collect yourself after your quarrel with Shadeling."

        e "Gosh how many times amm I going to have to do that."

        "You make your towards your apartment."

        "The hallways wind more than you remember them, and they're darker than you remember."

        e "This is earily quite."

        "You stop at your door and unlock it."

        "You walk inside and the second you shut the door behind you, you make eye contact with a tall green monster."

        e "Hello..?"

        secret "Ah [name], you finally made it, you are a bit earlier than expected which leads me to believe that Shadeling couldn't hold ou back."

        e "Uhh, yeah, I guess..."

        secret "Oh how rude of me to not introduce myself."

        secret "My name is Helltalon, the ruler of all monster, and the one to lead monsters to the Human relm of Earth."

        e "Oh, you're Helltalon, I was expecting someone more, you know, evil looking."

        boss "Well I was expecting someone taller."

        e "Touche"

        e "So what are you doing in my apartment again?"

        boss "Well you see, your apartment is the only one with this"

        "Helltalon picked up a small flat cylinder from beside your TV."

        "You look at it and blink."

        e "..."

        "Once your brain catches up to you you burst out laughing"

        e "You have got to be kidding me right now!"

        e "My old Portal of Power from a game I used to play is how you get into the human relm."

        boss "...What's so funny?"

        e "Oh my gosh, this is crazy"

        boss "..."

        "You eventually stop laughing and Helltalon just looks at you."

        e "Ah, I'm sorry, that was hilarious okay well apperently it is my job to stop you, so please, put down the Portal of Power."

        boss "I'm not just going to stop because you said I should."

        e "Alright the hard way."

        "Helltalon puts down the Portal of Power and chuckles"

        "His eyes glow red and in a split second there are 10 of him in the room."

        e "What-?"

        boss "I am the amalgamation of all monsters who gave themselves up to me or died in my name."

        "Helltalon's hand caught fire much like Shadeling, and various objects around him started levitating like Abysswing."

        e "Well this is going to be harder than I thought it would be."

        boss "This is the end the line for you [name]"

        e "We'll see about that"

        if classopt == "hat":
            "Helltalon sets fire to one of your chairs and prepares to throw it at you."

            e "Oh cmon, my chair, I live here you know."

            boss "You won't be living when I'm done with you."

            "Helltalon throws it at you and you dodge it."

            e "Seriously, come on."

            "You pull out your sword and sheild prepared for more flying furniture."

            e "Let's keep the property damage to a minimum."

            "Helltalon completely ignores you and another one of his clones throws another flaming chair at you."

            "You roll to dodge it."

            e "Did you not hear what I just said?"

            "Helltalon just laughs maniacally"

            e "*Sighs* great."

            menu:
                "Protect yourself":
                    jump protect9

                "Attack Helltalon":
                    jump attack9

        if classopt == "pen":
            "Helltalon sets fire to one of your chairs and prepares to throw it at you."

            e "Oh cmon, my chair, I live here you know."

            boss "You won't be living when I'm done with you."

            "Helltalon throws it at you and you dodge it."

            e "Seriously, come on."

            "You pull out your light saber prepared for more flying furniture."

            e "Let's keep the property damage to a minimum."

            "Helltalon completely ignores you and another one of his clones throws another flaming chair at you."

            "You cut through it."

            e "Did you not hear what I just said?"

            "Helltalon just laughs maniacally"

            e "*Sighs* great."

            menu:
                "Protect yourself":
                    jump protect10

                "Attack Helltalon":
                    jump attack10


        if classopt == "twig":
            "Helltalon sets fire to one of your chairs and prepares to throw it at you."

            e "Oh cmon, my chair, I live here you know."

            boss "You won't be living when I'm done with you."

            "Helltalon throws it at you and you dodge it."

            e "Seriously, come on."

            "You pull out your wand prepared for more flying furniture."

            e "Let's keep the property damage to a minimum."

            "Helltalon completely ignores you and another one of his clones throws another flaming chair at you."

            "You turn it into a paper and almost immediately it falls."

            e "Did you not hear what I just said?"

            "Helltalon just laughs maniacally"

            e "*Sighs* great."

            menu:
                "Protect yourself":
                    jump protect11

                "Attack Helltalon":
                    jump attack11

        if classopt == "sweater":
            "Helltalon sets fire to one of your chairs and prepares to throw it at you."

            e "Oh cmon, my chair, I live here you know."

            boss "You won't be living when I'm done with you."

            "Helltalon throws it at you and you dodge it."

            e "Seriously, come on."

            "You close your eyes and relax as much as possible"

            "You begin to levitate and when you open your eyes to look at Helltalon, your eyes glow purple."

            "Helltalon looks slightly paniced for a second then composes himself"

            boss "You're one of them"

            e "I've been told that 3 times today, I don't care who \"them\" are"

            e "Let's keep the property damage to a minimum."

            "Helltalon completely ignores you and another one of his clones throws another flaming chair at you."

            "You stop it mid air and change it's tradgectory"

            e "Did you not hear what I just said?"

            "Helltalon just laughs maniacally"

            e "*Sighs* great."

            menu:
                "Protect yourself":
                    jump protect12

                "Attack Helltalon":
                    jump attack12

    label protect9:
        "You decide it is best to attack when he is caught off guard"

        "Another one of Helltalon's clones throws another flaming chair at you duck behind your shield to protect yourself from the projectile."

        boss "Cmon [name], you think your tiny shield is going to protect you from me?"

        e "Yes, Yes I do."

        "A plan then forms in your mind of what to do to loose his bearings"

        jump attack9

    label attack9:
        "You know you can't attack all the clones, so you have to find the real Helltalon"

        e "Heh this really feels like an anime I used to watch."

        "The way to get rid of the clones is to is to hit them with a strong enough force"

        "You remember you have hair spray in your bathroom, so you run into the bathroom to grab it"

        boss "Where are you-?"

        boss "Ha you think that will stop me?"

        "You take the cap off the hair spray and throw it at one of the clones who caught it in their flaming hands"

        "Almost immediatly it explodes spanning the entire length of your small living room."

        "All the clones dissolved and only one Helltalon was left dazed"

        "You decide that this is the best time to attack"

        "Sword and shield in hand you run at Helltalon and hold your sword against his neck"

        e "Don't make me kill you, leave the human relm alone."

        boss "Why would I listen to you, I'm more powerful than you."

        "Helltalon begins to levitate your furniture again"

        "In a last second thought you drop your sheild and lunge for the Portal of Power and pull it towards you."

        e "I have this"

        "You shake the Portal in his face, about to break it when Helltalon yells"

        boss "NO! Don't damage it, it's your way home too, how else would you get home when that is the only link between the monster relm and the human relm?"

        "Helltalon smirks"

        "You realize that you must make a decision here, a very dire and important one."

        boss "You can either leave it intact allowing you to go home, but with us trailing not far behind invading the human relm..."

        boss "or you can destroy it and stay here, trapped, with a bounty on your back for the rest of your life."

        "Helltalon laughs"

        boss "So what will it be?"

        menu:
            "Keep it intact":
                jump end1

            "Destory it":
                jump end2

    label protect10:
        "You decide it is best to attack when he is caught off guard"

        "Another one of Helltalon's clones throws another flaming chair at you, and you cut through it again."

        boss "Cmon [name], you think your light saber is going to protect you from me?"

        e "Yes, Yes I do."

        "A plan then forms in your mind of what to do to lose his bearings"

        jump attack9

    label attack10:
        "You know you can't attack all the clones, so you have to find the real Helltalon"

        e "Heh this really feels like an anime I used to watch."

        "The way to get rid of the clones is to is to hit them with a strong enough force"

        "You remember you have hair spray in your bathroom, so you run into the bathroom to grab it"

        boss "Where are you-?"

        boss "Ha you think that will stop me?"

        "You take the cap off the hair spray and throw it at one of the clones who caught it in their flaming hands"

        "Almost immediatly it explodes spanning the entire length of your small living room."

        "All the clones dissolved and only one Helltalon was left dazed"

        "You decide that this is the best time to attack"

        "Light saber in hand you run at Helltalon and hold your saber against his neck"

        e "Don't make me kill you, leave the human relm alone."

        boss "Why would I listen to you, I'm more powerful than you."

        "Helltalon begins to levitate your furniture again"

        "In a last second thought you use the force to the Portal of Power towards you."

        e "I have this"

        "You shake the Portal in his face, about to break it when Helltalon yells"

        boss "NO! Don't damage it, it's your way home too, how else would you get home when that is the only link between the monster relm and the human relm?"

        "Helltalon smirks"

        "You realize that you must make a decision here, a very dire and important one."

        boss "You can either leave it intact allowing you to go home, but with us trailing not far behind invading the human relm..."

        boss "or you can destroy it and stay here, trapped, with a bounty on your back for the rest of your life."

        "Helltalon laughs"

        boss "So what will it be?"

        menu:
            "Keep it intact":
                jump end1

            "Destory it":
                jump end2

    label protect11:
        "You decide it is best to attack when he is caught off guard"

        "Another one of Helltalon's clones throws another flaming chair at you, this time you change it into a stuffed animal."

        boss "Cmon [name], you think your tiny wand is going to protect you from me?"

        e "Yes, Yes I do."

        "A plan then forms in your mind of what to do to lose his bearings"

        jump attack9

    label attack11:
        "You know you can't attack all the clones, so you have to find the real Helltalon"

        e "Heh this really feels like an anime I used to watch."

        "The way to get rid of the clones is to is to hit them with a strong enough force"

        "You remember you have hair spray in your bathroom, so you run into the bathroom to grab it"

        boss "Where are you-?"

        boss "Ha you think that will stop me?"

        "You take the cap off the hair spray and throw it at one of the clones who caught it in their flaming hands"

        "Almost immediatly it explodes spanning the entire length of your small living room."

        "All the clones dissolved and only one Helltalon was left dazed"

        "You decide that this is the best time to attack"

        "Wand in hand you run at Helltalon and hold your wand against his neck"

        e "Don't make me kill you, leave the human relm alone."

        boss "Why would I listen to you, I'm more powerful than you."

        "Helltalon begins to levitate your furniture again"

        "In a last second thought you lunge for the Portal of Power and pull it towards you."

        e "I have this"

        "You shake the Portal in his face, about to break it when Helltalon yells"

        boss "NO! Don't damage it, it's your way home too, how else would you get home when that is the only link between the monster relm and the human relm?"

        "Helltalon smirks"

        "You realize that you must make a decision here, a very dire and important one."

        boss "You can either leave it intact allowing you to go home, but with us trailing not far behind invading the human relm..."

        boss "or you can destroy it and stay here, trapped, with a bounty on your back for the rest of your life."

        "Helltalon laughs"

        boss "So what will it be?"

        menu:
            "Keep it intact":
                jump end1

            "Destory it":
                jump end2

    label protect12:

    label attack12:
        "You know you can't attack all the clones, so you have to find the real Helltalon"

        e "Heh this really feels like an anime I used to watch."

        "The way to get rid of the clones is to is to hit them with a strong enough force"

        "You remember you have hair spray in your bathroom, so you turn your hand toward the bathroom and the hairspray comes float towards you."

        "Helltalon looks at you confused"

        boss "What are you-?"

        boss "Ha you think that will stop me?"

        "You take the cap off the hair spray and launch it at one of the clones who caught it in their flaming hands"

        "Almost immediatly it explodes spanning the entire length of your small living room."

        "All the clones dissolved and only one Helltalon was left dazed"

        "You decide that this is the best time to attack"

        "You levitate towards Helltalon and lift him off the ground not allowing for his arms or legs to move"

        e "Don't make me kill you, leave the human relm alone."

        boss "Why would I listen to you, I'm more powerful than you."

        "Helltalon begins to levitate your furniture again"

        "That is where you are wrong."

        "You make eye contact and take over his mind, motor functions and all."

        "All the previously levitating objets fall."

        e "Now please hand me the Portal of Power"

        "You let him down and he grabs it and gives it to you"

        "You release the grip on his mind."

        e "Thank you for this"

        "You shake the Portal in his face, about to break it when Helltalon yells"

        boss "NO! Don't damage it, it's your way home too, how else would you get home when that is the only link between the monster relm and the human relm?"

        "Helltalon smirks"

        "You realize that you must make a decision here, a very dire and important one."

        boss "You can either leave it intact allowing you to go home, but with us trailing not far behind invading the human relm..."

        boss "or you can destroy it and stay here, trapped, with a bounty on your back for the rest of your life."

        "Helltalon laughs"

        boss "So what will it be?"

        menu:
            "Keep it intact":
                jump end1

            "Destory it":
                jump end2

    label end1:
        "You set the Portal down and it quintuples in size"

        "A blue light shines and your door slams open, monster filing into your apartment running to the portal"

        boss "I knew you would've picked that, you're too weak to pick the other."

        boss "This is the flaw with humans, they are too selfish for their own good."

        e "I didn't lose yet"

        "You say with last ditch confidence"

        "Helltalon laughs"

        boss "It's too late, monsters are already in the human world, your act is futile."

        boss "Just face that you failed, the Portal of Power has opened and there is nothing you can do to save humanity now"

        e "No I haven't failed yet I can still-"

        "Everything went black"

        wise2 "No you can't, it's too late, you failed, they're in the human world."

        e "W-what? Eilyan?"

        wise2 "You have one more chance at this [name], don't fail again"

        wise2 "Second chances rarely ever come around, don't mess it up."

        "Everything goes white"

        jump story

    label end2:
        "You throw the portal as hard as you can against the ground breaking it into many pieces."

        "Helltalon screams."

        boss "NOOO! YOU IDIOT DO YOU UNDERSTAND WHAT YOU JUST DID?!?!"

        e "I just saved humanity, that's what I did."

        boss "Oh that's it, that was my life's work completely ruined all because of you worthless and infinitesimal human."

        boss "I am going to end you."

        "You laugh at his emotion fueled actions"

        e "I would like to see you try."

        "Helltalon multiplies again and they all prepare to throw fireballs at you."

        boss "You must pay for your actions!"

        e "This, can't end well"

        if classopt == "sweater":
            "You conjour a shield around you, but all the fireballs are too much for you to handle."

            "Your sheild gets smaller and smaller with every wave of fire that is thrown at you"

        "The Helltalons all scream as they throw the flaming balls at you."

        "You can't do anything about it now, this is really your end you think"

        "You feel the temperature of the surrounding oxygen incease as they move closer to you..."

        "Then everything goes black."

        e "..."

        wise2 "You did it [name], you saved humanity."

        e "E-Eilyan? Am I dead?"

        wise2 "No, I simply just removed you from the situation."

        e "Oh thank you? If you could do that all along?...Nevermind."

        e "So what now?"

        wise2 "You get to go home, but you will be contacted again if you are needed, do not forget who you are and what you have done."

        e "I'll, uh try my best."

        "Everything goes white and you are lying in bed in your small apartment"

        e "Uhhhhhhhhh..."

        e "Was I dreaming? or did that actually just happen?"

        "You get up from your bed and walk into your living room."

        "At a first glance everything seemed normal"

        "Then you walk back into your room and notice something sticking out of your closet"

        e "No way..."

        if classopt == "hat":

            "You open the door to find a green hat with a tag that reads \"E\" in a fansy font."

            e "Oh my god I wasn't dreaming"

            "You put the hat on and a sword and sheild appear on your person much like it did earlier in the day"

            "You laugh and walk over to the mirror to see how you look."

            e "My gosh I look crazy"

            "You pose in the mirror and you swear for a split second you saw Helltalon standing behind you"

            "You whip around and nothing is there."

            jump finish

        if classopt == "pen":
            "You open the door to find a yellow light saber in a stand with a tag that reads \"E\" in a fansy font"

            e "Oh my god I wasn't dreaming"

            "You take the light saber out and spin it around you like Obi wan in the movies."

            "You then walk over to the mirror, just incase evil [name] is your reflection."

            "You swear for a split second you saw Helltalon standing behind you"

            "You whip around and nothing is there."

            jump finish

        if classopt == "twig":
            "You open the door to find a box with a tag that reads \"E\" in a fansy font"

            e "Oh my god I wasn't dreaming"

            "You open the box and pull out your wand."

            "You walk over to the mirror and conjour a small light from the top of your wand."

            "You glance down at it, then back up in the mirror..."

            "You swear for a split second you saw Helltalon standing behind you"

            "You whip around and nothing is there."

            jump finish

        if classopt == "sweater":
            "You open the door to find a purple University of Waterloo Sweater"

            e "Oh my god I wasn't dreaming."

            "You put it on and you relax which allowed you to start levitating in the mirror."

            "You look at yourself in the mirror and your eyes glow purple."

            e "This is craz-"

            "You're interupted by a knock at the door."

            "You float down like nothing happened and walk to the door to open it."

            "When you do you are greeted with 3 people in purple aswell."

            secret "You are one of us, now normally, people like us go to a specific highschool and we nurture our powers there with our likeminded peers, but you seem to be the exception."

            secret "Now, we must go, your training starts now."

            e "Uh, wait go where?"

            secret "Well University of course, its grind time."

            jump finish

    # This ends the game.
    label finish:
        "That's the end of the game, hope you enjoyed it!"

        "It was made in Renpy by Mel Fletcher and Amy Uccello."

        "See ya later"

        return
