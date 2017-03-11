#Settings will hold all Globals
def init(): #This works, somehow...
    global RaceList #Essentially a list of all the things in this
    global ClassList#Also functionality
    global UserRace
    global UserClass
    global stats
    global DwarvenToughness

    
    RaceList = ['Hill Dwarf', 'Mountain Dwarf', 'High Elf', 'Forest Elf', \
            'Lightfoot Halfling', 'Stout Halfling', 'Human', 'Dragonborn', \
            'Forest Gnome', 'Rock Gnome', 'Half-Elf', 'Half-Orc', 'Tiefling']

    ClassList = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', \
             'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', \
             'Wizard']
    UserRace = ''
    UserClass = ''
    
    stats = {'Str' : 0, 'Dex' : 0, 'Con' : 0, 'Int' : 0, 'Wis' : 0, 'Cha' : 0}

    DwarvenToughness = 1

    
