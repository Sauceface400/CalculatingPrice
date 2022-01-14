from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from Name.model import person

class entryName(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(max=30)])
    submit = SubmitField("Enter Username")

    def validate_username(self, username):
        user = person.query.filter_by(username=username.data).first()

class deleteBTN(FlaskForm):
    submit = SubmitField("Delete")