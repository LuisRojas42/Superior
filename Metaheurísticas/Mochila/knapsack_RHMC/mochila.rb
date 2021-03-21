#!/usr/bin/env ruby
require "./objeto.rb"
class Mochila
  attr_accessor :lista_objetos,:peso_max
  def initialize(lista_objetos=[],peso_max=10)
    @lista_objetos=lista_objetos
    @peso_max=peso_max
  end

  def obtener_lista()
    str=""
    @lista_objetos.each{|i|
      str+="[ ] #{i.to_s}\n"
    }
    str
  end

  def obtener_lista_sel(arr)
    # arr -> contiene 0 o 1 para saber si esta o no en la mochila
    str=""
    @lista_objetos.each_with_index{|i,j|
      if arr[j]==1
        str+="True #{i.to_s}\n"
      end
    }
    str
  end

  def obtener_peso(arr)
    # Se obtiene de los objetos seleccionados
    peso=0
    @lista_objetos.each_with_index{|i,j|
      if arr[j]==1
        peso+=i.peso
      end
    }
    peso
  end

  def obtener_beneficio(arr)
    ben=0
    @lista_objetos.each_with_index{|i,j|
      if arr[j]==1
        ben+=i.beneficio
      end
    }
    ben
  end

  def agregar_objeto(peso,beneficio)
    @lista_objetos.push(Objeto.new(peso,beneficio))
  end
end
