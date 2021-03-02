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
public class Transición {
    
    private String estado;
    private String estado_siguiente;
    private String simbolo;

    /**
     * Designa una transición completa
     * @param estado valor del estado 
     * @param estado_siguiente valor del estado siguiente
     * @param simbolo valor del simbolo de la transición
     */
    public Transición(String estado, String estado_siguiente, String simbolo) {
        this.estado = estado;
        this.estado_siguiente = estado_siguiente;
        this.simbolo = simbolo;
    }   
    
    public Transición(){
    
    }
    
    /**
     * Consulta del estado de la transición
     * @return valor del estado
     */
    public String obtener_estado() {
        return estado;
    }

    /**
     * Designa el valor del estado de la transición
     * @param estado valor del estado 
     */
    public void guardar_estado(String estado) {
        this.estado = estado;
    }

    /**
     * Consulta del estado siguiente de la transición
     * @return valor del estado siguiente
     */
    public String obtener_estado_siguiente() {
        return estado_siguiente;
    }

    /**
     * Designa el valor del estado siguiente de la transición
     * @param estado_siguiente valor del estado siguiente
     */
    public void guardar_estado_siguiente(String estado_siguiente) {
        this.estado_siguiente = estado_siguiente;
    }

    /**
     * Consulta del símbolo de la transición
     * @return valor del símbolo
     */
    public String obtener_simbolo() {
        return simbolo;
    }

    /**
     * Designa el valor del símbolo de la transición
     * @param simbolo valor del simbolo de la transición
     */
    public void guardar_simbolo(String simbolo) {
        this.simbolo = simbolo;
    }
    
}
