def north():
    print('You are facing north now')
    print('Where do you want to face now?')
    switch = True 
    while switch:
        change = input('')
        if change.lower() == 'north':
            print('You are facing North already, please type a different position')
        elif change.lower() == 'south':
            south()
            switch = False
            break
        elif change.lower() == 'west':
            west()
            switch = False 
            break
        elif change.lower() == 'east':
            east()
            switch = False
            break
        else:
            print('Please type North South West East to change your position')


def east():
    print('You are facing east now')
    print('Where do you want to face now?')
    switch = True 
    while switch:
        change = input('')
        if change.lower() == 'north':
            north()
            switch = False
            break
        elif change.lower() == 'south':
            south()
            switch = False
            break
        elif change.lower() == 'west':
            west()
            switch = False 
            break
        elif change.lower() == 'east':
            print('You are already facing east, type a different position')
        else:
            print('Please type North South West East to change your position')

def west():
    print('You are facing west now')
    print('Where do you want to face now?')
    switch = True 
    while switch:
        change = input('')
        if change.lower() == 'north':
            north()
            switch = False
            break
        elif change.lower() == 'south':
            south()
            switch = False
            break
        elif change.lower() == 'west':
            print('You are already facing west. please type a different position')
        elif change.lower() == 'east':
            east()
            switch = False
            break
        else:
            print('Please type North South West East to change your position')
def south():
    print('You are facing south now')
    print('Where do you want to face now?')
    switch = True 
    while switch:
        change = input('')
        if change.lower() == 'north':
            north()
            switch = False
            break
        elif change.lower() == 'south':
            print('you are already facing south, please type a different position')
        elif change.lower() == 'west':
            west()
            switch = False 
            break
        elif change.lower() == 'east':
            east()
            switch = False
            break
        else:
            print('Please type North South West East to change your position')

print('you are fixed to facing North')
print('where do you want to face?')
first = True
while first:
    print('Use North South West East to switch positions')
    change = input('')
    if change.lower() == 'north':
        print('You are already facing North, please type a different postion')
    elif change.lower() == 'south':
        south()
        first = False
        break
    elif change.lower() == 'west':
        west()
        first = False
        break
    elif change.lower() == 'east':
        east()
        first = False
        break
    else:
        print('Please pick either North South West or West')