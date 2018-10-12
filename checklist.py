
checklist = list()

def create(item):
    checklist.append(item)
    list_all_items()

def read(index):
    return checklist[int(index)]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    checklist[index] = "DONE: " + checklist[index]

def select(function_code):
    # Create item
    if function_code == "C" or "c":
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    elif function_code == "R" or "r":
            item_index = user_input("Index Number? ")
            # Remember that item_index must actually exist or our program will crash.
            print(read(item_index))

        # Print all items
    elif function_code == "P" or "p":
            list_all_items()

        # Stop our loop
    elif function_code == "Q" or "q":
            return False

        # Update
    elif function_code == "U":
        item_index = user_input("Index Number: ")
        input_item = user_input("Input item: ")
        update(item_index, input_item)

    # Catch all
    else:
        print("Unknown Option")

    return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

running = True
# print("running is {}".format(running))
while running:
    selection = user_input(
        "Press C to add to list, U to update, R to Read items, P to display, Q to quit")
    running = select(selection)



def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))

    list_all_items()

    mark_completed(0)
        # Call your new function with the appropriate value
    select("C")
        # View the results
    list_all_items()
        # Call function with new value
    select("R")
        # View results
    list_all_items()
        # Continue until all code is run
    user_input("What is user input")
