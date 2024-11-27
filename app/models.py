from app import db
from datetime import datetime
from sqlalchemy.orm import relationship, backref

post_tags = db.Table(
    'post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    posted = db.Column(db.DateTime, default=db.func.current_timestamp())
    is_active = db.Column(db.Boolean, default=True)

    # Вказуємо ім'я для ForeignKey
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', name='fk_user_post'))
    author = db.relationship('User', back_populates='posts')
    tags = db.relationship('Tag', secondary=post_tags, back_populates='posts')

class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    posts = db.relationship('Post', secondary=post_tags, back_populates='tags')


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Двосторонній зв'язок із моделлю Post
    posts = db.relationship('Post', back_populates='author')

    def __repr__(self):
        return f"<User {self.username}>"

