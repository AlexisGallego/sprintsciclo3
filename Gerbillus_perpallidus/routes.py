from os import error
from flask import render_template, flash, redirect, url_for, request
from Gerbillus_perpallidus import app
from Gerbillus_perpallidus import forms
import sqlite3

def sqlite_connection():
    try:
        db = sqlite3.connect('Gerbillus_perpallidus\db\db.sqlite')
        return db
    
    except error:
        print(error)

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE usuarios( email text PRYMARY KEY, contrasena text, usuario text, ciudad text)")
    connection.commit()

def insert_data(form):
    insertar = sqlite_connection()
    cursor = insertar.cursor()
    sql = "INSERT INTO usuarios (email, contrasena, usuario, ciudad) VALUES (?,?,?,?)"
    cursor.execute(sql, [form.correo_electronico.data, form.contrasena.data, form.usuario.data, form.ciudad.data])
    insertar.commit()
    insertar.close()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registrar_usuario():
    form = forms.registro()
    if form.validate_on_submit(): 

        insert_data(form)
        flash('usuario registrado')
        return redirect(url_for('index'))
    else:
        flash('no se ha podido registrar el usuario')

    return render_template('registro.html',  form = form)

@app.route('/mensajes')
def mensajes():
    return redirect('mensajes.html')

@app.route('/notificaciones')
def notificaciones():
    return redirect('notificaciones.html')    

#Vistas Sofia
@app.route('/ingresar')
def ingresar():
    return redirect('ingresar.html')   

@app.route('/perfil')
def perfil():
    return redirect('perfil.html')   

@app.route('/post')
def post():
    return redirect('post.html') 

#Vistas Lina
@app.route('/login')
def login():
    return redirect('login.html')
 
@app.route('/recuperarcontra')
def recuperar_contraseña():
    return redirect('recuperarcontra.html') 

@app.route('/revisarusuario')
def revisar_usuario():
    return redirect('revisarusuario.html')

@app.route('/buscarusuarios')
def buscarusuarios():
    return redirect('buscarusuarios.html')      