let aIniciado = false;
const fpsCount = 8;
let P = [];
// Esta función se ejecuta una vez antes de dibujar algo en pantalla.
function setup() {
  let canvas = createCanvas(700, 500);
  canvas.parent("canvasTag");

  //frameRate(fpsCount);
  //nFrame = 0;
  fill("#001b48");
  stroke(255);
  rect(0, 0, width, height);
}

function sleep(milis) {
  return new Promise((resolve) => setTimeout(resolve, milis));
}

function dibujarPuntos(array, etiquetas) {
  // Crea el marco blanco que rodea al canvas;
  fill("#001b48");
  stroke(255);
  rect(0, 0, width, height);
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
  stroke(255);
  rect(0, 0, width, height);
  strokeWeight(2);
  for (let i = 0; i != array.length; i++) {
    array[i].draw();
    array[i].drawEtiqueta("" + i);
    await sleep(100);
  }
}

function mousePressed() {
  nFrame = 0;
  if (!aIniciado) {
    if (mouseX < width && mouseX > 0 && mouseY < height && mouseY > 0) {
      P.push(new Punto(mouseX, mouseY));
      fill("#001b48");
      stroke(255);
      rect(0, 0, width, height);
      dibujarPuntos(P, true);
      // dibuja los puntos
    }
  }
}

let botonInicio = document.getElementById("botonIniciar");

botonInicio.addEventListener("click", async (e) => {
  aIniciado = true;
  e.preventDefault();
  let n = P.length;
  let res = await closest(P, n);
  console.log("The smallest distance is " + res);
  botonInicio.id = "botonDisabled";
});

// A Brute Force method to return the smallest distance between two points
// in P[] of size n
async function bruteForce(Pa, n, psMinimos) {
  let min = Number.POSITIVE_INFINITY;
  for (let i = 0; i < n; ++i) {
    //dibujarPuntos(P, false);
    for (let j = i + 1; j < n; ++j) {
      console.log(Pa[i], Pa[j]);
      Pa[i].conectarA(Pa[j]);
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
      Pa[i].conectarA(Pa[j], 0, 27, 72);
    }
  }

  //console.log(min);
  psMinimos.p1.conectarA(psMinimos.p2, 1, 138, 190);
  await sleep(1000);
  return min;
}

// A utility function to find a minimum of two float values
async function min2(x, y, parMinx, parMiny, parMinR) {
  console.log("x", x);
  console.log("y", y);
  parMinx.p1.conectarA(parMinx.p2, 0, 27, 72);
  parMiny.p1.conectarA(parMiny.p2, 0, 27, 72);
  if (x < y) {
    parMinR.p1.set(parMinx.p1.x, parMinx.p1.y);
    parMinR.p2.set(parMinx.p2.x, parMinx.p2.y);
  } else {
    parMinR.p1.set(parMiny.p1.x, parMiny.p1.y);
    parMinR.p2.set(parMiny.p2.x, parMiny.p2.y);
  }
  parMinR.p1.conectarRojo(parMinR.p2);
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
  parMinimo.p1.conectarA(parMinimo.p2, 0, 27, 72);

  // Pick all points one by one and try the next points till the difference
  // between y coordinates is smaller than d.
  // This is a proven fact that this loop runs at most 6 times
  for (let i = 0; i < size; ++i) {
    for (let j = i + 1; j < size && strip[j].y - strip[i].y < min; ++j) {
      strip[i].conectarA(strip[j]);
      await sleep(500);
      if (strip[i].distanciaA(strip[j]) < min) {
        parMinimo.p1.set(strip[i].x, strip[i].y);
        parMinimo.p2.set(strip[j].x, strip[j].y);
        min = strip[i].distanciaA(strip[j]);
      }
    }
  }
  await sleep(1000);
  for (let i = 0; i < size; ++i) {
    for (let j = i + 1; j < size && strip[j].y - strip[i].y < min; ++j) {
      strip[i].conectarA(strip[j], 0, 27, 72);
    }
  }
  console.log("min", min);

  parMinimo.p1.conectarRojo(parMinimo.p2);
  await sleep(1000);
  //await sleep(1000);
  return min;
}

