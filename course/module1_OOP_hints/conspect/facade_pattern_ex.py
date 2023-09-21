class UsersSystem:

    @staticmethod
    def get_users() -> list:
        users = [
            {
                "name": "Allen Raymond",
                "email": "nulla.ante@vestibul.co.uk",
                "gender": "male",
            },
            {
                "name": "Chaim Lewis",
                "email": "dui.in@egetlacus.ca",
                "gender": "male",
            },
            {
                "name": "Kennedy Lane",
                "email": "mattis.Cras@nonenimMauris.net",
                "gender": "female",
            },
            {
                "name": "Wylie Pope",
                "email": "est@utquamvel.net",
                "gender": "female",
            },
        ]
        return users

    @staticmethod
    def separate_users(users: list[dict[str, str]]) -> tuple:
        male, female = [], []
        for person in users:
            if person.get('gender', None) == 'male':
                male.append(person)
            else:
                female.append(person)
        return male, female


class EmailSystem:

    @staticmethod
    def get_text_email(gender) -> str:
        text = 'Default text'
        if gender == 'male':
            text = 'Male text email'
        elif gender == 'female':
            text = 'Female text email'
        return text

    @staticmethod
    def send_email(users: list[dict[str, str]], text: str) -> str:
        for person in users:
            print(f'Send {person.get("name")} email: {text}')
        return 'Done'


class FacadeNewsletter:
    def __init__(self, users_system: UsersSystem, email_system: EmailSystem) -> None:
        self._users_system = users_system
        self._email_system = email_system

    def sending(self) -> str:
        users = self._users_system.get_users()
        male, female = self._users_system.separate_users(users)
        text_for_male = self._email_system.get_text_email('male')
        text_for_female = self._email_system.get_text_email('female')
        result_male_sending = self._email_system.send_email(male, text_for_male)
        print(result_male_sending)
        result_female_sending = self._email_system.send_email(female, text_for_female)
        print(result_female_sending)
        return 'Done Sending'


def client_code(newsletter: FacadeNewsletter) -> None:
    print(newsletter.sending(), end='')


if __name__ == '__main__':
    facade = FacadeNewsletter(UsersSystem(), EmailSystem())
    client_code(facade)
