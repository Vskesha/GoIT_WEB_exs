from jinja2 import Template

if __name__ == '__main__':
    persons = [
        {'name': 'Andrej', 'age': 34},
        {'name': 'Mark', 'age': 17},
        {'name': 'Thomas', 'age': 44},
        {'name': 'Lucy', 'age': 14},
        {'name': 'Robert', 'age': 23},
        {'name': 'Dragomir', 'age': 54}
    ]

    tm = Template("{% for person in persons -%}"
                  "{{ person.name }} {{ person.age }}\n"
                  "{% endfor %}")

    print(tm.render(persons=persons))
