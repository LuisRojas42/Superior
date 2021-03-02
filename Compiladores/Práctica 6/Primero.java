package tablall1;

import java.util.ArrayList;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author luisrojas
 */
public class Primero {
    
    private GLC glc = new GLC();
    //private ArrayList<Calculando> calculados = new ArrayList<Calculando>();
    private ArrayList<String> calculados = new ArrayList<String>();

    public ArrayList<String> obtener_calculados() {
        return calculados;
    }

    public void guardar_calculados(ArrayList<String> calculados) {
        this.calculados = calculados;
    }

    public GLC obtener_glc() {
        return glc;
    }

    public void guardar_glc(GLC glc) {
        this.glc = glc;
    }
    
    public ArrayList<Character> obtener_primeros(String elemento){
        ArrayList<Character> p = new ArrayList<Character>();
        int tam_elemento = elemento.length();
        
        if (!calculados.contains(elemento)) {
            calculados.add(elemento);
            if (tam_elemento==1) {
                char T = primera_regla(elemento.charAt(0));
                if(T!='\0'){
                    p.add(T);
                }else{
                    p.addAll(segunda_regla(elemento.charAt(0)));
                }
            }else{
                p.addAll(tercera_regla(elemento));
            }
        }
       
        return p;
    }
    
    public char primera_regla(char T){
        ArrayList<Character> terminales = glc.obtener_terminales();
        if(terminales.contains(T) || T == 'E'){
            return T;
        }
        
        return '\0';
    }
    
    public ArrayList<Character> segunda_regla(char N){
        ArrayList<Character> p = new ArrayList<Character>();
        ArrayList<Character> no_terminales = glc.obtener_no_terminales();
        ArrayList<Producción> producciones = glc.obtener_producciones();
        int num_producciones = producciones.size();
        char no_terminal;
        String alfa;
        
        if(no_terminales.contains(N)){
            for (int i = 0; i < num_producciones; i++) {
                no_terminal = producciones.get(i).obtener_no_terminal();
                alfa = producciones.get(i).obtener_alfa();
                if (no_terminal==N) {
                    if(alfa.equals("E")){
                        p.add('E');
                    }else{
                        p.addAll(obtener_primeros(alfa));        
                    }
                }
            }
        }
        
        return p;
    }
    
    
    
    public ArrayList<Character> tercera_regla(String alfa){
        ArrayList<Character> p = new ArrayList<Character>();
        int Xi=0;
        int tam_alfa = alfa.length();
        String simbolo;
        boolean continuar=true;
        
        while(continuar && Xi<tam_alfa){
            simbolo = alfa.charAt(Xi)+"";
            p.addAll(obtener_primeros(simbolo));
            if(p.contains('E') && Xi != tam_alfa-1){
                quitar_de_calculados(simbolo);
                p = eliminar_E(p);
            }else{
                continuar = false;
            }
            Xi++;   
        }
        
        return p;
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
   
    private void quitar_de_calculados(String simbolo) {
        int num_elementos = calculados.size();
        
        for (int i = 0; i < num_elementos; i++) {
            if (calculados.get(i)==simbolo) {
                calculados.remove(i);
                break;
            }
        }
    }
    
}
