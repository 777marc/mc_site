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
                print("User logged in:", user)
                login_user(user)
                return redirect('/')
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect('/')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')
        return render_template('register.html')

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