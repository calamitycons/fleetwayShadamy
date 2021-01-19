init -1:

    # These determine some of Shadow's reactions to events and can disable
    # future dialog choices if the score is too high
    default heroScore = 0
    default darkScore = 0

    # Relationship values
    default amyTrust = 1 # Amy might not know you but she'll give you a chance
    default shadamy = 0  # Kiss da girl

    default sonicTrust = 0 # Sonic thinks you stink
    default sonadow = 0 # Kiss the boy

    default eggTrust = 0 # Eggman doesn't want to kiss you

    default yourePirate = 0 # Does Shadow the Hedgehog is Sky Pirate?
    default firstMate = 0 # Kiss the robot pirates (Whisker and Johnny)
    default shadouge = 0 # Kiss this one treasure hunter in particular

    # Personality values that affect shadow's
    # responses to things during narration.
    default silence = 0 # Sometimes Shadow will just choose not to say anything
    default injury = 0 # Shadow's body won't cooperate because it hurts too much
    default cruelty = 0 # Will he say mean and pompous things?
    default kindness = 0 # Will he offer compassion?
    default pride = 0 # Does he wanna FITE?
    default cunning = 0 # Does he notice when he's being tricked or manipulated?

    # Story-crucial booleans that dramatically change a lot of important things
    default amnesia = False
    default sonicArrested = False
