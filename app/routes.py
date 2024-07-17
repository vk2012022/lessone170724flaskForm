from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

users = []

@main.route('/')
def index():
    return render_template('index.html', users=users)

@main.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    age = request.form.get('age')
    city = request.form.get('city')
    hobby = request.form.get('hobby')
    users.append({'name': name, 'age': age, 'city': city, 'hobby': hobby})
    return redirect(url_for('main.index'))
