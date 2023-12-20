from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, TextAreaField, URLField, PasswordField
from wtforms.validators import InputRequired, NumberRange, Email, Length, EqualTo

class MovieForm(FlaskForm):
    title = StringField("Başlık", validators=[InputRequired()])
    director = StringField("Yönetmen", validators=[InputRequired()])
    year = IntegerField("Yıl", validators=[InputRequired(), NumberRange(min=1878, message="Geçerli bir yıl girin!")])
    submit = SubmitField("Film ekle")

class StringListField(TextAreaField):
    def _value(self):
        if self.data:
            return "\n".join(self.data)
        else:
            return ""

    def process_formdata(self, valuelist):
        if valuelist and valuelist[0]:
            self.data = [line.strip() for line in valuelist[0].split("\n")]
        else:
            self.data = []

class ExtendedMovieForm(MovieForm):
    cast = StringListField("Oyuncular")
    series = StringListField("Series")
    tags = StringListField("Etiketler")
    description = TextAreaField("Açıklama")
    video_link = URLField("Video linki")
    submit = SubmitField("Onayla")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Şifre", validators=[InputRequired(), Length(min=4, max=20, message="Şifreniz 4 ile 20 karakter arasında olmalı.")])
    confirm_password = PasswordField("Şifreyi doğrula", validators=[InputRequired(), EqualTo("password", message="Şifreler eşleşmiyor")])
    submit = SubmitField("Kayıt Ol")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Şifre", validators=[InputRequired()])
    submit = SubmitField("Giriş")