import time  # to sleep some times
import random  # to select random objects
import sys  # allows to exit from Python

# Lists Of Objects
Places = ['Jungle', 'Desert', 'House']
Weapons = ['Gun', 'Knife', 'Rock', 'Sword']
Jungle_Monsters = ['Bear', 'squirrel', 'Lion', 'Wolf', 'Monkey']
Desert_Monsters = ['cheetah', 'Fennec fox', 'Snake', 'Dog']
House = ['Eat', 'Drink', 'Sleep', 'Wach Movie']
Game_Result = ['Win', 'Lose']
UserEntry = ['yes', 'no']
Monster = ''
# Define Function To print Messages

# Let user choose the Place


def GetUserInput(Choise):
    if Choise.lower() == 'J'.lower():
        return 'Jungle'
    elif Choise.lower() == 'D'.lower():
        return 'Desert'
    elif Choise.lower() == 'H'.lower():
        return 'House'
    else:
        return ''

# Chooese the monster Randomly from user place choise


def GetMonster(Choise):
    if Choise == 'Jungle':
        Monster = random.choice(Jungle_Monsters)
        print(Monster)
    if Choise == 'Desert':
        Monster = random.choice(Desert_Monsters)
        print(Monster)
    if Choise == 'House':
        Monster = random.choice(House)
        print(Monster)

# Print


def Print(msg):
    print(msg)


# let user choose if they want to change weapon


def WeaponChange():
    changerequest = input('would you like to change weapon\n')
    while changerequest not in UserEntry:
        print('Invalid input please choose yes or no')
        changerequest = input('would you like to change weapon ' +
                              'for yes write yes , for no write no \n')
    if changerequest == 'yes':
        weaponchoosed = random.choice(Weapons)
        print(weaponchoosed)

# ask user if they want to play again


def RetryGame():
    Retry = input('If You want to play again write yes or no to get out ')
    while Retry not in UserEntry:
        print('Invalid input please choose yes or no')
        Retry = input('If You want to play again \n'
                      'write yes or no to get out \n')
    if Retry == 'yes':
        return S()
    elif Retry == 'no':
        sys.exit('Thank you')

# Game Start


def StartGame():
    while True:
        Print('Welcome to the adventures fun game ')
        time.sleep(2)
        Print('Takes you to the world of fun and thrill')
        time.sleep(2)
        Print('You have to think well before each selection to win')
        time.sleep(2)
        name = input('Please Enter Your Name To Start Game \n')
        while name.strip() == '':
            name = input('Please Enter Your Name To Start Game \n')
        time.sleep(1)
        print('Please Choose Witch Place you want to play \n')
        time.sleep(1)
        for place in Places:
            print(place)
            time.sleep(1)
        Choise = ''
        while Choise not in Places:
            message = 'Give me your choise\n\
for Jungle press J\n\
for desert press d\n\
for house press h\n'
            Choise = input(message)
            Choise = GetUserInput(Choise)
        time.sleep(2)
        print('you have a weapon ')
        weaponchoosed = random.choice(Weapons)
        print(weaponchoosed)
        WeaponChange()
        print('\nyou now in ' + Choise +
              ' and you have a weapon ' + weaponchoosed)
        time.sleep(1)
        print('now you see front of you ')
        GetMonster(Choise)

        time.sleep(2)
        Print('Use weapon to kill monster')
        time.sleep(2)
        if (weaponchoosed == 'Gun' or
            weaponchoosed == 'Knife' or
            weaponchoosed == 'Rock' or
            weaponchoosed == 'Sword')
        and Monster == 'squirrel':
            print('you Win')
            time.sleep(2)
            print ('Game Over')
        elif Choise == 'House':
            print('you Win')
            time.sleep(2)
            print ('Game Over')
        else:
            print('you ' + random.choice(Game_Result))
            time.sleep(2)
            print ('Game Over')
        RetryGame()

StartGame()
