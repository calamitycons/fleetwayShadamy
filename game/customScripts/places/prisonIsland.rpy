label prisonIsland:

    scene prisonIsland

    show amy at side_left with moveinleft
    show shad:
        side_right
        flipped
    with moveinright

    # These display lines of dialogue.
    shadow "My injury status is [injured]"
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
            show shad at side_left

            shadow "My injury status is [injured]"

            jump groovyTrainCafe
