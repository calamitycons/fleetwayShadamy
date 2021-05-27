label testRoom:
    scene test room
    show a at sideLeft with moveinleft
    show sh xarm at sideRight

    a "Hello Shadow."
    sh "Hello Amy."

    show sh xarm:
        pause 0.5
        jittering

    sh "I would like to be facing you, actually. {w=5} Give me a second."

    # Amy approaches to help, getting a little close...
    show a:
        sideLeft
        ease 1.0 defaultPos

    a "Do you need any help with that?"

    menu:
        a "Do you need any help with that?"
        "No thanks.":
            jump noThanks

        "Maybe...":
            #Shadow jitters more violently
            "You clicked the button."
        "Yes, please.":
            #Shadow stops jittering
            "You clicked the button."

label noThanks:
    #Shadow flips on his own
    show sh xarm:
        flip

    show a at sideLeft with move

    sh "Thank you, but I'm okay."
    a "Oh! Sorry."
