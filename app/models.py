from app import db


class Person(db.Model):
    __tablename__ = 'people'

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer)
    job = db.Column(db.Text)

    def __repr__(self):
        return f'Person Name: {self.name} age: {self.age} job: {self.job}'
    

class User(db.Model):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    role = db.Column(db.Text)
    description = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'User Name: {self.username} role: {self.role}'

    def get_id(self):
        return self.uid
