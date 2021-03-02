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
public class Destado {
    private ArrayList<String> conjunto_estados = new ArrayList<String>();
    private boolean marcado;
    private char etiqueta;
    private boolean es_inicial=false;
    private boolean es_final=false;

    /**
     * Consulta al objeto para saber si es un estado inicial
     * @return valor del atributo es_inicial
     */
    public boolean es_inicial() {
        return es_inicial;
    }

    /**
     * Designa al objeto como un estado inicial o no
     * @param es_inicial valor para el atributo.
     */
    public void guardar_es_inicial(boolean es_inicial) {
        this.es_inicial = es_inicial;
    }

    /**
     * Consulta al objeto para saber si es un estado final
     * @return valor del atributo es_final
     */
    public boolean es_final() {
        return es_final;
    }

    /**
     * Designa al objeto como un estado final o no
     * @param es_inicial valor para el atributo.
     */
    public void guardar_es_final(boolean es_final) {
        this.es_final = es_final;
    }

    /**
     * Consulta al objeto para saber su etiqueta
     * @return valor del atributo etiqueta
     */
    public char obtener_etiqueta() {
        return etiqueta;
    }

    /**
     * Designa al objeto la etiqueta del estado que contiene
     * @param etiqueta valor para el atributo etiqueta.
     */
    public void guardar_etiqueta(char etiqueta) {
        this.etiqueta = etiqueta;
    }

    /**
     * Consulta del subconjunto de estados que contiene el objeto
     * @return conjunto de estados del objeto
     */
    public ArrayList<String> obtener_conjunto_estados() {
        return conjunto_estados;
    }

    /**
     * Asigna un conjunto de estados al objeto
     * @param conjunto_estados valor para el atributo conjunto_estados.
     */
    public void guardar_conjunto_estados(ArrayList<String> conjunto_estados) {
        this.conjunto_estados = conjunto_estados;
    }

    /**
     * Consulta al objeto para saber si esta marcado
     * @return valor del atributo marcado
     */
    public boolean esta_marcado() {
        return marcado;
    }

    /**
     * Designa al objeto como marcado o no
     * @param marcado valor para el atributo marcado.
     */
    public void guardar_marcado_como(boolean marcado) {
        this.marcado = marcado;
    }
  
}

