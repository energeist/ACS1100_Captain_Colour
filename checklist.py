checklist = []

# checklist.append('Blue')
# print(checklist)
# checklist.append('Orange')
# print(checklist)

#  CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

# checklist = ['Blue', 'Orange']
# checklist[1] = 'Cats'
# print(checklist)

# UPDATE
def update(index, item):
    checklist[index] = item

# checklist.pop(1)
# print(checklist)

# DESTROY
def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print(f'{str(index)} {list_item}')
        index += 1

def mark_completed():
    index = 0
    for list_item in checklist:
        checklist[index] = '√ ' + list_item
        print(checklist[index])
        index += 1

def user_input(prompt):
    # the input function will display a message in the terminal and wait
    # for user input
    user_input = input(prompt)
    return user_input

def select(function_code):
    # create item
    if function_code.lower() == "c":
        input_item = user_input("Input item > ")
        create(input_item)
        return True

    # read item      
    elif function_code.lower() == "r":
        item_index = int(user_input("Index Number? > "))
        while item_index >= len(checklist):
            item_index = int(input(f"Not a valid index number, please enter a number from 0 - {len(checklist) -1} > "))
        print(f"{item_index} {read(item_index)}")
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
    select("R")
    list_all_items()

# test()

running = True
while running:
    selection = user_input("Press C to add to list, R to Read from list, P to display list or Q to quit > ")
    running = select(selection)