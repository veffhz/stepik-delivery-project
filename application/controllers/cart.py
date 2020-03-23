from flask import render_template, session
from flask import flash, redirect, url_for
from flask_login import login_required, current_user

from application import app
from application.extensions import db
from application.forms import OrderForm
from application.models import Order, User
from application.data_helper import preview_cart


@app.route('/addtocart/<int:meal_id>/')
def add_to_cart(meal_id):
    form = OrderForm()
    cart_ids = session.get("cart", [])
    if meal_id not in cart_ids:
        cart_ids.append(meal_id)
    session['cart'] = cart_ids
    cart_data = preview_cart(cart_ids)
    flash('Блюдо добавлено в корзину', 'success')
    return render_template("cart.html", cart_data=cart_data,
                           form=form)


@app.route('/remove_from_cart/<int:meal_id>/')
def remove_from_cart(meal_id):
    form = OrderForm()
    cart_ids = session.get("cart")
    if meal_id in cart_ids:
        cart_ids.remove(meal_id)
    session['cart'] = cart_ids
    cart_data = preview_cart(cart_ids)
    flash('Блюдо удалено из корзины', 'warning')
    return render_template("cart.html", cart_data=cart_data,
                           form=form)


@app.route('/cart/')
def get_cart():
    form = OrderForm()
    cart_ids = session.get("cart")
    cart_data = preview_cart(cart_ids)
    return render_template("cart.html", cart_data=cart_data,
                           form=form)


@app.route('/cart/', methods=['POST'])
@login_required
def send_cart():
    form = OrderForm()
    cart_ids = session.get("cart")
    cart_data = preview_cart(cart_ids)

    if form.validate_on_submit():
        new_order = Order()
        form.populate_obj(new_order)
        user = User.query.filter_by(email=current_user.email).one()
        new_order.meals = cart_data['meals']
        new_order.total = cart_data['total_price']
        new_order.user = user
        db.session.add(new_order)
        db.session.commit()
        session.pop('cart')
        return redirect(url_for('ordered'))
    return render_template("cart.html", cart_data=cart_data,
                           form=form)
