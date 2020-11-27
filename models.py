from project import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin





@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(40), unique=True)
    username = db.Column(db.String(40))
    password_hash = db.Column(db.String(128))


    def set_password(self,password):
        #self.email = email
        #self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):

        return check_password_hash(self.password_hash,password)