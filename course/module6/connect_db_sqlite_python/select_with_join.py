from sqlite3 import DatabaseError

from connect import create_connection, database


def select_projects(conn):
    """
    Query all rows in the projects table with its tasks
    :param conn: the Connection object
    :return: rows projects or None
    """

    rows = None
    sql = """
        SELECT *
        FROM projects as p
        JOIN tasks as t ON t.project_id = p.id;
    """
    cur = conn.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchall()
    except DatabaseError as err:
        print(err)
    finally:
        cur.close()

    return rows


if __name__ == "__main__":
    with create_connection(database) as conn:
        print("Projects:")
        projects = select_projects(conn)
        print(*projects)
