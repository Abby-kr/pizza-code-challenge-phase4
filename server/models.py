from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from datetime import datetime

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    restaurant_pizzas = db.relationship('RestaurantPizza', backref = 'restaurant')

# add any models you may need. 
class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow())
    updated_at = db.Column(db.DateTime)

    restaurant_pizzas = db.relationship('RestaurantPizza', backref = 'pizza')


class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'),nullable=False)
    restaurant_id = db.Column(db.Integer,db.ForeignKey('restaurants.id'),nullable=False)
    price = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow())
    updated_at = db.Column(db.DateTime)

    @validates('price')
    def validate_price(self, key, price):
        if not 1 <= price <= 30:
            raise ValueError("Price must be between 1 and 30.")
        return price
