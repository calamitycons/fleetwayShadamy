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
        show bob at side_right with easeinright
        show bob at speaking

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

        # First incoming amy, then in comes shadow
        show amy at default with easeinright
        show shad injured at side_right with easeinright

        show shad at breathing
        show amy at speaking
        "I'm sorry, Ebony, I know I ask a lot from you."

        ebony "You really brought some trouble to my place, Amy."

        amy "I know! But this is important."
        amy "Can you help me get him somewhere safe?"

        ebony "Grumble..."

        return

    label gtcDark:

        # Placeholder, checking to see if the function works.
        show bob at side_left with easeinright

        bob "This is bob. You fucked it."

        return
