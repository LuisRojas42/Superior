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
public class TablaLL1 {
    
    private String[][] tablall1;

    /**
     * Consulta la tabla ll1 contenida
     * @return tabla ll1 contenida
     */
    public String[][] obtener_tablall1() {
        return tablall1;
    }

    /**
     * Almacena una tabla ll1 en el objeto
     * @param izquierdo elemento que será el nodo izquierdo.
     */
    public void guardar_tablall1(String[][] tablall1) {
        this.tablall1 = tablall1;
    }
    
    /**
     * Imprime la tabla ll1 contenida
     */
    public void imprimir_tabla(){        
        for(int i=0; i<tablall1.length; i++){
            for(int j=0; j<tablall1[i].length; j++){
                System.out.print(tablall1[i][j]+"\t");
            }
            System.out.println("");
        }
    }
    
}
