from random import choice   # Imports an already made function so that I don't have to re-code it :)

def Scramble(ListOfNames, NumberPerGroups):
    Team = []   # Creation of the final list
    Groups =[] # Creation of a temporary list in order to make the groups
    TheList = ListOfNames # Creation of a list to replace the list of names
    
    while len(TheList) != 0: # The main loop
        RandomChoice = choice(TheList) # Takes a random value in TheList, in here it will be 1 of the names

        # Checking the list to then delete the correct value, it's here so that names will only appear once in the final groups
        j = 0
        while TheList[j] != RandomChoice: # Checks if the  element at the postion j is the name we've chosen or not
            j += 1 # If not, it will check the next one by making j the position 1 higher
        del(TheList[j]) # Once the correct position found, it delets it

        if len(Groups) == NumberPerGroups: # Checks if the Group is already full or not
            Team.append(Groups) # If yes, it will make it's way into the list of the groups
            Groups = [] # And create a new one
            Groups.append(RandomChoice) # That will have the random name chosen earlier
        else: # If not,
            Groups.append(RandomChoice) # Groups will take the random name chosen

    Team.append(Groups) # Making the last group a part of the list of groups
    print(*Team, sep = "\n\n") # returns the list of groups

#______________________________________(._.)____________________________________________#

ListOfNames = ['Fred','Pierre','Mathilde','Clementine','Valentin','Mr Colin'] # All names MUST be between '' or ""
NumberPerGroups = 2 # Must be a number

Scramble(ListOfNames, NumberPerGroups) 
# Calls the function, 1 element in the brakets beeing the list of names (the first one) & the 2nd one being the number of persones per groups