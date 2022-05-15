from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    post = TextAreaField('Your pitch', validators=[InputRequired()])
    category = SelectField('Category', choices=[('product', 'product'), ('pickup_line', 'pickup_line'), ('business', 'business')],
                           validators=[InputRequired()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = TextAreaField('Post a comment', validators=[InputRequired()])
    submit = SubmitField('Post')