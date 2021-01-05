## Shadow has teleported Amy away from GUN and Eggman
## But Amy's friends are all confused and suspicious of Shadow.

label metalHarbor:

    scene metalHarbor with dissolve

    "You did it you made it to the Metal Harbor."

    menu:
        "Do you fuck it up or not?"

        "Fucked it up.":
            $ sonicArrested = True

            show bob at center

            bob "lol bye."

            jump gtcDark

        "No I'm a good kid.":
            show tekno at side_left

            tekno "I knew you could be trusted!"
            tekno "Let's go to the groovy train!"

            jump groovyTrainCafe

    return
