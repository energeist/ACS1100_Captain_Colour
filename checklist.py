from os import system
from random import randint
from time import sleep

global checklist
checklist = []

# List of colours to select from
colours = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

#List of clothing to select from
clothing = ['Headband', 'Cape', 'Shirt', 'Belt', 'Pants', 'Left Boot', 'Right Boot']

#  CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

# List all items
def list_all_items(checklist):
    index = 0
    for list_item in checklist:
        print(f'Index value: {str(index)} || Item: {list_item}')
        index += 1

# Checkmark (√) an item
def mark_completed(input_item):
    if checklist[input_item][0] != '√':
        for list_item in checklist:
            checklist[input_item] = '√ ' + list_item
    else:
        print("That item is already checkmarked")

# Uncheck (remove √) an item       
def uncheck(input_item):
    if checklist[input_item][0] == '√':
        checklist[input_item] = checklist[input_item][2:]
    else:
        print("That item is not checkmarked yet")

def randomizer(clothing, colours, checklist):
    checklist = []
    print(clothing)
    print(colours)
    while len(clothing) > 0:
        rand_clothing_index = randint(0, (len(clothing) - 1))
        rand_colour_index = randint(0, (len(colours) - 1))
        added_item = f'{colours[rand_colour_index]} {clothing[rand_clothing_index]}'
        print(clothing[rand_clothing_index])
        print(colours[rand_colour_index])
        checklist.append(added_item)
        print(checklist)
        colours.pop(rand_colour_index)
        clothing.pop(rand_clothing_index)
        print(len(colours))
        print(len(clothing))
    return checklist
    
def user_input(prompt):
    # the input function will display a message in the terminal and wait
    # for user input
    user_input = input(prompt)
    return user_input

def select(function_code):
    
    # ADD item
    if function_code.lower() == "a":
        input_item = user_input("Input item > ")
        create(input_item)
        return True

    # REMOVE item
    if function_code.lower() == "d":
        if len(checklist) > 0:
            input_item = int(user_input(f"Index number (0 - {len(checklist) - 1}) > "))
            destroy(input_item)
        else:
            print("You haven't added anything to the checklist yet.")
        return True

    # RANDOMIZE outfit
    
    # CHECKMARK (item
    if function_code.lower() == "c":
        if len(checklist) > 0:
            input_item = int(user_input(f"Index number (0 - {len(checklist) - 1}) > "))
            mark_completed(input_item)
        else:
            print("You haven't added anything to the checklist yet.")
        return True

    if function_code.lower() == "u":
        if len(checklist) > 0:
            input_item = int(user_input(f"Index number (0 - {len(checklist) - 1}) > "))
            uncheck(input_item)
        else:
            print("You haven't added anything to the checklist yet.")
        return True        

    # read item      
    elif function_code.lower() == "i":
        item_index = int(user_input("Index Number? > "))
        while item_index >= len(checklist):
            item_index = int(input(f"Not a valid index number, please enter a number from 0 - {len(checklist) - 1} > "))
        print(f"{item_index} {read(item_index)}")
        return True

    #RANDOMIZE outfit
    elif function_code.lower() == "r":
        checklist = []
#        print(len(checklist))
        if len(checklist) > 0:
            print("You've already added items to your checklist.")
            print("This function will erase the existing list and generate a new randomized list.")
            proceed = input("Proceed? Enter y/n > ")
            if proceed.lower == 'y':
                randomizer(clothing, colours, checklist)
                print("Randomized outfit generated!")
            elif proceed.lower == 'n':
                print("Returning to main menu.")
            else:
                proceed = input("Not a valid entry, please entry y/n > ")
        else:
            checklist = randomizer(clothing, colours, checklist)

        return True

    # print all items
    elif function_code.lower() == "p":
        if len(checklist) > 0:
            list_all_items(checklist)
        else:
            print("You haven't added anything to the checklist yet.")
        return True

    # exit/quit    
    elif function_code.lower() == "q":
        print("Done!")
        return False

    # catch all
    else:
        print("Unknown Option")
        return True
    
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple sox")
    destroy(1)

    print(read(0))
    mark_completed()

    list_all_items()

    select("C")
    list_all_items()
    select("D")
    list_all_items()

# test()

running = True
while running:
    selection = user_input("""Enter a command:
    'A' to add to list
    'D' to delete from list
    'C' to checkmark an item as completed
    'U' to uncheck an already checkmarked item
    'R' to generate a random outfit
    'P' to display the whole list
    'I' to display a single list item
    'Q' to quit
    Enter your command here > """)
    # sleep(1)
    # system('clear')
    running = select(selection)
    # sleep(3)