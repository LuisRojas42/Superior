// Clase de ayuda para representar toda la lógica de los puntos
class Punto {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
  set(x, y) {
    this.x = x;
    this.y = y;
  }

  draw() {
    push();
    stroke(255);
    strokeWeight(4);
    fill(255);
    point(this.x, this.y);
    pop();
  }
  drawEtiqueta(texto) {
    if (texto === undefined) {
      texto = "0";
    }
    push();
    noStroke();
    fill(255);
    text(texto, this.x + 10, this.y + 10);
    pop();
  }
  conectarA(punto, r = 0, g = 255, b = 0) {
    push();
    stroke(r, g, b);
    line(this.x, this.y, punto.x, punto.y);
    pop();
  }
  conectarRojo(punto, r = 255, g = 0, b = 0) {
    push();
    stroke(r, g, b);
    line(this.x, this.y, punto.x, punto.y);
    pop();
  }
  conectarLimpiar(punto, r = 255, g = 0, b = 0) {
    push();
    stroke(r, g, b);
    strokeWeight(3);
    line(this.x, this.y, punto.x, punto.y);
    pop();
  }

  distanciaA(punto) {
    let a = punto.x - this.x;
    a = a * a;
    let b = punto.y - this.y;
    b = b * b;
    return Math.sqrt(a + b);
  }
}
