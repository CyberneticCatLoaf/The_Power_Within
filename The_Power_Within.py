import time
import random
import webbrowser
import os

##    print(" /$$$$$$$$ /$$                "      " /$$$$$$$                                            "      " /$$      /$$ /$$   /$$     /$$       /$$          ")
##    print("|__  $$__/| $$                "      "| $$__  $$                                           "      "| $$  /$ | $$|__/  | $$    | $$      |__/          ")
##    print("   | $$   | $$$$$$$   /$$$$$$ "      "| $$  \ $$ /$$$$$$  /$$  /$$  /$$  /$$$$$$   /$$$$$$ "      "| $$ /$$$| $$ /$$ /$$$$$$  | $$$$$$$  /$$ /$$$$$$$ ")
##    print("   | $$   | $$__  $$ /$$__  $$"      "| $$$$$$$//$$__  $$| $$ | $$ | $$ /$$__  $$ /$$__  $$"      "| $$/$$ $$ $$| $$|_  $$_/  | $$__  $$| $$| $$__  $$")
##    print("   | $$   | $$  \ $$| $$$$$$$$"      "| $$____/| $$  \ $$| $$ | $$ | $$| $$$$$$$$| $$  \__/"      "| $$$$_  $$$$| $$  | $$    | $$  \ $$| $$| $$  \ $$")
##    print("   | $$   | $$  | $$| $$_____/"      "| $$     | $$  | $$| $$ | $$ | $$| $$_____/| $$      "      "| $$$/ \  $$$| $$  | $$ /$$| $$  | $$| $$| $$  | $$")
##    print("   | $$   | $$  | $$|  $$$$$$$"      "| $$     |  $$$$$$/|  $$$$$/$$$$/|  $$$$$$$| $$      "      "| $$/   \  $$| $$  |  $$$$/| $$  | $$| $$| $$  | $$")
##    print("   |__/   |__/  |__/ \_______/"      "|__/      \______/  \_____/\___/  \_______/|__/      "      "|__/     \__/|__/   \___/  |__/  |__/|__/|__/  |__/")


prompts = ["Destroying every drug dealer in Gotham",
               "Opening random vats of radiated goo",
               "Demolishing cities",
               "Stopping trains with bare hands",
               "Exploring galixies",
               "Punching clowns",
               "Eradicating the moon",
               "Walking through walls",
               "Rubber-Necking with X-Ray",
               "Melting steel beams",
               "Exacting justice",
               "Assembling the Avengers",
               "Absorbing radiation",
               "Releasing the MEGA NUT",
               "Collecting the infinity stones",
               "Receiving maximum foodage",
               "Fucking Julius' Mom",
               "Rebuilding the multiverse",
               "Gathering Kryptonite",
               "Experimenting on rats",
               "Cloaking",
               "Uncloaking",
               "Phasing through walls",
               "Fighting Godzilla",
               "Shooting eye lasers",
               "Soaring the skies",
               "Wreaking Havoc",
               "Warping though space",
               "─=≡Σᕕ(⏒ ʖ̯⏒)ᕗ",
               "Running at lightspeed",
               "Breaking the sound barrier",
               "Talking to animals",
               "Reading minds",
               "Transforming",
               "Breaking faces",
               "Collecting the chaos emeralds"
               ]


power_types = ["Almighty",
               "Construct",
               "Enhancements",
               "Magical Powers",
               "Manipulations",
               "Meta Powers",
               "Physiology",
               "Psychic Powers",
               "Science Powers"]

power_links = {"Almighty": 'https://powerlisting.fandom.com/wiki/Special:RandomInCategory/Almighty_Powers',
               "Construct": 'https://powerlisting.fandom.com/wiki/Special:RandomInCategory/Constructs',
               "Enhancements": 'https://powerlisting.fandom.com/wiki/Special:RandomInCategory/Enhancements',
               "Magical Powers": 'https://powerlisting.fandom.com/wiki/Special:RandomInCategory/Magical_Powers',
               "Manipulations": 'https://powerlisting.fandom.com/wiki/Special:RandomInCategory/Manipulations',
               "Meta Powers": 'https://powerlisting.fandom.com/wiki/Special:RandomInCategory/Meta_Powers',
               "Physiology": 'https://powerlisting.fandom.com/wiki/Special:RandomInCategory/Physiology',
               "Psychic Powers": 'https://powerlisting.fandom.com/wiki/Special:RandomInCategory/Psychic_Powers' ,
               "Science Powers": 'https://powerlisting.fandom.com/wiki/Special:RandomInCategory/Science_Powers'
               }

