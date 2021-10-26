from os import error
from flask import render_template, flash, redirect, url_for, request
from Gerbillus_perpallidus import app
from Gerbillus_perpallidus import forms
import sqlite3

def sqlite_connection():
    try:
        db = sqlite3.connect('db.sqlite')
        return db
    
    except error:
        print(error)

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE usuarios(email text PRYMARY KEY, contraseña text, usuario text, nacimiento date, ciudad text)")
    connection.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registrar_usuario():
    form = forms.registro()
    if form.validate_on_submit():
        flash('todo salio perfect')
        return redirect(url_for('index'))
    else:
        flash

    return render_template('registro.html',  form = form)

@app.route('/mensajes')
def mensajes():
    return redirect('mensajes.html')

@app.route('/notificaciones')
def notificaciones():
    return redirect('notificaciones.html')    

#Vistas Sofia
@app.route('/ingresar')
def notificaciones():
    return redirect('ingresar.html')   

@app.route('/perfil')
def notificaciones():
    return redirect('perfil.html')   

@app.route('/post')
def notificaciones():
    return redirect('post.html') 

#Vistas Lina
@app.route('/login')
def notificaciones():
    return redirect('login.html')
 
@app.route('/recuperarcontra')
def notificaciones():
    return redirect('recuperarcontra.html') 

@app.route('/revisarusuario')
def notificaciones():
    return redirect('revisarusuario.html') 
  