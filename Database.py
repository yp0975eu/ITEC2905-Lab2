import sqlite3
import json

# DB Design
# books ( id<primary key>, name, edition, price, course.id<foreign key>, users.username<foreign key> )
# courses ( id<primary key>, course, department)
# users ( username<primary key> ) TODO: will probably add more to the user class



class DB:
    # Class variable shared by all instances of the DB class
    # https://docs.python.org/2/tutorial/classes.html#class-and-instance-variables
    # http://programmers.stackexchange.com/a/200529

    # double underscore to provide data mangling in case of
    __db_connection = None
    __db_cursor = None

    # variable starting with underscore to indicate non-public class variables
    __db_name = 'textbook.db'
    __seed_data_filename = 'books.txt'

    # To add a table, enter the name to this tuple, then create a method with
    # make_table_<table_name> that contains the table sql,
    # see make_table_users for an example
    __table_names = ('books', 'users', 'db_meta', 'course')

    def __init__(self):
        try:
            self.__db_connection = sqlite3.connect(self.__db_name)
            self.__db_cursor = self.__db_connection.cursor()

            # checks if our table inside __table_names exist, if not it creates them
            self.check_for_tables()

            # check if out tables are empty.
            if self.tables_need_data():
                self.seed_data()

        except sqlite3.Error as e:
            print("Cannot connect to database.", e)

    def check_for_tables(self):
        for table in self.__table_names:
            if not self.table_exist(table):
                try:
                    # this calls the method named: self.make_table_<table_name>
                    getattr(self, 'make_table_'+table)()
                except AttributeError as a_error:
                    print("Error making table. "
                          "Does table '{}' have a corresponding method 'make_table_{}()' ?".format(table, table))
                    print(a_error)

    def tables_need_data(self):
        #  we are only checking the books table,
        #  but in the future can check multiple tables to seed
        #  If there is are books then seed the db
        row_count = self.does_table_have_data()
        return row_count <= 0

    # returns true if table exists
    def table_exist(self, table_name):
        cur = self.__db_cursor

        # SQL from http: // stackoverflow.com / a / 8827554
        check_table = "SELECT count(*) FROM sqlite_master WHERE type='table' AND name = ?;"
        try:
            values = table_name,
            cur.execute(check_table, values)
            count = cur.rowcount
            return count == 1
        except sqlite3.OperationalError as o_err:
            print('Operational Error', o_err)
        except sqlite3.DatabaseError as db_err:
            print('Table Exists Error', db_err)

    # Returns row count
    # returns 0 if there is not data
    def does_table_have_data(self):
        cur = self.__db_cursor
        # table names cannot be parametrized arguments?
        # http://stackoverflow.com/questions/3247183/variable-table-name-in-sqlite
        sql = "SELECT count(*) FROM books;"
        try:
            # execute takes a tuple for arg2
            cur.execute(sql)
            return cur.rowcount
        except sqlite3.OperationalError as o_err:
            print("Table data check Operational Error", o_err)
        except sqlite3.DatabaseError as db_err:
            print(db_err)

    def make_table_db_meta(self):
        sql = 'CREATE TABLE IF NOT EXISTS db_meta  ( version REAL, last_update DATETIME);'
        self.make_table(sql)

    def make_table_users(self):
        sql = 'CREATE TABLE IF NOT EXISTS users  ( username VARCHAR(8) PRIMARY KEY);'
        self.make_table(sql)

    def make_table_course(self):
        sql = '''CREATE TABLE IF NOT EXISTS courses(
               course     TEXT NOT NULL,
               department     VARCHAR(4) NOT NULL,
               PRIMARY KEY (course, department)
               );'''
        self.make_table(sql)

    def make_table_books(self):
        # id removed because sqlite3 makes an id automatically
        # id          INTEGER NOT NULL PRIMARY KEY,
        sql = '''CREATE TABLE  IF NOT EXISTS books  (
            title       TEXT NOT NULL,
            author      TEXT NOT NULL,
            edition     INTEGER,
            course      INTEGER NOT NULL,
            username    TEXT NOT NULL,
            isbn        TEXT NOT NULL,
            price       REAL NOT NULL,
            status      REAL NOT NULL,
            FOREIGN KEY(course) REFERENCES courses(course),
            FOREIGN KEY(username) REFERENCES users(username)
            );'''
        self.make_table(sql)

    def make_table(self, sql):
        try:
            cur = self.__db_cursor
            cur.execute(sql)
        except sqlite3.OperationalError as o_err:
            print("Error Making Table", o_err)
        except sqlite3.DatabaseError as db_err:
            print("Database Error while making table", db_err)

    def get_test_data_from_file(self):
        # read example data from file and insert it into database
        filename = self.__seed_data_filename
        with open(filename, 'r') as file_obj:
            raw_json = file_obj.read()
        file_obj.close()
        books_data = json.loads(raw_json)
        return books_data

    def seed_data(self):
        books_json = self.get_test_data_from_file()
        # for each book insert into database
        # insert course
        # insert users
        # insert books
        for entry in books_json:
            course_row_id = self.insert_course(entry['course'], entry['department'])
            self.insert_user(entry['username'])
            self.insert_book((entry['title'], entry['author'], entry['edition'], course_row_id, entry['username'], entry['isbn'],
                              entry['price'], entry['status']))

    def insert_course(self, course, department):
        insert_sql = 'INSERT INTO courses VALUES(?, ?);'
        cursor = self.__db_cursor
        conn = self.__db_connection
        try:
            cursor.execute(insert_sql, (course, department))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.DatabaseError as db_err:
            row_id = self.select_course(course, department)
            print("WARNING: Insert Course Failed. Course already exists, use ROWID: {} for ({}-{})".format(row_id, department, course))
            return row_id

    def select_course(self, course, department):
        insert_sql = 'SELECT ROWID, course, department FROM courses WHERE course=? and department=?;'
        cursor = self.__db_cursor
        try:
            cursor.execute(insert_sql, (course, department))
            # index 0 is the row ID
            return cursor.fetchone()[0]
        except sqlite3.DatabaseError as db_err:
            print(db_err, "Course Selection Failed: (" + course + " : " + department + ")")

    def insert_user(self, username):
        insert_sql = 'INSERT INTO users VALUES( ? );'
        cursor = self.__db_cursor
        conn = self.__db_connection
        try:
            # Need comma at end of username to make a single value a tuple, otherwise it is just a grouped expression
            # http://stackoverflow.com/a/16856730
            cursor.execute(insert_sql, (username,))
            conn.commit()
        except sqlite3.DatabaseError as db_err:
            print("WARNING: User Insertion Failed for {} user already exists".format(username))

    # parameter username is a string,
    # returns a row
    # row['ROWID','username']
    def select_user(self, username):
        insert_sql = 'SELECT ROWID, username FROM users WHERE username=?;'
        cursor = self.__db_cursor
        try:
            cursor.execute(insert_sql, (username, ))
            # index 0 is the row ID
            return cursor.fetchone()[0]
        except sqlite3.DatabaseError as db_err:
            print(db_err, "Values: (" + username + ")")

    def insert_book(self, values):
        insert_sql = 'INSERT INTO books VALUES(?, ?, ?, ?, ?, ?, ?, ? );'
        cursor = self.__db_cursor
        conn = self.__db_connection
        try:
            # Need comma at end of username to make a single value a tuple, otherwise it is just a grouped expression
            # http://stackoverflow.com/a/16856730
            cursor.execute(insert_sql, values)
            conn.commit()
            return cursor.lastrowid
        except sqlite3.DatabaseError as db_err:
            print(db_err, "Value:", values, ")")
            return cursor.lastrowid
            # username is a string,

    # returns a list of rows
    # takes a field to search and a value to search for
    # for example 'title', 'Microsoft'
    def select_book(self, field, value):
        sql = 'SELECT * FROM books WHERE ?=%?%;'
        cursor = self.__db_cursor
        try:
            cursor.execute(sql, (field, value,))
            # index 0 is the row ID
            return cursor.fetchall()
        except sqlite3.DatabaseError as db_err:
            print(db_err, "Values: (" + field + " " + value + ")")


