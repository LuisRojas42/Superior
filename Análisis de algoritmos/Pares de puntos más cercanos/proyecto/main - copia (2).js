let aIniciado = false;
let colorCuadro = 255;
let colorLimpiar = "#001b48";
let colorLimpiarRGB = [0, 27, 72];
let azul0Rgb = [0, 27, 72];
let azul1Rgb = [2, 69, 122];
let azul2Rgb = [1, 138, 190];
let azul3Rgb = [151, 202, 219];
let azul4Rgb = [214, 232, 238];
let tooltip1 = document.getElementsByClassName("tooltiptext")[1];
let tooltip2 = document.getElementsByClassName("tooltiptext")[0];
tooltip1.classList.remove("tooltiptext");

let colorliniaComparRGB = [214, 232, 238];
let checkBoxTuto = document.getElementById("checkTuto");
let ejecutaDicaticamente = false;
let pasos = 0;
let botonSiguiente = document.getElementById("botonAdelante");
let botonInicio = document.getElementById("botonIniciar");
let botonReiniciar = document.getElementById("botonReiniciar");
let botonTuto = document.getElementById("botonTuto");
let pComentarios = document.getElementById("pComentarios");
let divTuto = document.getElementById("divTuto");
let imagen = divTuto.children[0];
let video = divTuto.children[1];
let flagTuto = false;

const fpsCount = 8;
let P = [];
let PxGlobal = [];
// Esta función se ejecuta una vez antes de dibujar algo en pantalla.
function setup() {
  let canvas = createCanvas(750, 550);
  canvas.parent("canvasTag");

  //frameRate(fpsCount);
  //nFrame = 0;
  fill("#001b48");

  rect(0, 0, width, height);
}

function sleep(milis) {
  return new Promise((resolve) => setTimeout(resolve, milis));
}

function dibujarPuntos(array, etiquetas) {
  // Crea el marco blanco que rodea al canvas;
  fill("#001b48");

  rect(0, 0, width, height);
  strokeWeight(2);
  for (let i = 0; i != array.length; i++) {
    array[i].draw();
    if (etiquetas) {
      array[i].drawEtiqueta("" + i);
    }
  }
}

function dibujarPuntosLimpiar(array, etiquetas) {
  strokeWeight(2);
  for (let i = 0; i != array.length; i++) {
    array[i].draw();
    if (etiquetas) {
      array[i].drawEtiqueta("" + i);
    }
  }
}

async function dibujarPuntosAsync(array) {
  // Crea el marco blanco que rodea al canvas;
  fill("#001b48");

  rect(0, 0, width, height);
  strokeWeight(2);
  for (let i = 0; i != array.length; i++) {
    array[i].draw();
    array[i].drawEtiqueta("" + i);
    await sleep(100);
  }
}

function dibujaCuadro(PuntoIzq, PuntoDer, limpiar, color = colorCuadro) {
  push();
  if (limpiar) {
    stroke(colorLimpiar);
    strokeWeight(2.5);
  } else {
    stroke(color);
    strokeWeight(1);
  }

  line(PuntoIzq.x - 5, 15, PuntoIzq.x - 5, height - 15);
  line(PuntoDer.x + 5, 15, PuntoDer.x + 5, height - 15);
  line(PuntoIzq.x - 5, 15, PuntoDer.x + 5, 15);
  line(PuntoIzq.x - 5, height - 15, PuntoDer.x + 5, height - 15);
  //rect(startPoint.x - 5, 50, endPoint.x + 5, height - 100);
  pop();
}

function dibujaLineaHorizontal(Punto, direccion, limpiar, color = colorCuadro) {
  let mov;
  push();
  if (limpiar) {
    stroke(colorLimpiar);
    strokeWeight(2.5);
  } else {
    stroke(color);
    strokeWeight(1);
  }
  if (direccion) {
    mov = +5;
  } else {
    mov = -5;
  }
  line(Punto.x + mov, 10, Punto.x + mov, height - 10);
  pop();
}

function mousePressed() {
  nFrame = 0;
  if (!aIniciado) {
    if (
      mouseX < width - 15 &&
      mouseX > 15 &&
      mouseY < height - 15 &&
      mouseY > 15
    ) {
      P.push(new Punto(mouseX, mouseY));
      if (P.length > 2) {
        tooltip1.innerHTML = "";
        tooltip1.classList.remove("tooltiptext");
      }
      fill("#001b48");

      rect(0, 0, width, height);
      dibujarPuntos(P, true);
      // dibuja los puntos
    }
  }
}

