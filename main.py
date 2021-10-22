import re
from sqlite3.dbapi2 import Row
from flask import *
import sqlite3
import hashlib
from markupsafe import escape
import os
from werkzeug.security import check_password_hash, generate_password_hash
from flask_wtf import form
from sesion17 import *
variableGlobalVacia = None
ciclos = ""

from formulario import formularioI

app = Flask(__name__)

app.secret_key = os.urandom(24)



#componente practico sesión 14
@app.route('/rutaDescargaPdf/', methods=["POST", "GET"])
def descargarPdf():
    return send_file( "resources/documento.pdf", as_attachment=True )

@app.route('/rutaDescargaImg/', methods=["POST", "GET"])
def descargarImg():
    return send_file( "resources/analisis.jpg", as_attachment=True )

@app.route('/cerrarSesion/', methods=["POST", "GET"])
def cerrarSesion():
    if "usuario" in session:#aquí amarro para que él esté logueado para que pueda entrar a los contenidos, sino, no entra
        session.pop("usuario", None)
        return render_template("logOut.html")
    else:
        return "La sesión ya ha sido cerrada o nunca fue abierta"

#fin componente 14

# @app.route('/', methods=["GET", "POST"])
# def index():
#     form = formularioI()
#     return render_template('formulario.html', form = form)#Controles creados en .py
#     #formulario referenciado form = form al que va

#Segunda versión sesión 14 solo este método
# @app.route('/', methods=["GET", "POST"])
# def index():
#     if "usuario" == session:#Sino inicia no entra :((
#         form = formularioI()
#         return render_template('formulario.html', form = form)
#     else:
#         return "Acción no permitida, Inicie sesión primero, <a href='/experimento/'>Redirección</a>"

# @app.route('/estudiante/guardar/', methods=["POST"])
# def guardar():
#     if "usuario" in session:
#         form = formularioI()#Instancia de la clase en formulario.py
#         if request.method == "POST":
#             docum = form.documento.data#Recupera datos
#             nombr = form.nombre.data
#             cicl = form.ciclo.data
#             sex = form.sexo.data
#             estad = form.estado.data
#             with sqlite3.connect("Estudiantes.db") as conn:#Manejador de contexto ->conexion
#                 cur = conn.cursor()#manipula la db
#                 #se va a usar el PreparedStatement
#                 #Acciones
#                 cur.execute("INSERT INTO Estudiantes (Documento, Nombre, Ciclo, Sexo, Estado) VALUES (?,?,?,?,?)", (docum, nombr, cicl, sex, estad))
#                 conn.commit()#Confirmación de inserción de datos :)
#                 return "¡Datos guardados exitosamente!"
#         return "No se pudo guardar T_T"
#     else: 
#         return "Inicie sesión primeramente para acceder a este contenido"

# @app.route('/estudiante/visualizar/', methods=["POST"])
# def visualizar():
#     if "usuario" in session:
#         form = formularioI()
#         if request.method == "POST":
#             docum = form.documento.data
#             with sqlite3.connect("Estudiantes.db") as conn:#conexion
#                 conn.row_factory = sqlite3.Row
#                 cur = conn.cursor()#manipula la db
#                 cur.execute("SELECT * FROM Estudiantes WHERE Documento = ?", [docum])
#                 row = cur.fetchone()
#                 if row is None:
#                     return "No se encontró el registro en la base de datos...... :'( "
#                 return render_template("vistaEstudiante.html", row = row)
#         return "Error"
#     else:
#         return "Inicie sesión primeramente para acceder a este contenido"

# @app.route('/estudiante/eliminar/', methods=["POST"])
# def eliminar():
#     if "usuario" in session:
#         form = formularioI()
#         if request.method == "POST":
#             docum = form.documento.data
#             with sqlite3.connect("Estudiantes.db") as conn:
#                 conn.row_factory = sqlite3.Row
#                 cur = conn.cursor()#manipula la db
#                 cur.execute("DELETE FROM Estudiantes WHERE Documento = ?", [docum])
#                 if conn.total_changes > 0:
#                     return "Estudiante borrado ^v^"
#                 return render_template("formulario.html")
#         return "Error"
#     else:
#         return "Inicie sesión primeramente para acceder a este contenido"

