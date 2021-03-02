/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package af;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;

/**
 *
 * @author luisrojas
 */
public class Thompson {
    
    private static int estados = 0;

 
    /**
     * Convierte una expresion regular en un AFN
     * @return objeto tipo AF con un AFN contenido
     */
    public AF convertir(String expresión_regular){
        
        Convertidor_postfix regEx = new Convertidor_postfix();
        String expresión_en_postfix = regEx.converir_expresión(expresión_regular);
        
        Nodo nodo_raiz = new Nodo();
        Árbol_sintáctico árbol_sintáctico = new Árbol_sintáctico();
        nodo_raiz = árbol_sintáctico.construir_árbol(expresión_en_postfix);
        
        AF af = construye(nodo_raiz);
        
        return af;
    }
    
    /**
     * Contruye un AFN con las plantillas de Thompsom para un nodo del arbol de análisis sintáctico 
     * @return objeto tipo AF con un AFN contenido
     */
    public AF construye(Nodo nodo_raiz ){
        AF af = new AF();
        try{
            switch(nodo_raiz.obtener_valor()){
                case '.':
                    af = concatenar(construye(nodo_raiz.obtener_izquierdo()), construye(nodo_raiz.obtener_derecho()));
                    break;

                case '*':
                    af = cerradura_kleene(construye(nodo_raiz.obtener_izquierdo()));
                    break;

                case '|':
                    af = unir(construye(nodo_raiz.obtener_izquierdo()), construye(nodo_raiz.obtener_derecho()));
                    break;

                default:
                    af = básico(nodo_raiz.obtener_valor()+"");
                    break;

            }
        }catch(Exception e){
            System.out.println("Error en construye: "+e);
        }
        return af;
    }
    
    /**
     * Construye un AFN a partir de un siímbolo, que puede ser
     * un símbolo del alfabeto o el simbolo vacio.
     * @param simbolo El símbolo a partir del cual construir el AFN.
     * @return El AFN para el símbolo contenido en un objeto AF.
     */
    public static AF básico(String simbolo) {
        AF af = new AF();
        
        /* Estados inicial y final */
        String estado_inicial = estados+"";
        af.guardar_estado_inicial(estado_inicial);
        estados++;
        String estado_final = estados+"";
        af.guardar_estado_final(estado_final);
        estados++;
       
        /* Transicion entre los estados inicial y final */
        af.guardar_transición(estado_inicial, estado_final, simbolo);
       
        /* Agregamos los estados al AFN */
        af.guardar_estado(estado_inicial);
        af.guardar_estado(estado_final);
       
        /* Agregamos el símbolo al alfabeto */
        af.guardar_simbolo(simbolo);
        
        af.guardar_EsAFN(true);
        
        return af;
    }
    
    /**
     * Agrega las transiciones de un AFN a otro
     * @param af AFN al cual se le agregarán las transiciones
     * @param af1 AFN que copiara sus transiciones
     * @return objeto tipo AF con un AFN contenido
     */
    public static AF agregar_transiciones(AF af, AF af1){
        ArrayList<Transición> transiciones_af1 = af1.obtener_transiciones();
        int num_transiciones = transiciones_af1.size();
        
        for (int i = 0; i < num_transiciones; i++) {
            af.guardar_transición(transiciones_af1.get(i));
        }
        
        return af;
    }
    
    /**
     * Agrega el alfabeto de un AFN a otro
     * @param af AFN al cual se le agregará el alfabeto
     * @param af1 AFN que copiara su alfabeto
     * @return objeto tipo AF con un AFN contenido
     */
    public static AF agregar_alfabetos(AF af, AF af1){
        ArrayList<String> alfabeto_af1 = af1.obtener_alfabeto();
        int num_simbolos = alfabeto_af1.size();
        
        for (int i = 0; i < num_simbolos; i++) {
            af.guardar_simbolo(alfabeto_af1.get(i));
        }
        
        return af;
    }
    
