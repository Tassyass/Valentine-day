from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Gift(db.Model, SerializerMixin):
    __tablename__='gifts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    giftlist_id = db.Column(db.Integer, db.ForeignKey("giftlists.id"))

    @validates('price')
    def validate_price(self, key, value):
        if value is None or not (1 <= value <= 30000):
            raise ValueError("Price must be between 1 and 30000")
        return value
    
    serialize_rules = ('-giftlists.gift', )

    def __repr__(self):
        return f"Gift {self.name} Description: {self.description} Price: Ksh{self.price}"


class Giftlist(db.Model, SerializerMixin):
    __tablename__="giftlists"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    gifts = db.relationship('Gift', backref='giftlist')
    
    serialize_rules = ('-gifts.giftlist', )

    def __repr__(self):
        return f"Giftlist ID: {self.id}, Description: {self.description}, Budget: Ksh{self.budget}"

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(254), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    giftlists = db.relationship('Giftlist', backref='user')
    
    serialize_rules = ('-giftlists.user', )

    def __repr__(self):
        return f"<id {self.id} User {self.name}, Email: {self.email}>"

