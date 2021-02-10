var lista = [];
var accion = 0;

function desactivaTxt(){
  document.getElementById("sample3").style.display = "none";
  document.getElementById("lblValor").style.display = "none";
  document.getElementById("sample4").style.display = "none";
  document.getElementById("lblValor2").style.display = "none";	
  document.getElementById("ok").style.display = "none";	
}

function activaTxt(){
  if(accion != 4 && accion != 5 && accion != 6){
    document.getElementById("sample3").style.display = "block"; 
    document.getElementById("lblValor").style.display = "block";
  }
  if(accion == 3 || accion == 6){
    document.getElementById("sample4").style.display = "block";
    document.getElementById("lblValor2").style.display = "block"; 
  }
  document.getElementById("ok").style.display = "block";  
}

function desactivaBtn(){
  document.getElementById("insInicio").disabled = true;
  document.getElementById("insFinal").disabled = true;  
  document.getElementById("insPos").disabled = true;  
  document.getElementById("eliInicio").disabled = true; 
  document.getElementById("eliFinal").disabled = true;  
  document.getElementById("eliPos").disabled = true;
  
}

function activaBtn(){
  document.getElementById("insInicio").disabled = false;
  document.getElementById("insFinal").disabled = false;  
  document.getElementById("insPos").disabled = false;  
  document.getElementById("eliInicio").disabled = false; 
  document.getElementById("eliFinal").disabled = false;  
  document.getElementById("eliPos").disabled = false;
}

function insertaInicio(){
  accion = 1; //numero definido para la funcion de insertar al inicio
  desactivaBtn();
  activaTxt();
}

function insertaFinal(){
  accion = 2; //numero definido para la funcion de insertar al final
  desactivaBtn();
  activaTxt();
}

function insertaPosicion(){
  accion = 3; //numero definido para la funcion de insertar en cierta posicion
  desactivaBtn();
  activaTxt();
}

function eliminaInicio(){
  accion = 4; //numero definido para la funcion de eliminar al inicio
  desactivaBtn();
  activaTxt();
}

function eliminaFinal(){
  accion = 5; //numero definido para la funcion de eliminar al final
  desactivaBtn();
  activaTxt();
}

function eliminaPosicion(){
  accion = 6; //numero definido para la funcion de eliminar en cierta posicion
  desactivaBtn();
  activaTxt();
}

