class PersonInfo:
    def value_of(self):
        raise NotImplementedError


class PersonPhone(PersonInfo):

    def __init__(self, phone: str, operator_code: str):
        self.phone = phone
        self.operator_code = operator_code

    def value_of(self):
        return f"+38({self.operator_code}){self.phone}"


class PersonAddress(PersonInfo):

    def __init__(self, zip: str, city: str, street: str):
        self.zip = zip
        self.city = city
        self.street = street

    def value_of(self):
        return f"{self.zip}, {self.city}, {self.street}"


class Person:
    def __init__(self, name: str, phone: PersonInfo, address: PersonInfo):
        self.name = name
        self.phone = phone
        self.address = address

    def get_phone_number(self):
        return f"{self.name}: {self.phone.value_of()}"

    def get_address(self):
        return f"{self.name}: {self.address.value_of()}"


if __name__ == '__main__':

    phone_number = PersonPhone('4865345', '067')
    person_address = PersonAddress('12345', 'Ternopil', 'Shevchenko')

    person = Person("Alexander", phone_number, person_address)
    print(person.get_phone_number())
    print(person.get_address())