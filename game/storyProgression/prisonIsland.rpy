label start:

    scene prisonIsland

    show amy at side_right with moveinright

    show shadow at side_left with moveinleft

    # These display lines of dialogue.
    amy "Time for the big plot."
    shadow "Okay."

    # This is a story choice
    menu:
        amy "Make your choice!"

        "Escape":
            shadow "We've teleported."

            jump metalHarbor

        "Intervene":
            # Activate shadow's Injured flag
            $ injured = True
            show shadow injured at side_left

            shadow "I'm going to pass out now."

            jump groovyTrainCafe

"If you're here something went wrong, try again."
