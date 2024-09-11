from flask_sqlalchemy import SQLAlchemy
from flask import url_for
db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    pages = db.Column(db.Integer, nullable=False , default=0)
    cover = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return f"{self.title}"
    
    @property
    def cover_url(self):
        return url_for('static', filename=f"books/images/{self.cover}")
    
    @property
    def show_url(self):
        return url_for('books.show', id=self.id)
    @property
    def delete_url(self):
        return url_for('books.delete', id=self.id)