# The script of the game goes in this file.

# Initialize all backgrounds
jump backgrounds

# - Implement these vars you defined down there VVVV

default heroScore = 0
default darkScore = 0
default shadamy = 0
default injured = False
default amnesia = False
default sonicArrested = False

# The game starts here.
label start:

    # Show a background.
    scene prisonIsland

    # This shows the character sprites.
    show amy at side_right
    show shadow at side_left

    # These display lines of dialogue.
    amy "Time for the big plot."
    shadow "Okay."

    # This is a story choice
    menu:
        amy "Make your choice!"

        "Escape":

            jump transEscape

        "Intervene":

            jump transIntervene


    label  transIntervene:
        # Activate shadow's Injured flag
        $ injured = True
        show shadow injured at side_left

        shadow "I'm going to pass out now."

        jump groovyTrainCafe

    label transEscape:

        shadow "We've teleported."

        jump metalHarbor

"If you're here something went wrong, try again."

return
