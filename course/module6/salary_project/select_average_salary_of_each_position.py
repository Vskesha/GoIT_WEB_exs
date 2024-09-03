import sqlite3

from scrapy.cmdline import execute


def execute_query(sql):
    with sqlite3.connect("salary.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


if __name__ == '__main__':
    sql = """
        SELECT e.post as position, ROUND(AVG(p.total), 2) as average_salary
        FROM payments as p
        JOIN employees as e ON e.id = p.employee_id
        GROUP BY e.post
    """
    result = execute_query(sql)
    print(*result, sep="\n")