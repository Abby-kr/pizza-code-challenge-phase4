#!/usr/bin/env python3

from datetime import datetime
from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

db.init_app(app)

def seed_data():
    with app.app_context():
        # Restaurants
        restaurant1 = Restaurant(name='Pizza Place', address='123 Main St')
        restaurant2 = Restaurant(name='Papa Joe', address='21 Harlem Blvd')
        restaurant3 = Restaurant(name='Suzys', address='Long Island')
        restaurant4 = Restaurant(name='Lucy Lee', address='56 Avenue')
        restaurant5 = Restaurant(name='Pasta House', address='32 Broadway St')

        db.session.add_all([restaurant1, restaurant2, restaurant3, restaurant4, restaurant5])
        db.session.commit()

        # Pizzas
        pizza1 = Pizza(name='Margherita', ingredients='Tomato, mozzarella, basil', created_at=datetime.utcnow())
        pizza2 = Pizza(name='Pepperoni', ingredients='Pepperoni, cheese, tomato sauce', created_at=datetime.utcnow())
        pizza3 = Pizza(name='Hawaiian', ingredients=' pizza sauce, cheese, cooked ham, pineapple', created_at=datetime.utcnow())
        pizza4 = Pizza(name='Cheese', ingredients='pizza dough, tomato sauce, cheese', created_at=datetime.utcnow())
        pizza5 = Pizza(name='Veggie', ingredients='cherry tomatoes, artichoke, bell pepper, olives, red onion', created_at=datetime.utcnow())

        db.session.add_all([pizza1, pizza2, pizza3, pizza4, pizza5])
        db.session.commit()

        # Restaurant Pizzas
        restaurant_pizza1 = RestaurantPizza(pizza=pizza1, restaurant=restaurant1, price=15, created_at=datetime.utcnow())
        restaurant_pizza2 = RestaurantPizza(pizza=pizza2, restaurant=restaurant2, price=20, created_at=datetime.utcnow())
        restaurant_pizza3 = RestaurantPizza(pizza=pizza5, restaurant=restaurant3, price=20, created_at=datetime.utcnow())
        restaurant_pizza4 = RestaurantPizza(pizza=pizza3, restaurant=restaurant4, price=20, created_at=datetime.utcnow())
        restaurant_pizza5 = RestaurantPizza(pizza=pizza4, restaurant=restaurant5, price=20, created_at=datetime.utcnow())

        db.session.add_all([restaurant_pizza1, restaurant_pizza2, restaurant_pizza3, restaurant_pizza4, restaurant_pizza5])
        db.session.commit()

if __name__ == "__main__":
    seed_data()