// A recursive function to find the smallest distance. The array Px contains
// all points sorted according to x coordinates and Py contains all points
// sorted according to y coordinates
async function closestUtil(Px, Py, n, alpha, pMinimoArg) {
  // If there are 2 or 3 points, then use brute force

  if (n <= 3) {
    let pMinimoBF = { p1: new Punto(0, 0), p2: new Punto(0, 0) };
    let r = await bruteForce(Px, n, pMinimoBF);
    pMinimoArg.p1.set(pMinimoBF.p1.x, pMinimoBF.p1.y);
    pMinimoArg.p2.set(pMinimoBF.p2.x, pMinimoBF.p2.y);

    console.log("r", r);
    return r;
  }

  // Find the middle point
  let mid = Math.floor(n / 2);
  let midPoint = Px[mid];
  //console.log(Px, midPoint, mid);
  push();
  stroke(255, alpha);
  line(midPoint.x, 0, midPoint.x, height);
  pop();
  alpha -= 50;
  await sleep(500);
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
  let pMinimoDl = { p1: new Punto(0, 0), p2: new Punto(0, 0) };
  let pMinimoDr = { p1: new Punto(0, 0), p2: new Punto(0, 0) };
  let dl = await closestUtil(Px, Pyl, mid, alpha, pMinimoDl);
  let dr = await closestUtil(rightArray, Pyr, n - mid, alpha, pMinimoDr); // porque suma mid

  pMinimoDl.p1.conectarRojo(pMinimoDl.p2, 255, 255, 0);
  pMinimoDr.p1.conectarRojo(pMinimoDr.p2, 255, 255, 0);
  await sleep(300);
  console.log("dl:", dl, pMinimoDl);
  console.log("dr:", dr, pMinimoDr);

  // Find the smaller of two distances

  //console.log(d);
  let pMinimo = { p1: new Punto(0, 0), p2: new Punto(0, 0) };
  let d = await min2(dl, dr, pMinimoDl, pMinimoDr, pMinimo);
  console.log("d", d, pMinimo);

  pMinimo.p1.conectarA(pMinimo.p2, 247, 191, 22);
  await sleep(300);
  // Build an array strip[] that contains points close (closer than d)
  // to the line passing through the middle point
  let strip = [];
  let j = 0;
  for (let i = 0; i < n; i++)
    if (Math.abs(Py[i].x - midPoint.x) < d) (strip[j] = Py[i]), j++;

  // Find the closest points in strip.  Return the minimum of d and closest
  // distance is strip[]

  let stripCo = await stripClosest(strip, j, d, pMinimo);
  console.log("Minimos", stripCo, pMinimo);
  pMinimoArg.p1.set(pMinimo.p1.x, pMinimo.p1.y);
  pMinimoArg.p2.set(pMinimo.p2.x, pMinimo.p2.y);
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
  }

  //qsort(Px, n, sizeof(Point), compareX);
  Px.sort(function (a, b) {
    return a.x - b.x;
  });
  Py.sort(function (a, b) {
    return a.y - b.y;
  });

  await dibujarPuntosAsync(Px);

  //text("1", 100, 100);

  //qsort(Py, n, sizeof(Point), compareY);

  // Use recursive function closestUtil() to find the smallest distance
  let alpha = 255;
  let parMinn = { p1: new Punto(0, 0), p2: new Punto(0, 0) };
  let res = await closestUtil(Px, Py, n, alpha, parMinn);
  parMinn.p1.conectarRojo(parMinn.p2, 255, 0, 0);
  parMinn.p1.drawEtiqueta("Puntos mas cercanos");
  console.log(res);
  return res;
}
