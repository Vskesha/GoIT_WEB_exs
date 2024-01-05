import pathlib
import time
from typing import Optional

from fastapi import FastAPI, Path, Query, Depends, HTTPException, status, Request, File, Form, UploadFile
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field, ValidationError
from sqlalchemy.orm import Session

from db import get_db, Note

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


class ResponseNoteModel(BaseModel):
    id: int = Field(default=1, ge=1)
    name: str
    description: str
    done: bool


class Item(BaseModel):
    name: str
    price: float


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/api/healthchecker")
def healthchecker(db: Session = Depends(get_db)):
    try:
        # Здійснюємо запит
        result = db.query(Note).first()
        if result is None:
            raise HTTPException(status_code=500, detail="Database is not configured correctly")
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connecting to the database")


@app.get("/notes")
async def read_notes(skip: int = 0, limit: int = Query(default=10, le=100, ge=10), db: Session = Depends(get_db)) -> \
        list[ResponseNoteModel]:
    notes = db.query(Note).offset(skip).limit(limit).all()
    return notes


@app.get("/notes/{note_id}", response_model=ResponseNoteModel)
async def read_note(note_id: int = Path(description="The ID of the note to get", gt=0, le=10),
                    db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found')
    return note


class NoteModel(BaseModel):
    name: str
    description: str
    done: bool


@app.post("/notes")
async def create_note(note: NoteModel, db: Session = Depends(get_db)):
    new_note = Note(name=note.name, description=note.description, done=note.done)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


class ItemNotFoundError(Exception):
    pass


@app.exception_handler(ItemNotFoundError)
def item_not_found_error_handler(request: Request, exc: ItemNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": "Item not found"},
    )


def get_item_by_id(item_id: int) -> Optional[Item]:
    pass


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = get_item_by_id(item_id)
    if item is None:
        raise ItemNotFoundError
    return item


@app.post("/items/")
async def create_item(item: Item):
    if item.price < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Price should be a positive number",
        )
    return item


@app.exception_handler(ValidationError)
def validation_error_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": "Invalid input data"}
    )


@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


@app.exception_handler(Exception)
def unexpected_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "An unexpected error occurred"},
    )


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File()):
    pathlib.Path("uploads").mkdir(exist_ok=True)
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"file_path": file_path}
