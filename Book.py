import sqlite3,traceback
DEV = True
# test merge to master

class Book():
    # Create a Book object
    def __init__(self, bookID, title, author, edition, course, username, ISBN, price, status):
        # initialize a Book object
        self.ID = bookID
        self.title = title
        self.author = author
        self.edition = edition
        self.courseNum = course
        self.username = username
        self.isbn = ISBN
        self.price = price
        self.status = status

    # some getters
    def get_courseID(self):
        return self.courseID

    def get_title(self):
        return self.title

    def getISBN(self):
        return self.ISBN

    # some setters
    def setCourseNum(self,ID):
        self.courseNum = ID

    def setTitle(self,title):
        self.title = title

    def setAuthor(self,auth):
        self.author = auth

    def setPrice(self,price):
        self.price = price

    def setStatus(self,status):
        self.status = status

    def setSold(self):
        # a quick'n'easy way to set a book as having been sold
        self.status = True

    # to check if Book sold and not availble
    # right way to code
    def isSold(self):
        return self.status

    # to add new Book to database
    def insert(self):
        qryString = "INSERT INTO books VALUES (?,?,?,?,?,?,?,?);"
        values = (self.title,
            self.author,
            self.edition,
            self.courseNum,
            self.username,
            self.isbn,
            self.price,
            self.status)
        try:
            conn = sqlite3.connect("textbook.db")
            conn.execute(qryString, values)
            conn.commit()
        except sqlite3.Error as e:
            # report an error and roll back the changes
            print("Unable to insert record into books table: " + str(self))
            if DEV: traceback.print_exc()
            conn.rollback()
        finally:
            conn.close()
    # end insert

    def update(self,field,value):
        # updates the value of a field for a given book
        qryString = "UPDATE books SET " + field + " = ? WHERE id = " + self.ID
        try:
            conn = sqlite3.connect("textbook.db")
            conn.execute(qryString, value)
            conn.commit()
        except sqlite3.Error as e:
            # report an error and roll back the changes
            print("Unable to update record in books table: " + str(self))
            if DEV: traceback.print_exc()
            conn.rollback()
        finally:
            conn.close()
    # end update

    def __str__(self):
        # this lets us stringify a Book's information
        return self.ID + ": " + self.title + ", " + self.edition + ", " \
               + self.author+ ", " + self.courseNum + ", " + self.ISBN + ", " + self.price
# end Book


