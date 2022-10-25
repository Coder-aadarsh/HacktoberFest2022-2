# Python3
# Sort or Order dictionary with key-value pairs.

# Initialized a dictionary
fruitscolor = {"Banana" : "Yellow",
    "Mango" : "Green",
    "Apple" : "Red",
    "Grapefruit" : "Pink",
    "Blackberry" : "Purple",
    "Sapodilla" : "Brown"}

# sort and print the items of dictionary
for fruit, color in sorted(fruitscolor.items()):
  print(fruit, ":", color)
