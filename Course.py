# this defines Course object and methods to get Course info from database
import sqlite3, traceback
DEV = True; # flag to switch between prod and dev.

class Course():

    def __init__(self, CourseID, CourseName, CourseDepartment):
        # initialize a course object
        self.ID = CourseID
        self.Name = CourseName
        self.Department = CourseDepartment

    # plus some simple getters and setters
    # omitting 'course' from method names because syntax is Course.getFoo().
    def getID(self):
        return self.ID

    def getName(self):
        return self.Name

    def getDepartment(self):
        return self.Department

    def __str__(self):
        # this lets us stringify a course's information
        return self.ID + ": " + self.Department + ", " + self.Name

# and some generic methods to pull data out of the database

def getByDepartment(Department):
    # this will run a database query and returns a list of all courses in a department
    # TODO: should this be moved to book.py?  it might make more sense to return a list of book objects...
    courselist = []
    try:
        # query for books in a department
        conn = sqlite3.connect("textbook.db")

        cursor = conn.execute("""SELECT * FROM books \
            INNER JOIN users \
            ON books.course = users.course \
            WHERE courses.department = ?""", Department)

        # build a list of courses - need to print rows in order to figure out the order the fields are returned
        for row in cursor:
            print(row)

    except sqlite3.Error as e:
        # report the error and rollback
        print('Unable to retrieve data from database.')
        # if in dev environment, print traceback
        if DEV: traceback.print_exc()
        # revert all changes
        conn.rollback()
    finally:
        #close connection
        conn.close()
        # for now, return an empty list
        return courselist
# end getByDepartment

def getByCourseID(CourseID):
    # this will run a query and return a particular course by its ID
    course = None
    try:
        # query for courses by ID
        conn = sqlite3.connect("textbook.db")

        # return a single record
        cursor = conn.execute("SELECT * FROM courses WHERE ID = ?", CourseID).fetchone()
        cID = cursor[0]
        cName = cursor[1]
        cDept = cursor[2]

        course = Course(cID,cName,cDept)
    except sqlite3.Error as e:
        # report the error and rollback
        print('Unable to retrieve data from database.')
        # if in dev environment, print traceback
        if DEV: traceback.print_exc()
        # revert all changes
        conn.rollback()
    finally:
        # close the connection
        conn.close()
        # for now, return an empty list
        return course
# end getByCourseID