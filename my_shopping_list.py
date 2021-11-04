import os

shopping_list = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_help():
    print("What shall we get at the store today?")
    print("""
    Enter 'DONE' to stop adding items
    Enter 'REMOVE' to remove an item
    Enter 'HELP' for this help
    Enter 'SHOW' to show your list
    """)


def add_to_list(item):
    show_list()
    if shopping_list:
        position = input("""
        Where should we add {}
        Press ENTER to add to the end of the list
        """.format(item))
    else:
        position = 0
    try:
        abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.append(new_item)
    show_list()


def show_list():
    clear_screen()
    print("Here's your list:")

    for index, item in enumerate(shopping_list, start=1):
        print("{}. {}".format(index, item))

    print("-" * 17)


def remove_from_list():
    show_list()
    what_to_remove = input("""
        Which item do you want to remove?
        Type 'CANCEL' to cancel
        > """)
    if what_to_remove.upper() == 'CANCEL' or what_to_remove.upper() == 'QUIT':
        pass
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass


show_help()

while True:
    new_item = input("> ")
    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break
    if new_item.upper() == 'CANCEL' or new_item.upper() == 'EXIT':
        break
    elif new_item.upper() == 'REMOVE' or new_item.upper() == 'DELETE':
        remove_from_list()
    elif new_item.upper() == 'HELP' or new_item.upper() == 'HELP ME':
        show_help()
        continue
    elif new_item.upper() == 'SHOW' or new_item.upper() == 'SHOW LIST':
        show_list()
        continue
    else:
        add_to_list(new_item)
