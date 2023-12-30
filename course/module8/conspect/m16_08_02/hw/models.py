from mongoengine import connect, Document, StringField, ListField, ReferenceField, CASCADE

connect(
    db="vs_hw8",
    host="mongodb+srv://***:***@***.fmxueib.mongodb.net/?retryWrites=true&w=majority",
)


class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=150)
    description = StringField()
    meta = {'collection': 'authors'}


class Quote(Document):
    author = ReferenceField(Author, required=True, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    quote = StringField()
    meta = {'collection': 'quotes'}
