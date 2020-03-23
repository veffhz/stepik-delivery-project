import random

import pymorphy2

from application.models import Meal

morph = pymorphy2.MorphAnalyzer()
meal_word = morph.parse('блюдо')[0]


def random_limit(items, quantity):
    """
    Randomize list
    """
    if len(items) < quantity:
        return random.sample(items, len(items))
    return random.sample(items, quantity)


def get_meals_from_categories(categories, meal_ids):
    """
    Get meals by ids from preloaded categories
    """
    meals = [meal for category in categories for meal in category.meals
             if meal.id in meal_ids]

    return get_cart_params(meals)


def preview_cart(cart_ids):
    """
    Prepare dict with cart data
    """
    meals = []
    if cart_ids:
        meals = Meal.query.filter(Meal.id.in_(cart_ids)).all()
    return {
        'meals': meals,
        **get_cart_params(meals)
    }


def get_cart_params(meals):
    """
    Get dict with cart data details
    """
    length = len(meals)
    return {
        'length': length,
        'total_price': sum(meal.price for meal in meals),
        'is_not_empty': length > 0,
        'plural': meal_word.make_agree_with_number(length).word,
    }
