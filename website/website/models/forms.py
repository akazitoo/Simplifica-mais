from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class MainForm(FlaskForm):
    county = StringField("county", validators=[DataRequired()])
    gender = StringField("gender", validators=[DataRequired()])
    lgbtqia_plus = StringField("lgbtqia_plus", validators=[DataRequired()])


class AuthForm(FlaskForm):
    full_name = StringField("full_name", validators=[DataRequired()])
    birth_date = StringField("birth_date", validators=[DataRequired()])
    cpf = StringField("cpf", validators=[DataRequired()])
    cellphone_number = StringField("cellphone_number", validators=[DataRequired()])
