from flask import render_template, request, redirect
from flask_login import login_user, logout_user, current_user, login_required

from models import Person, User


def register_routes(app, db, bcrypt):

    @app.route('/')
    def index():
        people = Person.query.all()
        return render_template('index.html', people=people)


    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            user = User.query.filter_by(username=username).first()
            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect('/')
        return render_template('login.html')

    @app.route('/add', methods=['POST'])
    def add_person():
        name = request.form.get('name')
        age = request.form.get('age')
        job = request.form.get('job')
        new_person = Person(name=name, age=age, job=job)
        db.session.add(new_person)
        db.session.commit()
        return redirect('/')

    @app.route('/delete/<int:pid>', methods=['DELETE'])
    def delete_person(pid):
        person = Person.query.get(pid)
        if person:
            db.session.delete(person)
            db.session.commit()
        return redirect('/', 204)

    @app.route('/details/<int:pid>')
    def person_details(pid):
        person = Person.query.get(pid)
        if person:
            return render_template('details.html', person=person)
        return redirect('/')