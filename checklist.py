checklist = list()

def create(item):
  checklist.append(item)

def read(index):
  return checklist[index]

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
  print("* {}".format(checklist[index]))

running = True

def select(function_code):
    if function_code == ("C" or "c"):
        print('Function code: C')
        input_item = user_input("Input Item: ")
        create(input_item)

    elif function_code == ("R" or "r"):
        print('Function Code R')
        item_index = int(user_input("Index Number? "))
        if item_index > (len(checklist))-1:
            print("Invalid Index")
            return True
        read(item_index)

    elif function_code == ("P" or "p"):
        print('Function Code P')
        list_all_items()

    elif function_code == ("Q" or "q"):
        print(running)
        return False

    else:
        print("unknown option!")
    return True



def user_input(prompt):
    user_input = raw_input(prompt)
    return user_input



while running:
    selection = user_input("Press C to add to list, R to read from list, P to display list ")
    print(selection)

    if selection == ("Q" or "q"):
        break

    runnning = select(selection)
    print(running)


    # print(running)






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
