/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package af;

import java.util.ArrayList;
import java.util.Stack;

/**
 *
 * @author luisrojas
 */
public class AFN{
    
    private AF af;

    /**
     * Consulta el AFN
     * @return af Autómata finito no determinista.
     */
    public AF obtener_Af() {
        return af;
    }

    /**
     * Asigna un AFN
     * @param af Autómata finito no determinista.
     */
    public void guardar_Af(AF af) {
        this.af = af;
    }
    
    
    /*CERRADURA*/
    /*
        
        meter todos los estados de T en pila; 
        inicializar ε-cerradura(T) con T; 
        while ( pila no está vacía ) {
            sacar t, el elemento superior, de la pila;
            for ( cada estado u con un flanco de t a u, Indecidible como ε )
                if ( u no está en ε-cerradura(T) ) { 
                    agregar u a ε-cerradura(T);
                    meter u en la pila;
                }
        }
        
    */
     /**
     * Funcion cerradura sobre un conjunto de estados
     * @param conjunto_estados Es el conjunto de estados sobre el que trabajará.
     * @return Nuevo conjunto de estados como resultado de la función
     */
    public ArrayList<String> eCerradura(ArrayList<String> conjunto_estados){
        Stack pila = new Stack();
        ArrayList<String> eCerradura = new ArrayList<String>();
        ArrayList<Transición> transiciones =  af.obtener_transiciones();
        ArrayList<Transición> transiciones_con_E = new ArrayList<Transición>();
        int num_estados = conjunto_estados.size();
        int num_transiciones = transiciones.size();
        String estado;
        String estado_sig;
        String simbolo;
        
        for(int i=0; i<num_estados; i++){
            pila.push(conjunto_estados.get(i));
            eCerradura.add(conjunto_estados.get(i));
        }
        
        while(!pila.empty()){
            String t = (String) pila.pop();
            for(int i=0; i<num_transiciones; i++){
                estado = transiciones.get(i).obtener_estado();
                estado_sig = transiciones.get(i).obtener_estado_siguiente();
                simbolo = transiciones.get(i).obtener_simbolo();
                if(estado.equals(t) && simbolo.equals("E")){
                    transiciones_con_E.add(transiciones.get(i));
                }
            }
            
            int num_transiciones_con_E = transiciones_con_E.size();
            for(int i=0; i<num_transiciones_con_E;i++){
                String u = transiciones_con_E.get(i).obtener_estado_siguiente();
                if(!eCerradura.contains(u)){
                    eCerradura.add(u);
                    pila.push(u);
                }
            }
        }
        
        return eCerradura;
    }
    
    /**
     * Funcion mover sobre un conjunto de estados con un simbolo dado
     * @param estados Es el conjunto de estados sobre el que trabajará.
     * @param simbolo Simbolo del alfabeto con el que movera los estados.
     * @return Nuevo conjunto de estados como resultado de la función
     */
    public ArrayList<String> mover(ArrayList<String> estados, String simbolo){
        ArrayList<Transición> transiciones =  af.obtener_transiciones();
        ArrayList<String> mover = new ArrayList<String>();
        int num_estados = estados.size();
        int num_transiciones = transiciones.size();
        
        for(int i=0; i<num_estados; i++){
            for(int j=0; j<num_transiciones; j++){
                String estado_trans = transiciones.get(j).obtener_estado();
                String simbolo_trans = transiciones.get(j).obtener_simbolo();
                if(estado_trans.equals(estados.get(i)) && simbolo_trans.equals(simbolo)){
                    mover.add(transiciones.get(j).obtener_estado_siguiente());
                }
            }
        }
        return mover;
    }
    
    /**
     * Comprueba si en un conjunto de estados existe alguno sin estar marcado
     * @param Destados Es el conjunto de estados sobre el que buscará.
     * @return Indicie del primer estado encontrado como desmarcado, devolverá -1 si no hay alguno
     */
    public int hay_desmarcados(ArrayList<Destado> Destados){
        int numDestados = Destados.size();
        
        for (int i = 0; i < numDestados; i++) {
            if(!Destados.get(i).esta_marcado()){
                return i;
            }
        }
        
        return -1;
    }
    
    /**
     * Comprueba si ya fue agregado previamente un conjunto de estados en la lista Destados
     * @param Destados Lista de conjuntos de estados en la buscará.
     * @param conjunto_estados Conjunto de estados que buscara en Destados.
     * @return Indice del arreglo en el que se encuentra la lista, devlverá -1 si no se encuentra
     */
    private int esta_en_Destados(ArrayList<Destado> Destados, ArrayList<String> conjunto_estados) {
        int num_Destados = Destados.size();

        for (int i = 0; i < num_Destados; i++) {
            if (Destados.get(i).obtener_conjunto_estados().toString().equals(conjunto_estados.toString())) {
                return i;
            }
        }
        
        return -1;
    }
    
