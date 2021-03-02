/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package af;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.PrintWriter;
import static java.lang.Integer.parseInt;
import java.util.ArrayList;
import java.util.regex.Pattern;

/**
 *
 * @author luisrojas
 */
public class Operador_AF {
    
    private AF af;
    private String error;
    String[][] tabla_transiciones;
    
    /*AF*/
    /**
     * Consulta el AF
     * @return af Autómata finito.
     */
    public AF obtener_Af() {
        return af;
    }

    /**
     * Asigna un AF
     * @param af Autómata finito.
     */
    public void guardar_Af(AF af) {
        this.af = af;
    }
    
    /*ERROR*/
    /**
     * Consulta el error almacenado
     * @return error almacenado.
     */
    public String obtener_error() {
        return error;
    }
    
    /**
     * Almacena un posible error
     * @param error error producido para almacenar.
     */
    public void guardar_error(String error) {
        this.error = error;
    }
    
    /*Cargar autómata*/
    /**
     * Lee un archivo txt 
     * @param nombre ruta seguido del nombre del archivo de texto a leer.
     * @return Lineas del archivo de texto cargado en un ArrayList.
     */
    public ArrayList<String> leer_archivo(String nombre){
        File archivo = null;
        FileReader fr = null;
        BufferedReader br = null;
        ArrayList<String> lineas = new ArrayList<String>();

        try {
            archivo = new File (nombre);
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
     * Valida que el autómata este correctamente descrito en un ArrayList
     * @param lineas Lineas de texto de un archivo de texto
     * @return Verdadero para decir que el autómata esta bien descrito y falso de lo contrario.
     */
    public boolean validar_automata(ArrayList<String> lineas){
        boolean hay_inicio=false;
        boolean hay_final=false;
        boolean trans_correctas = false;
        String patron_transicion = "[\\d]+->[\\d]+,[a-zE]+";
        
        hay_inicio = lineas.get(0).indexOf("inicial:") !=-1? true: false;
        hay_inicio = lineas.get(0).replaceAll("[^\\d]", "") !=""? true: false;
        
        hay_final = lineas.get(1).indexOf("finales:") !=-1? true: false;
        hay_final = lineas.get(1).replaceAll("[^\\d]", "") !=""? true: false;
        
        for(int i=2; i<lineas.size(); i++){
            trans_correctas = Pattern.matches(patron_transicion, lineas.get(i));
            if(!trans_correctas)
                break;
        }
        
        return hay_inicio && hay_final && trans_correctas;
    }
    
    /**
     * Almacena en un objeto AF un AFN o AFD desde un archivo de texto
     * @param nombre ruta seguido del nombre del archivo de texto a leer.
     */
    public void cargar_desde_ruta(String nombre){
        ArrayList<String> lineas = leer_archivo(nombre);
        boolean automata_correcto = validar_automata(lineas);
        
        if(automata_correcto){
            af = new AF();
            String estado_inicial = lineas.get(0).replaceAll("[^\\d]", "");
            String estados_finales[] = lineas.get(1).replaceAll("finales:", "").split(",");
            int num_estados_finales = estados_finales.length;
            int num_transiciones = lineas.size();
            
            af.guardar_estado_inicial(estado_inicial);
            for(int i=0; i<num_estados_finales; i++){
                af.guardar_estado_final(estados_finales[i]);
            }
            
            for(int i=2; i<num_transiciones; i++){
                String estado = lineas.get(i).split("->")[0];
                String estado_siguiente = lineas.get(i).split("->")[1].replaceAll("[^\\d]", "");
                String simbolo = lineas.get(i).split(",")[1];
                
                af.guardar_simbolo(simbolo);
                af.guardar_estado(estado);
                af.guardar_transición(estado, estado_siguiente, simbolo);
            }
        }else{
            error = "Autómata no reconocido";
        }
        hacer_tabla_transiciones();
        comprobar_determinismo();
    }
    
    /**
     * Escribe y guarda el AF contenido en este objeto en un archivo de texto
     * @param nombre nombre del archivo que se guarda.
     */
    public void guardar_en_archivo(String nombre){
        FileWriter fichero = null;
        PrintWriter pw = null;
        ArrayList alfabeto = af.obtener_alfabeto();
        int num_simbolos = alfabeto.size();
        String estado_inicial = af.obtener_estado_inicial();
        ArrayList<String> estados_finales = af.obtener_estados_finales();
        int num_estados_finales = estados_finales.size();
        String estados_finales_cadena="";
        ArrayList<Transición> transiciones = af.obtener_transiciones();
        int num_transiciones = transiciones.size();
        String estado;
        String estado_siguiente;
        String simbolo;
        String transicion;
        
        if(num_simbolos!=0)
            try
            {
                fichero = new FileWriter("/Users/luisrojas/Documents/ESCOM/7mo/COMPILADORES/AF/"+nombre);
                pw = new PrintWriter(fichero);

                pw.println("inicial:"+estado_inicial);
                
                for(int i=0; i<num_estados_finales; i++){
                    estados_finales_cadena += estados_finales.get(i)+",";
                }
                estados_finales_cadena = estados_finales_cadena.substring(0, estados_finales_cadena.length()-1);
                pw.println("finales:"+estados_finales_cadena);

                for (int i = 0; i < num_transiciones; i++){
                    estado = transiciones.get(i).obtener_estado();
                    estado_siguiente = transiciones.get(i).obtener_estado_siguiente();
                    simbolo = transiciones.get(i).obtener_simbolo();
                    transicion = estado+"->"+estado_siguiente+","+simbolo;
                    pw.println(transicion);
                }

            } catch (Exception e) {
                e.printStackTrace();
                error = e.toString();
            } finally {
               try {
               if (null != fichero)
                  fichero.close();
               } catch (Exception e2) {
                  e2.printStackTrace();
                  error = e2.toString();
               }
            }
    }
    
    /**
     * Elimina una transición de un af
     * @param estado estado de la transición a eliminar
     * * @param estado_siguiente estado siguiente de la transición a eliminar
     * * @param simbolo simbolo de la transición a eliminar
     */
    public void eliminar_transicion(String estado, String estado_siguiente, String simbolo){
        ArrayList<Transición> transiciones = af.obtener_transiciones();
        int num_transiciones = transiciones.size();
        int indice_transicion;
        String estado_af;
        String estado_siguiente_af;
        String simbolo_af;
        
        for(indice_transicion=0; indice_transicion<num_transiciones; indice_transicion++){
            estado_af = transiciones.get(indice_transicion).obtener_estado();
            estado_siguiente_af = transiciones.get(indice_transicion).obtener_estado_siguiente();
            simbolo_af = transiciones.get(indice_transicion).obtener_simbolo();
            if(estado.equals(estado_af) && estado_siguiente.equals(estado_siguiente_af) && simbolo.equals(simbolo_af)){
                transiciones.remove(indice_transicion);
                break;
            }
        }
        af.guardar_transiciones(transiciones);
    }
    
    /**
     * Llena todos los espacios de una tabla con una cadena vacia
     * @param filas numero de filas de la tabla
     * * @param columnas numero de columnas de la tabla
     */
    public void vaciar_tabla(int filas, int columnas){
        for(int i=0; i<filas; i++){
            for(int j=0; j<columnas; j++){
                tabla_transiciones[i][j]="";
            }
        }
    }
    
    /**
     * Agrega los estados de un af en la primera columna y en diferentes filas de una tabla 
     * @param filas numero de filas de la tabla
     * * @param estaods Arreglo con los estados de un af contenidos
     */
    public void agregar_filas_tabla(int filas, ArrayList<String> estados){
        for(int i=1; i<filas; i++){
            tabla_transiciones[i][0] = estados.get(i-1);
        }
    }
    
    /**
     * Agrega el alfabeto de un af en la primera fila y en diferentes columnas de una tabla 
     * @param filas numero de filas de la tabla
     * * @param estaods Arreglo con los estados de un af contenidos
     */
    public void agregar_columnas_tabla(int columnas, ArrayList<String> alfabeto){
        for(int i=1; i<columnas; i++){
            tabla_transiciones[0][i] = alfabeto.get(i-1);
        }
    }
    
    /**
     * Agrega cada transición de un af a una tabla 
     */
    public void hacer_tabla_transiciones(){
        ArrayList<String> alfabeto =  af.obtener_alfabeto();
        ArrayList<String> estados =  af.obtener_estados();
        ArrayList<Transición> transiciones =  af.obtener_transiciones();
        int num_transiciones = transiciones.size();
        int filas = estados.size()+1;
        int columnas = alfabeto.size()+1;
        String estado;
        String estado_siguiente;
        String simbolo;
        
        tabla_transiciones = new String[filas][columnas];
        vaciar_tabla(filas, columnas);
        agregar_filas_tabla(filas, estados);
        agregar_columnas_tabla(columnas, alfabeto);
        
        for(int i=0; i<num_transiciones; i++){
            estado = transiciones.get(i).obtener_estado();
            estado_siguiente = transiciones.get(i).obtener_estado_siguiente();
            simbolo = transiciones.get(i).obtener_simbolo();
            
            for(int j=1; j<filas; j++){
                if(estado.equals(tabla_transiciones[j][0])){
                    for(int k=0; k<columnas; k++){
                        if(simbolo.equals(tabla_transiciones[0][k])){
                            if(!tabla_transiciones[j][k].equals("")){
                                tabla_transiciones[j][k]= tabla_transiciones[j][k]+"/"+estado_siguiente;
                            }else{
                                tabla_transiciones[j][k]= estado_siguiente;
                            }
                        }
                    }
                }
            }
        }
    }
    
    /**
     * Imprime una tabla en un formato para lectura
     */
    public void imprimir_tabla_transiciones(){
        ArrayList<String> alfabeto =  af.obtener_alfabeto();
        ArrayList<String> estados =  af.obtener_estados();
        int filas = estados.size()+1;
        int columnas = alfabeto.size()+1;
        
        for(int i=0; i<filas; i++){
            for(int j=0; j<columnas; j++){
                try{
                    System.out.print(tabla_transiciones[i][j]+"\t");
                }catch(Exception e){
                    error=e.toString();
                }               
            }  
            System.out.println("");
        }
    }
    
    /**
     * Imprime las transiciones con el formato: estado -> estado siguiente, simbolo
     */
    public void imprimir_transiciones(){
        ArrayList<Transición> transiciones = af.obtener_transiciones();
        int num_transiciones = transiciones.size();
        for (int i = 0; i < num_transiciones; i++) {
            System.out.print(transiciones.get(i).obtener_estado()+"->");
            System.out.print(transiciones.get(i).obtener_estado_siguiente()+",");
            System.out.println(transiciones.get(i).obtener_simbolo());
        }
    }
    
    /**
     * Determina si un af es determinista o no buscando si en su tabla de transiciones
     * hay entradas dobles
     */
    public boolean comprobar_determinismo(){
        ArrayList<String> alfabeto =  af.obtener_alfabeto();
        ArrayList<String> estados =  af.obtener_estados();
        int filas = estados.size()+1;
        int columnas = alfabeto.size()+1;
        af.guardar_EsAFD(true);
        
        for(int i=0; i<filas; i++){
            for(int j=0; j<columnas; j++){
                if (tabla_transiciones[i][j].contains("/")) {
                    af.guardar_EsAFN(true);
                    af.guardar_EsAFD(false);
                }
            }  
            System.out.println("");
        }
        return true;
    }
    
     /**
     * Comprueba si una cadea es aceptada por un af
     * @param entrada cadena de prueba
     */
    public boolean aceptar(String entrada){
        if(af.EsAFD()){
            AFD afd = new AFD();
            afd.guardar_Af(af);
            return afd.aceptaAFD(entrada, tabla_transiciones);
        }else{
            AFN afn = new AFN();
            afn.guardar_Af(af);
            return afn.aceptaAFD(entrada, tabla_transiciones);
        }
        //return false;
    }
    
}
