label ironGate:

    scene blackcover

    "You've just woken up to the pitch blackness of a stasis pod."

    menu firstChoice:
        "[pick]Examine self":
            $ cunning += 1
            "You are Shadow the Hedgehog, the world's Ultimate Life Form born and raised aboard the Space Colony ARK."
            "You check your wrists and- Ah, what a relief. Your inhibitor rings are still there."
            # the world shudders and pulses
            "When you bend to check your ankles as well, you are overwhelmed with a sense of vertigo. Acid wells up in the back of your throat."
            "You grasp your mouth and swallow against the churning of your empty stomach."
            "How long have you been in stasis? Were you improperly activated? Your body shouldn't notice time has passed when properly released."

        "[pick]Spark a light source":
            $ pride += 1
            scene smallLight
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
        "[pick]Exit from the top.":
            $ heroScore += 0.5
            $ shadamy += 1
            shad "Now I have met Amy Rose. Hero Score is [heroScore]"
        "[pick]Exit from the bottom.":
            $ darkScore += 0.5
            shadow "Hello Doctor. Dark Score is [darkScore]"

    "Oh shit Big Foot's here now."
    "And it just goes straight to the fight."
    "Amy wants to mediate but nobody listens."
    shad "Stupid humans."

    menu:
        "[pick]Intervene":
            $ heroScore += 1
            shad "Now I have [heroScore] Hero Score"
            "Then Shadow gets stabbed in the forehead by a piece of shrapnel!"
            shad "OW!"
            $ injury += 100
            "You pass out from the pain."
            jump groovyTrainCafe

        "[pick]Escape":
            $ darkScore += 1
            shad "Now I have [darkScore] Dark Score"
            if shadamy > 0:
                jump conscience

            else:
                shad "Because I don't know Amy and she does not know me, I'll just leave."
                jump metalHarbor

label conscience:
    "You grab the Chaos Emerald but you feel guilty about abandoning Amy."

    menu:
        "[pick]Go back for her.":
            $ heroScore += 2
            $ shadamy += 2
            "She's in the middle of reloading her crossbow when you use the Chaos Emerald to teleport behind her."
            "You undershoot your Z axis a little so you soften your descend with your rocket shoes."
            amy "Hey! Watch where you're grabbin'!"
            shadow "Chaos Control!"
            jump prisonIsland

        "[pick]Escape":
            $ darkScore += 2
            shadow "Chaos Control!"
            jump metalHarbor
