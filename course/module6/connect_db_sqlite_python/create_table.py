from sqlite3 import Error

from connect import create_connection, database


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


if __name__ == '__main__':
    sql_create_projects_table = """
    CREATE TABLE IF NOT EXISTS projects (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      begin_date TEXT,
      end_date TEXT
    );
    """

    sql_create_tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      priority INTEGER,
      project_id INTEGER NOT NULL,
      status BOOLEAN DEFAULT FALSE,
      begin_date TEXT NOT NULL,
      end_date TEXT NOT NULL,
      FOREIGN KEY (project_id) REFERENCES projects (id)
    );
    """

    with create_connection(database) as conn:
        if conn is not None:
            # create projects table
            create_table(conn, sql_create_projects_table)
            # create tasks table
            create_table(conn, sql_create_tasks_table)
        else:
            print("Error! Cannot create the database connection.")