player_list = []

def Game_Name():
    print(" /$$$$$$$$ /$$                ")
    print("|__  $$__/| $$                ")
    print("   | $$   | $$$$$$$   /$$$$$$ ")
    print("   | $$   | $$__  $$ /$$__  $$")
    print("   | $$   | $$  \ $$| $$$$$$$$")
    print("   | $$   | $$  | $$| $$_____/")
    print("   | $$   | $$  | $$|  $$$$$$$")
    print("   |__/   |__/  |__/ \_______/")
    print("")
    print(" /$$$$$$$                                            ")
    print("| $$__  $$                                           ")
    print("| $$  \ $$ /$$$$$$  /$$  /$$  /$$  /$$$$$$   /$$$$$$ ")
    print("| $$$$$$$//$$__  $$| $$ | $$ | $$ /$$__  $$ /$$__  $$")
    print("| $$____/| $$  \ $$| $$ | $$ | $$| $$$$$$$$| $$  \__/")
    print("| $$     | $$  | $$| $$ | $$ | $$| $$_____/| $$      ")
    print("| $$     |  $$$$$$/|  $$$$$/$$$$/|  $$$$$$$| $$      ")
    print("|__/      \______/  \_____/\___/  \_______/|__/      ")
    print("")
    print(" /$$      /$$ /$$   /$$     /$$       /$$          ")
    print("| $$  /$ | $$|__/  | $$    | $$      |__/          ")
    print("| $$ /$$$| $$ /$$ /$$$$$$  | $$$$$$$  /$$ /$$$$$$$ ")
    print("| $$/$$ $$ $$| $$|_  $$_/  | $$__  $$| $$| $$__  $$")
    print("| $$$$_  $$$$| $$  | $$    | $$  \ $$| $$| $$  \ $$")
    print("| $$$/ \  $$$| $$  | $$ /$$| $$  | $$| $$| $$  | $$")
    print("| $$/   \  $$| $$  |  $$$$/| $$  | $$| $$| $$  | $$")
    print("|__/     \__/|__/   \___/  |__/  |__/|__/|__/  |__/")
    print("")

def Gallows():

    print(" ___________.._______")
    print("| .__________))______|")
    print("| | / /      ||")
    print("| |/ /       ||")
    print("| | /        ||.-''.")
    print("| |/         |/  _  \"")
    print("| |          ||  `/,|")
    print("| |          (\\`_.'")
    print("| |         .-`--'.")
    print("| |        // . . \\")
    print("| |       // |   | \\")
    print("| |      //  | . |  \\")
    print("| |     []   |   |  []")
    print("| |          ||'||")
    print("| |          || ||")
    print("| |          || ||")
    print("| |          || ||")
    print('| |         / | | \'')
    print('""""""""""|_--- --- |"""|"')
    print('|"|"""""""\ \        "|"|')
    print("| |        \ \        | |")
    print(": :         \ \       : :")
    print(". .          `'       . .")
    print("00o0ooo0o00o00o00ooo0o00o0oo0o0o00o0o00o0oo0o0o0000o0oo0oo0o000o0o0oo0o0o0")
    print("0o0o000o0o0o00o00o00o00o00o00o00o0o0o00o000o00o00o00o00o00o00o0o00o0o000o0")
    print("")


