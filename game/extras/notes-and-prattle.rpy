# TO DO:
# - visual polish can happen last, focus on coding and making sure the
#    templates work correctly
# - Create a dialog tree system for all dialog
# - Fix the character transition

### Jan 06 2021 ###
# When you need to apply two transforms onto a character, you write it like this:
#
# show character:
#     transform1
#     transform2
# with motion
### DO NOT USE "at" IT WILL NOT WORK RIGHT ###

# Code that has been removed:
    #
    # show amy at side_left with moveinleft
    # show shad:
    #     side_right
    #     flipped
    # with moveinright
    #
    # # These display lines of dialogue.
    # shadow "My injury status is [injured]"
    # amy "Time for the big plot."
    # shadow "Okay."
    #
    # # This is a story choice
    # menu:
    #     amy "Make your choice!"
    #
    #     "Escape":
    #         shadow "We've teleported."
    #
    #         jump metalHarbor
    #
    #     "Intervene":
    #         # Activate shadow's Injured flag
    #         $ injured = True
    #         show shad at side_left
    #
    #         shadow "My injury status is [injured]"
    #
    #         jump groovyTrainCafe
