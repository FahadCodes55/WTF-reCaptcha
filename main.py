from flask import Flask, render_template, request, flash
from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_wtf.recaptcha import RecaptchaField

app = Flask(__name__, template_folder="template")
app.config['SECRET_KEY'] = "abc"
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = "6LfZ9TAqAAAAAPdeEGi4cIx4L0DyhtIGYxpxDymz"
app.config['RECAPTCHA_PRIVATE_KEY'] = "6LfZ9TAqAAAAAKmKQ-X4Xeu7Fo_UTxfLXpKTSALG"
app.config['RECAPTCHA_OPTIONS'] = {'theme': 'black'}


class ContactForm(Form):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    comment = TextAreaField("Comment", validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField("Submit")


@app.route("/")
def home():
    form = ContactForm()
    return render_template("wtform.html", form=form)


@app.route("/info", methods=["POST"])
def info():
    form = ContactForm(request.form)
    if request.method == "POST" and form.validate():
        username = form.username.data
        email = form.email.data
        comment = form.comment.data
#        flash("Data Submit Successfully!!!")
        return f"username: {username} <br> email: {email} <br> comment: {comment}"
    return render_template("wtform.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
