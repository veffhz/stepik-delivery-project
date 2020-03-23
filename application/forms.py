import phonenumbers
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Email, ValidationError, EqualTo


class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    password = StringField(validators=[InputRequired()])
    submit = SubmitField('submit')


class RegisterForm(FlaskForm):
    name = StringField(label='Ваше имя', validators=[InputRequired()])
    email = StringField(validators=[InputRequired(), Email()])
    password = StringField(validators=[InputRequired()])
    password_2 = StringField(validators=[InputRequired(), EqualTo('password', message='Пароли должны совпадать')])
    submit = SubmitField('submit')


class OrderForm(FlaskForm):
    comment = StringField(label='Комментарий')
    address = StringField(label='Адрес', validators=[InputRequired()])
    phone = StringField('Телефон')
    submit = SubmitField('submit')

    def validate_phone(self, phone):
        try:
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError('Invalid phone number')
