from wtforms import StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import Email, InputRequired, EqualTo, Length
from wtforms.fields.html5 import DateField, EmailField
from wtforms.fields.simple import SubmitField
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class registro(FlaskForm):
    correo_electronico = EmailField('correo electronico',\
    validators=[Email(), InputRequired()])

    contraseña = PasswordField('contraseña', 
    validators=[InputRequired(message='este campo es requerido'), Length(min=6, max=20, 
    message='la contraseña debe tener entre 6 y 20 caracteres')])

    confirmar_contraseña = PasswordField('confirmar contraseña',\
    validators=[InputRequired(), EqualTo('contraseña', 
    message='las contraseñas no coinciden')])
    
    usuario = StringField('usuario', 
    validators=[InputRequired()])

    fecha_nacimiento = DateField('fecha nacimiento', format='%y/%m/%d', 
    validators=[InputRequired()])

    ciudad = StringField('ciudad', 
    validators=[InputRequired()])

    gustos = StringField()
    registrarse = SubmitField('registrarse')

    def email(email):
        if re.fullmatch(regex, email):
            return ('correo electronico valido')
        else:
            return ('correo electronico no valido') 