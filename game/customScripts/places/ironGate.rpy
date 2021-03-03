label ironGate:

    scene blackcover
    # the sound of alarms from the other side of a wall
    "The air you breathe in stabs your lungs after being in stasis for so long."

    # Machinery moves around you
    "You hear voices from outside your pod as the machinery around it pushes you up and out of your prison."
    # Everything is bright for a while
    scene whitecover
    "???" "Stoppit right there, Eggman!"
    "???" "Don't you call me Eggman, hedgehog girl! I am Doctor ROBOTNIK, the most brilliant scientific genius in the world!"

    # A splash screen of Eggman and Amy arguing with each other and ignoring
    # Shadow.

    "You are Shadow the Hedgehog, the world's Ultimate Lifeform..."

    # A panel of Shadow balking in confusion at this scene slides in from the
    # right.
    "...Nobody's paying much attention to you right now, though."

    egg "Don't be hasty with that crossbow, little brat."

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
