label testRoom:
    scene test room

    "Nothing but tests in here."
    shad "Hello."

    while cruelOrKind != 10:
        menu:
            "We need cruelOrKind to be 10."
            "make cruelOrKind 100":
                $ cruelOrKind = assignWithinLimit(100)
                "Now the cruelOrKind variable is [cruelOrKind]."
            "increment cruelOrKind by + 1":
                $ cruelOrKind += assignWithinLimit(1)
                "I'm working on it. cruelOrKind is [cruelOrKind]"

    "Now it is at 10. Good job."
    jump ironGate
