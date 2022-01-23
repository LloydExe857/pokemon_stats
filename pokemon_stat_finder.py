# Make sure we import pandas for help working with data
import pandas as pd

# Finds what the user wants to do with stats
def stat_action():
    # Again, checking for invalid inputs
    action = 0
    while action not in ['1','2','3']:
        # What does the user want to find?
        action = input('\nWhat would you like to find?\n\
        Average(1)\n\
        Highest(2)\n\
        Lowest(3)\n\t')
        if action not in ['1','2','3']:
            print("Something's not right... Try again.")

    # Let's make that an int now
    action = int(action)
    
    # More validity checks!
    stat = "none"
    while stat not in ['Total','Hp','Attack','Defense','Sp. Atk','Sp. Def','Speed']:
        stat = input('\nWhat stat would you like to check for? Type "list" for a list of stats. ').title()
       # stat = stat.lower()
        if stat not in ['List','Total','Hp','Attack','Defense','Sp. Atk','Sp. Def','Speed']:
            print("You might wanna check that list of stats...")

        # Gotta deliver on that list promise
        elif stat == 'List':
            print_list()

    # Everything needs to be capitalized except HP. It needs to be uppered. We'll make sure it is.
    if stat == 'Hp':
        stat = stat.upper()

    # Now time for some calculation!
    calculate_stats(action,stat)
    
# Print checkable stats
def print_list():
    print("You can check for:\nTotal\nHP\nAttack\nDefense\nSp. Atk\nSp. Def\nSpeed")

# Call the respective functions for calculating
def calculate_stats(action,stat):

    # Find average
    if action == 1:
        find_avg(stat)

    # Find highest
    if action == 2:
        find_highest(stat)

    # Find lowest
    if action == 3:
        find_lowest(stat)



# Find the average value of a given stat
def find_avg(stat):
    # Get all the items in the column into one variable
    stat_total = 0
    for index, row in df.iterrows():
        stat_total += row[stat]
    
    average_stat = round(stat_total / (index + 1))
    print(f"The average {stat.lower()} is {average_stat}.")

# Find the highest value of a stat and its respective Pokemon
def find_highest(stat):
    # We want to compare every value in the column to find the largest
    highest = 0
    # We also want to save what Pokemon have this stat
    pokemon_with_high = list()
    for index, row in df.iterrows():
        # If we have a new highest
        if row[stat] > highest:
            # Save the new highest
            highest = row[stat]
            # Out with the old...
            del pokemon_with_high
            # ...and in with the new. This helps us in the case of a tie for highest stat
            pokemon_with_high = list()
            pokemon_with_high.append(row['Name'])

        # If we ahve a tie
        elif row[stat] == highest:
            # We just need to add a new Pokemon to the list
            pokemon_with_high.append(row['Name'])
            
    # If it is not a tie
    if len(pokemon_with_high) == 1:
        
        # Do some grammer work
        if stat != 'HP' and stat.lower() != 'attack':
            print(f"{pokemon_with_high[0]} has the highest {stat.lower()} with a {stat.lower()} of {highest}!")
        
        else:
            if stat.lower() == 'attack':
                stat = stat.lower()
            print(f"{pokemon_with_high[0]} has the highest {stat} with an {stat} of {highest}!")

        # If it is a tie
    else:
        # Yay for HP!
        if stat != 'HP' and stat.lower() != 'attack':
            print(f"The highest {stat.lower()} of {highest} is shared by:")
        
        else:
            print(f"The highest {stat} of {highest} is shared by:")
        # Print out the Pokemon that tied
        for pokemon in pokemon_with_high:
            print(pokemon)
            


# Find the lowest value of a stat and its respective Pokemon
def find_lowest(stat):
    # We want to compare every value in the column to find the lowest stat
    lowest = 90000
    # We also want to save what Pokemon have this stat
    pokemon_with_low = list()
    for index, row in df.iterrows():
        # If we have a new lowest
        if row[stat] < lowest:
            # Save the new lowest
            lowest = row[stat]
            # Out with the old...
            del pokemon_with_low
            # ...and in with the new. This helps us in the case of a tie for lowest stat
            pokemon_with_low = list()
            pokemon_with_low.append(row['Name'])

        # If we ahve a tie
        elif row[stat] == lowest:
            # We just need to add a new Pokemon to the list
            pokemon_with_low.append(row['Name'])

    # If it is not a tie
    if len(pokemon_with_low) == 1:
        # Again HP is the exception
        if stat != 'HP' and stat.lower() != 'attack':
            print(f"{pokemon_with_low[0]} has the lowest {stat.lower()} with a {stat.lower()} of {lowest}!")
        
        else:
            if stat.lower() == 'attack':
                stat = stat.lower()
            print(f"{pokemon_with_low[0]} has the lowest {stat} with an {stat} of {lowest}!")

    # If it is a tie
    else:
        # Yay for HP!
        if stat != 'HP':
            print(f"The lowest {stat.lower()} of {lowest} is shared by:")
        
        else:
            print(f"The lowest {stat} of {lowest} is shared by:")

        # Print out the Pokemon that tied
        for pokemon in pokemon_with_low:
            print(pokemon)
            
# START HERE
# We want to start of course by reading in the csv file
df = pd.read_csv("pokemon_edit.csv")

again = 'y'

# For if the user wants to go again
while again.lower() == 'y':
    stat_action()
    again = input('\nWould you like to do anything else? (y/n) ')

print("Goodbye\n")