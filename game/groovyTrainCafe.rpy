## Lots of possible ways to make it here. We have to account for all of them.
## Maybe even ones that aren't supposed to happen?

label groovyTrainCafe:

    # Fade to black, transition to the groovy train
    scene blackcover with fade
    scene groovyTrainCafe with dissolve
    "You are in the groovy train."

    if injured:

        jump gtcHero

    elif sonicArrested:

        jump gtcDark

    else:

        # Placeholder, checking to see if the function works.
        show bob:
            easein 0.3 side_right

        bob "This is bob on the right."

    label gtcHero:

        # Here comes Ebony
        show ebony:
            easein 0.5 side_left

        ebony "Hello yes this is cat."
        ebony "You gonna turn on another variable or not?"

        menu:
            "You gonna turn on another variable or not?"

            "Sonic goes to jail.":
                $ sonicArrested = True
                jump gtcDark

            "No thanks.":

                ebony "Okay bye I guess."

        return

    label gtcDark:

        # Placeholder, checking to see if the function works.
        show bob:
            easein 0.3 side_left

        bob "This is bob. You fucked it."
