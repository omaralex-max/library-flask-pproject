from flask import Flask, render_template, request, redirect, url_for
from app.books import books_blueprint
from app.models import db, Book
from werkzeug.utils import secure_filename
import os
@books_blueprint.route('', endpoint='index')
def index():
    books = Book.query.all()
    return render_template('books/index.html', books=books) 


@books_blueprint.route("/<int:id>", endpoint="show")
def show(id):
    book = db.get_or_404(Book , id)
    return render_template('books/show.html', book=book)

@books_blueprint.route("/<int:id>/delete", endpoint="delete" , methods=["POST"])
def delete(id):
    book = db.get_or_404(Book , id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('books.index'))  



#--------------------------------------------------------------
from app.books.forms import BookForm

@books_blueprint.route("/form/create", endpoint="createform", methods=["POST","GET"])
def create_form():
    form = BookForm()
    if form.validate_on_submit():
        cover = form.cover.data
        cover_name = secure_filename(cover.filename)
        cover.save(os.path.join('app/static/books/images', cover_name))
        print (cover)
        book = Book(
            title=request.form.get('title'),
            author=request.form.get('author'),
            description=request.form.get('description'),
            pages=request.form.get('pages'),
            cover=cover_name,
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('books.index'))
    return render_template('books/forms/create_form.html', form=form)

@books_blueprint.route('/<int:id>/update', methods=['GET' , 'POST'] , endpoint="update")
def update(id):
    book = Book.query.get_or_404(id)  # Use .query.get_or_404 to fetch the book
    form = BookForm(obj=book)

    if form.validate_on_submit():
        # Update book attributes
        book.title = form.title.data
        book.author = form.author.data
        book.description = form.description.data
        book.pages = form.pages.data

        # Handle cover file if provided
        if form.cover.data:
            cover = form.cover.data
            cover_name = secure_filename(cover.filename)
            cover_path = os.path.join('app/static/books/images', cover_name)
            cover.save(cover_path)
            book.cover = cover_name

        db.session.commit()
        return redirect(url_for('books.index'))

    return render_template('books/forms/update.html', form=form)