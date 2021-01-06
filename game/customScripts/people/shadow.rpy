# Shadow the Hedgehog
define shadow = Character("Shadow")

init python:
    # getPose looks for an image of the character shadow that is
    # within the folder labeled status and finds the specific
    # picture with the name of the pose.
    def getPose(character, status, pose): return Image("images/chr/%s/%s/%s.png" % (character, status, pose))

# Shadow's images are affected by story values, so he gets
# a conditional statement for all his sprite calls.
# 
# image shadow = getPose("shadow", "default", "default")
image shadow injured = getPose("shadow", "injured", "default")
#
# if injured:
#     # This is what it looks like when he's injured
    show shadow injured
# else:
#     # These are the default calls
#     show shadow
