import sqlite3
from datetime import datetime
from random import choice, randint

from faker import Faker

from course.module6.conspect.company_example.fill_data import prepare_data

NUMBER_COMPANIES = 3
NUMBER_EMPLOYEES = 30
NUMBER_POSTS = 5


def generate_fake_data(number_companies, number_employees, number_post) -> tuple:
    fake_companies = []
    fake_employees = []
    fake_posts = []

    fake_data = Faker("uk")

    for _ in range(number_companies):
        fake_companies.append(fake_data.company())

    for _ in range(number_employees):
        fake_employees.append(fake_data.name())

    for _ in range(number_post):
        fake_posts.append(fake_data.job())

    return fake_companies, fake_employees, fake_posts


def prepare_data(companies, employees, posts) -> tuple:
    for_companies = [(c,) for c in companies]

    for_employees = [
        (emp, choice(posts), randint(1, len(companies))) for emp in employees
    ]

    for_payments = []
    for month in range(1, 13):
        for emp in range(1, len(employees) + 1):
            payment_date = datetime(2023, month, randint(10, 20)).date()
            for_payments.append((emp, payment_date, randint(6000, 10000)))

    return for_companies, for_employees, for_payments


def insert_data_to_db(companies, employees, payments):
    with sqlite3.connect("salary.db") as con:
        cur = con.cursor()

        sql_to_companies = """
            INSERT INTO companies (company_name)
            VALUES (?)
        """
        sql_to_employees = """
            INSERT INTO employees (employee, post, company_id)
            VALUES (?, ?, ?)
        """
        sql_to_payments = """
            INSERT INTO payments (employee_id, date_of, total)
            VALUES (?, ?, ?)
        """

        cur.executemany(sql_to_companies, companies)
        cur.executemany(sql_to_employees, employees)
        cur.executemany(sql_to_payments, payments)

        con.commit()


if __name__ == "__main__":
    companies, employees, payments = prepare_data(
        *generate_fake_data(NUMBER_COMPANIES, NUMBER_EMPLOYEES, NUMBER_POSTS)
    )
    # print("\nCompanies:")
    # print(*companies, sep=";\n")
    # print("\nEmployees:")
    # print(*employees, sep=";\n")
    # print("\nPayments:")
    # print(*payments, sep=";\n")
    insert_data_to_db(companies, employees, payments)