# @app.route('/estudiante/actualizar/', methods=["POST"])
# def actualizar():
#     if "usuario" in session:
#         form = formularioI()#Instancia de la clase en formulario.py
#         if request.method == "POST":
#             docum = form.documento.data#Recupera datos
#             nombr = form.nombre.data
#             cicl = form.ciclo.data
#             sex = form.sexo.data
#             estad = form.estado.data
#             with sqlite3.connect("Estudiantes.db") as conn:#Manejador de contexto ->conexion
#                 cur = conn.cursor()#manipula la db
#                 #se va a usar el PreparedStatement
#                 #Acciones
#                 cur.execute("UPDATE Estudiantes SET Nombre = ?, Ciclo = ?, Sexo = ?, Estado = ? WHERE Documento = ?;", [nombr, cicl, sex, estad, docum])
#                 conn.commit()#Confirmación de inserción de datos :)
#                 return "¡Datos actualizados exitosamente ^v^!"
#         return "No se pudo actualizar T_T"
#     else:
#         return "Inicie sesión primeramente para acceder a este contenido"

#Desde aquí comenzará la clase de la sesión 13
#Ojo las librerías son diferentes, hay más
@app.route("/experimento/", methods=["GET", "POST"])
def experimento():
    return render_template("usuario.html")

# @app.route("/experimentoBusqueda/", methods=["GET", "POST"])#INJECCION SQL
# def experimento2busqueda():
#     if "usuario" in session:
#         usuario2 = request.form["usuario"]
#         contrasena2 = request.form["contrasena"]
#         with sqlite3.connect("Estudiantes.db") as conn:#Manejador de contexto ->conexion
#             cur = conn.cursor()#manipula la db
#             cur.execute("SELECT * FROM Usuarios WHERE Usuario= ? AND Clave = ?", [usuario2, contrasena2])
#             #cur.execute("SELECT * FROM Usuarios WHERE Usuario = '"+usuario2+"' AND Clave = '"+contrasena2+"'; ")
#             row = cur.fetchone()
#             if row is None:
#                 return "No se encontró el registro en la base de datos...... :'( "
#             else: 
#                 return "Usuario logueado :)"
#     else:
#         return "Inicie sesión primeramente para acceder a este contenido"
        #return "Error"

@app.route("/experimentoSEGUNDO/", methods=["GET", "POST"])#INJECCION SCRIPT tipo XSS
#Ese es el injección de XSS<script> while (true){console.log("1")}</script>
def experimentoSEGUNDO():
    return render_template("vistaH.html")

@app.route("/experimentoSEGUNDO2/", methods=["GET", "POST"])
def experimentoSEGUNDO2():
    #texto = request.form["datos"]
    texto = escape(request.form["datos"])#LÍNEA DE PROTECCIÓN DE DATOS X = escape(X.X["X"])
    return texto

#encriptación con md5
# @app.route("/experimento3/", methods=["GET", "POST"])#Ataque de diccionario
# def experimento3():
#     if request.method == "POST":
#         usuario2 = request.form["usuario"]
#         contrasena2 = request.form["contrasena"]
#         variableX = hashlib.md5(contrasena2.encode())
#         #Es lo mismo que variableX = hashlib.md5(contrasena2.encode()).hexdigest()
#         variableY = variableX.hexdigest()    
#         with sqlite3.connect("Estudiantes.db") as conn:#Manejador de contexto ->conexion
#                 cur = conn.cursor()#manipula la db
#                 #se va a usar el PreparedStatement
#             #Acciones
#                 cur.execute("INSERT INTO Usuarios (Usuario, Clave) VALUES (?,?)", (usuario2, variableY))
#                 conn.commit()#Confirmación de inserción de datos :)
#                 return "¡Datos guardados exitosamente!"
#         return "No se pudo guardar T_T"

#SESION 14 CAMBIOS :)
#encriptacion con hash
@app.route("/experimento3/", methods=["GET", "POST"])
def experimento3():
    if request.method == "POST":
        usuario2 = request.form["usuario"]
        contrasena2 = request.form["contrasena"]
        variablez = generate_password_hash(contrasena2)
        with sqlite3.connect("Estudiantes.db") as conn:#Manejador de contexto ->conexion
            cur = conn.cursor()#manipula la db
            #se va a usar el PreparedStatement
            #Acciones
            cur.execute("INSERT INTO Usuarios (Usuario, Clave) VALUES (?,?)", (usuario2, variablez))
            conn.commit()#Confirmación de inserción de datos :)
            return "¡Datos guardados exitosamente!"
    return "Error"
    

