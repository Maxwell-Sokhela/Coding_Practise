#! /usr/bin/env python3
#Original Source from Python 3 for Absolute Beginners by Tim Hall and JP Stacey
#Very shitty code but, just for practice. Numerous errors

"""
rpcombat.py 
Purpose: Simple Role-Playing Combat Game.
Target System: GNU/Linux
Interface: Command-line
Functional Requirements: The user must be able to generate more than one character profile, equip those characters with suitable weapons, and model hand-to-hand combat between characters.
Testing methods: trace table and play testing.
Test values: (Ez, Tall, Pixie, female), (Inkon, Small, Troll, male)
Expected results: All statistics should be intergers in the (1-99) range. Apart from that, this script needs play-testing.
Limitations: Too many to mention.
"""

__version__ = 0.2
__maintainer__ = "maintainer@website.com"
__status__ = "Prototype"

# Import modules

import random

# set up a constant data.

stock = {'shield':(15,20,50),
        'sword':(60,60,40),
        'dagger':(25,30,50),
        'halberd':(80,80,30),
        'club':(15,30,30),
        'flail':(50,70,45),
        'hammer':(99,100,20),
        'cuirass':(30,45,20),
        'armour':(101,100,0),
        'lantern':(10,5,30),
        'pole':(10,5,50),
        'rope':(10,5,70)}
armour_types = set(['shield','cuirass','armour'])
hits = ('hits','bashes','smites','whacks','shreds','mutilates','lacerates','annihilates')
misses = ('misses', 'nearly hits', 'fails to connect with', 'swipes widlet at', 'flails ineffectually at', 'gets nowhere near', 'nearly decapitates self instead of', 'hits self on the foot, to the amusement of')
damage_report = ('small insult','flesh wound','deep slash','ragged gash','savage laceration','fractured rib-cage','smashed-up face','split skull')
life_changing = ('a scar.','bruising.','serious blood-loss.','total debilitation.', 'chromic concussion.','a severed limb.','multiple fractures.','an amputated head.')

# Preferences
# Set to 'True' to trace variables.
trace = False
reply = input('How many players? ')
max_players = int(reply)

# This is a global variable.
players = []

def roll(sides, dice = 1):
    """Dice rolling simulator
    
    sides: Number of sides the die has 
    dice: number of dice to be rolled (defaults to 1)
    Returns a random number between dice and dice * sides 
    weighted towards the average.
    """
    result = 0
    for rolls in range(1,dice):
        result += random.randint(1,sides)
    return result
    
def ziply(seq=None):
    """Create a matrix of matches from a sequence
    
    Takes one argument seq, which should be a sequence of length > 1
    Returns a tuple of tuples - matches.
    """
    
    opponents = list(seq[:])
    opponents.reverse()
    matches = [(actor, target) for actor in seq
                for target in opponents
                if target != actor]
    return tuple(matches)
def join_with_and(sequence): 
    """Join up a list with commas and 'and' between last two items
    
    Takes a sequence and returns a sentence.
    """
    if len(sequence) > 1:
        last_item = sequence[-1]
        sentence = ", ".join(sequence[:-1])
        sentence = sentence + " and " + last_item
    #In the book it is elif sequence but the correct command is elif len(sequence)
    elif len(sequence) < 1:
        sentence = "whole lot of nothing"
    else:
        sentence = sequence[0]
    return sentence
    
def fix_gender(gender, phrase):
    """Replace the word 'them' with gender-specific pronoun
    
    Take two arguments:
    gender - a string which can be 'male', 'female' or something else.
    phrase - the string to be modified.
    Returns a string with non-gender specific pronouns replaced by 
    gender specific ones.
    """
    if gender == 'female':
        sentence = phrase.replace('themself','herself')
    elif gender == 'male':
        sentence = phrase.replace('themself','himself')
    else:
        sentence = phrase.replace('themself','itself')
    return sentence
    