def Round_Two_Logo():

    print(" /$$$$$$$   /$$$$$$  /$$   /$$ /$$   /$$ /$$$$$$$         /$$$$$$  /$$")
    print("| $$__  $$ /$$__  $$| $$  | $$| $$$ | $$| $$__  $$       /$$__  $$| $$")
    print("| $$  \ $$| $$  \ $$| $$  | $$| $$$$| $$| $$  \ $$      |__/  \ $$| $$")
    print("| $$$$$$$/| $$  | $$| $$  | $$| $$ $$ $$| $$  | $$        /$$$$$$/| $$")
    print("| $$__  $$| $$  | $$| $$  | $$| $$  $$$$| $$  | $$       /$$____/ |__/")
    print("| $$  \ $$| $$  | $$| $$  | $$| $$\  $$$| $$  | $$      | $$          ")
    print("| $$  | $$|  $$$$$$/|  $$$$$$/| $$ \  $$| $$$$$$$/      | $$$$$$$$ /$$")
    print("|__/  |__/ \______/  \______/ |__/  \__/|_______/       |________/|__/")
    print("")


def Credits():
    print('"Batman Was Trash" - Cameron')
    time.sleep(.5)
    print('')
    time.sleep(.5)
    print('')
    time.sleep(.5)
    print('')
    time.sleep(.5)
    print('"Locating Fucks To Give" - King Dong')
    time.sleep(.5)
    print('')
    time.sleep(.5)
    print('')
    time.sleep(.5)
    print('')
    time.sleep(.5)
    print('"Please Give Me Bread Mimicry Again!" - Ethan')
    time.sleep(.5)
    print('')
    time.sleep(.5)
    print('')
    time.sleep(.5)
    print('')
    time.sleep(.5)
    print('"Fucking Bitches Since 2003 With No Kids" - Julius')
    time.sleep(.5)
    print('')
    time.sleep(.5)
    print('')
    time.sleep(.5)
    print('')
    time.sleep(.5)
    print('"Your IP Is Now Mine" - Josh')
    time.sleep(.5)
    print('')
    time.sleep(.5)
    print('')
    time.sleep(.5)
    print('')
    time.sleep(.5)

    for i in range(6):
        print(random.choice(prompts))
        time.sleep(.5)
        print('')
        time.sleep(.5)
        print('')
        time.sleep(.5)
        print('')
        time.sleep(.5)
        print(random.choice(prompts))
        time.sleep(.5)
        print('')
        time.sleep(.5)
        print('')
        time.sleep(.5)
        print('')
        time.sleep(.5)
        print(random.choice(prompts))
        time.sleep(.5)
        print('')
        time.sleep(.5)
        print('')
        time.sleep(.5)
        print('')
        time.sleep(.5)
    
##Game Mechanics

def Round_Load():               
    
    for i in range(3):
        msg = random.choice(prompts)

        Round_Two_Logo()
        print('{}.'.format(msg))
        print("|===------------------------|")
        time.sleep(0.2)
        clear()
        Round_Two_Logo()
        print('{}..'.format(msg))
        print("|======---------------------|")
        time.sleep(0.2)
        clear()
        Round_Two_Logo()
        print('{}...'.format(msg))
        print("|=========------------------|")
        time.sleep(0.2)
        clear()

        Round_Two_Logo()
        print('{}.'.format(msg))
        print("|===============------------|")
        time.sleep(0.2)
        clear()
        Round_Two_Logo()
        print('{}..'.format(msg))
        print("|=================----------|")
        time.sleep(0.2)
        clear()
        Round_Two_Logo()
        print('{}...'.format(msg))
        print("|===================--------|")
        time.sleep(0.2)
        clear()
        
        Round_Two_Logo()
        print('{}.'.format(msg))
        print("|===================--------|")
        time.sleep(0.2)
        clear()
        Round_Two_Logo()
        print('{}..'.format(msg))
        print("|===================--------|")
        time.sleep(0.2)
        clear()
        Round_Two_Logo()
        print('{}...'.format(msg))
        print("|========================---|")
        time.sleep(0.2)
        clear()

        Round_Two_Logo()
        print('{}.'.format(msg))
        print("|=========================--|")
        time.sleep(0.2)
        clear()
        Round_Two_Logo()
        print('{}..'.format(msg))
        print("|==========================-|")
        time.sleep(0.2)
        clear()
        Round_Two_Logo()
        print('{}...'.format(msg))
        print("|===========================|")
        time.sleep(0.2)
        clear()
        prompts.remove(msg)

