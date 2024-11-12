from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, DateField, SelectField
from wtforms.validators import DataRequired
from datetime import date

CATEGORIES = [('tech', 'Tech'), ('science', 'Science'), ('lifestyle', 'Lifestyle')]

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    is_active = BooleanField('Active')
    publication_date = DateField('Publication Date', default=date.today)
    category = SelectField('Category', choices=CATEGORIES)
    submit = SubmitField('Submit')
