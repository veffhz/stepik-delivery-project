import sys

from application import create_app
from config import ProductionConfig
from application.models import db, Meal, Category, User

categories = [
    {
        'id': '1',
        'code': 'sushi',
        'title': 'Суши',
        'meals': []
    },
    {
        'id': '2',
        'code': 'pasta',
        'title': 'Паста',
        'meals': []
    },
    {
        'id': '3',
        'code': 'streetfood',
        'title': 'Стритфуд',
        'meals': []
    },
    {
        'id': '4',
        'code': 'new',
        'title': 'Новинки',
        'meals': []
    },
    {
        'id': '5',
        'code': 'pizza',
        'title': 'Пицца',
        'meals': []
    },
]

meals = [
    {
        'id': '1',
        'title': 'Ролл "Томато"',
        'description': 'Лосось, снежный краб, вяленые томаты, авокадо, сыр, микс соусов, кунжут, 6 шт.',
        'picture': 'dish1.jpg',
        'price': 370,
        'category_id': 1,
    },
    {
        'id': '2',
        'title': 'Паста Карбонара',
        'description': 'Бекон, Лук репчатый, Сливки, Спагетти, Сыр пармезан, Черный перец, Чеснок.',
        'picture': 'dish2.jpeg',
        'price': 339,
        'category_id': 2,
    },
    {
        'id': '3',
        'title': 'Ролл "Трюфельный"',
        'description': 'Лакедра, лосось, трюфельный сыр, авокадо, трюфельная паста, соус «Спайс», тобико, перец, кунжут, зеленый лук, 6 шт.',
        'picture': 'dish3.jpeg',
        'price': 395,
        'category_id': 1,
    },
    {
        'id': '4',
        'title': 'Шаверма с цыпленком',
        'description': 'Капуста китайская, Куриная грудка, Лаваш армянский, Огурцы, Помидоры, Соус сливочный, Соус Черный перец.',
        'picture': 'dish4.jpeg',
        'price': 270,
        'category_id': 3,
    },
    {
        'id': '5',
        'title': 'Паста Три мяса',
        'description': 'Бекон, Курица, Лук репчатый, Свинина, Сливки, Спагетти, Сыр пармезан, Чеснок.',
        'picture': 'dish5.jpeg',
        'price': 329,
        'category_id': 2,
    },
    {
        'id': '6',
        'title': 'Грин Карри',
        'description': 'Курица, креветки, зеленый карри, кокосовое молоко, шампиньоны, брокколи, цукини.',
        'picture': 'dish6.jpeg',
        'price': 390,
        'category_id': 4,
    },
    {
        'id': '7',
        'title': 'Ролл "Игай"',
        'description': 'Лосось, мидии, огурец, перец гриль, зеленый лук, 6 шт.',
        'picture': 'dish7.jpeg',
        'price': 360,
        'category_id': 1,
    },
    {
        'id': '8',
        'title': 'Суши "Желтохвост спайс"',
        'description': 'Спайси хамачи',
        'picture': 'dish8.jpeg',
        'price': 95,
        'category_id': 1,
    },
    {
        'id': '9',
        'title': 'Ролл "Курай"',
        'description': 'Лосось, угорь, сыр, кунжут и острый соус, 6 шт.',
        'picture': 'dish9.jpeg',
        'price': 360,
        'category_id': 1,
    },
    {
        'id': '10',
        'title': 'Пицца Маргарита классическая',
        'description': 'Базилик, Моцарелла, Помидоры, Томатный пицца-соус.',
        'picture': 'dish10.jpeg',
        'price': 390,
        'category_id': 5,
    },
    {
        'id': '11',
        'title': 'Бургер Бродвей',
        'description': 'Булочка с кунжутом белая, Говядина, Огурцы маринованные, Помидоры, Салат Айсберг, Соус барбекю, Соус сливочный, Сыр Чеддер.',
        'picture': 'dish11.jpeg',
        'price': 312,
        'category_id': 3,
    },
    {
        'id': '12',
        'title': 'Паста с баклажанами',
        'description': 'Спагетти, баклажаны, пармезан, перец чили, чеснок, томатный соус, специи, зелень, базилик.',
        'picture': 'dish12.jpeg',
        'price': 250,
        'category_id': 2,
    },
    {
        'id': '13',
        'title': 'Спагетти с морепродуктами, запечённые в пергаменте по-лигурийски',
        'description': 'Спагетти, салатные мидии, филе кальмара, тигровые креветки, лук порей, помидоры черри, чеснок, базилик, соус песто, кедровые орешки, пармезан.',
        'picture': 'dish13.jpeg',
        'price': 290,
        'category_id': 2,
    },
    {
        'id': '14',
        'title': 'Пицца Карбонара классическая',
        'description': 'Бекон, Моцарелла, Соус сливочный, Сыр пармезан.',
        'picture': 'dish14.jpeg',
        'price': 499,
        'category_id': 5,
    },
    {
        'id': '15',
        'title': 'Пицца Барбекю классическая',
        'description': 'Колбаски охотничьи, Курица, Моцарелла, Соус барбекю, Томатный пицца-соус, укроп.',
        'picture': 'dish15.jpeg',
        'price': 480,
        'category_id': 5,
    },
    {
        'id': '16',
        'title': 'Паста с рагу из индейки и шпинатом',
        'description': 'Спагетти, индейка, сливки, шампиньоны, лук репчатый, пармезан, шпинат, чеснок.',
        'picture': 'dish16.jpeg',
        'price': 290,
        'category_id': 2,
    },

    {
        'id': '17',
        'title': 'Буррито',
        'description': 'Капуста китайская, Курица, Лук красный, Моцарелла, Перец болгарский, Помидоры, Рис, Соус мексиканский, Тортилья, Фасоль красная.',
        'picture': 'dish17.jpeg',
        'price': 289,
        'category_id': 3,
    },
    {
        'id': '18',
        'title': 'Бургер Гранд Каньон',
        'description': 'Булочка белая, Капуста китайская, Куриная грудка, Огурцы маринованные, Помидоры, Соус барбекю, Соус сливочный, Сыр Чеддер.',
        'picture': 'dish18.jpeg',
        'price': 299,
        'category_id': 3,
    },
    {
        'id': '19',
        'title': 'Овощной салат с цыпленком',
        'description': 'Куриное филе, огурцы , помидоры, полба, пармезан, соус Цезарь, зелень, кинза, базилик, яйцо.',
        'picture': 'dish19.jpeg',
        'price': 250,
        'category_id': 4,
    },
    {
        'id': '20',
        'title': 'Фреш-ролл с курицей',
        'description': 'Капуста китайская, Курица, Огурцы, Помидоры, Соус Тар-тар, Сыр пармезан, Тортилья.',
        'picture': 'dish20.jpeg',
        'price': 269,
        'category_id': 3,
    },
    {
        'id': '21',
        'title': 'Харчо',
        'description': 'Говядина, лук репчатый, томатная паста, чеснок, рис, кинза, специи, зелень.',
        'picture': 'dish21.jpeg',
        'price': 220,
        'category_id': 4,
    },
    {
        'id': '22',
        'title': 'Пицца Деревенская классическая',
        'description': 'Бекон, Грибы шампиньоны, Лук красный, Моцарелла, Свинина, Томатный пицца-соус, укроп.',
        'picture': 'dish22.jpeg',
        'price': 569,
        'category_id': 5,
    },
    {
        'id': '23',
        'title': 'Ролл Такаши',
        'description': 'Угорь, огурец, чукка, рис, сливочный сыр, авокадо, кунжут, спайси соус, унаги соус.',
        'picture': 'dish23.jpeg',
        'price': 300,
        'category_id': 4,
    },
    {
        'id': '24',
        'title': 'Рис с овощами, свининой и шампиньонами с соусом удон',
        'description': 'Рис, морковь, цукини, перец болгарский, китайская капуста, шампиньоны, свинина, кунжут, соус удон.',
        'picture': 'dish24.jpeg',
        'price': 320,
        'category_id': 4,
    },
    {
        'id': '25',
        'title': 'Пицца Четыре сыра классическая',
        'description': 'Моцарелла, Сливочный пицца-соус, Сыр Дор Блю, Сыр пармезан, Сыр Чеддер.',
        'picture': 'dish25.jpeg',
        'price': 559,
        'category_id': 5,
    },
]


def prepare_app():
    """
    Helper for check prod env
    """
    if len(sys.argv) > 1 and sys.argv[1] == 'prod':
        return create_app(config_class=ProductionConfig)
    else:
        return create_app()


def run():
    """
    Add test data to db.
    """
    app = prepare_app()
    app.app_context().push()

    for category_dict in categories:
        category = Category(**category_dict)
        db.session.add(category)

    db.session.commit()

    for meal_dict in meals:
        meal = Meal(**meal_dict)
        db.session.add(meal)

    db.session.commit()

    user = User(name='admin', email='admin@localhost.com', password='12345678')

    db.session.add(user)
    db.session.commit()


if __name__ == "__main__":
    run()