def generate_rpc():
    """Role-Playing Character generator
    
    Take no arguments
    Returns a new character profile dictionary
    """
    print()
    print("New Character")
    print()
    # Create empty profile dictionary
    profile = {'Name':"", 'Desc':"", 'Gender':"", 'Race':"", 'Muscle':0, 'Brainz':0, 'Speed':0, 'Charm':0, 'life':0, 'magic':0, 'prot':0, 'gold':0, 'inventory':[]}
    
    # Prompt user for user-defined information (Name, Desc, Gender, Race)
    name = input('What is your name? ')
    desc = input('Describe yourself: ')
    gender = input('What Gender are you? (male/female/unsure): ')
    race = input('What Race are you? - (Pixie/Vulcun/Gelfing/Troll): ')
    # Validate user input
    profile['Name'] = name.capitalize()
    profile['Desc'] = desc.capitalize()
    gender = gender.lower()
    if gender.startswith('f'):
        profile['Gender'] = 'female'
    elif gender.startswith('m'):
        profile['Gender'] = 'male'
    else:
        profile['Gender'] = 'neuter'
    race = race.capitalize()
    if race.startswith('P'):
        profile['Race'] = 'Pixie'
    elif race.startswith('V'):
        profile['Race'] = 'Vulcan'
    elif race.startswith('G'):
        profile['Race'] = 'Gelfing'
    elif race.startswith('T'):
        profile['Race'] = 'Troll'
    else:
        profile['Race'] = 'Goblin'
        
    # Generate stats ('Muscle', 'Brainz', 'Speed', 'Charm')
    profile['Muscle'] = roll(33,3)
    profile['Brainz'] = roll(33,3)
    profile['Speed'] = roll(33,3)
    profile['Charm'] = roll(33,3)
    
    # Work out combat stats (life, magic, prot, gold)
    life = (profile['Muscle'] + (profile['Speed']/2) + roll(49,1))/2
    magic = (profile['Brainz'] + (profile['Charm']/2) + roll(49,1))/2
    prot = (profile['Speed'] + (profile['Brainz']/2) + roll(49,1))/2
    gold = roll(40,4)
    
    # Validate stats
    if 0 < life < 100:
        profile['life'] = life
    else:
        profile['life'] = roll(33,3)
    if 0 < magic < 100:
        profile['magic'] = magic
    else:
        profile['magic'] = roll(33,3)
    if 0 < prot < 100:
        profile['prot'] = prot
    else:
        profile['prot'] = roll(33,3)
    profile['gold'] = gold
    
    # Output the character sheet
    fancy_line = "<~~|#|==~~++**@/**++~~==|#|==~~>"
    print()
    print(fancy_line)
    print("\t", profile['Name'])
    print("\t", profile['Race'], profile['Gender'])
    print("\t", profile['Desc'])
    print(fancy_line)
    print()
    print("\tMuscle: ", profile['Muscle'], "\tlife: ", profile['life'])
    print("\tBrainz: ", profile['Brainz'], "\tmagic: ", profile['magic'])
    print("\tSpeed: ", profile['Speed'], "\tprotection: ", profile['prot'])
    print("\tCharm: ", profile['Charm'], "\tgold: ", profile['gold'])
    print()
    return profile

def buy_equipment():
    """Purchase an item of equipment
    
    Takes no arguments.
    This function modifies the current character profilke dictionary in place.
    It returns a value which evaluates as either True or False
    intended to control the shopping loop.
    """
    # Display shop stock list with prices.
    print()
    print("<==|#|==SHOP/==|#|==>")
    for item in stock:
        print("\t", item, stock[item][0])
    print("<==|#|==@@@@/==|#|==>")
    print()
    print("You have", profile['gold'], "gold.")
    # Prompt user to make a purchase.
    purchase = input('Please choose an item or type "done" to quit. ')
    # If the item is in stock and the player has enough gold, buy it.
    if purchase in stock:
        if stock[purchase][0] <= profile['gold']:
            test_phrase = profile['Name'] + " buys themself some equipment"
            print(fix_gender(profile['Gender'], test_phrase))
            print("You buy a", purchase, "for",stock[purchase][0], "gold pieces.")
            profile['gold'] -= stock[purchase][0]
            profile['inventory'].append(purchase)
            print("You have a", join_with_and(profile['inventory']), "in your bag.")
            print("Oy have", profile['gold'], "left.")
        else:
            print("You don't have enough gold to buy that.")
    elif purchase == 'done' or purchase == "":
        return profile['inventory'] == [] and profile['gold'] > 10
    else:
        print("We don't have", purchase, "in stock")
    return purchase
    
def calc_velocity(attacker, target):
    """Calculate velocity of hit (or miss)
    
    Takes two arguments:
    attacker and target are integer pointers to the players list
    This function looks up values from the players list
    and returns a weighted semi-random integer
    representing the velocity of the strike.
    """
    attack_speed = players[attacker]['Speed']
    weapon_speed = players[attacker]['weapon'][2]
    attack_chance = roll(players[attacker]['Brainz'])
    attack_velocity = attack_speed + weapon_speed + attack_chance
    target_prot = players[target]['prot']
    armour_speed = players[target]['armour'][2]
    target_velocity = target_prot + armour_speed
    velocity = (attack_velocity - target_velocity) / 2
    return velocity
    
