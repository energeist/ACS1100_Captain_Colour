from os import system
from time import sleep
import random

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

def get_input(checklist):
    input_item = int(user_input(f"Index number? (0 - {len(checklist) - 1}) > "))
    while input_item >= len(checklist):
        input_item = int(input(f"Not a valid index number, please enter a number from 0 - {len(checklist) - 1} > "))
    return input_item

# List all items
def list_all_items():
    index = 0
    for list_item in checklist:
        print(f'Index value: {str(index)} || Item: {list_item}')
        index += 1

# Checkmark (√) an item
def mark_completed(input_item):
    if checklist[input_item][0] != '√':
        checklist[input_item] = '√ ' + checklist[input_item]
    else:
        print("That item is already checkmarked")

# Uncheck (remove √) an item       
def uncheck(input_item):
    if checklist[input_item][0] == '√':
        checklist[input_item] = checklist[input_item][2:]
    else:
        print("That item is not checkmarked yet")

def randomizer(colours, clothing):
    checklist.clear()
    random.shuffle(colours)
    random.shuffle(clothing)
    for item in range(len(colours)):
        checklist.append(f'{colours[item]} {clothing[item]}') 
    return checklist

def user_input(prompt):
    # the input function will display a message in the terminal and wait
    # for user input
    user_input = input(prompt)
    return user_input

def select(function_code):
    
    # ADD item
    if function_code.lower() == "a":
        input_item = user_input("Input a colour and an article of clothing > ")
        create(input_item)
        return True

    # REMOVE item
    if function_code.lower() == "d":
        if len(checklist) > 0:
            input_item = get_input(checklist)
            destroy(input_item)
        else:
            print("You haven't added anything to the checklist yet.")
        return True
    
    # RANDOMIZE a list
    if function_code.lower() == "r":
        randomizer(colours, clothing)
        print("Random list generated!")
        return True

    # CHECKMARK (item
    if function_code.lower() == "c":
        if len(checklist) > 0:
            input_item = get_input(checklist)
            mark_completed(input_item)
        else:
            print("You haven't added anything to the checklist yet.")
        return True

    if function_code.lower() == "u":
        if len(checklist) > 0:
            input_item = get_input(checklist)
            uncheck(input_item)
        else:
            print("You haven't added anything to the checklist yet.")
        return True        

    # READ item
           
    elif function_code.lower() == "i":
        if len(checklist) > 0:
            input_item = get_input(checklist)
            print(f"Index value: {input_item} || Item: {read(input_item)}")
        else:
            print("You haven't added anything to the checklist yet.")
        return True

    # print all items

    elif function_code.lower() == "p":
        if len(checklist) > 0:
            list_all_items()
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
    
# def test():
#     create("purple sox")
#     create("red cloak")

#     print(read(0))
#     print(read(1))

#     update(0, "purple sox")
#     destroy(1)

#     print(read(0))
#     mark_completed()

#     list_all_items()

#     select("C")
#     list_all_items()
#     select("R")
#     list_all_items()

# test()

running = True
while running:
    selection = user_input("""Enter a command:
    'A' to add to the list
    'D' to delete from the list
    'R' to generate a new random list
    'C' to checkmark an item as completed
    'U' to uncheck an already checkmarked item
    'P' to display the whole list
    'I' to display a single list item
    'Q' to quit
    Enter your command here > """)
    sleep(1)
    system('clear')
    running = select(selection)
    sleep(1)


