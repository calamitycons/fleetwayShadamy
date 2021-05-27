## Homemade Transforms ##

image blackcover = "#000"
image whitecover = "#FFF"

# Basic placement

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

transform jittering:
    linear 0.1 xoffset -0.1
    linear 0.1 xoffset 0.1
    repeat
