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