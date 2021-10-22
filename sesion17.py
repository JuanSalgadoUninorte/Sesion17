import sqlite3
variableNombreBD = "Estudiantes.db"

def seleccion(variableSQL):
    with sqlite3.connect(variableNombreBD) as conn:
        cur = conn.cursor()
        variableResultado = cur.execute(variableSQL).fetchall()
        #aquí se hace con fetch all la consulta desde uno hasta ....
        #estos one y all son solo de consulta
        return variableResultado

def accion(variableSQL):
    with sqlite3.connect(variableNombreBD) as conn:
        cur = conn.cursor()
        variableResultado = cur.execute(variableSQL).rowcount()
        #con rowcount se traerán los datos para poder editar o crear
        if variableResultado != 0:
            conn.commit()
        return variableResultado
        #devuelve un entero diciendo la cantidad de registros afectados