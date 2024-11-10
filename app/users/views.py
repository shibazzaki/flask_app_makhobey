from . import bp
from flask import render_template, redirect, request, url_for, make_response, session, flash
from datetime import timedelta, datetime


### ЗАДАЄМО ПРАВИЛЬНІ ДАНІ ДЛЯ ЛОГІНА ###
valid_user = {
    "username": "testuser",
    "password": "testpassword"
}

@bp.route("/profile")
def profile():
    if 'username' in session:
        cookies = request.cookies.to_dict()  # Зберігає всі кукі у словник
        theme = cookies.get('theme', 'light')  # Отримує значення теми або 'light' за замовчуванням
        return render_template('users/profile.html', username=session['username'], cookies=cookies, theme=theme)
    else:
        flash('Спочатку увійдіть в систему', 'warning')
        return redirect(url_for('users.login'))


@bp.route("/login",  methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == valid_user['username'] and password == valid_user['password']:
            session['username'] = username
            flash('Вхід успішний!', 'success')
            return redirect(url_for('users.profile'))
        else:
            flash('Невірні дані для входу', 'danger')
            return redirect(url_for('users.login'))
    return render_template('users/login.html')

@bp.route('/logout')
def logout():
    session.pop('username', None)
    flash('Ви вийшли з системи', 'info')
    return redirect(url_for('users.login'))



@bp.route("/hi/<string:name>")   #/hi/ivan?age=45
def greetings(name):
    name = name.upper()
    age = request.args.get("age", None, int)

    return render_template("users/hi.html",
                           name=name, age=age)

@bp.route("/admin")
def admin():
    to_url = url_for("users.greetings", name="administrator", age=45, _external=True)     # "http://localhost:8080/hi/administrator?age=45"
    print(to_url)
    return redirect(to_url)


@bp.route('/set_cookie')
def set_cookie():
    response = make_response('Кука встановлена')
    response.set_cookie('username', 'student', max_age=timedelta(seconds=60))
    response.set_cookie('color', '', max_age=timedelta(seconds=60))
    return response


@bp.route('/add_cookie', methods=['POST'])
def add_cookie():
    if 'username' not in session:
        flash('Спочатку увійдіть в систему', 'warning')
        return redirect(url_for('users.login'))
    key = request.form['key']
    value = request.form['value']
    duration = int(request.form['duration'])
    response = make_response(redirect(url_for('users.profile')))
    response.set_cookie(key, value, max_age=duration)
    flash(f'Кукі "{key}" додано!', 'success')
    return response


@bp.route('/delete_cookie', methods=['POST'])
def delete_cookie():
    if 'username' not in session:
        flash('Спочатку увійдіть в систему', 'warning')
        return redirect(url_for('users.login'))

    key = request.form['key']
    response = make_response(redirect(url_for('users.profile')))
    response.set_cookie(key, '', expires=0)  # Видаляє кукі шляхом встановлення минулого терміну дії
    flash(f'Кукі "{key}" видалено!', 'info')
    return response


@bp.route('/set_theme/<theme>', methods=['GET'])
def set_theme(theme):
    if 'username' not in session:
        flash('Спочатку увійдіть в систему', 'warning')
        return redirect(url_for('users.login'))

    response = make_response(redirect(url_for('users.profile')))
    response.set_cookie('theme', theme, max_age=60 * 60 * 24 * 30)  # Зберігає вибір теми на 30 днів
    flash(f'Тема "{theme}" застосована!', 'success')
    return response