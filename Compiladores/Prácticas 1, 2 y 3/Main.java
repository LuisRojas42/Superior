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
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        Operador_AF operador_af = new Operador_AF();
        operador_af.cargar_desde_ruta("/Users/luisrojas/Documents/ESCOM/7mo/COMPILADORES/AF/afn.af");
        
        //operador_af.eliminar_transicion("1", "2", "E");
        
        AF af = new AF();
        af = operador_af.obtener_Af();
        
        /*INICIAL*/
        System.out.println(af.obtener_estado_inicial());
        
        /*FINALES*/
        System.out.println(af.obtener_estados_finales());
        
        /*GUARDA*/
        operador_af.guardar_en_archivo("af_guardado.af");
        
        /*ALFABETO*/
        System.out.println(af.obtener_alfabeto());
        
        /*ESTADOS*/
        System.out.println(af.obtener_estados());
        
        /*TRANSICIONES*/
        operador_af.imprimir_transiciones();
        
        /*TABLA DE TRANSICIONES*/
        operador_af.imprimir_tabla_transiciones();
        
        /*ES AFD*/
        System.out.println("afd:"+af.EsAFD());
        
        /*ES AFN*/
        System.out.println("afn:"+af.EsAFN());
        
        /*ACEPTA*/
        String entrada = "abb";
        System.out.println("Pertenece "+entrada+":"+operador_af.aceptar(entrada));
        
        String expresión_regular = "(a|b)*abb";
        //String expresión_regular = "bb";
        //String expresión_regular = "ab*";
        //String expresión_regular = "(a|b)*";
        //String expresión_regular = "(a*|b*)*";
        //String expresión_regular = "a|(E|ab*)";
        
        /*ÁRBOL SINTÁCTICO*/
        
        System.out.println("\nAlgortimo Thompson\n");
        
        Árbol_sintáctico arbol = new Árbol_sintáctico();
        Convertidor_postfix cv = new Convertidor_postfix();
        Nodo nodo_raiz = arbol.construir_árbol(cv.converir_expresión(expresión_regular));
        
        
        /*AF CON THOMPSON*/
        
        Thompson thompson = new Thompson();
        AF af_Thompson = thompson.convertir(expresión_regular);
        
        
        /*CREAR AFN CON SIMBOLO*/
        //AF af1 = thompson.básico("a");
        //AF af2 = thompson.básico("b");
        
        /*UNIR*/
        //AF af = thompson.unir(af1, af2);
        
        /*CONCATENAR*/
        //AF af = thompson.concatenar(af1, af2);
        
        /*CERRADURA DE KLEEN*/
        //AF af = thompson.cerradura_kleene(af1);
        
        /*CERRADURA POSITIVA*/
        //AF af = thompson.cerradura_positiva(af1);
        
        operador_af.guardar_Af(af_Thompson);
        
        String entrada_Thompson = "abb";
        System.out.println(operador_af.aceptar(entrada_Thompson));
        System.out.println("");
    }
    
}
