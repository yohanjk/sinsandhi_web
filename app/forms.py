from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField


class WordJoinerForm(Form):
    word1 = StringField('Word 1:', validators=[validators.DataRequired()])
    word2 = StringField('Word 2:', validators=[validators.DataRequired()])
    submit = SubmitField('Join Words')


class WordSplitterForm(Form):
    word1 = StringField('Word:', validators=[validators.DataRequired()])
    submit = SubmitField('Split Word')

