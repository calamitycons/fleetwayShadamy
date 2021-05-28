################################################################################
## Initialization
################################################################################

init offset = -1

# Following code provided by @Salvr on Discord
init python:
    def assignWithinLimit(newValue, statMIN=-5, statMAX=5):
        return min(max(newValue, statMIN), statMAX)

################################################################################
## Plot Values
################################################################################

# Story-crucial booleans that dramatically change a lot of important story
# beats such as who is where, and where to go next
default sonicArrested = False # changes if Sonic is available or not
default youAreAPirate = False # Does Shadow the Hedgehog is Sky Pirate?

# Relationship values
default amyTrust = 1 # Amy trusts strangers by default
default shadamy = 0  # But do YOU trust her back?

################################################################################
## Social Values
################################################################################
# Personality values that affect shadow's responses in narration.
################################################################################

# These determine some of Shadow's reactions to events and can disable
# or automate future choices if the score is too high
default darkScore = 0 # Black hearted evil?
default heroScore = 0 # Brave hearted hero?

default silence = 0
# Shadow will be silent and watch rather than activate a dialog choice. If
# he MUST say something, this won't apply, but if this number is too high he
# will stop participating in conversation until prompted by another character.

default injury = 0
# Shadow can't do something physical, so he's forced to rest/engage in
# conversation instead. This leads to more opportunities to talk to people.

default cruelty = 0
default kindness = 0
# Will he be arrogant or offer compassion?

default pride = 0
default cunning = 0
# Does he go fast and fight, or slow down and think? Positive = impulsive,
# negative = cunning.

################################################################################
## Skills
################################################################################
# Things Shadow remembers he can do.
################################################################################
