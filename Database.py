import sqlite3

# DB Design
# books ( id<primary key>, name, edition, price, course.id<foreign key>, users.username<foreign key> )
# courses ( id<primary key>, num, dept.code<foreign key>)
# users ( username<primary key> ) TODO: will probably add more to the user class


class DB:

    def __init__(self):
        pass

    # Initialize a database if there isn't one already
    @staticmethod
    def init_db():
        db_name = 'textbook.db'
        user_sql = 'CREATE TABLE  IF NOT EXISTS users  ( username VARCHAR(50) PRIMARY KEY);'
        course_sql = '''CREATE TABLE IF NOT EXISTS courses(
               id       INTEGER NOT NULL PRIMARY KEY,
               name     TEXT NOT NULL,
               dept     VARCHAR(4) NOT NULL
               );'''
        books_sql = '''CREATE TABLE  IF NOT EXISTS books  (
            id          INTEGER NOT NULL  PRIMARY KEY,
            name        TEXT NOT NULL,
            edition     INTEGER,
            course_id   INTEGER NOT NULL,
            user_name   TEXT NOT NULL,
            FOREIGN KEY(course_id) REFERENCES courses(id),
            FOREIGN KEY(user_name) REFERENCES users(username)
            );'''

        try:
            conn = sqlite3.connect(db_name)
            cur = conn.cursor()
            cur.execute(user_sql)
            cur.execute(course_sql)
            cur.execute(books_sql)
        except sqlite3.OperationalError as o_err:
            print(o_err+"err")
        except sqlite3.DatabaseError as db_err:
            print(db_err)
        finally:
            conn.close()
        pass

    pass
