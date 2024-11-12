from . import post_bp
from flask import render_template, abort, flash, redirect, url_for, session
import json
from .forms import PostForm
import os

posts = [
    {"id": 1, 'title': 'My First Post', 'content': 'This is the content of my first post.', 'author': 'Vlad'},
    {"id": 2, 'title': 'Another Day', 'content': 'Today I learned about Flask macros.', 'author': 'Jane Smith'},
    {"id": 3, 'title': 'Flask and Jinja2', 'content': 'Jinja2 is powerful for templating.', 'author': 'Mike Lee'}
]

@post_bp.route('/')
def get_posts():
    return render_template("posts.html", posts=posts)

@post_bp.route('/<int:id>')
def detail_post(id):
    if id > 3:
        abort(404)
    post = posts[id-1]
    return render_template("detail_post.html", post=post)

@post_bp.route('/add_post', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        # Створення поста
        post = {
            "id": get_next_id(),
            "title": form.title.data,
            "content": form.content.data,
            "category": form.category.data,
            "is_active": form.is_active.data,
            "publication_date": form.publication_date.data.isoformat(),
            "author": session.get('username', 'Anonymous')
        }
        save_post(post)
        flash(f"Post '{post['title']}' added successfully!", 'success')
        return redirect(url_for('posts.add_post'))
    return render_template('add_post.html', form=form)

def get_next_id():
    if not os.path.exists("app/posts/posts.json"):
        return 1
    with open("app/posts/posts.json", "r") as f:
        try:
            posts = json.load(f)
            if not posts:
                return 1
            return max(post["id"] for post in posts) + 1
        except json.JSONDecodeError:
            return 1


def save_post(post):
    posts = []
    if os.path.exists("app/posts/posts.json"):
        with open("app/posts/posts.json", "r") as f:
            posts = json.load(f)
    posts.append(post)
    with open("app/posts/posts.json", "w") as f:
        json.dump(posts, f, indent=4)

@post_bp.route('/all_posts')
def all_posts():
    posts = []
    if os.path.exists("app/posts/posts.json"):
        with open("app/posts/posts.json", "r") as f:
            posts = json.load(f)
    return render_template('all_posts.html', posts=posts)