    /**
     * Recolecta las etiquetas que existen en una colección de Destados
     * @param Destados Colección de objetos tipo Destado
     * @return Arreglo con las etiquetas existente en la colección
     */
    private ArrayList<String> obtener_estados(ArrayList<Destado> Destados) {
        int num_estados = Destados.size();
        ArrayList<String> estados = new ArrayList<String>();

        for (int i = 0; i < num_estados; i++) {
            String etiqueta=Destados.get(i).obtener_etiqueta()+"";
            estados.add(etiqueta);
        }
        return estados;
    }

    /**
     * Comprueba si en un conjunto de estados se encuentra alguno de los estados finales existentes
     * @param estados_finales Estados finales que se concideran
     * @param conjunto_estados Es el conjunto de estados sobre el que buscará.
     * @return Verdadero en el caso de encontrarse alguno, false de lo contrario
     */
    private boolean tiene_estados_finales(ArrayList<String> estados_finales, ArrayList<String> conjunto_estados) {
        int num_estados_finales = estados_finales.size();
        
        for (int j = 0; j < num_estados_finales; j++) {
            if(conjunto_estados.contains(estados_finales.get(j))){
                return true;
            }
        }
        return false;
    }
    
    /**
     * Comprueba si en un conjunto de estados se encuentra un estado inicial dado
     * @param estado_inicial Estados inicial que se conciderá
     * @param conjunto_estados Es el conjunto de estados sobre el que buscará.
     * @return Verdadero en el caso de encontrarse alguno, false de lo contrario
     */
    private boolean tiene_estado_inicial(String estado_inicial, ArrayList<String> conjunto_estados) {
        if(conjunto_estados.contains(estado_inicial)){
            return true;
        }
        return false;
    }
    
    /**
     * Dado una colección de objetos Dtrans se interpretan para obtener las 
     * transiciones del nuevo AFD
     * @param Dtrans_table Colección de objetos Dtrans
     * @return Arralist con las transiciones obtenidas
     */
    private ArrayList<Transición> construir_transiciones(ArrayList<Dtrans> Dtrans_table){
        ArrayList<Transición> transiciones = new ArrayList<Transición>();
        int num_transiciones = Dtrans_table.size();
        Transición transición = new Transición();
        String estado;
        String estado_siguiente;
        String simbolo;
        
        for (int i = 0; i < num_transiciones; i++) {
            estado = Dtrans_table.get(i).obtener_T()+"";
            estado_siguiente = Dtrans_table.get(i).obtener_U()+"";
            simbolo = Dtrans_table.get(i).obtener_simbolo();
            transición = new Transición();
            transición.guardar_estado(estado);
            transición.guardar_estado_siguiente(estado_siguiente);
            transición.guardar_simbolo(simbolo);
            transiciones.add(transición);
        }
        return transiciones;
    }
    
    /**
     * Busca en una coleccion de objetos Destado aquel que contiene en 
     * su conjunto de estados al estado inicial
     * @param destados Colección de objetos Destado
     * @return Etiqueta del elemento que contiene el estado inicial en sus estados
     */
    private String etiqueta_estado_inicial(ArrayList<Destado> destados){
        String etiqueta;
        int num_estados = destados.size();
        
        for (int i = 0; i < num_estados; i++) {
            if(destados.get(i).es_inicial()){
                etiqueta = destados.get(i).obtener_etiqueta()+"";
                return etiqueta;
            }
        }
        return "";
    }
    
    /**
     * Busca en una coleccion de objetos Destado aquellos que contienen en 
     * su conjunto de estados alguno de los estados finales
     * @param destados Colección de objetos Destado
     * @return Etiqueta del elemento que contiene algun estado final en sus estados
     */
    private ArrayList<String> etiqueta_estados_finales(ArrayList<Destado> destados){
        ArrayList<String> etiquetas = new ArrayList<String>();
        int num_estados = destados.size();
        
        for (int i = 0; i < num_estados; i++) {
            if(destados.get(i).es_final()){
                etiquetas.add(destados.get(i).obtener_etiqueta()+""); //;
            }
        }
        return etiquetas;
    }
    
