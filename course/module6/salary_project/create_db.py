import sqlite3


def create_db():
    with open("salary.sql", "r", encoding="utf-8") as f:
        sql = f.read()

    with sqlite3.connect("salary.db") as con:
        cur = con.cursor()
        cur.executescript(sql)


if __name__ == "__main__":
    create_db()
