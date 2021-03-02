/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tablall1;

import java.util.ArrayList;

/**
 *
 * @author luisrojas
 */
public class GLC {
    
    private ArrayList<Character> Terminales = new ArrayList<Character>();
    private ArrayList<Character> No_terminales = new ArrayList<Character>();
    private ArrayList<Producción> Producciones = new ArrayList<Producción>();

    /*TERMINALES*/
    /**
     * Consulta los terminales de la grámática
     * @return ArrayList con los terminales contenidos
     */
    public ArrayList<Character> obtener_terminales() {
        return Terminales;
    }

    /**
     * Almacena los terminales de la gramática
     * @param Terminales ArrayList con los terminales contenidos
     */
    public void guardar_terminales(ArrayList<Character> Terminales) {
        this.Terminales = Terminales;
    }

    /*NO TERMINALES*/
    /**
     * Consulta los no terminales de la grámática
     * @return ArrayList con los no terminales contenidos
     */
    public ArrayList<Character> obtener_no_terminales() {
        return No_terminales;
    }

    /**
     * Almacena los no terminales de la gramática
     * @param Terminales ArrayList con los no terminales contenidos
     */
    public void guardar_no_terminales(ArrayList<Character> No_terminales) {
        this.No_terminales = No_terminales;
    }

    /*PRODUCCIONES*/
    /**
     * Consulta las producciones de la grámática
     * @return ArrayList con las producciones contenidas
     */
    public ArrayList<Producción> obtener_producciones() {
        return Producciones;
    }

    /**
     * Almacena las producciones de la gramática
     * @param Producciones ArrayList con las producciones contenidas
     */
    public void guardar_producciones(ArrayList<Producción> Producciones) {
        this.Producciones = Producciones;
    }
    
    
}
