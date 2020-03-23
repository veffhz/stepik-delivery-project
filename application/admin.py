from werkzeug.utils import redirect
from flask_login import current_user
from flask import url_for, request, flash
from flask_admin.contrib.sqla import ModelView

from application.models import db, User, Meal, Category, Order


class AdminView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        flash('Требуется аутентификация!', 'danger')
        return redirect(url_for('login', next=request.url))


class UserView(AdminView):
    column_exclude_list = ['password']
    column_searchable_list = ['name', 'email']

    form_widget_args = {
        'password': {
            'type': 'password'
        }
    }


def init_admin(admin):
    admin.add_view(UserView(User, db.session))
    admin.add_view(AdminView(Meal, db.session))
    admin.add_view(AdminView(Category, db.session))
    admin.add_view(AdminView(Order, db.session))