def Loading(): 
    
    for i in range(3):
        msg = random.choice(prompts)

        Game_Name()
        print('{}.'.format(msg))
        print("|===------------------------|")
        time.sleep(0.2)
        clear()
        Game_Name()
        print('{}..'.format(msg))
        print("|======---------------------|")
        time.sleep(0.2)
        clear()
        Game_Name()
        print('{}...'.format(msg))
        print("|=========------------------|")
        time.sleep(0.2)
        clear()

        Game_Name()
        print('{}.'.format(msg))
        print("|===============------------|")
        time.sleep(0.2)
        clear()
        Game_Name()
        print('{}..'.format(msg))
        print("|=================----------|")
        time.sleep(0.2)
        clear()
        Game_Name()
        print('{}...'.format(msg))
        print("|===================--------|")
        time.sleep(0.2)
        clear()
        
        Game_Name()
        print('{}.'.format(msg))
        print("|===================--------|")
        time.sleep(0.2)
        clear()
        Game_Name()
        print('{}..'.format(msg))
        print("|===================--------|")
        time.sleep(0.2)
        clear()
        Game_Name()
        print('{}...'.format(msg))
        print("|========================---|")
        time.sleep(0.2)
        clear()

        Game_Name()
        print('{}.'.format(msg))
        print("|=========================--|")
        time.sleep(0.2)
        clear()
        Game_Name()
        print('{}..'.format(msg))
        print("|==========================-|")
        time.sleep(0.2)
        clear()
        Game_Name()
        print('{}...'.format(msg))
        print("|===========================|")
        time.sleep(0.2)
        clear()
        prompts.remove(msg)


def clear():
    os.system( 'clear' )

def Rolling():
    for i in range(10): 
        print('Rolling.')
        time.sleep(0.1)
        clear()
        print('Rolling..') 
        time.sleep(0.1)
        clear()
        print('Rolling...') 
        time.sleep(0.1)
        clear()

def Not_Done():
    player_list.append(player)
    
def Duplicate_Player():
    print("Player already in list")
    player_list.append(player)
    player_list.pop()
    

def Delete_Player():
    clear()
    Gallows()
    print(player_list)
    print("")
    delete_player = input("Who shall be terminated?: ").strip().title()
    if delete_player in player_list:
        player_list.remove(delete_player)
        print("")
        print("{} has been executed for his war crimes".format(delete_player))
        time.sleep(2)
    else:
        print("")
        print("Player not in list... Quit wasting my time")
        time.sleep(2)
        
def Player_Creation():
    
    if player == "Delete":
        Delete_Player()
        
    elif player in player_list:
        Duplicate_Player()
        
    elif player != "Done":
        Not_Done()     


##Player Turns

def Player_One_Turn():
    
    player_one = player_list[0]
    print("It is {}'s turn".format(player_one))
    print("")
    time.sleep(1)
    
    input("Press enter to roll!")
    Rolling()
    
    first_power = random.choice(list(power_types))
    print("{} received {}".format(player_one, first_power))
    print("")
    
    reroll = input("Would you like to take {} off the table? (Y/N): ".format(first_power).strip())

    if reroll != "y":
        print('')
        print("{} chose to keep his {}!".format(player_one, first_power))
        
        time.sleep(2)
        
        power_roll = power_links.get('{}'.format(first_power))
        webbrowser.open('{}'.format(power_roll))
    else:
        power_types.remove(first_power)
        Rolling()
        new_power = random.choice(list(power_types))
        print("Your new power is {}".format(new_power))

        time.sleep(2)
        
        power_types.append(new_power)
        power_roll = power_links.get('{}'.format(new_power))
        webbrowser.open('{}'.format(power_roll))

def Player_Two_Turn():

    player_two = player_list[1]
    print("It is {}'s turn".format(player_two))
    print("")
    time.sleep(1)
    
    input("Press enter to roll!")
    Rolling()
    
    first_power = random.choice(list(power_types))
    print("{} received {}".format(player_two, first_power))
    print("")
    
    reroll = input("Would you like to take {} off the table? (Y/N): ".format(first_power).strip())
    
    if reroll != "y":
        print('')
        print("{} chose to keep his {}!".format(player_two, first_power))

        time.sleep(2)
        
        power_roll = power_links.get('{}'.format(first_power))
        webbrowser.open('{}'.format(power_roll))
    else:
        power_types.remove(first_power)
        Rolling()
        new_power = random.choice(list(power_types))
        print("Your new power is {}".format(new_power))

        time.sleep(2)
        
        power_types.append(new_power)
        power_roll = power_links.get('{}'.format(new_power))
        webbrowser.open('{}'.format(power_roll))

