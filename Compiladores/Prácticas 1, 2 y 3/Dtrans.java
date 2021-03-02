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
public class Dtrans {
    
    private String simbolo;
    private char T;
    private char U;

    /**
     * Consulta del simbolo de la transición
     * @return valor del atributo simbolo
     */
    public String obtener_simbolo() {
        return simbolo;
    }

    /**
     * Designa el simbolo de la transición
     * @param simbolo valor para el atributo.
     */
    public void guardar_simbolo(String simbolo) {
        this.simbolo = simbolo;
    }

    /**
     * Consulta del estado de la transición
     * @return valor del atributo T
     */
    public char obtener_T() {
        return T;
    }

    /**
     * Designa el estado de la transición
     * @param T valor para el atributo T.
     */
    public void guardar_T(char T) {
        this.T = T;
    }

    /**
     * Consulta del estado siguiente de la transición
     * @return valor del atributo U
     */
    public char obtener_U() {
        return U;
    }

    /**
     * Designa el estado siguiente de la transición
     * @param U valor para el atributo U.
     */
    public void guardar_U(char U) {
        this.U = U;
    }
    
}
