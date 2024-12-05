from sqlalchemy import create_engine, select, and_
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/library', echo=False)

Base = automap_base()
Base.prepare(autoload_with=engine)

Books = Base.classes.books
def books_repr(self):
    return f"<Books(id={self.id}, title='{self.title}', no_of_pages={self.no_of_pages})>"
Books.__repr__ = books_repr

Authors = Base.classes.authors
def authors_repr(self):
    return f"<Authors(id={self.id}, first_name='{self.first_name}', last_name={self.last_name})>"
Authors.__repr__ = authors_repr

AuthorBooks = Base.classes.author_books
def author_books_repr(self):
    return f"<AuthorBooks(id={self.id}, author_id='{self.author_id}', book_id={self.book_id})>"
AuthorBooks.__repr__ = author_books_repr

def add_book(_session, _title, _no_of_pages):
    _book = session.execute(select(Books).filter(
        and_(Books.title == _title, Books.no_of_pages == _no_of_pages)
    )).scalar_one_or_none()
    if _book is not None:
        print("Book exists in the database.")
        return None
    else:
        print("Book does not exist in the database.")
        _book = Books(title=_title, no_of_pages=_no_of_pages)
        _session.add(_book)
        print(_book)
        return _book

def add_author(_session, _first_name, _last_name):
    _author = session.execute(select(Authors).filter(
        and_(Authors.first_name == _first_name, Authors.last_name == _last_name)
    )).scalar_one_or_none()
    if _author is not None:
        print("Author exists in the database.")
    else:
        print("Author does not exist in the database.")
        _author = Authors(first_name=_first_name, last_name=_last_name)
        session.add(_author)
    print(_author)
    return _author

def add_author_book(_session, _author_id, _book_id):
    _author_book = AuthorBooks(author_id=_author_id, book_id=_book_id)
    session.add(_author_book)
    print(_author_book)
    return _author_book

if __name__ == "__main__":
    print("Input new book:\n")

    title = input("What is the title of the book?\n")
    no_of_pages = int(input("How many pages are in the book?\n"))
    first_name = input("What is the first name of the author?\n")
    last_name = input("What is the last name of the author?\n")

    print("Inputting book data:\n")

    with Session(engine) as session:
        book = add_book(session, title, no_of_pages)
        if book is not None:
            author = add_author(session, first_name, last_name)
            session.flush()

            author_book = add_author_book(session, author.id, book.id)
            session.commit()

    print("Done!")