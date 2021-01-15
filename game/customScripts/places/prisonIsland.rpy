label prisonIsland:

    scene prisonIslandBreakIn

    # play Iron Gate theme from Sonic Adventure 2

    "Intruder Alert! Level 7 has been breached by a heavily armed mech. All precautions have been lifted. Destroy the intruder at all costs!"
    # sfx of eggman aiming at and shooting a bunch of GUN sentry beetles

    # Eggman is in the stompy robot from SA2, the Beetles have their white and
    # dark blue color scheme from SA2
    show egg walker at left
    show GUNBeetle at right #should be animated to be bobbing up and down

    "GUN Beetle" "Intruder located. Lethal force has been authorized."
    # animation of GUN Beetle shooting at Eggman
    "???" "Get your nose out of my business! I'm hacking through your rudimentary security system."
    # Eggman shoots the Beetle until it falls apart
    "???" "Really, I'm insulted. GUN thought it could keep my birthright away from me when its precautions are THIS bad? ME?"
    show GUNBeetle at right
    # eggman quickly dispatches it
    "???" "I am Doctor Robotnik! The most brilliant scientific genius in the world!"

    "Dr. Robotnik" "And they think I'm afraid of these paltry excuses for guardian robots. Did they arm their Beetles with lazer pointers? Honestly, a wooden bow and arrow would be more effective against me at this point."

    # As though summoned, an analog crossbow bolt shoots through the air and
    # catches right in the joint of one of the egg walker's legs.

    show egg walker damaged at right #with smoke coming out of him and shaking like a leaf
    # sfx of the machine failing
    # music stops
    "Dr. Robotnik" "Gr! Augh!"
    "???" "Even Tails knows to knock on wood when tempting fate, Eggman!"
    "Dr. Robotnik" "You!"

    # A peppy Collision Chaos remix plays to represent Amy's arrival on the
    # scene
    show amy aiming rappel at left
    show egg walker damaged with flipped at right # slide him over with easein?

    # Eggman stalls Amy while Shadow's pod thing rises up from the ground #
    # I ran out of steam at this point so I'll do the rest later, here's a summary #
    # pew phwoosh phwoooo sound effects and smoke and dust all over #
    # We take control of Shadow, who has no clue what's going on #
    # Big Foot arrives immediately, the guy piloting it gives a military order for everyone to stand down #
    # Amy tries to bargain with the Big Foot saying she's part of the Resistance and they should be on the same side #
    # Eggman stops giving a shit and bargains for Shadow to go with him because he is the grandsom of Professor Gerald, his creator! #
    # Eggman offers the chaos emerald in return for his undying loyalty and help taking over the world #
    # Shadow is distasteful of Eggman and hates the Big Foot, but Amy throws a wrench in his perceptions #
    # Now Shadow must choose: #

    scene prisonIsland
    show amy at left
    show egg walker damaged at center
    show shadow at right

    menu firstChoice:
        "[pick]Take the Chaos Emerald.":
            shadow "My injury status is [injured]"
            jump metalHarbor
        "[pick]Help the girl fight off GUN.":
            $ injured = true
            shadow "My injury status is [injured]"
            jump groovyTrainCafe