botonInicio.addEventListener("click", async (e) => {
  if (P.length > 2) {
    tooltip2.className += " displayNone";
    aIniciado = true;
    tooltip2.classList.remove("tooltiptext");
    if (ejecutaDicaticamente) {
      botonSiguiente.classList.remove("displayNone");
    }
    botonInicio.disabled = true;
    checkBoxTuto.disabled = true;
    botonReiniciar.disabled = true;
    botonTuto.disabled = true;
    tooltip1.innerHTML = "";
    tooltip1.classList.remove("tooltiptext");
    e.preventDefault();
    let n = P.length;
    let res = await closest(P, n);
    console.log("The smallest distance is " + res);
    botonInicio.id = "botonDisabled";
  } else {
    tooltip1.innerHTML = "Debes color al menos 3 puntos ";
    tooltip1.className += " tooltiptext";
  }
});

// A Brute Force method to return the smallest distance between two points
// in P[] of size n
async function bruteForce(Pa, n, psMinimos) {
  let min = Number.POSITIVE_INFINITY;
  for (let i = 0; i < n; ++i) {
    //dibujarPuntos(P, false);
    for (let j = i + 1; j < n; ++j) {
      console.log(Pa[i], Pa[j]);
      Pa[i].conectarA(Pa[j], azul3Rgb[0], azul3Rgb[1], azul3Rgb[2]);
      dibujarPuntosLimpiar(PxGlobal, true);
      await sleep(500);
      //            console.log(dist(P[i], P[j]),P[i],P[j],P[i].distanciaA(P[j]));
      if (Pa[i].distanciaA(Pa[j]) < min) {
        min = Pa[i].distanciaA(Pa[j]);
        psMinimos.p1 = Pa[i];
        psMinimos.p2 = Pa[j];
      }
    }
  }

  await sleep(1000);
  for (let i = 0; i < n; ++i) {
    //dibujarPuntos(P, false);
    for (let j = i + 1; j < n; ++j) {
      console.log(Pa[i], Pa[j]);
      Pa[i].conectarLimpiar(
        Pa[j],
        colorLimpiarRGB[0],
        colorLimpiarRGB[1],
        colorLimpiarRGB[2]
      );
      dibujarPuntosLimpiar(PxGlobal, true);
    }
  }

  //console.log(min);
  psMinimos.p1.conectarA(psMinimos.p2, azul2Rgb[0], azul2Rgb[1], azul2Rgb[2]);
  await sleep(1000);
  dibujarPuntosLimpiar(PxGlobal, true);
  return min;
}

// A utility function to find a minimum of two float values
async function min2(x, y, parMinx, parMiny, parMinR) {
  console.log("x", x);
  console.log("y", y);
  parMinx.p1.conectarA(parMinx.p2, azul3Rgb[0], azul3Rgb[1], azul3Rgb[2]);
  parMiny.p1.conectarA(parMiny.p2, azul3Rgb[0], azul3Rgb[1], azul3Rgb[2]);
  parMinR.p1.conectarA(parMinR.p2, azul3Rgb[0], azul3Rgb[1], azul3Rgb[2]);
  dibujarPuntosLimpiar(PxGlobal, true);
  await sleep(1000);
  parMinx.p1.conectarLimpiar(
    parMinx.p2,
    colorLimpiarRGB[0],
    colorLimpiarRGB[1],
    colorLimpiarRGB[2]
  );
  parMiny.p1.conectarLimpiar(
    parMiny.p2,
    colorLimpiarRGB[0],
    colorLimpiarRGB[1],
    colorLimpiarRGB[2]
  );
  parMinR.p1.conectarLimpiar(
    parMinR.p2,
    colorLimpiarRGB[0],
    colorLimpiarRGB[1],
    colorLimpiarRGB[2]
  );
  dibujarPuntosLimpiar(PxGlobal, true);

  if (x < y) {
    parMinR.p1.set(parMinx.p1.x, parMinx.p1.y);
    parMinR.p2.set(parMinx.p2.x, parMinx.p2.y);
  } else {
    parMinR.p1.set(parMiny.p1.x, parMiny.p1.y);
    parMinR.p2.set(parMiny.p2.x, parMiny.p2.y);
  }
  parMinR.p1.conectarA(parMinR.p2, azul2Rgb[0], azul2Rgb[1], azul2Rgb[2]);
  dibujarPuntosLimpiar(PxGlobal, true);
  await sleep(1000);
  return x < y ? x : y;
}

