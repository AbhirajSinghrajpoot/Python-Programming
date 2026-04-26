# Error in code
from random import randint
dice_imgs = ["a","b","c","d","e","f"]
dice_num = randint(1,6)
print(dice_imgs[dice_num])

# Fix Error
from random import randint
dice_imgs = ["a","b","c","d","e","f"]
dice_num = randint(0,5)
print(dice_imgs[dice_num])

