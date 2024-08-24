from sqlite3 import Error

from connect import database, create_connection


def delete_all_data(conn):
    """
    Drops all records in all tables
    :param conn:
    :return:
    """

    get_tables_sql = "SELECT name FROM sqlite_master WHERE type='table';"

    cur = conn.cursor()
    try:
        cur.execute(get_tables_sql)
        tables = cur.fetchall()
        for table in tables:
            cur.execute(f"DELETE FROM {table[0]};")
            print(f"Table \"{table[0]}\" cleared.")
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()


if __name__ == '__main__':
    with create_connection(database) as conn:
        delete_all_data(conn)
    print("All data has been deleted!")