# #Consulta con hash para iniciar sesión v1
# @app.route("/experimentoConHash/", methods=["GET", "POST"])
# def experimentoHash():
#     usuario2 = request.form["usuario"]
#     contrasena2 = request.form["contrasena"]
#     with sqlite3.connect("Estudiantes.db") as conn:#Manejador de contexto ->conexion
#         cur = conn.cursor()#manipula la db
#         #mala forma
#         #cur.execute("SELECT * FROM Usuarios WHERE Usuario= ? AND Clave = ?", [usuario2, contrasena2])
#         #buena forma
#         varibleVector = cur.execute(f"SELECT Clave FROM Usuarios WHERE Usuario = '{usuario2}'").fetchone()
#         #solo consulta un campo
#         if varibleVector != None:
#             variableInterna = varibleVector[0]
#             if check_password_hash(variableInterna, contrasena2):
#                 session["usuario"] = usuario2
#                 form = formularioI()
#                 return render_template("formulario.html", form=form)#form = form significa todos los datos que van a pasar
#             else: 
#                 return "Usuario y clave falsas o inexactas, vuelva a intentar o llamamos a la policía :)"
#     return "Error en la conexión y proceso, revise por favor :'("

#Consulta con hash para iniciar sesión v2
@app.route("/experimentoConHash/", methods=["GET", "POST"])
def experimentoHash():
    usuario2 = request.form["usuario"]
    contrasena2 = request.form["contrasena"]
    with sqlite3.connect("Estudiantes.db") as conn:#Manejador de contexto ->conexion
        cur = conn.cursor()#manipula la db
        #mala forma
        #cur.execute("SELECT * FROM Usuarios WHERE Usuario= ? AND Clave = ?", [usuario2, contrasena2])
        #buena forma
        varibleVector = cur.execute(f"SELECT Clave FROM Usuarios WHERE Usuario = '{usuario2}'").fetchone()
        #solo consulta un campo
        if varibleVector != None:
            variableInterna = varibleVector[0]
            session.clear()
            if check_password_hash(variableInterna, contrasena2):
                session["usuario"] = usuario2
                form = formularioI()
                print(ciclos)
                return render_template("formulario.html", form=form, usuario2=usuario2, ciclos=ciclos)#form = form significa todos los datos que van a pasar
            else: 
                return ("Usuario y clave falsas o inexactas, vuelva a intentar o llamamos a la policía :)")
    return "Error en la conexión y proceso, revise por favor :'("

# #SESION 16
# #No lleva paréntesis
# @app.before_request#El método se llama beforeRequest
# def conBeforeRequest():
#     session.get("usuario")#Quiere guardar la información, puede ser cualquier cosa
#     if session.get("usuario") is None:
#         global variableGlobalVacia#sI TIENE ALGO ASÍGNELE ALGO
#         variableGlobalVacia = "login"
#     else:
#         variableGlobalVacia = None#SINO VACÍELA 

# @app.route('/', methods=["GET", "POST"])#Aunque se esté en la ruta principal, si no está logueado se redireccionará a el logIn
# def index():
#     global variableGlobalVacia
#     if variableGlobalVacia is not None:
#         return redirect(url_for('experimento'))
#     form = formularioI()
#     return render_template('formulario.html', form = form)

@app.route("/experimentoBusqueda/", methods=["GET", "POST"])#INJECCION SQL
def experimento2busqueda():
    usuario2 = request.form["usuario"]
    contrasena2 = request.form["contrasena"]
    with sqlite3.connect("Estudiantes.db") as conn:#Manejador de contexto ->conexion
        cur = conn.cursor()#manipula la db
        cur.execute("SELECT * FROM Usuarios WHERE Usuario= ? AND Clave = ?", [usuario2, contrasena2])
        #cur.execute("SELECT * FROM Usuarios WHERE Usuario = '"+usuario2+"' AND Clave = '"+contrasena2+"'; ")
        row = cur.fetchone()
        if row is None:
            return "No se encontró el registro en la base de datos...... :'( "
        else: 
            return "Usuario logueado :)"

