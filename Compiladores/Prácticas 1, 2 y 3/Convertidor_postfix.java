package af;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Stack;

public class Convertidor_postfix {

	/** Mapa de precedencia de operadores. */
	private static final Map<Character, Integer> Mapa_precedencia;
	static {
            Map<Character, Integer> map = new HashMap<Character, Integer>();
            map.put('(', 1);
            map.put('|', 2);
            map.put('.', 3); 
            map.put('?', 4);
            map.put('*', 4);
            map.put('+', 4);
            map.put('^', 5);
            Mapa_precedencia = Collections.unmodifiableMap(map);
	};

	/**
	 * Obtiene la precedencia de operadores
	 * 
	 * @param c simbolo 
	 * @return precedencia correspondiente
	 */
	private static Integer obtener_precedencia(Character simbolo) {
            Integer precedencia = Mapa_precedencia.get(simbolo);
            return precedencia == null ? 6 : precedencia;
	}

	/**
	 * Inserta un '.' en la expresión para denotar concatenación
	 * @param expresión expresión regular 
	 * @return expresión regular con el '.' para denotar concatenación
	 */
	private static String dar_formato(String expresión) {
		String expresión_con_formato = new String();
		List<Character> operadores = Arrays.asList('|', '+', '*');
		List<Character> operadores_binarios = Arrays.asList('|');

		for (int i = 0; i < expresión.length(); i++) {
                    Character simbolo = expresión.charAt(i);
                    if (i + 1 < expresión.length()) {
                        Character simbolo_siguiente = expresión.charAt(i + 1);
                        expresión_con_formato += simbolo;
                        if (!simbolo.equals('(') && !simbolo_siguiente.equals(')') && !operadores.contains(simbolo_siguiente) && !operadores_binarios.contains(simbolo)) {
                            expresión_con_formato += '.';
                        }
                    }
		}
		expresión_con_formato += expresión.charAt(expresión.length() - 1);

		return expresión_con_formato;
	}

	/**
	 * Convierte  una expresión regular de la notación infix a postfix
	 * Algoritmo de Shunting-yard .
	 * 
	 * @param expresión expresión regular en notación infix
	 * @return postfix expresión regular en notación postfix
	 */
	public static String converir_expresión(String expresión) {
		String postfix = new String();
		Stack<Character> pila = new Stack<Character>();
		String expresión_con_formato = dar_formato(expresión);

		for (Character simbolo : expresión_con_formato.toCharArray()) {
                    switch (simbolo) {
                        case '(':
                            pila.push(simbolo);
                            break;

                        case ')':
                            while (!pila.peek().equals('(')) {
                                    postfix += pila.pop();
                            }
                            pila.pop();
                            break;

                        default:
                            while (pila.size() > 0) {
                                Character último_elemento_pila = pila.peek();

                                Integer precedencia_ultimo_elemento = obtener_precedencia(último_elemento_pila);
                                Integer precedencia_actual_elemento = obtener_precedencia(simbolo);

                                if (precedencia_ultimo_elemento >= precedencia_actual_elemento) {
                                    postfix += pila.pop();
                                } else {
                                    break;
                                }
                            }
                            pila.push(simbolo);
                            break;
                    }

		}

		while (pila.size() > 0)
                    postfix += pila.pop();

		return postfix;
	}
}