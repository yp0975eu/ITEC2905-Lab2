from Database import DB
from Search import Search
# this one, we want to explicitly call Validator so we signal that's what we're doing.
import Validator, Book, re

# initialize DB object, seeding database if necessary.
db = DB()
search = Search(db)
# some static values for the menu options so we don't have to recode a bunch of stuff if we change the numbers

OPTION_BYCOURSENUMBER = '1'
OPTION_BYTITLE = '2'
OPTION_BYISBN = '3'
OPTION_LISTDEPARTMENTS = '4'
OPTION_BYDEPARTMENT = '5'
OPTION_ADD = '6'
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
            'Add a book',
            'Quit']
    count = 0
    for option in menu:
        if count == 0:
            print(option)
        else:
            print("{}.\t{}".format(count, option))
        count += 1


def print_results(results):
    if results == None: print("No results found.  Try a different search.")
    else:
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
            searchByCourseNumber()
        elif userchoice == OPTION_BYTITLE:
            searchByTitle()
        elif userchoice == OPTION_BYISBN:
            searchByIsbn()
        elif userchoice == OPTION_BYDEPARTMENT:
            searchByDepartmentID()
        elif userchoice == OPTION_LISTDEPARTMENTS:
            listAllDepartments()
        elif userchoice == OPTION_ADD:
            # add a new book
            addNewBook()
        else:
            print("You have not made a valid selection.  Please try again.")


def listAllDepartments():
    results = search.list_departments()
    if results:
        print_results(results)
    else:
        print("No departments to choose from , something is fishy :/")


def searchByDepartmentID():
    dept = input("Enter department ID ")
    results = search.by_department(dept)
    print_results(results)


def searchByTitle():
    title = input("Enter book title: ")
    results = search.by_book_title(title)
    print_results(results)


def searchByCourseNumber():
    course_number = input("Enter course number: ")
    # Validate course numbers
    while not Validator.isValidCourseNum(course_number):
        course_number = input("A valid course number must have 4 digits.")
    results = search.by_course_num(course_number)
    print_results(results)
# end searchByCourseNumber

def addNewBook():
    print("Enter a book title")
    title = input("> ")
    while len(title) < 4:
        print("Title must be at least 4 characters.\nEnter a book title")
        title = input("> ")
    print("Enter a author")
    author = input("> ")
    while len(author) < 4:
        print("Author must be at least 4 characters.\nEnter author")
        author = input("> ")
    print("Enter edition")
    edition = input("> ")
    while not edition.isnumeric():
        print("Edition cannot only be numbers.\nEnter edition")
        edition = input("> ")
    print("Enter course number")
    course_number = input("> ")
    while not Validator.isValidCourseNum(course_number):
        print("Course number must be 4 numbers")
        course_number = input("> ")
    print("Enter Department")
    department = input("> ")
    while not Validator.isValidDepartment(department):
        print("Department must be 4 letters")
        department = input("> ")
    print("Enter star ID")
    star_id = input("> ")
    # TODO: fix regex, it's not accepting "tk0654wm" which is Anna's ID.
    # while not re.match("[A-Za-z0-9]{7}", star_id) is None or len(star_id) > 7:
    while not (star_id.isalnum() and len(star_id) == 8):
        print("Star ID must be a combination of 8 letters and numbers")
        star_id = input("> ")
    print("Enter isbn without dashes or spaces")
    isbn = input("> ")
    # strip out dashes and spaces
    isbn = isbn.replace("-","").replace(" ", "")
    while not Validator.isValidISBN(isbn):
        print("ISBN must be 10 or 13 numbers")
        isbn = input("> ").replace("-","").replace(" ", "")
    print("Enter price")
    price = input(">")
    while not Validator.isValidPrice(price):
        print("Price must be a decimal number")
        price = input("> ")
    status = 'available'
    book = Book.Book(title, author, edition, course_number, department, star_id, isbn, price, status)
    # DB.newEntry(Book)
    book.insert()
    print("Your book has been successfully inserted.\n" + str(book))
# end addNewBook

def searchByIsbn():
    # prompt for an isbn, validate it, and print search results of a book is found.
    print("Please enter the ISBN number you wish to search for.  Leave out the dashes and spaces.")
    isbn = input("> ")
    # pull out dashes and spaces if they're input anyway
    isbn = isbn.replace("-","").replace(" ", "")
    # TODO: finish implementation of search by ISBN.
    if Validator.isValidISBN(isbn):
        # print("You have entered a valid ISBN")
        results = search.by_book_isbn(isbn)
        if results:
            print_results(results)
        else:
            print("No matches found. Try another search.")
    else:
        print("You have not entered a valid ISBN.")
# end searchByIsbn


# BODY OF CODE
print("Welcome to the used book browser!\n")
do_menu()
