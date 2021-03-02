/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package af;

/**
 *
 * @author luisrojas
 */
public class Nodo{
    
    private Nodo izquierdo, derecho;
    private boolean es_hoja;
    private char valor;
    private int numero_nodo;
   
    
    public Nodo(char valor, int numero_nodo, Nodo nodo_izquierdo, Nodo nodo_derecho){
        this.valor = valor;
        this.izquierdo = nodo_izquierdo;
        this.derecho = nodo_derecho;
        this.numero_nodo = numero_nodo;
    }
    
    public Nodo(char valor, int numero_nodo, Nodo nodo_izquierdo){
        this.valor = valor;
        this.izquierdo = nodo_izquierdo;
        this.derecho = null;
        this.numero_nodo = numero_nodo;
    }
    
    public Nodo(char valor, int numero_nodo, boolean es_hoja){
        this.valor = valor;
        this.izquierdo = null;
        this.derecho = null;
        this.numero_nodo = numero_nodo;
        this.es_hoja = es_hoja;
    }

    public Nodo(){
    }
    
    /**
     * Consulta el nodo izquierdo del árbol
     * @return Nodo izquierdo
     */
    public Nodo obtener_izquierdo(){
        return izquierdo;
    }

    /**
     * Asigna el nodo izquierdo del árbol
     * @param izquierdo elemento que será el nodo izquierdo.
     */
    public void guardar_izquierdo(Nodo izquierdo){
        this.izquierdo = izquierdo;
    }

    /**
     * Consulta el nodo derecho del árbol
     * @return Nodo derecho
     */
    public Nodo obtener_derecho(){
        return derecho;
    }
    
    /**
     * Asigna el nodo izquierdo del árbol
     * @param simbolo valor para el atributo.
     */
    public void guardar_derecho(Nodo derecho){
        this.derecho = derecho;
    }

    /**
     * Consulta si el nodo se trata de una hoja
     * @return valor del atributo es_hoja
     */
    public boolean es_hoja(){
        return es_hoja;
    }

    /**
     * Designa si el nodo es una hoja o no
     * @param simbolo valor para el atributo es_hoja.
     */
    public void guardar_es_hoja(boolean es_hoja){
        this.es_hoja = es_hoja;
    }

    /**
     * Consulta el valor del nodo
     * @return valor del nodo
     */
    public char obtener_valor(){
        return valor;
    }

    /**
     * Designa el valor del nodo
     * @param valor valor que se signará al nodo.
     */
    public void guardar_valor(char valor){
        this.valor = valor;
    }

    /**
     * Consulta el número del nodo
     * @return valor del número del nodo
     */
    public int obtener_numero_nodo(){
        return numero_nodo;
    }

    /**
     * Designa el valor del número del nodo
     * @param numero_nodo valor del número del nodo
     */
    public void guardar_numero_nodo(int numero_nodo){
        this.numero_nodo = numero_nodo;
    }
    
}