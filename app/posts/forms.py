from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, DateTimeLocalField, SelectField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime
from app.models import User
from wtforms_sqlalchemy.fields import QuerySelectField

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    is_active = BooleanField("Active")
    category = SelectField("Category", choices=[('Tech', 'Tech'), ('Lifestyle', 'Lifestyle'), ('Other', 'Other')])
    publication_date = DateTimeLocalField("Publish Date", format='%Y-%m-%dT%H:%M', default=datetime.utcnow)
    author = QuerySelectField("Author", query_factory=lambda: User.query, get_label="username", allow_blank=False)
    submit = SubmitField("Submit")
