import Settings

RaceList = Settings.RaceList
ClassList = Settings.ClassList
while True:
    while True:
        print('Choose a race:')
        print(str(RaceList))
        print('')
        Settings.UserRace = input()
        if Settings.UserRace not in (RaceList):
            print('That wasn\'t a race?')
            print('')
            continue
        elif Settings.UserRace == 'Dwarf Hill':
            import RaceInfo
            print('Is this the race you would like to be?')
            Resp1 = input()
            if Resp1 in ('No', 'no', 'on'):
                continue
        break
    while True:
        print('')
        print('Choose a class: ')
        print(ClassList)
        print('')
        Settings.UserClass = input()
        if Settings.UserClass not in ClassList:
            print('That is not a class.')
            print('')
            continue
        break

    print('You will be a ' + str(Settings.UserRace) + ' ' +\
          str(Settings.UserClass))
    print('Is this what you want?')
    Resp1 = input()
    if Resp1 in ('No', 'no', 'on'):
        print('Let us start over.')
        continue
    else:
        break
