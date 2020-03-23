from flask import render_template, session
from flask_login import login_required, current_user

from application import app
from application.models import Category, Order
from application.data_helper import random_limit
from application.data_helper import get_meals_from_categories

CATEGORY_COUNT = 3


@app.route('/')
def main():
    categories = Category.query.all()
    cart_data = {}

    cart_ids = session.get("cart")
    if cart_ids:
        cart_data = get_meals_from_categories(categories, cart_ids)

    category_set = {
        category.title: random_limit(category.meals, CATEGORY_COUNT)
        for category in categories
    }
    return render_template("main.html", categories=category_set,
                           cart_data=cart_data)


@app.route('/account/')
@login_required
def get_account():
    orders = Order.query.filter_by(user=current_user).all()
    return render_template("account.html", orders=orders)


@app.route('/ordered/')
def ordered():
    return render_template("ordered.html")
