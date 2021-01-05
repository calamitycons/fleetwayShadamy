# Shadow the Hedgehog
define shadow = Character("Shadow")

# Shadow's images are affected by story values, so he gets a conditional
# statement for all his sprite calls.
# if injured:
#     jump injuredSprites
# else:
#     jump regularSprites
#
# label injuredSprites:
#     ## Send all image calls to the version with injured shadow
#     image shadow = Image("/images/chr/shadow-injured.png")
#
# label regularSprites:
#     ## Regular images, no additions or edits
#     image shadow = Image("images/chr/shadow.png")
