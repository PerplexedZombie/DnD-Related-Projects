#This will be going in a sub-folder while I make one for each character
#while not the most efficient way, it will work
import Settings #Imports the universal things holder

#First line will be a description to give an idea of backstory
print('Hill like mini person')
print('Dwarves get a +1 to Constitution, Hill Dwarves get an additional\
 +1 to their Wisdom. Hill Dwarves have "Dwarven Toughness" giving +1 to \
HP max with an additional +1 every level') #This line is to explain bonuses 
Settings.stats['Con'] += 1 #Applies the bonuses
Settings.stats['Wis'] += 1

print('')
