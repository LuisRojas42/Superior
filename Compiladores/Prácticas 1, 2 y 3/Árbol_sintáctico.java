package af;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;


/**
 * Clase que construye el árbol sintáctico
 * @author Pablo
 * @param <T> Generic
 */
public class Árbol_sintáctico<T> {
   
    /**
     * Construye un árbol sintáctico a partir de una expresión regular en 
     * formato postfix
     * @param expresión_en_postfix Expresión regular en formato postfix
     * @return Nodo raiz del árbol
     */
    public Nodo construir_árbol(String expresión_en_postfix) {
        //Nodo nodo = new Nodo();
    
        Stack pila = new Stack();
        char simbolo;
        int tam_expresión_en_postfix = expresión_en_postfix.length();
        List<Character> operadores = Arrays.asList('|', '+', '*', '.');
        List<Character> operadores_binarios = Arrays.asList('|', '.');
        
        for (int i = 0; i < tam_expresión_en_postfix; i++) {
            simbolo = expresión_en_postfix.charAt(i);
            if(!operadores.contains(simbolo) ){
                Nodo nodo = new Nodo(simbolo, i, true);
                pila.push(nodo);
            }else if(operadores_binarios.contains(simbolo)){
                Nodo nodo_derecho = (Nodo) pila.pop();
                Nodo nodo_izquierdo = (Nodo) pila.pop();
                Nodo nodo = new Nodo(simbolo, i, nodo_izquierdo, nodo_derecho);
                pila.push(nodo);
            }else{
                Nodo nodo_hijo = (Nodo) pila.pop();
                Nodo nodo = new Nodo(simbolo, i, nodo_hijo);
                pila.push(nodo);
            }
        }
        
        return (Nodo)pila.pop();
    }
    
}