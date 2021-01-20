label ironGate:

    scene blackcover


    "You've just woken up to the pitch blackness of a stasis pod."

    menu firstChoice:
        "Examine self":
            $ proudOrCunning += assignWithinLimit(1)

            "proudOrCunning is set to [proudOrCunning], which means you are..."
            if proudOrCunning > 0:
                "proud, rough, and impulsive"
            elif proudOrCunning < 0:
                "humble, gentle, and cunning"
            else:
                "neutral"

            "You are Shadow the Hedgehog, the world's Ultimate Life Form born and raised aboard the Space Colony ARK."
            "You check your wrists and- Ah, what a relief. Your inhibitor rings are still there."
            # the world shudders and pulses
            "When you bend to check your ankles as well, you are overwhelmed with a sense of vertigo. Acid wells up in the back of your throat."
            "You grasp your mouth and swallow against the churning of your empty stomach."
            "How long have you been in stasis? Were you improperly activated? Your body shouldn't notice time has passed when properly released."

        "Spark a light source":
            $ proudOrCunning -= assignWithinLimit(1)
            scene smallLight
            "proudOrCunning is set to [proudOrCunning], which means you are..."
            if proudOrCunning > 0:
                "proud, rough, and impulsive"
            elif proudOrCunning < 0:
                "humble, gentle, and cunning"
            else:
                "neutral"

            "You create a light within your palms."
            # make the whole world shudder and pulse
            scene blackcover
            "Or you did, for about one second."
            "The pain that spikes through your head is unbearable. You grasp your temples and press your fingers in. Your jaw trembles from how tightly you clench it."
            # muffled sound of alarms from SA2
            "When you release your vice around your head, you notice the sound of alarms from outside your prison. You can barely tolerate it."

    "You don't get a chance to catch your breath before you feel a sharp scratch piercing the back of your neck..."

    "The next time you're awakened from stasis it remains dark, but you hear voices from outside your pod."
    "One voice from above your current location..."
    "???" "Aw, nuts! Eggman's already unleashed the thing!"
    "...And one from below you."
    "???" "Don't you call me Eggman, hedgehog girl! I am Doctor ROBOTNIK, the most brilliant scientific genius in the world!"
    "They both seem very loud and obnoxious."

    menu:
        "Exit from the top.":
            $ heroScore += 0.5
            $ shadamy += 1
            shad "Now I have met Amy Rose. Hero Score is [heroScore]. Shadamy is [shadamy]"
        "Exit from the bottom.":
            $ darkScore += 0.5
            shad "Hello Doctor. Dark Score is [darkScore]"

    "Oh shit Big Foot's here now."
    "And it just goes straight to the fight."
    "Amy wants to mediate but nobody listens."
    shad "Stupid humans."

    menu:
        "Intervene":
            $ heroScore += 1
            $ proudOrCunning += 1
            shad "Now I have [heroScore] Hero Score"
            "Then Shadow gets stabbed in the forehead by a piece of shrapnel!"
            shad "OW!"
            $ injury += assignWithinLimit(100)
            "You pass out from the pain."
            jump groovyTrainCafe

        "Escape":
            $ darkScore += 1
            shad "Now I have [darkScore] Dark Score"
            if shadamy > 0 or proudOrCunning <= 0:
                jump conscience

            else:
                shad "Because I don't know Amy and she does not know me, I'll just leave."
                jump metalHarbor

label conscience:
    "You grab the Chaos Emerald but..."
    if shadamy >0:
        "You feel guilty about abandoning Amy. She reminds you of someone. Someone you know you loved..."
    elif proudOrCunning <= 0:
        "Something about this situation is too suspicious. What was she doing here? Why does she care what the humans think?"
        "The Doctor intends to use you to further his plots, which doesn't surprise you. The GUN agent piloting his Big Foot is under orders to detain you and clearly isn't interested in negotiating."
        "If you leave without her, you may never get the answers you seek on your own."
    else:
        pass

    menu:
        "Go back for her.":
            $ heroScore += 2
            $ shadamy += 2
            "She's in the middle of reloading her crossbow when you use the Chaos Emerald to teleport behind her."
            "You undershoot your Z axis a little so you soften your descend with your rocket shoes."
            amy "Hey! Watch where you're grabbin'!"
            shad "Chaos Control!"
            jump prisonIsland

        "Escape":
            $ darkScore += 2
            $ shadamy -= 1
            "You shake your head. You don't know her. You don't know why she claims to be allied with the humans. It's none of your business."
            "You're not interested."
            shad "Chaos Control!"
            jump metalHarbor
