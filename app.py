# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp
"""
from flask import Flask, request, redirect, url_for, current_app, render_template
app = Flask(__name__, instance_relative_config=True)    # Construct an instance of Flask class for our webapp

app.config.from_pyfile("config.py", 
                       # silent=True
                       )
# app.config.from_object("config")


@app.route('/')   # URL '/' to be handled by main() route handler
def main():
    """Say hello"""
    return f'Hello, world!   {app.config["SECRET_KEY"]=} {app.instance_path=} {app.template_folder=}'



@app.route('/homepage') 
def home():
    """View for the Home page of your website."""
    return f"This is your homepage :) \n Your IP is {request.remote_addr} and you are using {request.user_agent}"

@app.route("/hi/<string:name>") # URL rule must start with a slash.
def greetings(name):
    """View function to greet the user by name."""
    name = name.upper()
    age = request.args.get("age")
    return f"Welcome {name=} {age=}!"


@app.route("/admin")
def admin():
    to_url = url_for("greetings", name="administrator") # return "/administrator"
    to_url = url_for("greetings", name="administrator", surname = "unknow") # return "/administrator?surname=unknow"
    print(to_url)
    return redirect(to_url)


import click
# Додаємо команду за допомогою Click
@app.cli.command("hello")
@click.argument("name")
def hello(name):
    """Привітати користувача по імені"""
    click.echo(f"Hello, {name}!")
    print("Hello server")

with app.app_context():
    # Тепер можна отримати доступ до current_app, хоча ми поза запитом
    print(current_app.name)  # Виведе назву додатка

if __name__ == '__main__':  # Script executed directly?
    app.run(port=81)  # Launch built-in web server and run this Flask webapp, debug=True\