// A utility function to find the distance between the closest points of
// strip of a given size. All points in strip[] are sorted according to
// y coordinate. They all have an upper bound on minimum distance as d.
// Note that this method seems to be a O(n^2) method, but it's a O(n)
// method as the inner loop runs at most 6 times
async function stripClosest(strip, size, d, parMinimo) {
  let min = d; // Initialize the minimum distance as d
  console.log(strip.length);
  let p1;
  let p2;
  if (size - 1 >= 1) {
    p1 = new Punto(strip[0].x, strip[0].y);
    p2 = new Punto(strip[1].x, strip[1].y);
  }

  parMinimo.p1.conectarA(parMinimo.p2, azul3Rgb[0], azul3Rgb[1], azul3Rgb[2]);
  dibujarPuntosLimpiar(PxGlobal, true);

  // Pick all points one by one and try the next points till the difference
  // between y coordinates is smaller than d.
  // This is a proven fact that this loop runs at most 6 times
  for (let i = 0; i < size; ++i) {
    for (let j = i + 1; j < size && strip[j].y - strip[i].y < min; ++j) {
      strip[i].conectarA(strip[j], azul3Rgb[0], azul3Rgb[1], azul3Rgb[2]);
      await sleep(500);
      if (strip[i].distanciaA(strip[j]) < min) {
        parMinimo.p1.conectarLimpiar(
          parMinimo.p2,
          colorLimpiarRGB[0],
          colorLimpiarRGB[1],
          colorLimpiarRGB[2]
        );
        dibujarPuntosLimpiar(PxGlobal, true);
        parMinimo.p1.set(strip[i].x, strip[i].y);
        parMinimo.p2.set(strip[j].x, strip[j].y);
        parMinimo.p1.conectarA(
          parMinimo.p2,
          azul2Rgb[0],
          azul2Rgb[1],
          azul2Rgb[2]
        );
        dibujarPuntosLimpiar(PxGlobal, true);
        min = strip[i].distanciaA(strip[j]);
      }
    }
  }
  await sleep(1000);
  for (let i = 0; i < size; ++i) {
    for (let j = i + 1; j < size && strip[j].y - strip[i].y < d; ++j) {
      strip[i].conectarLimpiar(
        strip[j],
        colorLimpiarRGB[0],
        colorLimpiarRGB[1],
        colorLimpiarRGB[2]
      );
    }
  }
  console.log("min", min);

  parMinimo.p1.conectarA(parMinimo.p2, azul2Rgb[0], azul2Rgb[1], azul2Rgb[2]);
  dibujarPuntosLimpiar(PxGlobal, true);
  await sleep(1000);
  //await sleep(1000);
  return min;
}

