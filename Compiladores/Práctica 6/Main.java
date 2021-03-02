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
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Operador_GLC operador_glc = new Operador_GLC();
        operador_glc.cargar_desde_ruta("/Users/luisrojas/Documents/ESCOM/7mo/COMPILADORES/TablaLL1/TablaLL1/GLC2.txt");
        operador_glc.imprimir_glc();
        
        Creador_TablaLL1 creador_tablall1 = new Creador_TablaLL1();
        creador_tablall1.guardar_glc(operador_glc.obtener_glc());
        creador_tablall1.crear_tablall1();
        creador_tablall1.calcular_tabla();
        
        TablaLL1 tablall1 = creador_tablall1.obtener_tablall1();
        tablall1.imprimir_tabla();
        
    }
    
}
