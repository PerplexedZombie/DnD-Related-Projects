#aiming to make code that will roll 3d6 6 times
#and make a list of the results then make a dictionairy 
#using the results as an example of a DnD character sheet
import Settings
import random #see XKCD.com/221
 #import random module to make a random number on a d6
numlist = [] #Will be using this to show rolled numbers
d6 = 3 #determines how many times to roll the d6
def pStat(): #simple func to roll the
 #d6 3 times then sum them
  global numblist #using the numlist at start
  rolls = [int(random.randint(1, 6)) for range in range(d6)]
  numlist.append(sum(rolls))
  
for x in range(0, 6): #uses the previous func to gen 6 numbers
  pStat() #for the stats

print(sorted(numlist, reverse=True)) #makes a list of the
 #availble number to use

stats = Settings.stats #dict for the end results
while True: #loop to assign stats
  print('Assign stats:') #Goes through the stats one by one
  print('Strength: ')
  x = int(input()) #with user unputting an int
  Settings.stats['Str'] = Settings.stats['Str'] + x #x is used as it doesn't
                                                    #have to remember
                                                    #the input throughout
  if x not in numlist: #int is checked to see if user rolled
    print('You do not have that number') #that number
    continue #if they don't have the number it loops
  else: #This then removes the number input
    numlist.remove(x) #to show remaining numbers
    print('') #and to avoid using the same number
    print(sorted(numlist, reverse=True)) #for all stats
    print('') #caused by a loop hole
  print('Dexterity: ') #repeats for all stats
  x = int(input())
  Settings.stats['Dex'] =  Settings.stats['Dex'] + x
  if x not in numlist:
    print('You do not have that number')
    continue
  else:
    numlist.remove(x)
    print('')
    print(sorted(numlist, reverse=True))
    print('')
  print('Constitution: ')
  x = int(input())
  Settings.stats['Con'] =  Settings.stats['Con'] + x
  if x not in numlist:
    print('You do not have that number')
    continue
  else:
    numlist.remove(x)
    print('')
    print(sorted(numlist, reverse=True))
    print('')
  print('Intelligence: ')
  x = int(input())
  Settings.stats['Int'] =  Settings.stats['Int'] + x
  if x not in numlist:
    print('You do not have that number')
    continue
  else:
    numlist.remove(x)
    print('')
    print(sorted(numlist, reverse=True))
    print('')
  print('Wisdom: ')
  x = int(input())
  Settings.stats['Wis'] =  Settings.stats['Wis'] + x
  if x not in numlist:
    print('You do not have that number')
    continue
  else:
    numlist.remove(x)
    print('')
    print(sorted(numlist, reverse=True))
    print('')
  print('Charisma: ')
  x = int(input())
  Settings.stats['Cha'] =  Settings.stats['Cha'] + x
  if x not in numlist:
    print('You do not have that number')
    continue
  else:
    numlist.remove(x)
    print('')
  break
print('') #Makes a couple gaps for reading clarity
print('') #Lists stats in a neat order
print('Your Stats (including bonuses) are:' + '\n\
Strength: ' + str(Settings.stats['Str']) + '\n\
Dexterity: ' + str(Settings.stats['Dex']) + '\n\
Constitution: ' + str(Settings.stats['Con']) + '\n\
Intelligence: ' + str(Settings.stats['Int']) + '\n\
Wisdom: ' + str(Settings.stats['Wis']) + '\n\
Charisma: ' + str(Settings.stats['Cha']))
#Done like this for code readability
