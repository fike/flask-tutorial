from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from flaskr import db 
# from sqlalchemy import UniqueConstraint



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    _password = db.Column("password", db.String, nullable=False)
    profile = db.Column(db.Text, nullable=False)
    bgcolor = db.Column(db.String(50), nullable=False)


    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        """Store the password as a hash for security"""
        self._password = generate_password_hash(value)

    def check_password(self, value):
        return check_password_hash(self.password, value)