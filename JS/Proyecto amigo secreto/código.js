let amigos = [];

function CambiarTextHtml (id, texto){
    let elementoHTML = document.getElementById(id);
    elementoHTML.innerHTML=texto
}

function ObtenerNombres (){
    let Nombres = document.getElementById("amigo").value;
        // validar que no esté vacío
    if (Nombres === "") {
        console.alert("Por favor, escribe un nombre");
        return;
    }
    amigos.push(Nombres);
    LimpiarCaja();
}

function SortearAmigo(){
   let MostrarLista = document.getElementById("listaAmigos");
   MostrarLista.innerHTML="";

   if (amigos.length== 0){
    console.alert("Por favor ingresa elementos a la lista");
    return;
   }

   for (let i=0;i<amigos.length;i++){
    MostrarLista.innerHTML += "<li>" + amigos[i] + "</li>";
   }
   let aleatorio = Math.floor(Math.random() * amigos.length);
   resultado = (`El ganador es ${amigos[aleatorio]}`);
   CambiarTextHtml("resultado",resultado);
}

function LimpiarCaja(){
        document.getElementById("amigo").value = "";
    }

function MostrarLista(amigos){
    for (let i = 0; i<amigos.length; i++){
        i = document;
    }
}