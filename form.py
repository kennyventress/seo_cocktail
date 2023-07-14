from flask_wtf import FlaskForm
from wtforms import TextAreaField, RadioField, SubmitField, StringField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class ReviewForm(FlaskForm):
    rating = RadioField('How Satisfied were You?', validators=[DataRequired()], choices=[('Very Satisfied'), ('Satisfied'), ('Neutral'), ('Dissatisfied'), ('Very Dissatisfied')])
    review_text = TextAreaField('Please Describe Your Experience!', validators=[DataRequired()])
    submit = SubmitField('Submit Response!')