/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tablall1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;

/**
 *
 * @author luisrojas
 */
public class Operador_GLC {
    
    private GLC glc = new GLC();

    /**
     * Consulta la GLC vinculada
     * @return glc vinculada
     */
    public GLC obtener_glc() {
        return glc;
    }

    /**
     * Asigna una glc
     * @param glc GLC que se vinculará
     */
    public void guardar_glc(GLC glc) {
        this.glc = glc;
    }
    
    /**
     * Lee un archivo con una GLC contenida y guarda las lineas en un ArrayList
     * @param ruta Ruta del archivo a leer
     * @return ArrayList con las lineas del archivo contenidas
     */
    public ArrayList<String> leer_archivo(String ruta){
        File archivo = null;
        FileReader fr = null;
        BufferedReader br = null;
        ArrayList<String> lineas = new ArrayList<String>();

        try {
            archivo = new File (ruta);
            fr = new FileReader (archivo);
            br = new BufferedReader(fr);

            String linea;
            while((linea=br.readLine())!=null)
                lineas.add(linea);
        }
        catch(Exception e){
            e.printStackTrace();
        }finally{
            try{                    
                if( null != fr ){   
                    fr.close(); 
                }                  
            }catch (Exception e2){ 
                e2.printStackTrace();
            }
        }
        return lineas;
    }
    
    /**
     * Lee un archivo con una GLC contenida y guarda las lineas en un ArrayList
     * @param ruta Ruta del archivo a leer
     * @return ArrayList con las lineas del archivo contenidas
     */
    public ArrayList<Character> leer_terminales(ArrayList<String> lineas){
        String[] partes_produccion;
        ArrayList<Character> terminales = new ArrayList<Character>();
        int num_lineas = lineas.size();
        
        for(int i=0; i<num_lineas; i++){
            partes_produccion = lineas.get(i).split("->");
            String alfa = partes_produccion[1];
            for(int j=0; j<alfa.length(); j++){
                if(!terminales.contains(alfa.charAt(j)) && !Character.isUpperCase(alfa.charAt(j))){
                    terminales.add(alfa.charAt(j));
                }
            }
        }
        
        return terminales;
    }
    
    /**
     * Obtiene los no terminales de una gramática contenida en un ArrayList 
     * @param lineas ArrayList con una glc contenida
     * @return ArrayList con los no terminales 
     */
    public ArrayList<Character> leer_no_terminales(ArrayList<String> lineas) {
        ArrayList<Character> no_terminales = new ArrayList<Character>();
        int num_lineas = lineas.size();
        
        for(int i=0; i<num_lineas; i++){
            if(!no_terminales.contains(lineas.get(i).charAt(0))){
                no_terminales.add(lineas.get(i).charAt(0));
            }
        }
        
        return no_terminales;
    }
    
    /**
     * Obtiene y construye una produccion a partir de una cadena y un id
     * @param linea Cadena a leer con una producción dentro
     * @param numero Identificador de la producción
     * @return Objeto producción con la producción leida contenida
     */
    public Producción leer_producción(String linea, int numero){
        Producción producción = new Producción();
        char no_terminal = linea.charAt(0);
        String alfa = linea.split("->")[1];
        
        producción.guardar_no_terminal(no_terminal);
        producción.guardar_alfa(alfa);
        producción.guardar_numero(numero);
        if(numero==0){
            producción.guardar_es_inicio(true);
        }
        
        return producción;
    }
    
    /**
     * Obtiene y construye todas las producciones a partir de un arreglo con 
     * las lineas leidas de un archivo
     * @param lineas ArrayList con las lineas leidas del archivo
     * @return ArrayList de objetos producción con una producción contenida
     */
    public ArrayList<Producción> leer_producciones(ArrayList<String> lineas) {
        int num_lineas = lineas.size();
        Producción producción;
        ArrayList<Producción> producciones = new ArrayList<Producción>();
        
        for(int i=0; i<num_lineas; i++){
            producción = leer_producción(lineas.get(i), i);
            producciones.add(producción);
        }  
        return producciones;
    }
    
    /**
     * Carga una glc desde un archivo
     * @param ruta Ruta y nombre del archivo a cargar
     */
    public void cargar_desde_ruta(String ruta){
        ArrayList<String> lineas = leer_archivo(ruta);
        glc.guardar_no_terminales(leer_no_terminales(lineas));
        glc.guardar_producciones(leer_producciones(lineas));
        glc.guardar_terminales(leer_terminales(lineas));
    }
    
    /**
     * Imprime la glc almacenda en el contexto actual
     */
    public void imprimir_glc(){
        ArrayList<Producción> producciones = glc.obtener_producciones();
        int num_producciones = producciones.size();
        Producción producción = new Producción();
        char no_terminal;
        String alfa;
        int numero;
        
        for (int i = 0; i < num_producciones; i++) {
            producción = producciones.get(i);
            no_terminal = producción.obtener_no_terminal();
            alfa = producción.obtener_alfa();
            numero = producción.obtener_numero();
            System.out.println(no_terminal+"->"+alfa+" ["+numero+"]");
        }
        System.out.println("");
    }
    
}
