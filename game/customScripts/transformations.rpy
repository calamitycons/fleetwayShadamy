########################################################################
## States
########################################################################

image blackcover = "#000"
image whitecover = "#FFF"

########################################################################
## Basic placement
########################################################################

transform defaultPos:
    xalign 0.5
    yalign 1.0

transform sideLeft:
    xalign 0.2
    yalign 1.0

transform sideRight:
    xalign 0.8
    yalign 1.0

transform flip:
    xzoom -1.0

########################################################################
## Expressing an emotion
########################################################################

transform jittering:
    linear 0.1 xoffset -0.1
    linear 0.1 xoffset 0.1
    repeat
    # shiver back and forth by a tiny amount

transform sighing:
    linear 0.3 yoffset -0.1
    # take a second to lift up as though taking in a breath
    easeout_back 1.0 yalign 1.1
    # sink down below the bottom of the screen

########################################################################
# Movement
########################################################################

transform scrollingText:
    # bring in text blocks from the bottom to the top
