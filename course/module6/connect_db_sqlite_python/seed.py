from sqlite3 import Error

from connect import database, create_connection


def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """

    sql = """
        INSERT INTO projects (name, begin_date, end_date) 
        VALUES (?, ?, ?)
        """

    cur = conn.cursor()
    try:
        cur.execute(sql, project)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

    return cur.lastrowid


def create_task(conn, task):
    """
    Create a new task into the tasks table
    :param conn:
    :param task:
    :return: task id
    """

    sql = """
        INSERT INTO tasks (name, priority, project_id, status, begin_date, end_date) 
        VALUES (?, ?, ?, ?, ?, ?)
        """

    cur = conn.cursor()
    try:
        cur.execute(sql, task)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

    return cur.lastrowid


if __name__ == "__main__":
    with create_connection(database) as conn:
        # create new project
        project = ("Cool App with SQLite & Python", "2022-01-01", "2022-01-30")
        project_id = create_project(conn, project)
        print(project_id)

        # create new tasks
        task_1 = (
            "Analyze the requirements of the app",
            1,
            project_id,
            True,
            "2022-01-01",
            "2022-01-02",
        )
        task_2 = (
            "Confirm with user about the top requirements",
            1,
            project_id,
            False,
            "2022-01-03",
            "2022-01-05",
        )

        print(create_task(conn, task_1))
        print(create_task(conn, task_2))
