class book():


 def __init__(self, bookID, title, edition, author, ISBN, price, coursID, false=None):
    # initialize a course object
    self.ID = bookID
    self.Title = title
    self.edition = edition
    self.author = author
    self.isbn = ISBN
    self.price = price
    self.courseID = coursID
    self.soldout = false
# to check if book sold out and not availble  but I don't know  if it can work out
    # right way to code
    def sold_out(self):
        price(self.soldout)
        return self.soldout
# to add book
def addbook(self, title, edition, author, ISBN, price):
    add_book = book(title, edition, author, ISBN, price)
#
    def get_courseID(self):
        return self.courseID

    def get_title(self):
        return self.title

    def getISBN(self):
        return self.ISBN


def __str__(self):
    # this lets us stringify a book's information
    return self.ID + ": " + self.title + ", " + self.edition + ", " \
           + self.author + ", " + self.ISBN + ", " + self.price
