# empty main method to verify push works -- amdudda

# starting to create main menu
# will push this new comment and then Brandon will demo merging for Marian

# some static values for the menu options so we don't have to recode a bunch of stuff if we change the numbers
OPTION_BYCOURSENAME = '1'
OPTION_BYTITLE = '2'
OPTION_BYISBN = '3'
OPTION_BYDEPARTMENT = '4'
OPTION_BYCOURSEID = '5'
OPTION_QUIT = '6'

# FUNCTIONS USED BY MAIN METHOD

def showmenu():
    # shows the option menu at launch
    menu = "Select an option:\n"
    menu += "1.\t Search by course name\n" + \
           "2.\t Search by book title\n" + \
            "3.\t Search by ISBN\n" + \
            "4.\t Search by course department\n" + \
            "5.\t Search by course ID\n" + \
            "6.\t Quit\n"
    print(menu)

def do_menu():
    # calls showmenu and acts on the choice made
    # TODO build objects and methods to handle the user's selections.
    while True:
        showmenu()
        userchoice = raw_input("> ")
        # act on choice
        if userchoice == OPTION_QUIT:
            # quit the program
            exit()
            break   # just being cautious so we don't leave an endless loop lingering.
        elif userchoice == OPTION_BYCOURSENAME:
            print("This option to search by course name has not been implemented.")
        elif userchoice == OPTION_BYTITLE:
            print("This option to search by book title has not been implemented.")
        elif userchoice == OPTION_BYISBN:
            print("This option to search by book ISBN has not been implemented.")
        elif userchoice == OPTION_BYDEPARTMENT:
            print("This option to search by course department has not been implemented.")
        elif userchoice == OPTION_BYCOURSEID:
            print("This option to search by course ID has not been implemented.")
        else:
            print("You have not made a valid selection.  Pleae try again.")

# BODY OF CODE
print("Welcome to the used book browser!\n")
do_menu()