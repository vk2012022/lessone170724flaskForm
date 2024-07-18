from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

users = []

def get_age_suffix(age):
    if 11 <= age % 100 <= 14:
        return 'лет'
    elif age % 10 == 1:
        return 'год'
    elif 2 <= age % 10 <= 4:
        return 'года'
    else:
        return 'лет'

@main.route('/')
def index():
    return render_template('index.html', users=users)

@main.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    age = int(request.form.get('age'))
    city = request.form.get('city')
    hobby = request.form.get('hobby')
    age_suffix = get_age_suffix(age)
    users.append({'name': name, 'age': age, 'age_suffix': age_suffix, 'city': city, 'hobby': hobby})
    return redirect(url_for('main.index'))
