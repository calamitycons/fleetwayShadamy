label ironGate:

    scene blackcover
    # the sound of alarms from the other side of a wall
    "The air you breathe in stabs your lungs after being in stasis for so long."

    # Machinery moves around you
    "You hear voices from outside your pod as the machinery around it pushes you up and out of your prison."

    scene whitecover with fade #too bright to see
    "???" "Stoppit right there, Eggman!"
    "???" "Don't you call me Eggman, hedgehog girl! I am Doctor ROBOTNIK, the most brilliant scientific genius in the world!"

    # A splash screen of Eggman and Amy arguing with each other and ignoring
    # Shadow.

    "You are Shadow the Hedgehog, the world's Ultimate Lifeform..."

    scene ironGate with dissolve #where we're at
    show a fight at side_right #amy shoots
    show e at side_left #eggy shouts
    "Eggman" "Don't be hasty with that crossbow, little lady. You might hurt someone. Here, let me take it off your hands!"
    "Eggman shoots a small missile out of his egg walker."
    "With pinpoint accuracy, the hedgehog girl shoots it right out of the air with a crossbow bolt."

    a "They don't call me Aiming for nothing, Ro-butt-nik!"
    "Eggman" "That nickname is even worse!"

    # A panel of Shadow balking in confusion at this scene slides in from the
    # right.
    show sh at side_left
    hide a
    hide e
    "They don't seem to realize you're here."
    menu:
        "Look for an escape.":
            $ proudOrCunning -= 1
            "You don't know how long you've been in suspended animation..."
            # closeup of the chaos emerald imbedded in the computer
            "But you can recognize a Chaos Emerald anywhere."
            jump conscience
        "Stay quiet and watch.":
            $ proudOrCunning -= 1
            "You stand back and watch them argue."
            jump standBack
        "Bark at them.":
            $ proudOrCunning += 1
            "Shadow's proud or cunning stat is now [proudOrCunning]."
            sh xarm @ xarm 2 "Which one of you released me from stasis?"
            jump bigFootArrives

label standBack:
    "Shadow's proud or cunning stat is now [proudOrCunning]."
    "Nothing is here yet."
    return

label bigFootArrives:
    "Oh shit Big Foot's here now."
    "And it just goes straight to the fight."
    "Amy wants to mediate but nobody listens."
    sh @ xarm 2 "Stupid humans."

    menu:
        "Intervene":
            $ heroScore += 1
            $ proudOrCunning += 1
            sh @ fight "Now I have [heroScore] Hero Score"
            "Then Shadow gets stabbed in the forehead by a piece of shrapnel!"
            sh "OW!"
            $ injury += assignWithinLimit(100)
            "You pass out from the pain."
            return

        "Escape":
            $ darkScore += 1
            sh "Now I have [darkScore] Dark Score"
            if shadamy > 0 or proudOrCunning <= 0:
                jump conscience

            else:
                sh "Because I don't know Amy and she does not know me, I'll just leave."
                return

label conscience:
    "You grab the Chaos Emerald but..."

    if shadamy > 0:
        # amy portrait slides in from right
        "You feel guilty about abandoning Amy. She reminds you of someone. Someone you know you loved..." #Maria fades in

    elif proudOrCunning <= 0:
        show sh xarm 2

        "Who is this Doctor Robotnik? What does he want? His name seems familiar to you, somehow."
        show a fight at right
        "And what was the hedgehog girl doing here?"
        "If you leave without her, you may never get the answers you seek on your own."
    else:
        pass

    menu:
        "Go back for her.":
            $ heroScore += 2
            $ shadamy += 2

            show sh fight at flipped
            show a fight behind sh

            "She's in the middle of reloading her crossbow when you use the Chaos Emerald to teleport behind her."
            "You undershoot your Z axis a little so you soften your descend with your rocket shoes."

            show a fight

            a "Hey! Watch where you're grabbin'!"
            sh "It isn't safe here. You'll need me to get us out."
            jump bigFootArrives

        "Escape":
            $ darkScore += 2
            $ shadamy -= 1
            "You shake your head. You don't know her. You don't know why she claims to be allied with the humans. It's none of your business."
            "You're not interested."
            sh "Chaos Control!"
