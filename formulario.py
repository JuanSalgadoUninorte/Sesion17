# Documento => StringField
# nombre => StringField
# cliclo => SelectField
# sexo => StringField
# estado => BooleanField
# BotonCrear => SubmitField
# BotonActualizar => SubmitField
# BotonEliminar => SubmitField
# BotonVisualizar => SubmitField
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class formularioI(FlaskForm):
    documento = StringField("Documento")
    nombre = StringField("Nombre")
    # ciclo = SelectField("Ciclo", choices=[("Ciclo 1"), ("Ciclo 2"), ("Ciclo 3"), ("Ciclo 4"), ("Ciclo 5")])
    ciclo = SelectField("Ciclo")
    sexo = StringField("Sexo")
    estado = BooleanField("Estado")
    botonCrear = SubmitField("botonCrear", render_kw={"onmouseover": "guardar()"})
    botonEliminar = SubmitField("botonEliminar", render_kw={"onmouseover": "eliminar()"})
    botonActualizar = SubmitField("botonActualizar", render_kw={"onmouseover": "actualizar()"})
    botonVisualizar = SubmitField("botonVisualizar", render_kw={"onmouseover": "visualizar()"})
    botonListar = SubmitField("listarTodos", render_kw={"onmouseover": "listarTodo()"})