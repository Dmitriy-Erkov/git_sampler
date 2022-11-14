from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Email, DataRequired, Length


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[Email(), DataRequired()])
    psw = PasswordField("Password", validators=[DataRequired(), Length(min=4, max=50)])
    remember = BooleanField(default=False)
    submit = SubmitField()