    /**
     * Agrega los estados de un AFN a otro
     * @param af AFN al cual se le agregarán los estados
     * @param af1 AFN que copiara sus estados
     * @return objeto tipo AF con un AFN contenido
     */
    public static AF agregar_estados(AF af, AF af1){
        ArrayList<String> estados_af1 = af1.obtener_estados();
        int num_estados = estados_af1.size();
        
        for (int i = 0; i < num_estados; i++) {
            af.guardar_estado(estados_af1.get(i));
        }
        
        return af;
    }
    
    /**
     * Aplica el operador de union a dos AFNs dados.
     * @param af1 El primer operando de la union.
     * @param af2 El segundo operando de la union.
     * @return El AFN resultante de la union de
     * afn1 y afn2 contenido en un objeto AF.
     */
    public static AF unir(AF af1, AF af2) {
        AF af = new AF();
        String estado_inicial_af1 = af1.obtener_estado_inicial();
        String estado_inicial_af2 = af2.obtener_estado_inicial();
        ArrayList <String> estado_final_af1 = af1.obtener_estados_finales();
        ArrayList <String> estado_final_af2 = af2.obtener_estados_finales();
        
        af = agregar_transiciones(af, af1);
        af = agregar_transiciones(af, af2);
        
        af = agregar_alfabetos(af, af1);
        af = agregar_alfabetos(af, af2);
        
        af = agregar_estados(af, af1);
        af = agregar_estados(af, af2);
        
        /* Estados inicial y final */
        String estado_inicial = estados+"";
        af.guardar_estado_inicial(estado_inicial);
        af.guardar_estado(estado_inicial);
        estados++;
        String estado_final = estados+"";
        af.guardar_estado_final(estado_final);
        af.guardar_estado(estado_final);
        estados++;
        
        af.guardar_transición(estado_inicial, estado_inicial_af1, "E");
        af.guardar_transición(estado_inicial, estado_inicial_af2, "E");
        
        for (int i = 0; i < estado_final_af1.size(); i++) {
            af.guardar_transición(estado_final_af1.get(i), estado_final, "E");
        }
        for (int i = 0; i < estado_final_af1.size(); i++) {
            af.guardar_transición(estado_final_af2.get(i), estado_final, "E");
        }
        
        af.guardar_EsAFN(true);
        
        return af;
    }
    
    /**
     * Aplica el operador de concatenacion a dos AFNs dados.
     * @param af1 El primer operando de la concatenacion.
     * @param af2 El segundo operando de la concatenacion.
     * @return El AFN resultante de la concatenacion de
     * af1 y af2 contenido en objeto AF.
     */
    public static AF concatenar(AF af1, AF af2){
        AF af = new AF();
        String estado_inicial_af1 = af1.obtener_estado_inicial();
        String estado_inicial_af2 = af2.obtener_estado_inicial();
        ArrayList <String> estado_final_af1 = af1.obtener_estados_finales();
        ArrayList <String> estado_final_af2 = af2.obtener_estados_finales();
        int num_estados_finales_fn1 = estado_final_af1.size();
        String estado_siguiente;
        String estado;
        String simbolo;
        
        af = agregar_transiciones(af, af1);
        af = agregar_transiciones(af, af2);
        
        af = agregar_alfabetos(af, af1);
        af = agregar_alfabetos(af, af2);
        
        af = agregar_estados(af, af1);
        af = agregar_estados(af, af2);
        
        af.guardar_estado_inicial(estado_inicial_af1);
        af.guardar_estados_finales(estado_final_af2);
        
        ArrayList<Transición> transiciones_fn = af.obtener_transiciones();
        int num_transiciones_fn = transiciones_fn.size();
        
        for (int i = 0; i < num_estados_finales_fn1; i++) {
            for (int j = 0; j < num_transiciones_fn; j++) {
                estado_siguiente = transiciones_fn.get(j).obtener_estado_siguiente();
                if (estado_siguiente.equals(estado_final_af1.get(i))) {
                    estado = transiciones_fn.get(j).obtener_estado();
                    simbolo = transiciones_fn.get(j).obtener_simbolo();
                    af.modificar_transición(j, estado, estado_inicial_af2, simbolo);
                }
            }
        }
        
        af.guardar_EsAFN(true);
        
        return af;
    }
    
