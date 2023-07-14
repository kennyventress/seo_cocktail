from flask_wtf import FlaskForm
from wtforms import TextAreaField, RadioField, SubmitField, StringField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class ReviewForm(FlaskForm):
    review_text = TextAreaField('Cocktail Feedbacks!', validators=[DataRequired()])
    rating = RadioField('Feedback', validators=[DataRequired()], choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5,'5 Stars')])
    #feedback= StringField('FeedBack:',validators=[DataRequired(),Tex)
    submit = SubmitField('Submit Response!')