from flask import Flask , render_template , redirect , url_for
from flask_bootstrap import Bootstrap5
from  app.models import Book
from flask_wtf import FlaskForm , CSRFProtect
from wtforms import StringField , SubmitField , IntegerField , SelectField , FileField , PasswordField
from wtforms.validators import DataRequired , Length , Email , EqualTo


class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=3, max=100)])
    author = StringField('Author', validators=[DataRequired(), Length(min=3, max=100)])
    description = StringField('Description', validators=[DataRequired(), Length(min=10, max=500)])
    pages = IntegerField('Pages', validators=[DataRequired()])
    cover = FileField('Cover Image')
    submit = SubmitField('Submit')