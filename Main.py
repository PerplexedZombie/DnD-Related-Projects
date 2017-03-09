#First full program
#Aim is to - using different files within a folder randomly generate
#numbers to make a DnD character then simulate the character fighting a goblin
#1000 times
import Settings

Settings.init()

import RaceClassSel


print('You are a ' + str(Settings.UserRace) + ' ' + str(Settings.UserClass))
