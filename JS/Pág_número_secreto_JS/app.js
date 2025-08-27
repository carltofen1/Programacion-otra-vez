let númeroSecreto = 0;
let númint = 0;
function asignarTextoElemento(elemento,texto){
    let elementoHTML = document.querySelector(elemento);
    elementoHTML.innerHTML = texto;
    return
}

function verificarIntento() {
    let númU = parseInt(document.getElementById("númU").value);
    
    if (númU === númeroSecreto){
        asignarTextoElemento("p",`Haz acertado el número en ${númint} ${(númint=== 1) ? "intento" : "intentos"}`);
        document.getElementById("reiniciar").removeAttribute("disable");
    } else {
        //El usuario no acertó
        if(númU>númeroSecreto){
            asignarTextoElemento("p","El número secreto es menor");
        } else {
            asignarTextoElemento("p","El número secreto es mayor");

        }
        númint++;
        limpiarCaja();
    }
    return;
}

function limpiarCaja(){ 
    document.getElementById("númU").value = "";
}

function generarNúmeroSecreto(){
    return Math.floor(Math.random()*10)+1;
}

function condicionesIniciales(){
    asignarTextoElemento("h1","Juego del núnmero secreto");
    asignarTextoElemento("p","Indica un número del 1 al 10");
    //Generar el número aleatorio
    númeroSecreto = generarNúmeroSecreto();
    //Inicializar el número de intentos
    númint = 1;
}

function reiniciarJuego(){
    //Limpiamos la caja
      limpiarCaja();
    //Indicar mensaje de intervalo de números
    condicionesIniciales();
    //Desabilitar el botón de nuevo juego
    document.getElementById("reiniciar").setAttribute("enable");
    
}

condicionesIniciales();

