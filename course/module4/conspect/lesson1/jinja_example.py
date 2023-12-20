from jinja2 import Template

if __name__ == '__main__':
    name = 'Bill'
    age = 20

    tm = Template("My name is {{ name }} and I am {{ age }}")
    msg = tm.render(name=name, age=age)

    print(msg)
