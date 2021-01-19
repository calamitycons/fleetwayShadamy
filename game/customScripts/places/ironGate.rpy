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
            $ amyTrust += 1
            $ eggTrust -= 1
            shadow "Now I have met Amy Rose. I have [amyTrust] trust levels with her."
        "[pick]Exit from the bottom.":
            $ eggTrust += 1
            $ amyTrust -= 1
            shadow "Now I have [eggTrust] trust levels with the Doctor."

    "Oh shit Big Foot's here now."
    "And it just goes straight to the fight."
    "Amy tries to "
    "Stupid humans."

    menu:
        "[pick]Intervene":
            $ heroScore += 1
            shadow "Now I have [heroScore] Hero Score"
            jump groovyTrainCafe

        "[pick]Escape":
            $ darkScore += 1
            shadow "Now I have [darkScore] Dark Score"
            if amyTrust > 0:
                jump conscience

            else:
                shadow "Because I don't trust Amy and she does not trust me, I'll just leave."
                jump metalHarbor

label conscience:
"You grab the Chaos Emerald but you feel guilty about abandoning Amy."

    menu:
        "[pick]Go back for her.":
            $ heroScore += 2
            "She's in the middle of reloading her crossbow when you use the Chaos Emerald to teleport behind her."
            "You undershoot your Z axis a little so you soften your descend with your rocket shoes."
            amy "Hey! Watch where you grabbin'!"
            shadow "Chaos Control!"
            jump prisonIsland
        "[pick]Escape":
            $ darkScore += 2
            shadow "Chaos Control!"
            jump metalHarbor
