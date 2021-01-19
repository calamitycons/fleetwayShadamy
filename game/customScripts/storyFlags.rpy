################################################################################
## Initialization
################################################################################

init offset = -1

################################################################################
## Plot Values
################################################################################

# These determine some of Shadow's reactions to events and can disable
# or automate future choices if the score is high
default darkScore = 0 # Black hearted evil?
default heroScore = 0 # Brave hearted hero?

# Story-crucial booleans that dramatically change a lot of important story
# beats such as who is where, and where to go next
default amnesia = False # disables certain dialog options
default sonicArrested = False # changes if Sonic is available or not
default yourePirate = False # Does Shadow the Hedgehog is Sky Pirate?

# Relationship values
default amyTrust = 1 # Amy trusts strangers b/c she's like that
default shadamy = 0  # But do YOU trust her back?

################################################################################
## Social Values
################################################################################
# Personality values that affect shadow's responses in narration.
# These rely on maximums and minimums
# Following code provided by @Salvr on Discord
################################################################################

$ statMIN = -10
$ statMAX = 10

def assignWithinLimit(newValue, statMIN, statMAX):
    return min(max(newValue, statMIN), statMAX)

def assignWithUpperLimit(newValue, 0, statMAX):
    return min(max(newValue, statMIN), statMAX)

default silence = assignWithUpperLimit(0)
# Shadow will be silent and watch rather than activate a dialog choice. If
# he MUST say something, this won't apply, but if this number is too high he
# will stop participating in conversation until prompted.

default injury = assignWithUpperLimit(0)
# Shadow can't do something physical, so he's forced to rest/engage in
# conversation instead. This leads to more opportunities to talk to people,
# or you can just sleep.

default cruelOrKind = assignWithinLimit(0)
# Will he say be arrogant or offer compassion?

default proudOrCunning = assignWithinLimit(0)
# Does he go fast and fight, or slow down and think?
