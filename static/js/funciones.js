function guardar(){
    document.getElementById("IdFormulario").action="/estudiante/guardar/";
}
function visualizar(){
    document.getElementById("IdFormulario").action="/estudiante/visualizar/";
}
function eliminar(){
    document.getElementById("IdFormulario").action="/estudiante/eliminar/";
}
function actualizar(){
    document.getElementById("IdFormulario").action="/estudiante/actualizar/";
}
//Función de la sesión 13
function otra(){
    document.getElementById("formularioA").action="/experimento3/";
}
//funcion de la sesion 14
function iniciarSesion(){
    document.getElementById("formularioA").action="/experimentoConHash/";
}
//funcion de la sesion 17
function listarTodo(){
    document.getElementById("IdFormulario").action="/listarTodos/";
}