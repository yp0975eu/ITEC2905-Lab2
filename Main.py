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

# TODO build menu display & selection handler

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
    # prints the menu and acts on the choice made
    while True:
        showmenu()
        userchoice = raw_input("> ")
        # act on choice
        if userchoice == OPTION_QUIT:
            # quit the program
            exit()
            break   # just being cautious so we don't leave an endless loop lingering.
        else:
            print("This option has not been implemented.")

# BODY OF CODE
do_menu()