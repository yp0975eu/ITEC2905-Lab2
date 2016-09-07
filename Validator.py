'''
A bunch of validators for our various data inputs
'''
# COURSE validation
def isValidCourseNum(num):
    # need to validate it's 4 digits long.
    # stringify num in case it has leading zeroes
    tocheck = str(num).zfill(4)  # http://www.tutorialspoint.com/python/string_zfill.htm
    if len(tocheck) != 4:
        return False
    for c in tocheck:
        if not (ord(c) > 47 and ord(c) < 58):
            return False
    return True

def isValidDepartment(dept):
    # need to validate it's exactly 4 characters long.
    if str(dept).isalpha():
        return len(dept) == 4
    return False

# BOOK validation
def isValidISBN(isbn):
    tocheck = str(isbn)
    return tocheck.isdigit() and (len(tocheck) == 10 or len(tocheck) == 13)

def isValidPrice(price):
    # first verify we don't have more than 2 digits after the decimal
    decimal = str(price).split(".")
    if len(decimal) == 2 and len(decimal[1]) <= 2:
        # then verify it parses as a float
        # http://stackoverflow.com/questions/16290373/validate-float-data-type-python#16290419
        try:
            float(price)
        except ValueError:
            return False
        else:
            return True
    else:
        return False
