#Settings will hold all Globals
def init():
    global RaceList
    global ClassList
    global UserRace
    global UserClass
    RaceList = ['Dwarf (Hill)', 'Dwarf (Mountain)', 'Elf (High)', 'Elf (Forest)', \
            'Halfling (Lightfoot)', 'Halfling (Stout)', 'Human', 'Dragonborn', \
            'Gnome (Forest)', 'Gnome (Rock)', 'Half-Elf', 'Half-Orc', 'Tiefling']

    ClassList = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', \
             'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', \
             'Wizard']
    UserRace = ''
    UserClass = ''
    
