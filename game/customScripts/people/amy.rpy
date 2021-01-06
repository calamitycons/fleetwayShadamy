# Define Amy as a Character object
define amy = Character("Amy", image="amy")

image amy = ConditionSwitch(
    "injured == True", "images/chr/amy/canon.png",
    "True", "images/chr/amy/default.png")
