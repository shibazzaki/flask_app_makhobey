from . import post_bp
from flask import render_template, abort, flash, redirect, url_for, request
from .. import db
from ..models import Post
from .forms import PostForm

@post_bp.route('/')
def get_posts():
    """Відображення всіх постів"""
    posts = Post.query.order_by(Post.posted.desc()).all()
    return render_template("all_posts.html", posts=posts)

@post_bp.route('/<int:id>')
def detail_post(id):
    post = Post.query.get_or_404(id)  # Отримання поста за ID або повернення 404
    return render_template('detail_post.html', post=post)



@post_bp.route('/add', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        try:
            # Логування введених даних
            print("Form Data:", form.data)

            # Створення нового поста
            new_post = Post(
                title=form.title.data,
                content=form.content.data,
                category=form.category.data,
                is_active=form.is_active.data,
                posted=form.publication_date.data,
                author=form.author.data
            )
            db.session.add(new_post)
            db.session.commit()

            # Логування успішного збереження
            print(f"Post '{new_post.title}' added successfully!")

            flash(f"Post '{new_post.title}' added successfully!", "success")
            return redirect(url_for('posts.get_posts'))
        except Exception as e:
            print("Error:", str(e))  # Логування помилки
            flash("An error occurred while adding the post.", "danger")
    else:
        print("Form Validation Errors:", form.errors)  # Логування помилок валідації
    return render_template('add_post.html', form=form)


@post_bp.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(post)
        db.session.commit()
        flash(f"Post '{post.title}' deleted successfully!", "success")
        return redirect(url_for('posts.get_posts'))
    return render_template('delete_post.html', post=post)



@post_bp.route('/inactive')
def inactive_posts():
    posts = Post.query.filter_by(is_active=False).order_by(Post.posted.desc()).all()
    return render_template('inactive_posts.html', posts=posts)

@post_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    post = Post.query.get_or_404(id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.category = form.category.data
        post.is_active = form.is_active.data
        post.posted = form.publication_date.data
        post.author = form.author.data
        db.session.commit()
        flash(f"Post '{post.title}' updated successfully!", "success")
        return redirect(url_for('posts.get_posts'))
    return render_template('edit_post.html', form=form, post=post)

