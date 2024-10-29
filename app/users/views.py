from flask import Blueprint, render_template, request

# Створюємо об'єкт Blueprint з назвою 'users'
users_bp = Blueprint('users', __name__, template_folder='templates')

@users_bp.route('/hi/<name>')
def greetings(name):
    age = request.args.get("age", "невідомий вік")
    return render_template('users/hi.html', name=name.upper(), age=age)

@users_bp.route('/resume')
def resume():
    return render_template('resume.html', title='Моє резюме')

@users_bp.route('/admin')
def admin():
    # Приклад простої сторінки адміністратора
    return render_template('admin.html', role="ADMINISTRATOR", age=45)
