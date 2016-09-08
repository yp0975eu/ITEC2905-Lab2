class Search:
    __DB = None

    def __init__(self, db):
        self.__DB = db
        pass

    def by_course_num(self, course_num):
        sql = "SELECT * FROM books WHERE course = (SELECT ROWID FROM courses WHERE course =?);"
        params = (course_num,)
        result = self.__DB.select(sql, params)
        if not result:
            return True
        return result

    def list_departments(self):
        sql = "SELECT DISTINCT department FROM courses"
        result = self.__DB.list(sql)
        return result

    def by_department(self, department):

        sql = "SELECT * FROM books INNER JOIN courses WHERE books.course=courses.ROWID AND department = ?;"
        params = (department,)
        result = self.__DB.select(sql, params)
        return result

    def by_book_title(self, book_title):
        sql = "SELECT ROWID, * FROM books WHERE title LIKE ?;"
        params = ('%'+book_title+'%',)
        result = self.__DB.select(sql, params)
        return result

    def by_book_isbn(self, isbn):
        sql = "SELECT * FROM books WHERE isbn = ?;"
        params = (isbn,)
        result = self.__DB.select(sql, params)
        return result