@app.route('/estudiante/actualizar/', methods=["POST"])
def actualizar():
    form = formularioI()#Instancia de la clase en formulario.py
    if request.method == "POST":
        docum = form.documento.data#Recupera datos
        nombr = form.nombre.data
        cicl = form.ciclo.data
        sex = form.sexo.data
        estad = form.estado.data
        with sqlite3.connect("Estudiantes.db") as conn:#Manejador de contexto ->conexion
            cur = conn.cursor()#manipula la db
            #se va a usar el PreparedStatement
            #Acciones
            cur.execute("UPDATE Estudiantes SET Nombre = ?, Ciclo = ?, Sexo = ?, Estado = ? WHERE Documento = ?;", [nombr, cicl, sex, estad, docum])
            conn.commit()#Confirmación de inserción de datos :)
            return "¡Datos actualizados exitosamente ^v^!"
    return "No se pudo actualizar T_T"

@app.route('/estudiante/eliminar/', methods=["POST"])
def eliminar():
    form = formularioI()
    if request.method == "POST":
        docum = form.documento.data
        with sqlite3.connect("Estudiantes.db") as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()#manipula la db
            cur.execute("DELETE FROM Estudiantes WHERE Documento = ?", [docum])
            if conn.total_changes > 0:
                return "Estudiante borrado ^v^"
            return render_template("formulario.html")
    return "Error"
    
@app.route('/estudiante/visualizar/', methods=["POST"])
def visualizar():
    form = formularioI()
    if request.method == "POST":
        docum = form.documento.data
        with sqlite3.connect("Estudiantes.db") as conn:#conexion
            conn.row_factory = sqlite3.Row#Gestiona la db
            cur = conn.cursor()#manipula la db
            cur.execute("SELECT * FROM Estudiantes WHERE Documento = ?", [docum])
            row = cur.fetchone()#La consulta es asignada y procesada
            #fetchone solo trae un registro específico
            #fetchall trae varios registros
            if row is None:
                return "No se encontró el registro en la base de datos...... :'( "
            return render_template("vistaEstudiante.html", row = row)
    return "Error"

@app.route('/estudiante/guardar/', methods=["POST"])
def guardar():
    form = formularioI()#Instancia de la clase en formulario.py
    if request.method == "POST":
        docum = form.documento.data#Recupera datos
        nombr = form.nombre.data
        cicl = form.ciclo.data
        sex = form.sexo.data
        estad = form.estado.data
        with sqlite3.connect("Estudiantes.db") as conn:#Manejador de contexto ->conexion
            cur = conn.cursor()#manipula la db
            #se va a usar el PreparedStatement
            #Acciones
            cur.execute("INSERT INTO Estudiantes (Documento, Nombre, Ciclo, Sexo, Estado) VALUES (?,?,?,?,?)", (docum, nombr, cicl, sex, estad))
            conn.commit()#Confirmación de inserción de datos :)
            return "¡Datos guardados exitosamente!"
    return "No se pudo guardar T_T"

#SESION 17
@app.route('/listarTodos/', methods=["GET", "POST"])
def listarTodos():
    if request.method == "POST":
        SQL = "SELECT * FROM Estudiantes"
        fISeleccion = seleccion(SQL)
        #print(fISeleccion)
        return render_template("listarTodos.html", fISeleccion=fISeleccion)
    return render_template("listarTodos.html")

#No lleva paréntesis
@app.before_request#El método se llama beforeRequest
#decorador que cuando se hacen peticiones, primeramente viene a cumplir esto
#y luego si se puede acceder al contenido
def conBeforeRequest():
    global ciclos
    # with sqlite3.connect("Estudiantes.db") as conn:
    #     conn.row_factory = sqlite3.Row
    #     cur = conn.cursor()
    #     cur.execute("SELECT DISTINCT Ciclo FROM Estudiantes")
    #     ciclos = cur.fetchall()
    SQL = "SELECT DISTINCT Ciclo FROM Estudiantes"
    ciclos = seleccion(SQL)
    print(ciclos)
    if "usuario" not in session and request.endpoint in ["listarTodos", "experimentoConHash", "experimento2Busqueda", "actualizar", "eliminar", "visualizar", "guardar", "index"]:
        return redirect(url_for("experimento"))
        
@app.route('/', methods=["GET", "POST"])#Aunque se esté en la ruta principal, si no está logueado se redireccionará a el logIn
def index():
    form = formularioI()
    return render_template('formulario.html', form = form)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=443, ssl_context=("micertificado.pem", "llaveprivada.pem"), debug=True)