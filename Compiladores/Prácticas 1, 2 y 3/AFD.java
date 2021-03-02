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
public class AFD{
    
    private AF af;

    /**
     * Consulta el AFD
     * @return af Autómata finito determinista.
     */
    public AF obtener_Af() {
        return af;
    }

    /**
     * Asigna un AFD
     * @param af Autómata finito determinista.
     */
    public void guardar_Af(AF af) {
        this.af = af;
    }
    
    /**
     * Comprueba si la cadena es aceptada por el AFD de este objeto
     * @param entrada Cadena que se probará
     * @param tabla_transiciones transiciones mostradas en formato de una tabla
     * @return Resultado booleano de la prueba 
     */
    boolean aceptaAFD(String entrada, String[][] tabla_transiciones){ 
        String estado_incial = af.obtener_estado_inicial();
        ArrayList<String> estados_finales = af.obtener_estados_finales();
        int filas = af.obtener_estados().size()+1;
        int columnas = af.obtener_alfabeto().size()+1;
        String estado_actual = estado_incial;
        String simbolo;
        int num_simbolos = entrada.length();
        int i = 0, j = 0, k = 0;
        
        while(num_simbolos > i){
            simbolo = entrada.charAt(i++)+"";
            for(j=0; j<filas; j++){
                if(tabla_transiciones[j][0].equals(estado_actual)){
                    break;
                }
            }
            for(k=0; k<columnas; k++){
                if(tabla_transiciones[0][k].equals(simbolo)){
                    break;
                }
            }
            estado_actual = tabla_transiciones[j][k]+"";
        } 
        
        for(i=0; i<estados_finales.size(); i++){
            String estado_final = estados_finales.get(i);
            if(estado_actual.equals(estado_final) ){
                return true;
            }
        }
        
        return false;
    }
    
    /*PSEUDO CÓDIGO*/
    /*
    
        delta[estado][simbolo]=estado_siguiente;
        estado_incicial = 1;
        estados_finales[3] = {2,3,4};
        
        estado_actual = estado_inicial;
        
        while(hay_simbolos(entrada)){
            simbolo = entrada[i++];
            estado_actual = delta[entado_actual][simbolo];
        }        
        if(estado_actual == estados_finales[2]){
            aceptar;
        }
    
    */
    
}
