/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tablall1;

/**
 *
 * @author luisrojas
 */
public class Producción {
    
    private char no_terminal;
    private String alfa;
    private boolean es_inicio=false;
    private int numero;

    /*NO TERMINAL*/
    /**
     * Consulta el no terminal de esta producción
     * @return no terminal de la producción
     */
    public char obtener_no_terminal() {
        return no_terminal;
    }

    /**
     * Asigna el no terminal de esta producción
     * @param no_terminal No terminal que se asignará
     */
    public void guardar_no_terminal(char no_terminal) {
        this.no_terminal = no_terminal;
    }

    /*ALFA*/
    /**
     * Consulta el lado derecho de esta producción
     * @return lado derecho de la producción
     */
    public String obtener_alfa() {
        return alfa;
    }

    /**
     * Asigna el lado derecho de esta producción
     * @param alfa Lado derecho que se asignará
     */
    public void guardar_alfa(String alfa) {
        this.alfa = alfa;
    }

    /*INICIO*/
    /**
     * Consulta si esta producción es de inicio 
     * @return valor de atributo es_inicio
     */
    public boolean es_inicio() {
        return es_inicio;
    }

    /**
     * Asigna si esta producción es de inicio 
     * @param es_inicio valor de atributo es_inicio que se asígnará
     */
    public void guardar_es_inicio(boolean es_inicio) {
        this.es_inicio = es_inicio;
    }
    
    /*NUMERO*/
    /**
     * Consulta el número asosiado a la producción
     * @return numero de la producción
     */
    public int obtener_numero() {
        return numero;
    }

    /**
     * Asigna el número asosiado a la producción
     * @param numero valor que se asociará
     */
    public void guardar_numero(int numero) {
        this.numero = numero;
    }
    
    
}
