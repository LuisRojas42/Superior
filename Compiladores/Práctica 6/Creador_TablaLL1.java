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
public class Creador_TablaLL1 {
    
    private TablaLL1 tablall1 = new TablaLL1();
    private GLC glc = new GLC();
    private char calculando;
    private Primero primero = new Primero();
    private Siguiente siguiente = new Siguiente();

    /**
     * Consulta la tabla LL1
     * @return tabla ll1 contenida
     */
    public TablaLL1 obtener_tablall1() {
        return tablall1;
    }

    /**
     * Almacena una tabla ll1 
     * @param tablall1 Tabla ll1 a almacenar
     */
    public void guardar_tablall1(TablaLL1 tablall1) {
        this.tablall1 = tablall1;
    }

    /**
     * Consulta la glc
     * @return glc contenida 
     */
    public GLC obtener_glc() {
        return glc;
    }

    /**
     * Almacena una glc
     * @param glc GLC a almacenar
     */
    public void guardar_glc(GLC glc) {
        this.glc = glc;
    }
    
    /**
     * Crea una tabla ll1 vacia pero con la primera fila contenidos los terminales
     * y en la primer columna los no terminales
     */
    public void crear_tablall1(){
        ArrayList<Character> no_terminales = glc.obtener_no_terminales();
        ArrayList<Character> terminales = glc.obtener_terminales();
        int m=terminales.size()+1; 
        int n=no_terminales.size()+2;
        String[][] tablall1_vacia = new String[m][n]; 
        
        for(int i = 0 ; i < m ; i++) {   
            for(int j = 0 ; j < n ; j++) {  
                if(i==0 && j>0)
                    if(j-1<terminales.size())
                        tablall1_vacia[i][j]=terminales.get(j-1)+"";
                    else
                        tablall1_vacia[i][j]="$";
                else
                    tablall1_vacia[i][j]=" ";
                if(i!=0 && j==0)
                    tablall1_vacia[i][j]=no_terminales.get(i-1)+"";
            } 
        }
        tablall1.guardar_tablall1(tablall1_vacia);
    }
    
    /**
     * Calcula las entradas de la tablla ll1 y las almacena en un arreglo
     */
    public void calcular_tabla(){
        ArrayList<Producción> producciones = glc.obtener_producciones();
        int num_producciones = producciones.size();        
        primero.guardar_glc(glc);
        siguiente.guardar_glc(glc);
        ArrayList<Character> entrada = new ArrayList<Character>();
        String no_terminal;
        int num_producción;
        
        for (int i = 0; i < num_producciones; i++) {
            
            entrada = calcular_entrada(producciones.get(i));
            //System.out.println("ent:"+entrada);
            no_terminal = producciones.get(i).obtener_no_terminal()+"";
            num_producción = producciones.get(i).obtener_numero();
            insertar_entrada(no_terminal, entrada, num_producción);
        }
    }
    
    /**
     * Restablece la lista de los alfa calculados para evitar bucles
     */
    public void restablecer_calculados(){
        ArrayList<String> rest_calculados_p = new ArrayList<String>();
        ArrayList<Character> rest_calculados_s = new ArrayList<Character>();
        
        primero.guardar_calculados(rest_calculados_p);
        siguiente.guardar_calculados(rest_calculados_s);
    }
    
    /**
     * Calcula una entrada de la tabla ll1
     * @param producción Producción a la se le calculará la entrada correspondiente en la tabla
     */
    public ArrayList<Character> calcular_entrada(Producción producción){
        String alfa = alfa = producción.obtener_alfa();
        ArrayList<Character> p = new ArrayList<Character>();
        ArrayList<Character> s = new ArrayList<Character>();
        restablecer_calculados();
        char no_terminal;
          
        p = primero.obtener_primeros(alfa);
        if(p.contains('E')){
            no_terminal = producción.obtener_no_terminal();
            s = siguiente.obtener_siguientes(no_terminal);
            return s;
        }
            
        return p;
    }
    
    /**
     * Inserta una entrada de la tabla ll1
     * @param no_terminal No terminal correspondiente de la inserción
     * @param entrada Símbolo de entrada correspondiente de la inserción
     * @param num_producción Número de la producción correspondiente de la inserción
     */
    public void insertar_entrada(String no_terminal, ArrayList<Character> entrada, int num_producción){
        ArrayList<Character> no_terminales = glc.obtener_no_terminales();
        ArrayList<Character> terminales = glc.obtener_terminales();
        int tam_entrada = entrada.size();
        String[][] tabla = tablall1.obtener_tablall1();
        int filas=tabla.length;
        int columnas=tabla[0].length;
        
        for (int i = 0; i < tam_entrada; i++) {
            for (int j = 0; j < filas; j++) {
                if(tabla[j][0].equals(no_terminal)){
                    for (int k = 0; k < columnas; k++) {
                        if(tabla[0][k].equals(entrada.get(i)+"")){
                            if (tabla[j][k].equals(" ")) {
                                tabla[j][k] += num_producción+"";
                            }else{
                                tabla[j][k] += "/"+num_producción;
                            }
                            j=filas;
                            break;
                        }
                    }
                }
            }
        }
        
    }
    
}
