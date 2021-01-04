## Lots of possible ways to make it here. We have to account for all of
## them. Maybe even ones that aren't supposed to happen?

label groovyTrainCafe:

    # Fade to black, transition to the groovy train
    scene blackcover with fade
    scene groovyTrainCafe with dissolve
    "You are now in the groovy train."

    if injured:
        # Go to the Hero path.
        jump gtcHero
    else:
        # Placeholder, checking to see if the function works.
        show bob at speaking with easeinright

        bob "This is bob on the right."
        bob "I am here to see if the functions all work correctly."
        bob "You are neither injured, nor is sonic arrested."
        show bob at stopspeaking

        bob "..."
        show bob at speaking

        bob "Okay see ya."

        return

    label gtcHero:
        # Here comes Ebony
        show ebony at side_left with easeinleft

        ebony "Hello yes this is cat."
        ebony "You gonna turn on another variable or not?"

        menu:
            "You gonna turn on another variable or not?{fast}"

            "Sonic goes to jail.":
                $ sonicArrested = True
                jump gtcDark

            "No thanks.":
                # Nothing happens
                ebony "Okay bye I guess."

        return

    label gtcDark:

        # Placeholder, checking to see if the function works.
        show bob at side_left with easeinright

        bob "This is bob. You fucked it."

        return
