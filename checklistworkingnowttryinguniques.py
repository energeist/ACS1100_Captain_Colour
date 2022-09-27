from os import system
from time import sleep
import random

checklist = []
list_colours = []
list_clothes = []
# List of colours to select from
colours = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
#List of clothing to select from
clothing = ['Headband', 'Cape', 'Shirt', 'Belt', 'Pants', 'Leftboot', 'Rightboot']

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

def colourize(item_colour):
    if item_colour.title() == 'Red':
        item_colour = '\33[31m' + item_colour + '\33[0m'
    elif item_colour.title() == 'Orange':
        item_colour = '\33[33m' + item_colour + '\33[0m'
    elif item_colour.title() == 'Yellow':
        item_colour = '\33[33m' + item_colour + '\33[0m'
    elif item_colour.title() == 'Green':
        item_colour = '\33[32m' + item_colour + '\33[0m'
    elif item_colour.title() == 'Blue':
        item_colour = '\033[36m' + item_colour + '\33[0m'               
    elif item_colour.title() == 'Indigo':
        item_colour = '\33[34m' + item_colour + '\33[0m'
    elif item_colour.title() == 'Violet':
        item_colour = '\33[35m' + item_colour + '\33[0m'
    return item_colour            

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
    list_colours.clear()
    list_clothes.clear()
    random.shuffle(colours)
    random.shuffle(clothing)
    for item in range(len(colours)):
        checklist.append(f'{colourize(colours[item])} {clothing[item]}') 
    return checklist

def split_list(checklist):
    split_list = []
    for i in range(len(checklist)):
        split_list.append(checklist[i].split())
        list_colours.append(split_list[i][0])
        colourize(split_list[i][0])
        list_clothes.append(split_list[i][1])
        coloured_item = split_list[i][0] + ' ' + split_list[i][1]
        update(i, coloured_item)
    return checklist

def user_input(prompt):
    # the input function will display a message in the terminal and wait
    # for user input
    user_input = input(prompt)
    return user_input

def select(function_code, checklist):
    
    # ADD item
    if function_code.lower() == "a":
        split_list(checklist)
        input_colour = user_input(f"Input a colour from this list: {colours} > ")
        while input_colour.title() not in colours:
            input_colour = user_input(f"We don't have that dye colour! Please select a colour from this list: {colours} > ")
        while input_colour.title() in list_colours:
            input_colour = user_input(f"You've already chosen {input_colour}, please choose another item from this list: {colours} > ")
        list_colours.append(input_colour.title())
        
        input_clothing = user_input(f"Input an item of clothing from this list: {clothing} > ")
        while input_clothing.title() not in clothing:
            input_clothing = user_input(f"You don't have any {input_clothing} in your wardrobe! Please select an item of clothing from this list: {clothing} > ")
        while input_clothing.title() in list_clothes:
            input_clothing = user_input(f"You've already chosen {input_clothing}, please choose another item from this list: {clothing} > ")
        list_clothes.append(input_clothing.title())
        
        input_item = f'{colourize(input_colour)} {input_clothing}' 
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
    running = select(selection, checklist)
    sleep(1)


