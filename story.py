# let the user know what's going on
print ("Answer the questions below to start the story.")
print ("-----------------------------------")

# variables containing all of your story info
animal = input("Enter an animal: ")
object0 = input("Name a object: ")
animal2 = input("Enter an animal with tusks:")
animal3 = input("Enter an animal with horns:")
animal4 = input("Enter an animal with heels:")

# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!


story = "A " + animal + " had come to the end of his days. " \
 " He lay helpless under a " + object0 + ", " \
"The animals came around him."\
  "When they saw that he was going to die, they thought to themselves, Now is the time to pay him back." \
  "So the "   + animal2 + " came up and rushed at him with his tusks. Then a"+ animal3 +" gored him with his horns."  \
"The "+animal+" still lay helpless before them."\
" So the " + animal4 + "  felt quite safe. He turned his tail to the"+animal+" and kicked up his heels into his face." \
"This is a double death."\
  " growled the " + animal + "."

# finally we print the story
print (story)