// A recursive function to find the smallest distance. The array Px contains
// all points sorted according to x coordinates and Py contains all points
// sorted according to y coordinates
async function closestUtil(Px, Py, n, alpha, pMinimoArg) {
  dibujarPuntosLimpiar(PxGlobal, true);
  //punto mas a la izquierda y punto mas a la derecha para dibujar cuadro
  let endPoint = Px[n - 1];
  let startPoint = Px[0];
  dibujaCuadro(startPoint, endPoint, false);
  await sleep(500);
  if (n <= 3) {
    if (ejecutaDicaticamente) {
      while (pasos == 2) {
        await sleep(100);
      }
      await sleep(300);
      pComentarios.innerHTML =
        "Cuando el problema el suficientemente pequeño aplica fuerza bruta para encontrar el par de puntos con la distancia mas pequeña";
      await sleep(300);
    }
    let pMinimoBF = { p1: new Punto(0, 0), p2: new Punto(0, 0) };
    //usar fuerza bruta para encontrar el mas corto
    let r = await bruteForce(Px, n, pMinimoBF);
    pMinimoArg.p1.set(pMinimoBF.p1.x, pMinimoBF.p1.y);
    pMinimoArg.p2.set(pMinimoBF.p2.x, pMinimoBF.p2.y);
    if (ejecutaDicaticamente) {
      while (pasos == 3) {
        await sleep(100);
      }
      await sleep(300);
      pComentarios.innerHTML =
        " Obteniendo asi el par de puntos con menos distancia, es por esto que se considera Divide y Venceras.";
      await sleep(300);
      while (pasos == 4) {
        await sleep(100);
      }
      if (pasos == 5) {
        botonSiguiente.className += " displayNone";
        pasos = 0;
        pComentarios.className += " displayNone";
        pComentarios.innerHTML = "";
      }
    }
    dibujaCuadro(startPoint, endPoint, true);

    return r;
  }

  // Se encuentra el punto medio
  let mid = Math.floor(n / 2);
  let midPoint = Px[mid];
  dibujaCuadro(startPoint, Px[mid - 1], false);
  await sleep(500);
  dibujaCuadro(startPoint, endPoint, true);
  dibujaCuadro(startPoint, Px[mid - 1], true);

  // Divide points in y sorted array around the vertical line.
  // Assumption: All x coordinates are distinct.
  //PointPyl[mid];   // y sorted points on left of vertical line
  //Point Pyr[n-mid];  // y sorted points on right of vertical line
  let Pyl = []; // y sorted points on left of vertical line
  let Pyr = []; // y sorted points on right of vertical line

  let li = 0,
    ri = 0; // indexes of left and right subarrays
  //console.log(Py);
  for (let i = 0; i < n; i++) {
    if (Py[i].x <= midPoint.x && li < mid) Pyl[li++] = Py[i];
    else Pyr[ri++] = Py[i];
  }

  // Consider the vertical line passing through the middle point
  // calculate the smallest distance dl on left of middle point and
  // dr on right side
  //console.log(Px,Pyl,n,mid);
  //console.log(Px,Pyr,n,mid);
  let rightArray = [];

  for (let i = mid; i < Px.length; i++) {
    rightArray.push(Px[i]);
  }
  //dibujaCuadro(startPoint, midPoint, true);

  let pMinimoDl = { p1: new Punto(0, 0), p2: new Punto(0, 0) };
  let pMinimoDr = { p1: new Punto(0, 0), p2: new Punto(0, 0) };
  console.log;
  let dl = await closestUtil(Px, Pyl, mid, alpha, pMinimoDl);
  let dr = await closestUtil(rightArray, Pyr, n - mid, alpha, pMinimoDr); // porque suma mid

  pMinimoDl.p1.conectarA(pMinimoDl.p2, azul2Rgb[0], azul2Rgb[1], azul2Rgb[2]);
  pMinimoDr.p1.conectarA(pMinimoDr.p2, azul2Rgb[0], azul2Rgb[1], azul2Rgb[2]);
  dibujarPuntosLimpiar(PxGlobal, true);
  await sleep(300);
  console.log("dl:", dl, pMinimoDl);
  console.log("dr:", dr, pMinimoDr);

  // Find the smaller of two distances

  //console.log(d);
  dibujaCuadro(startPoint, endPoint, false);
  await sleep(500);
  let pMinimo = { p1: new Punto(0, 0), p2: new Punto(0, 0) };
  let d = await min2(dl, dr, pMinimoDl, pMinimoDr, pMinimo);
  console.log("d", d, pMinimo);

  pMinimo.p1.conectarA(pMinimo.p2, azul2Rgb[0], azul2Rgb[1], azul2Rgb[2]);
  await sleep(300);
  dibujaCuadro(startPoint, endPoint, true);

  // Build an array strip[] that contains points close (closer than d)
  // to the line passing through the middle point

  let strip = [];
  let sripOrdX = [];
  let j = 0;
  for (let i = 0; i < n; i++) {
    if (Math.abs(Py[i].x - midPoint.x) < d) {
      strip[j] = Py[i];
      sripOrdX[j] = Py[i];
      j++;
    }
  }
  sripOrdX.sort(function (a, b) {
    return a.x - b.x;
  });
  let CompScriP = { p1: new Punto(0, 0), p2: new Punto(0, 0) };
  CompScriP.p1.set(sripOrdX[0].x, sripOrdX[0].y);
  CompScriP.p2.set(
    sripOrdX[sripOrdX.length - 1].x,
    sripOrdX[sripOrdX.length - 1].y
  );

  dibujaLineaHorizontal(CompScriP.p1, false, false);
  dibujaLineaHorizontal(CompScriP.p2, true, false);
  dibujaLineaHorizontal(midPoint, false, false, "#E30303");

  sripOrdX[sripOrdX.length] = pMinimo.p1;
  sripOrdX[sripOrdX.length] = pMinimo.p2;
  sripOrdX.sort(function (a, b) {
    return a.x - b.x;
  });

  //dibujaCuadro(Px[0], rightArray[n - mid - 1], true);
  let PuntoAux = { p1: new Punto(0, 0), p2: new Punto(0, 0) };
  if (Px[0].x < sripOrdX[0].x) {
    PuntoAux.p1.set(Px[0].x, Px[0].y);
  } else {
    PuntoAux.p1.set(sripOrdX[0].x, sripOrdX[0].y);
  }
  if (rightArray[n - mid - 1].x > sripOrdX[sripOrdX.length - 1].x) {
    PuntoAux.p2.set(rightArray[n - mid - 1].x, rightArray[n - mid - 1].y);
  } else {
    PuntoAux.p2.set(
      sripOrdX[sripOrdX.length - 1].x,
      sripOrdX[sripOrdX.length - 1].y
    );
  }
  dibujaCuadro(PuntoAux.p1, PuntoAux.p2, false);

  // Find the closest points in strip.  Return the minimum of d and closest
  // distance is strip[]
  await sleep(500);
  let stripCo = await stripClosest(strip, j, d, pMinimo);
  console.log("Minimos", stripCo, pMinimo);
  pMinimoArg.p1.set(pMinimo.p1.x, pMinimo.p1.y);
  pMinimoArg.p2.set(pMinimo.p2.x, pMinimo.p2.y);

  /*  dibujaLineaHorizontal(PuntoAux[0], false, true);
  dibujaLineaHorizontal(PuntoAux[1], true, true);
  
   */

  dibujaLineaHorizontal(CompScriP.p1, false, true);
  dibujaLineaHorizontal(CompScriP.p2, true, true);
  dibujaLineaHorizontal(midPoint, false, true);
  dibujaCuadro(PuntoAux.p1, PuntoAux.p2, true);

  await sleep(500);
  return stripCo;
}

