from os import system
from time import sleep
import random

checklist = []
chosen_colours = []
chosen_clothes = []
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

#User input
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

# Outfit randomizer
def randomizer(colours, clothing):
    checklist.clear()
    chosen_colours.clear()
    chosen_clothes.clear()
    random.shuffle(colours)
    random.shuffle(clothing)
    for item in range(len(colours)):
        chosen_colours.append(colours[item].title())
        chosen_clothes.append(clothing[item].title())
        checklist.append(f'{colourize(colours[item].title())} {clothing[item].title()}')
    split_list(checklist) 
    return checklist

# List splitter - generate individual lists of colours and clothing from tuples
def split_list(checklist):
    split_list = []
    for i in range(len(checklist)):
        split_list.append(checklist[i].split())
        colourize(split_list[i][0])
        coloured_item = split_list[i][0] + ' ' + split_list[i][1]
        update(i, coloured_item)
    return checklist

def user_input(prompt):
    # the input function will display a message in the terminal and wait
    # for user input
    user_input = input(prompt)
    return user_input

def clear_and_prompt(user_input):
    sleep(1)
    system('clear')
    print(f"Either you've already chosen {user_input}, or it's not a valid input for your last choice!")
    print(f"Your outfit currently looks like this:")
    list_all_items()
    print()

def select(function_code, checklist):
    
    # ADD item and check for unique entries
    if function_code.lower() == "a":
        if len(checklist) > 0:
            print(f"Your outfit currently looks like this:")
            list_all_items()
            print() 
        if len(checklist) < 7:
            input_colour = user_input(f"Input a colour from this list: {colours}, or push 'X' to exit > ")
            while input_colour.title() not in colours:
                if input_colour.title() == 'X':
                    break
                clear_and_prompt(input_colour)
                input_colour = user_input(f"Please select a colour from this list: {colours} > ")
            while input_colour.title() in chosen_colours:
                clear_and_prompt(input_colour)
                input_colour = user_input(f"Please choose another item from this list: {colours}, or push 'X' to exit > ")
            if input_colour.title() != 'X':              
                input_clothing = user_input(f"Input an item of clothing from this list: {clothing}, or push 'X' to exit > ")
                while input_clothing.title() not in clothing:
                    if input_clothing.title() == 'X':
                        break
                    clear_and_prompt(input_clothing)
                    input_clothing = user_input(f"Please select an item of clothing from this list: {clothing}, or push 'X' to exit > ")
                while input_clothing.title() in chosen_clothes:
                    sleep(1)
                    clear_and_prompt(input_clothing)
                    input_clothing = user_input(f"Please choose another item from this list: {clothing} > ")
                if input_clothing.title() != 'X':
                    chosen_colours.append(input_colour.title())
                    chosen_clothes.append(input_clothing.title())
                    input_item = f'{colourize(input_colour.title())} {input_clothing.title()}' 
                    create(input_item)
        else:
            print("You've already chosen a full outfit! Take a look at it and delete some things if you want to switch it up.")
        return True

    # REMOVE item
    if function_code.lower() == "d":
        if len(checklist) > 0:
            input_item = get_input(checklist)
            chosen_colours.pop(input_item)
            chosen_clothes.pop(input_item)
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
    
running = True
while running:
    selection = user_input("""
Enter a command:
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

