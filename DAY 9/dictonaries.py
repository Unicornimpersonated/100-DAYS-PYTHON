# dictonary = {key:value}

#  For multiple values

# dictionary = {"key":"value", "key":"value", "key":"value" }

colors ={"Apple":"Red",
         "Banana":"Yellow",
         "Grapes":"Green",
         "Blueberry":"Blue"
        
}
print(colors)

print(colors["Blueberry"])

colors["Orange"] = "Orange"
print(colors)

# Empty Dictionary
empty_dictionary = {}
# Add something into empty dictionary
empty_dictionary[1]="This is 1" 

# Wipe an existing dictionary
colors ={}
print (colors)
print(empty_dictionary)

# Edit an item of a dictionnary
colors ={"Apple":"Red",
         "Banana":"Yellow",
         "Grapes":"Green",
         "Blueberry":"Blue",
         "Watermelon":"Red" 
}
print(colors)
colors["Watermelon"]="Green"
print(colors)

# Looping through a Dictionary 
# IT PRINTS ONLY THE KEYS
for thing in colors:
    print(thing)
    print(colors[thing])

for key in colors:
    print(key)
    print(colors[key])