def Player_Three_Turn():
    
    player_three = player_list[2]
    print("It is {}'s turn".format(player_three))
    print("")
    time.sleep(1)
    
    input("Press enter to roll!")
    Rolling()
    
    first_power = random.choice(list(power_types))
    print("{} received {}".format(player_three, first_power))
    print("")
    
    reroll = input("Would you like to take {} off the table? (Y/N): ".format(first_power).strip())

    if reroll != "y":
        print('')
        print("{} chose to keep his {}!".format(player_three, first_power))
        
        time.sleep(2)
        
        power_roll = power_links.get('{}'.format(first_power))
        webbrowser.open('{}'.format(power_roll))
    else:
        power_types.remove(first_power)
        Rolling()
        new_power = random.choice(list(power_types))
        print("Your new power is {}".format(new_power))

        time.sleep(2)
        
        power_types.append(new_power)
        power_roll = power_links.get('{}'.format(new_power))
        webbrowser.open('{}'.format(power_roll))

def Player_Four_Turn():
    
    player_four = player_list[3]
    print("It is {}'s turn".format(player_four))
    print("")
    time.sleep(1)
    
    input("Press enter to roll!")
    Rolling()
    
    first_power = random.choice(list(power_types))
    print("{} received {}".format(player_four, first_power))
    print("")
    
    reroll = input("Would you like to take {} off the table? (Y/N): ".format(first_power).strip())

    if reroll != "y":
        print('')
        print("{} chose to keep his {}!".format(player_four, first_power))
        
        time.sleep(2)
        
        power_roll = power_links.get('{}'.format(first_power))
        webbrowser.open('{}'.format(power_roll))
    else:
        power_types.remove(first_power)
        Rolling()
        new_power = random.choice(list(power_types))
        print("Your new power is {}".format(new_power))

        time.sleep(2)
        
        power_types.append(new_power)
        power_roll = power_links.get('{}'.format(new_power))
        webbrowser.open('{}'.format(power_roll))

def Player_Five_Turn():
    
    player_five = player_list[4]
    print("It is {}'s turn".format(player_five))
    print("")
    time.sleep(1)
    
    input("Press enter to roll!")
    Rolling()
    
    first_power = random.choice(list(power_types))
    print("{} received {}".format(player_five, first_power))
    print("")
    
    reroll = input("Would you like to take {} off the table? (Y/N): ".format(first_power).strip())

    if reroll != "y":
        print('')
        print("{} chose to keep his {}!".format(player_five, first_power))
        
        time.sleep(2)
        
        power_roll = power_links.get('{}'.format(first_power))
        webbrowser.open('{}'.format(power_roll))
    else:
        power_types.remove(first_power)
        Rolling()
        new_power = random.choice(list(power_types))
        print("Your new power is {}".format(new_power))

        time.sleep(2) 
        
        power_types.append(new_power)
        power_roll = power_links.get('{}'.format(new_power))
        webbrowser.open('{}'.format(power_roll))

def Player_Six_Turn():
    
    player_six = player_list[5]
    print("It is {}'s turn".format(player_six))
    print("")
    time.sleep(1)
    
    input("Press enter to roll!")
    Rolling()
    
    first_power = random.choice(list(power_types))
    print("{} received {}".format(player_six, first_power))
    print("")
    
    reroll = input("Would you like to take {} off the table? (Y/N): ".format(first_power).strip())

    if reroll != "y":
        print("")
        print("{} chose to keep his {}!".format(player_six, first_power))
        
        time.sleep(2)

        power_roll = power_links.get('{}'.format(first_power))
        webbrowser.open('{}'.format(power_roll))
    else:
        power_types.remove(first_power)
        Rolling()
        new_power = random.choice(list(power_types))
        print("Your new power is {}".format(new_power))

        time.sleep(2)
        
        power_types.append(new_power)
        power_roll = power_links.get('{}'.format(new_power))
        webbrowser.open('{}'.format(power_roll))



