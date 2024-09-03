from select_average_salary_of_each_position import execute_query


if __name__ == '__main__':
    sql = """
        SELECT c.company_name, e.employee, e.post as position, p.date_of, p.total
        FROM companies as c
        LEFT JOIN employees as e ON e.company_id = c.id
        LEFT JOIN payments as p ON p.employee_id = e.id
        WHERE p.total > 5000 AND p.date_of BETWEEN '2023-07-01' AND '2023-07-31'
    """

    result = execute_query(sql)
    print(*result, sep="\n")
