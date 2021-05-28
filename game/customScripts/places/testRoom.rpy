label testRoom:
    scene test room
    show sh xarm:
        sideRight

    show a with moveinleft:
        sideLeft

    a "Hello Shadow."

    show sh xarm 2 at sighing

    sh "Hello Amy."

    show sh xarm:
        pause 0.2
        jittering

    sh "I would like to be facing you, actually. {w=2} Give me a second."

    # Amy approaches to help, getting a little close...
    show a behind sh:
        sideLeft
        ease 1.0 defaultPos

    a "Do you need any help with that?"

    menu:
        a "Do you need any help with that?"
        "No thanks.":
            jump noThanks

        "Maybe...":
            show a:
                easein_elastic 1.0 sideLeft

            show sh behind a:
                easein_elastic 1.0 defaultPos

            show t with moveinright:
                flip
                sideRight

            t "What is happening in here?"

            show sh xarm

            sh "Sorry. Who are you?"
            t "I am Tekno the Canary. I haven't any powers, but I /am/ tech talented!"

            show a happy:
                easein_expo 0.7 defaultPos
            show sh sigh:
                easein_back 0.5 left

            a "She's also my best mate!"
            jump theEnd

        "Yes, please.":
            jump needHelp

label noThanks:
    #Shadow flips on his own
    show sh xarm:
        flip
        defaultPos

    show a:
        defaultPos
        easein_elastic 1.0 sideLeft

    sh "Thank you, but I'm okay."
    a "Oh! Sorry."

    jump theEnd

label needHelp:
    show sh xarm 2 at sighing
    sh "Unfortunately the answer is yes."

label theEnd:
    "This concludes the test room."
