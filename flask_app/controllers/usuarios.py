from flask import render_template, redirect, request
from flask_app.models.users import User
from flask_app import app

@app.route('/')
def index():
    # llamar al método de clase get all para obtener todos los amigos
    users = User.get_all()
    return render_template("index.html", template_users=users)

@app.route('/crear_user')
def crear_user():
    return render_template('new_users.html')


@app.route('/agregar', methods=['POST'])
def agregar_usuario():

    data = {
        "first_name": request.form["nombre"],
        "last_name" : request.form["apellido"],
        "email" : request.form["email"]
    }

    User.save(data)

    return redirect('/')