function ok(){
  var valor = document.getElementById("sample3").value;
  valor != "" ? valor = valor : valor = "elemento";
  var valor2 = document.getElementById("sample4").value;
  valor2 != "" ? valor2 = valor2 : valor2 = "elemento";
  
  if(accion == 1){ //agrega al inicio
    lista.unshift(valor);
    insCode();
    agrega(valor, null);  
  }else if(accion == 2){ //agrega al final
    lista.push(valor);
    insCode();
    agrega(valor, null);
  }else if(accion == 3){ //agregar en posicion
    if(valor2.match(/^-{0,1}\d+$/)){
      var valorInt = parseInt(valor2, 10);
      if(valor2 < 0 || valor2 > lista.length-1)
        alert("Ingrese una pocisión existente");
      else{
        lista.splice(valor2, 0, valor);
        insCode();
        agrega(valor, valor2);
      }
    }else{
      alert("Ingrese un valor numerico");
    }
    //accion = 0;
  }else if (accion == 4) { //elimina el inicio
    lista.splice(0, 1);
    insCode();
    elimina(null);
  }else if (accion == 5) {
    lista.splice(lista.length-1, 1);
    insCode();
    elimina(null);
  }else if(accion == 6){
    if(valor2.match(/^-{0,1}\d+$/)){
      var valorInt = parseInt(valor2, 10);
      if(valor2 < 0 || valor2 > lista.length-1)
        alert("Ingrese una pocisión existente");
      else{
        lista.splice(valor2, 1);
        insCode();
        elimina(valor2);
      }
    }else{
      alert("Ingrese un valor numerico");
    }
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
    newDiv.style.float = "left";
    newDiv.style.border = "groove"
    newDiv.style.borderRadius = "15px";
    //newDiv.style.position = "relative";
    var newContent = document.createTextNode(valor); 
    newDiv.appendChild(newContent); //añade texto al div creado. 

    var currentDiv = document.getElementById("lista"); 
    var ancho = lista.length * 70 + "px";
    currentDiv.style.width = ancho;

    if(accion == 1){
      currentDiv.insertBefore(newDiv, currentDiv.firstChild);
    }else if (accion == 2){
      currentDiv.appendChild(newDiv);  
    }else if(accion == 3){
      var x = document.getElementsByName("newDiv")[valor2];
      currentDiv.insertBefore(newDiv, x);
    }
    accion = 0;
}

function elimina(valor2){
    var currentDiv = document.getElementById("lista"); 
    var x = document.getElementsByName("newDiv");
    if(accion == 4){
      x[0].setAttribute("class", "delDiv");
      setTimeout(function(){aux(currentDiv, x[0])},3000);
    }else if (accion == 5) {
      var x = document.getElementsByName("newDiv");
      var y = x[x.length-1];
      y.setAttribute("class", "delDiv");
      setTimeout(function(){aux(y, null)},3000);
    }else if (accion == 6) {
      var x = document.getElementsByName("newDiv");
      var y = x[valor2];
      y.setAttribute("class", "delDiv");
      setTimeout(function(){aux(y, null)},3000);
    }
}

function aux(currentDiv, x){
  if(accion == 4)
    currentDiv.removeChild(x);
  if(accion == 5)
    currentDiv.parentNode.removeChild(currentDiv);
  if(accion == 6)
    currentDiv.parentNode.removeChild(currentDiv);

  var ancho = (lista.length) * 70 + "px";
  currentDiv.style.width = ancho;
  
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
      accion = 2;
      agrega(listaAux[i], null);
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
  if(accion == 2){
    var cons = "int InsercionFinLista(Lista *lista, Elemento *actual, char *dato){<br>"+
                "&nbsp&nbspElemento *nuevo_elemento;<br>"+
                "&nbsp&nbspif((nuevo_elemento = (Elemento *)malloc(sizeof(Elemento)))==NULL)<br>"+
                    "&nbsp&nbsp&nbsp&nbspreturn -1;<br>"+
                "&nbsp&nbspif((nuevo_elemento->dato = (char *)malloc(50*sizeof(char)))==NULL)<br>"+
                    "&nbsp&nbsp&nbsp&nbspreturn -1;<br>"+
                "&nbsp&nbspstrcpy(nuevo_elemento->dato,dato);<br>"+
                "&nbsp&nbspactual->siguiente = nuevo_elemento;<br>"+
                "&nbsp&nbspnuevo_elemento->siguiente = NULL;<br>"+
                "&nbsp&nbsplista->fin = nuevo_elemento;<br>"+
                "&nbsp&nbsplista->tamano++;<br>"+
                "&nbsp&nbspreturn 0;<br>"+
                "}";
  }
  if(accion == 3){
    var cons = "int InsercionLista(Lista *lista, char *dato, int pos){<br>"+
                "&nbsp&nbspif(lista->tamano <2)<br>"+
                    "&nbsp&nbsp&nbsp&nbspreturn -1;<br>"+
                "&nbsp&nbspif(pos<1 || pos >=1)<br>"+
                    "&nbsp&nbsp&nbsp&nbspreturn -1;<br>"+
                "&nbsp&nbspElemento *actual;<br>"+
                "&nbsp&nbspElemento *nuevo_elemento;<br>"+
                "&nbsp&nbspint i;<br>"+
                "&nbsp&nbspif((nuevo_elemento=(Elemento *)malloc(sizeof(Elemento)))==NULL)"+
                        "&nbsp&nbsp&nbsp&nbspreturn -1;<br>"+
                "&nbsp&nbspif((nuevo_elemento->dato=(char *)malloc(50*sizeof(char)))==NULL)"+
                        "&nbsp&nbsp&nbsp&nbspreturn -1;<br>"+
                "&nbsp&nbspactual = actual->siguiente;<br>"+
                "&nbsp&nbspfor(i = 1; i<pos; ++i )"+
                        "&nbsp&nbsp&nbsp&nbspactual=actual->siguiente;<br>"+
                "&nbsp&nbspif(actual->siguiente == NULL)"+
                        "&nbsp&nbsp&nbsp&nbspreturn -1;<br>"+
                "&nbsp&nbspstrcpy(nuevo_elemento->dato, dato);<br>"+
                "}<br>";
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
  if(accion == 5){
    var cons = "int EliminarEnLista(Lista *lista, int pos){<br>"+
                "&nbsp&nbspif(lista->tamano <= 1 ||  pos < 1 || pos >= lista->tamano)<br>"+
                    "&nbsp&nbsp&nbsp&nbspreturn -1;<br>"+
                "&nbsp&nbspint i;<br>"+
                "&nbsp&nbspElemento *actual;<br>"+
                "&nbsp&nbspElemento *sup_elemento;<br>"+
                "&nbsp&nbspactual = lista->inicio;<br>"+
                "&nbsp&nbspfor(i=1;i<pos;++i)<br>"+
                    "&nbsp&nbsp&nbsp&nbspactual = actual ->siguiente;<br>"+
                "&nbsp&nbspsup_elemento = actual->siguiente;<br>"+
                "&nbsp&nbspactual->siguiente = actual->siguiente->siguiente;<br>"+
                "&nbsp&nbspif(actual->siguiente==NULL)<br>"+
                    "&nbsp&nbsplista->fin = actual;<br>"+
                "&nbsp&nbspfree(sup_elemento->dato);<br>"
                "&nbsp&nbspfree(sup_elemento);<br>"+
                "&nbsp&nbsplista->tamano--;<br>"+
                "&nbsp&nbspreturn 0;<br>"+
                "&nbsp&nbsp}";
  }
  if(accion == 6){
    var cons = "int EliminarEnLista(Lista *lista, int pos){<br>"+
                "&nbsp&nbspif(lista->tamano <= 1 ||  pos < 1 || pos >= lista->tamano)<br>"+
                    "&nbsp&nbsp&nbsp&nbspreturn -1;<br>"+
                "&nbsp&nbspint i;<br>"+
                "&nbsp&nbspElemento *actual;<br>"+
                "&nbsp&nbspElemento *sup_elemento;<br>"+
                "&nbsp&nbspactual = lista->inicio;<br>"+
                "&nbsp&nbspfor(i=1;i<pos;++i)<br>"+
                    "&nbsp&nbsp&nbsp&nbspactual = actual ->siguiente;<br>"+
                "&nbsp&nbspsup_elemento = actual->siguiente;<br>"+
                "&nbsp&nbspactual->siguiente = actual->siguiente->siguiente;<br>"+
                "&nbsp&nbspif(actual->siguiente==NULL)<br>"+
                    "&nbsp&nbsplista->fin = actual;<br>"+
                "&nbsp&nbspfree(sup_elemento->dato);<br>"
                "&nbsp&nbspfree(sup_elemento);<br>"+
                "&nbsp&nbsplista->tamano--;<br>"+
                "&nbsp&nbspreturn 0;<br>"+
                "&nbsp&nbsp}";
  }
  code.innerHTML = cons;
}
