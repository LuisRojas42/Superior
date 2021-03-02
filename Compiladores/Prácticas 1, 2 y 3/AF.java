/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package af;

import java.util.ArrayList;

/**
 *
 * @author luisrojas
 */
public class AF {
    
    private String estado_inicial;
    private ArrayList<String> alfabeto = new ArrayList<String>();
    private ArrayList<String> estados = new ArrayList<String>();
    private ArrayList<String> estados_finales = new ArrayList<String>();
    private ArrayList<Transición> transiciones = new ArrayList<Transición>();
    private boolean esAFN = false;
    private boolean esAFD = false;

    /*ESTADO INICIAL*/
    /**
     * Consulta el estado inicial del AF
     * @return valor del atributo estado_inicial
     */
    public String obtener_estado_inicial() {
        return estado_inicial;
    }

    /**
     * Designa el estado inicial del AF
     * @param estado_inicia valor para el atributo.
     */
    public void guardar_estado_inicial(String estado_inicial) {
        this.estado_inicial = estado_inicial;
    }

    /*ESTADOS FINALES*/
    /**
     * Consulta los estados finales del AF
     * @return valor del atributo estados_finales
     */
    public ArrayList<String> obtener_estados_finales() {
        return estados_finales;
    }

    /**
     * Designa los estados finales del AF
     * @param estads_finales valor para el atributo estados_finales.
     */
    public void guardar_estados_finales(ArrayList<String> estados_finales) {
        this.estados_finales = estados_finales;
    }
    
    /**
     * Designa un estado final del AF
     * @param estado estado final que se agregará a la lista de estados finales.
     */
    void guardar_estado_final(String estado){
        if(!estados_finales.contains(estado))   
            estados_finales.add(estado);
    }
    
    /**
     * Elimina un estado final del AF
     * @param estado valor que eliminará de la lista de estados finales.
     */
    void eliminar_estado_final(String estado){
        if(estados_finales.contains(estado)){
            int num_estados_finales = estados_finales.size();
            for (int i = 0; i < num_estados_finales; i++) {
                if (estados_finales.get(i).equals(estado)) {
                    estados_finales.remove(i);
                }
            }
        }
    }
    
    /*ALFABETO*/
    /**
     * Consulta el alfabeto del AF
     * @return lista de simbolos del alfabeto
     */
    public ArrayList<String> obtener_alfabeto() {
        return alfabeto;
    }

    /**
     * Designa el alfabeto del AF
     * @param alfabeto lista de simbolos del alfabeto
     */
    public void guarda_alfabeto(ArrayList<String> alfabeto) {
        this.alfabeto = alfabeto;
    }
    
    /**
     * Designa un simbolo pertenciente del alfabeto del AF
     * @param simbolo simbolo que se agregará a la lista simbolos o alfabeto.
     */
    void guardar_simbolo(String simbolo){
        if(!alfabeto.contains(simbolo))
            alfabeto.add(simbolo);
    }

    /*ESTADOS*/
    /**
     * Consulta de los estados del AF
     * @return Estados del AF
     */
    public ArrayList<String> obtener_estados() {
        return estados;
    }

    /**
     * Designa los estados del AF
     * @param estados ArrayList con los estados contenidos
     */
    public void guardar_estados(ArrayList<String> estados) {
        this.estados = estados;
    }
    
    /**
     * Designa un estado del AF
     * @param estado Estado que se agregará a la lista de estados
     */
    void guardar_estado(String estado){
        if(!estados.contains(estado))   
            estados.add(estado);
    }

    /*TRANSICIONES*/
    /**
     * Consulta de las transiciones del AF
     * @return Estados del AF
     */
    public ArrayList<Transición> obtener_transiciones() {
        return transiciones;
    }

    /**
     * Designa las transiciones del AF
     * @param transiciones ArrayList con las transiciones contenidas
     */
    public void guardar_transiciones(ArrayList<Transición> transiciones) {
        this.transiciones = transiciones;
    }
    
    /**
     * Designa una transición del AF
     * @param transición Transición que se agregará a la lista de transiciones
     */
    void guardar_transición(Transición transición){
        if(!transiciones.contains(transición))   
            transiciones.add(transición);
    }
    
    /**
     * Designa una transición del AF
     * @param estado Estado de la transición que se agregará a la lista de transiciones
     * @param estado_siguiente Estado al que llega la transición que se agregará a la lista de transiciones
     * @param simbolo simbolo de la transición que se agregará a la lista de transiciones
     */
    public void guardar_transición(String estado, String estado_siguiente, String simbolo){
        Transición transicion = new Transición();
        transicion.guardar_estado(estado);
        transicion.guardar_estado_siguiente(estado_siguiente);
        transicion.guardar_simbolo(simbolo);
        transiciones.add(transicion);
    }

    /**
     * Modifica una transición del AF
     * @param indice_transición Indice de donde se encuntra la transición a modifcar dentro de la lista de transiciones
     * @param estado Nuevo estado de la transición que se modificará
     * @param estado_siguiente Nuevo estado siguiente de la transición que se modificará
     * @param simbolo nUEVO simbolo de la transición que se modificará
     */
    public void modificar_transición(int indice_transición, String estado, String estado_siguiente, String simbolo){
        Transición transición = new Transición(estado, estado_siguiente, simbolo);
        transiciones.set(indice_transición, transición);
    }
    
    /*esAFN*/
    /**
     * Consulta al objeto para saber si es un AFN
     * @return valor del atributo esAFN
     */
    public boolean EsAFN() {
        return esAFN;
    }

    /**
     * Designa al objeto como un AFN o no
     * @param esAFN valor para el atributo.
     */
    public void guardar_EsAFN(boolean esAFN) {
        this.esAFN = esAFN;
    }

    /*esAFD*/
    /**
     * Consulta al objeto para saber si es un AFD
     * @return valor del atributo esAFD
     */
    public boolean EsAFD() {
        return esAFD;
    }

    /**
     * Designa al objeto como un AFD o no
     * @param esAFD valor para el atributo.
     */
    public void guardar_EsAFD(boolean esAFD) {
        this.esAFD = esAFD;
    }
    
}
