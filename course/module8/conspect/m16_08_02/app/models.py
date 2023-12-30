from mongoengine import connect, Document, StringField, BooleanField


connect(
    db="web16",
    host="mongodb+srv://***:***@***.fmxueib.mongodb.net/?retryWrites=true&w=majority",
)


class Task(Document):
    status = BooleanField(default=False)
    consumer = StringField(max_length=150)
