from sqlalchemy import event
from flask_login import UserMixin
from sqlalchemy_utils import ChoiceType
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from application.extensions import db

OrderStatusType = [
    ('new', 'новый'),
    ('processing', 'обрабатывается'),
    ('paid', 'оплачен'),
    ('collected', 'собран'),
    ('done', 'выполнен'),
]


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __str__(self):
        return f'{self.name}'


@event.listens_for(User.password, 'set', retval=True)
def hash_user_password(target, value, old_value, initiator):
    """
    Listener for hashing new password
    """
    if value != old_value:
        return generate_password_hash(value)
    else:
        return old_value


meals_orders = db.Table(
    'meals_orders',
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id')),
    db.Column('meal_id', db.Integer, db.ForeignKey('meals.id'))
)


class Meal(db.Model):
    __tablename__ = 'meals'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(80), nullable=False)
    picture = db.Column(db.String(80), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    category = db.relationship("Category", back_populates="meals", lazy='joined')
    orders = db.relationship('Order', secondary='meals_orders', back_populates='meals', lazy='joined')

    def __str__(self):
        return f'{self.title}'


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(15), unique=True, nullable=False)
    title = db.Column(db.String(80), unique=True, nullable=False)
    meals = db.relationship("Meal", back_populates="category", lazy='joined')

    def __str__(self):
        return f'{self.title}'


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    total = db.Column(db.Integer, nullable=False)
    status = db.Column(ChoiceType(OrderStatusType), nullable=False, default='new')
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User", lazy='joined')
    address = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    comment = db.Column(db.String(80), nullable=True)
    meals = db.relationship('Meal', secondary='meals_orders', back_populates='orders', lazy='joined')

    def __str__(self):
        return f'{self.id}'
