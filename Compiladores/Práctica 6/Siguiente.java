/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tablall1;

import java.util.ArrayList;
import java.util.HashSet;

/**
 *
 * @author luisrojas
 */
public class Siguiente {
    
    private GLC glc = new GLC();
    private Primero primero = new Primero();
    private ArrayList<Character> calculados = new ArrayList<Character>();

    public GLC obtener_glc() {
        return glc;
    }

    public void guardar_glc(GLC glc) {
        this.glc = glc;
        primero.guardar_glc(glc);
    }
    
    public ArrayList<Character> obtener_calculados() {
        return calculados;
    }

    public void guardar_calculados(ArrayList<Character> calculados) {
        this.calculados = calculados;
    }
    
    public ArrayList<Character> obtener_siguientes(char no_terminal){
        ArrayList<Character> s = new ArrayList<Character>();
        HashSet<Character> s_sin_repetidos;
    
        if (!calculados.contains(no_terminal)) {
            calculados.add(no_terminal);
            s.addAll(primera_regla(no_terminal));
            s.addAll(segunda_regla(no_terminal));
            s.addAll(tercera_regla(no_terminal));
        }
        
        s_sin_repetidos = new HashSet<Character>(s);
        s.clear();
        s.addAll(s_sin_repetidos);
        return s;
    }
    
    public ArrayList<Character> primera_regla(char S){
        ArrayList<Character> s = new ArrayList<Character>();
        ArrayList<Producción> producciones = glc.obtener_producciones();
        int num_producciones = producciones.size();
        char no_terminal;
        
        for (int i = 0; i < num_producciones; i++) {
            no_terminal = producciones.get(i).obtener_no_terminal();
            if(no_terminal == S && i==0){
                s.add('$');
                break;
            }
        }
        
        return s;
    }
    
    public ArrayList<Character> segunda_regla(char X){
        ArrayList<Character> s = new ArrayList<Character>();
        ArrayList<Producción> producciones = glc.obtener_producciones();
        int num_producciones = producciones.size();
        char no_terminal;
        String alfa;
        
        for (int i = 0; i < num_producciones; i++) {
            no_terminal = producciones.get(i).obtener_no_terminal();
            alfa = producciones.get(i).obtener_alfa();
            int ultimo_simbolo = alfa.length()-1;
            if(alfa.charAt(ultimo_simbolo)==X){
                s.addAll(obtener_siguientes(no_terminal));
            }
        }
        
        return s;
    }
    
    public ArrayList<Character> tercera_regla(char X){
        ArrayList<Character> s = new ArrayList<Character>();
        ArrayList<Character> s_aux = new ArrayList<Character>();
        ArrayList<Producción> producciones = glc.obtener_producciones();
        int num_producciones = producciones.size();
        char no_terminal;
        String lado_derecho_produccion;
        String alfa;
        String beta="";
        String patron_alfaXbeta = "(.*)"+X+"[a-zA-Z]";
        ArrayList<String> rest_calculados;
        
        for (int i = 0; i < num_producciones; i++) {
            no_terminal = producciones.get(i).obtener_no_terminal();
            lado_derecho_produccion = producciones.get(i).obtener_alfa();
            int ultimo_simbolo = lado_derecho_produccion.length()-1;
            if (lado_derecho_produccion.matches(patron_alfaXbeta)) {
                beta = "";
                for (int j = ultimo_simbolo; j >= 0; j--) {
                    if(lado_derecho_produccion.charAt(j)!=X || j == ultimo_simbolo){
                        beta = lado_derecho_produccion.charAt(j) + beta;
                    }else{
                        rest_calculados = new ArrayList<String>();
                        primero.guardar_calculados(rest_calculados);
                        s_aux = primero.obtener_primeros(beta);
                        if(!s_aux.contains('E')){
                            s.addAll(s_aux);
                        }else{
                            s_aux = eliminar_E(s_aux);
                            s.addAll(s_aux);
                            s.addAll(obtener_siguientes(no_terminal));
                        }
                    }
                }
            }
        }
        
        return s;
    }
    
    private ArrayList<Character> eliminar_E(ArrayList<Character> p) {
        int num_elementos = p.size();
        
        for (int i = 0; i < num_elementos; i++) {
            if (p.get(i)=='E') {
                p.remove(i);
                break;
            }
        }
        
        return p;
    }
    
}
