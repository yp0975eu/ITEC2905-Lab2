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
    courselist = []
    try:
        # query for books in a department
        conn = sqlite3.connect("textbook.db")
        # need to add wildcards to whatever user has input so the like syntax works
        cursor = conn.execute("SELECT * FROM courses WHERE department LIKE ?;", ("%" + Department + "%",))

        # build a list of courses - need to print rows in order to figure out the order the fields are returned
        for row in cursor:
            cName = row[0]
            cDept = row[1]
            cID = cDept + cName
            course = Course(cID,cName,cDept)
            courselist.append(course)

    except sqlite3.Error as e:
        # report the error and rollback
        print('Unable to retrieve data from database.')
        # if in dev environment, print traceback
        if DEV: traceback.print_exc()
        # revert all changes
        courselist = []
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

        # return a single record - there should only be one result anyway
        cursor = conn.execute("SELECT * FROM courses WHERE course = ?;", (CourseID,)).fetchone()

        # grab the data and create a course object
        cName = cursor[0]
        cDept = cursor[1]
        cID = cDept + cName
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
        # return whatever we find - either a course object or None
        return course
# end getByCourseID