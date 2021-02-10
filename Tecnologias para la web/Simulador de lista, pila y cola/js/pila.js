var lista = [];
var accion = 0;

function desactivaTxt(){
  document.getElementById("sample3").style.display = "none";
  document.getElementById("lblValor").style.display = "none";
  document.getElementById("ok").style.display = "none";	
}

function activaTxt(){
  if(accion != 4){
    document.getElementById("sample3").style.display = "block"; 
    document.getElementById("lblValor").style.display = "block";
  }
  document.getElementById("ok").style.display = "block";  
}

function desactivaBtn(){
  document.getElementById("insInicio").disabled = true;
  document.getElementById("eliInicio").disabled = true; 
}

function activaBtn(){
  document.getElementById("insInicio").disabled = false;
  document.getElementById("eliInicio").disabled = false;  
}

function insertaInicio(){
  accion = 1; //numero definido para la funcion de insertar al inicio
  desactivaBtn();
  activaTxt();
}

function eliminaInicio(){
  accion = 4; //numero definido para la funcion de eliminar al inicio
  desactivaBtn();
  activaTxt();
}

function ok(){
  var valor = document.getElementById("sample3").value;
  valor != "" ? valor = valor : valor = "elemento";
  
  if(accion == 1){ //agrega al inicio
    lista.unshift(valor);
    insCode();
    agrega(valor, null);  
  }else if (accion == 4) { //elimina el inicio
    lista.splice(0, 1);
    insCode();
    elimina(null);
  }
  activaBtn();  
  desactivaTxt();
}

function agrega(valor, valor2){
    var newDiv = document.createElement("div"); 
    newDiv.style.background = '#c2b0c9';
    newDiv.style.width = "60px"
    newDiv.style.height = "40px";
    newDiv.setAttribute("name", "newDiv");
    newDiv.setAttribute("class", "newDiv");
    newDiv.style.border = "groove"
    newDiv.style.borderRadius = "15px";
    var newContent = document.createTextNode(valor); 
    newDiv.appendChild(newContent); //añade texto al div creado. 

    var currentDiv = document.getElementById("lista"); 
    var ancho = lista.length * 70 + "px";
    currentDiv.style.width = ancho;

    if(accion == 1){
      currentDiv.insertBefore(newDiv, currentDiv.firstChild);
    }
    accion = 0;
}

function elimina(valor2){
    var currentDiv = document.getElementById("lista"); 
    var ancho = (lista.length) * 70 + "px";
    currentDiv.style.width = ancho;

    if(accion == 4){
      currentDiv.firstChild.setAttribute("class", "delDiv");
      setTimeout(function(){aux(currentDiv)},3000);
    }
}

function aux(currentDiv){
  if(accion == 4)
    currentDiv.removeChild(currentDiv.firstChild);
  accion = 0;
}

function guardaLista(){
  if(lista.length>0){
    var listaCadena="";

    for (var i=0; i<lista.length; i++){
      if(i!=lista.length-1)
        listaCadena = listaCadena + lista[i] + "-";
      else
        listaCadena = listaCadena + lista[i];
    }  
    alert(listaCadena);
    document.cookie = "Lista ="+listaCadena+";";
    alert("guardado"); 
  }else{
    alert("lista vacia");   
  }
}

function abrirLista(){
  var cookies = document.cookie;
  if(cookies){
    var listaAux = cookies.split("-");
    listaAux[0] = listaAux[0].charAt(6);
    var currentDiv = document.getElementById("lista"); 
    if ( currentDiv.hasChildNodes() )
      while ( currentDiv.childNodes.length >= 1 )
        currentDiv.removeChild( currentDiv.firstChild );
    for(var i = 0; i<listaAux.length; i++){
      accion = 1;
      agrega(listaAux[listaAux.length-i-1], null);
    }
  }
  accion = 0; 
}

function insCode(){
  var code = document.getElementById("code");
  if(accion == 1){
    var cons = "int InsercionInicioLista(Lista *lista, char *dato){<br>"+
                "&nbsp&nbspElemento *nuevo_elemento;<br>"+
                "&nbsp&nbspif((nuevo_elemento = (Elemento *)malloc(sizeof(Elemento)))==NULL)<br>"+
                    "&nbsp&nbsp&nbsp&nbspreturn -1;<br>"+
                "&nbsp&nbspif((nuevo_elemento->dato = (char *)malloc(50*sizeof(char)))==NULL)<br>"+
                    "&nbsp&nbsp&nbsp&nbspreturn -1;<br>"+
                "&nbsp&nbspstrcpy(nuevo_elemento->dato, dato);<br>"+
                "&nbsp&nbspnuevo_elemento->siguiente = lista->inicio;<br>"+
                "&nbsp&nbsplista->inicio=nuevo_elemento;<br>"+
                "&nbsp&nbsplista->tamano++;<br>"+
                "&nbsp&nbspreturn 0;<br>"+
                "&nbsp&nbsp}<br>";
  }
  if(accion == 4){
    var cons = "int EliminarInicio(Lista *lista){<br>"+
                "&nbsp&nbspif(lista->tamano == 0)<br>"+
                    "&nbsp&nbsp&nbsp&nbspreturn -1;<br>"+
                "&nbsp&nbspElemento *sup_elemento;<br>"+
                "&nbsp&nbspsup_elemento = lista->inicio;<br>"+
                "&nbsp&nbsplista->inicio=lista->inicio->siguiente;<br>"+
                "&nbsp&nbspif(lista->tamano==1)<br>"+
                    "&nbsp&nbsp&nbsp&nbsplista->fin = NULL;<br>"+
                "&nbsp&nbspfree(sup_elemento->dato);<br>"+
                "&nbsp&nbspfree(sup_elemento);<br>"+
                "&nbsp&nbsplista->tamano--;<br>"+
                "&nbsp&nbspreturn 0;<br>"
                "}";
             
  }
  code.innerHTML = cons;
}
