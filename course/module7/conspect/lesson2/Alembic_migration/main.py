from sqlalchemy import select

from connect_db import session
from models import Note, Tag, Record, note_m2m_tag

if __name__ == "__main__":
    stmt = (
        select(
            Note.id, Note.name, Record.description, Record.done, Tag.name.label("tag")
        )
        .join(Record)
        .join(note_m2m_tag)
        .join(Tag)
        .filter(Tag.name == "food")
    )
    print(stmt)
    print()
    q = session.execute(stmt).mappings().all()
    for row in q:
        print(row)
