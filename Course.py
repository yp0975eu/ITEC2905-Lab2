# this defines Course object and methods to get Course info from database

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

# and some generic methods to pull data out of the database

def getByDepartment(Department):
    # this will run a database query and returns a list of all courses in a department
    courselist = []
    # for now, return an empty list
    return courselist


def getByCourseID(CourseID):
    # this will run a query and return a list of courses with matching IDs
    courselist = []
    # for now, return an empty list
    return courselist