def Player_One_Turn_D():

    player_one = player_list[0]
    print("It is {}'s turn".format(player_one))
    print("")
    time.sleep(1)
    
    input("Press enter to roll!")
    Rolling()
    
    first_power = random.choice(list(power_types))
    print("{} received {}".format(player_one, first_power))

    time.sleep(3)

    power_roll = power_links.get('{}'.format(first_power))
    webbrowser.open('{}'.format(power_roll))


def Player_Two_Turn_D():

    player_two = player_list[1]
    print("It is {}'s turn".format(player_two))
    print("")
    time.sleep(1)
    
    input("Press enter to roll!")
    Rolling()
    
    first_power = random.choice(list(power_types))
    print("{} received {}".format(player_two, first_power))

    time.sleep(3)

    power_roll = power_links.get('{}'.format(first_power))
    webbrowser.open('{}'.format(power_roll))

def Player_Three_Turn_D():
    
    player_three = player_list[2]
    print("It is {}'s turn".format(player_three))
    print("")
    time.sleep(1)
    
    input("Press enter to roll!")
    Rolling()
    
    first_power = random.choice(list(power_types))
    print("{} received {}".format(player_three, first_power))

    time.sleep(3)

    power_roll = power_links.get('{}'.format(first_power))
    webbrowser.open('{}'.format(power_roll))

def Player_Four_Turn_D():
    
    player_four = player_list[3]
    print("It is {}'s turn".format(player_four))
    print("")
    time.sleep(1)
    
    input("Press enter to roll!")
    Rolling()
    
    first_power = random.choice(list(power_types))
    print("{} received {}".format(player_four, first_power))

    time.sleep(3)

    power_roll = power_links.get('{}'.format(first_power))
    webbrowser.open('{}'.format(power_roll))

def Player_Five_Turn_D():
    
    player_five = player_list[4]
    print("It is {}'s turn".format(player_five))
    print("")
    time.sleep(1)
    
    input("Press enter to roll!")
    Rolling()
    
    first_power = random.choice(list(power_types))
    print("{} received {}".format(player_five, first_power))

    time.sleep(3)

    power_roll = power_links.get('{}'.format(first_power))
    webbrowser.open('{}'.format(power_roll))

def Player_Six_Turn_D():
    
    player_six = player_list[5]
    print("It is {}'s turn".format(player_six))
    print("")
    time.sleep(1)
    
    input("Press enter to roll!")
    Rolling()
    
    first_power = random.choice(list(power_types))
    print("{} received {}".format(player_six, first_power))

    time.sleep(3)

    power_roll = power_links.get('{}'.format(first_power))
    webbrowser.open('{}'.format(power_roll))



def Round_Two():

    while True:
        
        player_one_reroll = input("{} would you like to reroll? (Y/N):".format(player_list[0]))
        if player_one_reroll != "n":
            Player_One_Turn()
        else:
            clear()
            pass
        
        player_two_reroll = input("{} would you like to reroll? (Y/N):".format(player_list[1]))
        if player_two_reroll != "n":
            Player_Two_Turn()
        else:
            clear()
            pass

        if len(player_list) < 3:
            break
        elif len(player_list) >= 3:
            player_three_reroll = input("{} would you like to reroll? (Y/N):".format(player_list[2]))
            if player_three_reroll != "n":
                Player_Three_Turn()
            else:
                clear()
                pass

        if len(player_list) < 4:
            break
        elif len(player_list) >= 4:
            player_four_reroll = input("{} would you like to reroll? (Y/N):".format(player_list[3]))
            if player_four_reroll != "n":
                Player_Four_Turn()
            else:
                clear()
                pass

        if len(player_list) < 5:
            break
        elif len(player_list) >= 5:
            player_five_reroll = input("{} would you like to reroll? (Y/N):".format(player_list[4]))
            if player_five_reroll != "n":
                Player_Five_Turn()
            else:
                clear()
                pass

        if len(player_list) < 6:
            break
        elif len(player_list) >= 6:
            player_six_reroll = input("{} would you like to reroll? (Y/N):".format(player_list[5]))
            if player_six_reroll != "n":
                Player_Six_Turn()
                break
            else:
                break

        
    