// The main function that finds the smallest distance
// This method mainly uses closestUtil()
async function closest(P, n) {
  let Px = [];
  let Py = [];
  for (let i = 0; i < n; i++) {
    Px[i] = P[i];
    Py[i] = P[i];
    PxGlobal[i] = P[i];
  }

  //qsort(Px, n, sizeof(Point), compareX);
  PxGlobal.sort(function (a, b) {
    return a.x - b.x;
  });

  Px.sort(function (a, b) {
    return a.x - b.x;
  });
  Py.sort(function (a, b) {
    return a.y - b.y;
  });

  await dibujarPuntosAsync(Px);

  if (ejecutaDicaticamente) {
    pComentarios.classList.remove("displayNone");
    pComentarios.innerHTML =
      'El algoritmo ordena los puntos conforme su coordenada "x"';
    while (pasos == 0) {
      await sleep(100);
    }
    await sleep(100);
    pComentarios.innerHTML =
      "Se considera un algoritmo Divide y venceras porque toma el conjunto de puntos (problema grande)";
    await sleep(300);
  }

  //text("1", 100, 100);

  //qsort(Py, n, sizeof(Point), compareY);

  // Use recursive function closestUtil() to find the smallest distance
  dibujaCuadro(Px[0], Px[n - 1], false);
  await sleep(500);
  if (ejecutaDicaticamente) {
    while (pasos == 1) {
      await sleep(100);
    }
    await sleep(300);
    pComentarios.innerHTML =
      "Divide el arreglo completo a la mitad hasta que el problema es suficientemente pequeño para resolverlo";
    await sleep(300);
  }
  dibujaCuadro(Px[0], Px[n - 1], true);
  let alpha = 255;
  let parMinn = { p1: new Punto(0, 0), p2: new Punto(0, 0) };
  let res = await closestUtil(Px, Py, n, alpha, parMinn);
  parMinn.p1.conectarRojo(parMinn.p2, 255, 0, 0);
  dibujarPuntosLimpiar(PxGlobal);
  parMinn.p1.drawEtiqueta("Puntos mas cercanos");

  botonReiniciar.disabled = false;
  console.log(res);

  return res;
}

function f_checkEjecutaD() {
  if (checkBoxTuto.checked) {
    ejecutaDicaticamente = true;
  } else {
    ejecutaDicaticamente = false;
  }
}

function f_Siguiente() {
  pasos = pasos + 1;
}

function f_reiniciar() {
  botonInicio.disabled = false;
  botonReiniciar.disabled = false;
  botonTuto.disabled = false;
  checkBoxTuto.disabled = false;
  checkBoxTuto.checked = false;
  aIniciado = false;
  ejecutaDicaticamente = false;
  fill("#001b48");
  tooltip2.className += " tooltiptext";
  tooltip2.classList.remove("displayNone");
  rect(0, 0, width, height);
  P = [];
  PxGlobal = [];
  pasos = 0;
}

function f_explicacion() {
  if (!flagTuto) {
    video.classList.remove("displayNone");
    imagen.className += " displayNone";
    flagTuto = !flagTuto;
  } else {
    video.className += " displayNone";
    imagen.classList.remove("displayNone");
    flagTuto = !flagTuto;
  }
}
