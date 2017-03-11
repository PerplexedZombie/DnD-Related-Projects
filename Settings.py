#Settings will hold all Globals
def init(): #This works, somehow...
    global RaceList #Essentially a list of all the things in this
    global ClassList#Also functionality
    global UserRace
    global UserClass
    global stats

    
    RaceList = ['Dwarf Hill', 'Dwarf (Mountain)', 'Elf (High)', 'Elf (Forest)', \
            'Halfling (Lightfoot)', 'Halfling (Stout)', 'Human', 'Dragonborn', \
            'Gnome (Forest)', 'Gnome (Rock)', 'Half-Elf', 'Half-Orc', 'Tiefling']

    ClassList = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', \
             'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', \
             'Wizard']
    UserRace = ''
    UserClass = ''
    
    stats = {'Str' : 0, 'Dex' : 0, 'Con' : 0, 'Int' : 0, 'Wis' : 0, 'Cha' : 0}

    
