from fastapi import APIRouter, HTTPException, status, path, Depends
from config import sessionLocal
from sqlalchemy.orm import Session
from schemas import BookSchema, RequestBook, ResponseBook
import crud

router = APIRouter()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create/")
async def create(request: RequestBook, db: Session = Depends(get_db)):
    crud.create_book(db, book=request.parameter)
    return ResponseBook(
        code=status.HTTP_201_CREATED,
        status=status.HTTP_200_OK,
        message="Book created successfully",
    ).dict(exclude_none=True)


@router.get("/read/")
async def get(db: Session = Depends(get_db)):
    crud.get_book(db, 0, 100)
    return ResponseBook(
        code=status.HTTP_200_OK,
        status=status.HTTP_200_OK,
        message="Successfully fetched all books",
    ).dict(exclude_none=True)


@router.get("/read/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    _book = crud.get_book_by_id(db, id, 100)
    return ResponseBook(
        code=status.HTTP_200_OK,
        status=status.HTTP_200_OK,
        message="Success get book",
        result=_book,
    ).dict(exclude_none=True)


@router.post("/update/")
async def update_book(request: RequestBook, db: Session = Depends(get_db)):
    _book = crud.update_book(
        db,
        book_id=request.parameter.id,
        title=request.parameter.title,
        description=request.parameter.description,
    )
    return ResponseBook(
        code=status.HTTP_200_OK,
        status=status.HTTP_200_OK,
        message="Success update book",
        result=_book,
    )


@router.delete("/{id}")
async def delete(id: int, db: Session = Depends(get_db)):
    crud.remove_book(db, book_id=id)
    return ResponseBook(
        code=status.HTTP_200_OK,
        status=status.HTTP_200_OK,
        message="Success delete book",
    ).dict(exclude_none=True)