def calc_damage(attacker, target, velocity):
    """Calculate the damage of the hit
    
    Takes three arguments:
    attacker and target are integer points to the players list
    velocity is an integer representing the velocity of the strike.
    Returns a tuple of two integers - damage and potential damage
    """
    attack_strength = players[attacker]['Muscle']
    weapon_damage = players[attacker]['weapon'][1]
    attack_damage = attack_strength + weapon_damage + velocity
    target_strength = players[target]['Muscle']
    armour_strength = players[target]['armour'][1]
    target_chance = roll(players[target]['Brainz'])
    target_defence = target_strength + armour_strength + target_chance
    potential_damage = (attack_damage - target_defence)
    if potential_damage < 1:
        potential_damage = 2
    damage = random.randint(1,potential_damage)
    return damage, potential_damage
    
# The main body of the program starts here,
# So this is where the flow of execution begins.
# Generate characters
while len(players) < max_players:
    # Call character generation function.
    profile = generate_rpc()
    # Go shopping if the inventory is empty
    shopping = profile['inventory'] == []
    while shopping:
        shopping = buy_equipment()
    handbag = join_with_and(profile['inventory'])
    print("You own a", handbag)
    
    # Choose a weapon
    print(profile['Name'] + ", prepare for mortal combat!!!")
    # See if player has any weapons
    weapon_stats = [stock[item] for item in profile['inventory'] if item not in armour_types]
    if len(weapon_stats) == 1:
        profile['weapon'] = weapon_stats[0]
    elif len(weapon_stats) < 1:
        profile['weapon'] = (0, 20, 50)
    else:
        weapon = input("And choose your weapon: ")
        # The weapon must be in player's inventory.
        # Default to fist if weapon not available.
        weapon = weapon.lower()
        if weapon in profile['inventory']:
            profile['weapon'] = stock[weapon]
        else:
            profile['weapon'] = (0,20,50)
    # See if player has any armour
    armour_stats = [stock[item] for item in profile['inventory'] if item in armour_types]
    if armour_stats:
        profile['armour'] = armour_stats[0]
    else:
        profile['armour'] = (0,0,50)
    print(profile['Name'], "is now ready for battle. ")
    # Add new player to list of players
    players.append(profile)
    
# Combat

print()
print("Then let the combat begin!")
print()

vel_max = 23
vel_min = 1
dam_max = 23

# Loop while more than one player is still alive
while len(players) > 1:
    # Create list of matches using ziply function
    matches = ziply(range(0,len(players)))
    if trace:
        print(matches)
    for attacker, target in matches:
        life_left = players[target]['life']
        
        # Calculate velocity of blow
        velocity = calc_velocity(attacker, target)
        if trace:
            print("\tvel\thit\tdam\tchange")
            print("\t", velocity)
        if velocity > 0:
            # Print suitable hit message
            if velocity > vel_max:
                vel_max = velocity
            hit_type = int(7 * velocity / vel_max)
            if hit_type > 7:
                hit_type = 7
            if trace:
                print("\t\tHit#", hit_type)
            print(players[attacker]['Name'], hits[hit_type], players[target]['Name'], end="")
        else:
            # Print suitable Miss message
            if velocity < vel_min:
                vel_min = velocity
            miss_type = int(velocity / vel_max)
            if miss_type > 7:
                miss_type = 7
            if trace:
                print("\t\tMiss#", miss_type)
            print(players[attacker]['Name'], fix_gender(players[attacker]['Gender'],misses[miss_type]), players[target]['Name'])
            # End player turn
            continue
        # Calculate damage inflicted by blow
        damage, potential_damage = calc_damage(attacker, target, velocity)
        if trace:
            print()
            print("\t\tDamage:", damage, potential_damage)
        if damage > dam_max:
            dam_max = damage
        # Print damage report
        damage_type = int(7 * damage/dam_max)
        if damage_type > 7:
            damage_type = 7
        if trace:
            print("\t\t\t\tDamage#", damage_type)
        change_type = int(5 * damage/life_left)
        if change_type > 7:
                change_type = 7    
        print("inflicting a", damage_report[damage_type], "and", life_changing[change_type])
        
        # Inflict damage on target.
        players[target]['life'] -= damage
        # Check whether target is still alive or not.
        if players[target]['life'] <= 0:
            #print Loser
            print()
            print(players[target]['Name'], "collapses in a pool of blood")
            # Remove loser from the players list
            del players[target]
            print()
            # End this round of combat immediately.
            break
            
if trace:
    print()
    print("\t\tmax damage | velocity", dam_max, vel_max, ":: min", vel_min)
    print()
    
# Print winner
print(players[0]['Name'], "wins the fight.")

