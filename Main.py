from Database import DB
from Search import Search
# this one, we want to explicitly call Validator so we signal that's what we're doing.
import Validator

# initialize DB object, seeding database if necessary.
db = DB()
search = Search(db)
# some static values for the menu options so we don't have to recode a bunch of stuff if we change the numbers

OPTION_BYCOURSENUMBER = '1'
OPTION_BYTITLE = '2'
OPTION_BYISBN = '3'
OPTION_LISTDEPARTMENTS = '4'
OPTION_BYDEPARTMENT = '5'
OPTION_BYCOURSEID = '6'
OPTION_QUIT = '7'

# FUNCTIONS USED BY MAIN METHOD


def showmenu():
    # shows the option menu at launch
    menu = ['Select an option:',
            'Search by course number',
            'Search by book title',
            'Search by ISBN',
            'List departments',
            'Search by department',
            'Quit']
    count = 0
    for option in menu:
        if count == 0:
            print(option)
        else:
            print("{}.\t{}".format(count, option))
        count += 1


def print_results(results):
    for row in results:
        print(row)

def do_menu():
    # calls showmenu and acts on the choice made
    # TODO build objects and methods to handle the user's selections.
    while True:
        showmenu()
        userchoice = input("> ")
        # act on choice
        if userchoice == OPTION_QUIT:
            # quit the program
            exit()
            break   # just being cautious so we don't leave an endless loop lingering.
        elif userchoice == OPTION_BYCOURSENUMBER:
            course_number = input("Enter course number: ")
            # TODO Validate course numbers
            # if Course.isValid(course_number)
            results = search.by_course_num(course_number)
            if results:
                print_results(results)
            else:
                print("No matches, try a department search.")
        elif userchoice == OPTION_BYTITLE:
            title = input("Enter book title: ")
            results = search.by_book_title(title)
            if results:
                print_results(results)
            else:
                print("No matches, try a department search.")
            print("This option to search by book title has not been implemented.")
        elif userchoice == OPTION_BYISBN:
            searchByIsbn()
        elif userchoice == OPTION_BYDEPARTMENT:
            dept = input("Enter department ID ")
            results = search.by_department(dept)
            if results:
                print_results(results)
            else:
                print("No matches")
            print("This option to search by course department has not been implemented.")
        elif userchoice == OPTION_LISTDEPARTMENTS:
            results = search.list_departments()
            if results:
                print_results(results)
            else:
                print("No departments to choose from , something is fishy :/")
        else:
            print("You have not made a valid selection.  Please try again.")


def searchByIsbn():
    print("This option to search by book ISBN has not been fully implemented.")
    isbn = input("Please enter the ISBN number you wish to search for.  Leave out the dashes and spaces.")
    # pull out dashes and spaces if they're input anyway
    isbn = isbn.replace("-","").replace(" ", "")
    # TODO: finish implementation of search by ISBN.
    if Validator.isValidISBN(isbn):
        print("You have entered a valid ISBN")
    else:
        print("You have not entered a valid ISBN")


# BODY OF CODE
print("Welcome to the used book browser!\n")
do_menu()
