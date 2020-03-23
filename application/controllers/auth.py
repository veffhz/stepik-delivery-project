from flask_login import logout_user, login_user, current_user
from flask import render_template, redirect, url_for, flash, request
from sqlalchemy.exc import IntegrityError

from application import app
from application.models import User
from application.extensions import db
from application.forms import LoginForm, RegisterForm


@app.route('/login/')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = LoginForm()
    return render_template('auth.html', form=form)


@app.route('/register/')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = RegisterForm()
    return render_template('register.html', form=form)


@app.route('/register/', methods=['POST'])
def post_register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User()
        try:
            form.populate_obj(new_user)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
        except IntegrityError as e:
            app.logger.warning(e)
            flash('Ошибка. Попробуйте еще раз', 'warning')
            return redirect(url_for('register'))
        next_ = request.args.get('next')
        return redirect(next_ or url_for('main'))
    return render_template('register.html', form=form)


@app.route('/login/', methods=['POST'])
def post_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user or not user.check_password(form.password.data):
            flash('Не удалось осуществить вход', 'warning')
            return redirect(url_for('login'))
        login_user(user)
        next_ = request.args.get('next')
        return redirect(next_ or url_for('main'))
    return render_template('auth.html', form=form)


@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for("main"))
