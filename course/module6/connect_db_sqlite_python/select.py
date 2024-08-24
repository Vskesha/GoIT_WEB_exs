from sqlite3 import Error

from connect import database, create_connection


def select_projects(conn):
    """
    Query all rows in the projects table
    :param conn:
    :return:
    """
    rows = None
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM projects;")
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()

    return rows


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn:
    :return:
    """
    rows = None
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM tasks;")
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()

    return rows


def select_task_by_status(conn, status):
    """
    Query tasks by priority
    :param conn:
    :param status:
    :return:
    """

    rows = None
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM tasks WHERE status = ?", (status, ))
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()

    return rows


if __name__ == '__main__':
    with create_connection(database) as conn:
        print("All projects:")
        projects = select_projects(conn)
        print(*projects, sep="\n")

        print("All tasks:")
        tasks = select_all_tasks(conn)
        print(*tasks, sep="\n")

        print("Tasks with status = True:")
        true_tasks = select_task_by_status(conn, True)
        print(*true_tasks, sep="\n")
