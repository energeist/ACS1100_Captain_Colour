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

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple sox")
    destroy(1)

    print(read(0))

test()    