    /**
     * Aplica la cerradura de Kleene (*) a un AFN dado.
     * @param af1 El AFN sobre el cual aplicar la cerradura de Kleene.
     * @return El AFN resultante de aplicar cerradura de Kleene al afn contenido en un objeto AF.
     */
    public static AF cerradura_kleene(AF af1) {
        AF af = new AF();
        String estado_inicial_af1 = af1.obtener_estado_inicial();
        ArrayList <String> estado_final_af1 = af1.obtener_estados_finales();
        int num_estados_finales_fn1 = estado_final_af1.size();
        
        af = agregar_transiciones(af, af1);
        af = agregar_alfabetos(af, af1);
        af = agregar_estados(af, af1);
        
        String estado_inicial = estados+"";
        af.guardar_estado_inicial(estado_inicial);
        af.guardar_estado(estado_inicial);
        estados++;
        String estado_final = estados+"";
        af.guardar_estado_final(estado_final);
        af.guardar_estado(estado_final);
        estados++;
        
        af.guardar_transición(estado_inicial, estado_inicial_af1, "E");
        for (int i = 0; i < num_estados_finales_fn1; i++) {
            af.guardar_transición(estado_final_af1.get(i), estado_final, "E");
            af.guardar_transición(estado_final_af1.get(i), estado_inicial_af1, "E");
        }
        af.guardar_transición(estado_inicial, estado_final, "E");
        
        af.guardar_EsAFN(true);
        
        return af;
    }
    
    /**
     * Desplaza todas las etiquetas de los estados de un AFN n posiciones
     * @param af AFN al cual se le desplazarán las etiquetas de los estados
     * @return objeto tipo AF con un AFN contenido
     */
    private static AF reetiquetar(AF af) {
        ArrayList<Transición> transiciones = af.obtener_transiciones();
        int num_transiciones = transiciones.size();
        int estado_inicial = Integer.parseInt(af.obtener_estado_inicial())+estados;
        af.guardar_estado_inicial(estado_inicial+"");
        ArrayList<String> estados_finales = af.obtener_estados_finales();
        int num_estados_finales = estados_finales.size();
        af.guardar_estados_finales(new ArrayList<String>());
        for (int i = 0; i < num_estados_finales; i++) {
            int estado_final = Integer.parseInt(estados_finales.get(i))+estados;
            af.guardar_estado_final(estado_final+"");
        }
        int estados_actuales = estados;
        String simbolo;
        String estado;
        String estado_siguiente;
        int nuevo_estado;
        int nuevo_estado_siguiente;
        
        for (int i = 0; i < num_transiciones; i++) {
            simbolo = transiciones.get(i).obtener_simbolo();
            estado = transiciones.get(i).obtener_estado();
            estado_siguiente = transiciones.get(i).obtener_estado_siguiente();
            nuevo_estado = estados + Integer.parseInt(estado);
            nuevo_estado_siguiente = estados + Integer.parseInt(estado_siguiente);
            af.modificar_transición(i, nuevo_estado+"", nuevo_estado_siguiente+"", simbolo);
            af.guardar_estado(nuevo_estado+"");
            af.guardar_estado(nuevo_estado_siguiente+"");
            estados_actuales++;
        }
        estados = estados_actuales+1;
        
        return af;
    }
    
     /**
     * Aplica la cerradura positiva (+) a un AFN dado.
     * @param af El AFN sobre el cual aplicar la cerradura positiva.
     * @return El AFN resultante de aplicar cerradura positiva a af contenido en un objeto AF.
     */
    public static AF cerradura_positiva(AF af) {
        AF af1 = cerradura_kleene(af);
        AF af2 = reetiquetar(af);
        return concatenar(af2, af1);
    }
    
}