    /**
     * Crea un objeto AF con un AFD 
     * @param destados Colección de objetos Destado
     * @param alfabeto Alfabeto del AFD
     * @param Dtrans_table Colección de objetos Dtrans que contienen las transiciones
     * @return Objeto AF que contiene un AFD
     */
    private AF construir_nuevo_af(ArrayList<Destado> destados, ArrayList<String> alfabeto, ArrayList<Dtrans> Dtrans_table) {
        //AFD afd = new AFD();
        AF af = new AF();
        
        af.guardar_EsAFD(true);
        af.guardar_estado_inicial(etiqueta_estado_inicial(destados));
        af.guardar_estados_finales(etiqueta_estados_finales(destados));
        af.guardar_estados(obtener_estados(destados));
        af.guarda_alfabeto(alfabeto);
        af.guardar_transiciones(construir_transiciones(Dtrans_table));
        
        //afd.guardar_Af(af);
        return af;
    }
    
    /*ALGORITMO DE SUBCONJUNTOS*/
    /*
        
        while ( hay un estado sin marcar T en Destados ) { 
            marcar T;
            for ( cada símbolo de entrada a ) {
                U = ε-cerradura(mover(T, a));
                if ( U no está en Destados )
                    agregar U como estado sin marcar a Destados;
                Dtran[T, a] = U;
            } 
        }
        
    */
    /**
     * Comprueba si la cadena es aceptada por el AFN de este objeto
     * @param entrada Cadena que se probará
     * @param tabla_transiciones transiciones mostradas en formato de una tabla
     * @return Resultado booleano de la prueba 
     */
    public boolean aceptaAFD(String entrada, String[][] tabla_transiciones){ 
        ArrayList<String> conjunto_estados = new ArrayList<String>();
        ArrayList<Destado> Destados = new ArrayList<Destado>();
        ArrayList<Dtrans> Dtrans_table = new ArrayList<Dtrans>();
        ArrayList<String> estados_finales = af.obtener_estados_finales();
        String estado_inicial = af.obtener_estado_inicial();
        int num_estados_finales = estados_finales.size();
        ArrayList<String> alfabeto = af.obtener_alfabeto();
        int tam_alfabeto = alfabeto.size();
        char[] etiquetas = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M','N','O','P','Q'};
        int num_etiqueta = 0;
        Destado destado = new Destado();
        AFD afd = new AFD();
        Operador_AF operador_af = new Operador_AF();
        Dtrans dtrans;
        String simbolo;
        
        conjunto_estados.add(estado_inicial);
        conjunto_estados = eCerradura(conjunto_estados);
        
        destado.guardar_conjunto_estados(conjunto_estados);
        destado.guardar_marcado_como(false);
        destado.guardar_etiqueta(etiquetas[num_etiqueta]);
        destado.guardar_es_inicial(true);
        destado.guardar_es_final(tiene_estados_finales(estados_finales,conjunto_estados));
        num_etiqueta++;
        Destados.add(destado);
        
        int indice_Destado = hay_desmarcados(Destados);
        while(indice_Destado != -1){
            Destados.get(indice_Destado).guardar_marcado_como(true);
            for (int i = 0; i < tam_alfabeto; i++) {
                simbolo = alfabeto.get(i);
                conjunto_estados = Destados.get(indice_Destado).obtener_conjunto_estados();
                if(!simbolo.equals("E")){
                    conjunto_estados = eCerradura(mover(conjunto_estados, simbolo));
                    int indice_encontrado = esta_en_Destados(Destados, conjunto_estados);
                    if (indice_encontrado == -1) {
                        destado = new Destado(); 
                        destado.guardar_conjunto_estados(conjunto_estados);
                        destado.guardar_marcado_como(false);
                        destado.guardar_etiqueta(etiquetas[num_etiqueta]);
                        destado.guardar_es_inicial(tiene_estado_inicial(estado_inicial,conjunto_estados));
                        destado.guardar_es_final(tiene_estados_finales(estados_finales,conjunto_estados));
                        Destados.add(destado);
                        num_etiqueta++;
                    }
                    dtrans = new Dtrans();
                    dtrans.guardar_simbolo(alfabeto.get(i));
                    dtrans.guardar_T(Destados.get(indice_Destado).obtener_etiqueta());
                    if (indice_encontrado == -1) {
                        dtrans.guardar_U(etiquetas[num_etiqueta-1]);
                    }else{
                        dtrans.guardar_U(Destados.get(indice_encontrado).obtener_etiqueta());
                    }
                    Dtrans_table.add(dtrans);
                }
            }
            indice_Destado = hay_desmarcados(Destados);
        }
        
        AF nuevo_af = construir_nuevo_af(Destados, alfabeto, Dtrans_table);
        operador_af.guardar_Af(nuevo_af);
        operador_af.hacer_tabla_transiciones();
        //operador_af.imprimir_tabla_transiciones();
        
        return operador_af.aceptar(entrada);
    }
    
}