def Classic():

    while True:

        clear()
        Player_One_Turn()
        clear()
        Player_Two_Turn()
        clear()
    
        if len(player_list) < 3:
            break
        elif len(player_list) >= 3:
            Player_Three_Turn()
            clear()

        if len(player_list) < 4:
            break
        elif len(player_list) >= 4:
            Player_Four_Turn()
            clear()

        if len(player_list) < 5:
            break
        elif len(player_list) >= 5:
            Player_Five_Turn()
            clear()

        if len(player_list) < 6:
            break
        elif len(player_list) >= 6:
            Player_Six_Turn()
            clear()
            break

    while True:
        Round_Load()
        Game_Name()
        print("")
        input("Thats was the end of round 1! Press enter to commence round 2!")
        clear()
        time.sleep(.5)
        
        Round_Two()
        break
    
        


def Double():

    while True:

        clear()
        Player_One_Turn()
        clear()
        Player_Two_Turn()
        clear()
    
        if len(player_list) < 3:
            break
        elif len(player_list) >= 3:
            Player_Three_Turn()
            clear()

        if len(player_list) < 4:
            break
        elif len(player_list) >= 4:
            Player_Four_Turn()
            clear()

        if len(player_list) < 5:
            break
        elif len(player_list) >= 5:
            Player_Five_Turn()
            clear()

        if len(player_list) < 6:
            break
        elif len(player_list) >= 6:
            Player_Six_Turn()
            clear()
            break

    while True:

        Player_One_Turn()
        clear()
        Player_Two_Turn()
        clear()
    
        if len(player_list) < 3:
            break
        elif len(player_list) >= 3:
            Player_Three_Turn()
            clear()

        if len(player_list) < 4:
            break
        elif len(player_list) >= 4:
            Player_Four_Turn()
            clear()

        if len(player_list) < 5:
            break
        elif len(player_list) >= 5:
            Player_Five_Turn()
            clear()

        if len(player_list) < 6:
            break
        elif len(player_list) >= 6:
            Player_Six_Turn()
            clear()
            break


def Destiny():

    while True:

        clear()
        Player_One_Turn_D()
        clear()
        Player_Two_Turn_D()
        clear()
    
        if len(player_list) < 3:
            break
        elif len(player_list) >= 3:
            Player_Three_Turn_D()
            clear()

        if len(player_list) < 4:
            break
        elif len(player_list) >= 4:
            Player_Four_Turn_D()
            clear()

        if len(player_list) < 5:
            break
        elif len(player_list) >= 5:
            Player_Five_Turn_D()
            clear()

        if len(player_list) < 6:
            break
        elif len(player_list) >= 6:
            Player_Six_Turn_D()
            clear()
            break





##Loading "Screen"

clear()
time.sleep(2)

Loading()


#Player Setup!        
while True:

    Game_Name()
    print("HERO ROSTER <{}> HERO ROSTER".format(player_list))
    print('')
    player = input("Enter your name (When done, type done)").strip().title()
    
    
    if player == "Done":
        clear()
        Game_Name()
        print("HERO ROSTER <{}> HERO ROSTER".format(player_list))
        print("")
        input("Here are our soon to be Heros! Press enter to continue!")
        clear()
        break
    elif player == "Debug_3":
        player_list = ["P1","P2","P3"]
        print(player_list)
        time.sleep(1)
        clear()
        break
    elif player == "Debug_All":
        player_list = ["P1","P2","P3","P4","P5","P6"]
        print(player_list)
        time.sleep(1)
        clear()
        break
    else:
        Player_Creation()
        clear()
        
    
#Round 1  
while True:

    clear()
    diff_choice = input("Choose a Game Mode! (Classic(C)/DoubleTrouble(DT)/Destiny(D)):").upper()
    
    if diff_choice == "C":
        Classic()
        break
    elif diff_choice == "DT":
        Double()
        break
    elif diff_choice == "D":
        Destiny()
        break
    else:
        print("Choice not in list!")
        
    
    
    



##Game Over

clear()
Game_Name()
Credits()
clear()

