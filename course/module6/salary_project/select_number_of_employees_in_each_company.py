from select_average_salary_of_each_position import execute_query


if __name__ == "__main__":
    sql = """
        SELECT c.company_name as company, COUNT(*)
        FROM companies as c
        JOIN employees as e ON e.company_id = c.id
        GROUP BY c.company_name
    """

    result = execute_query(sql)
    print(*result, sep="\n")
