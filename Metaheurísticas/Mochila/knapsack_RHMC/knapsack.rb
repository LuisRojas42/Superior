#!/usr/bin/env ruby
require "./rmhc.rb"
require "./fileLoader.rb"
puts "Hola bienvenido al Knapsack Problem"
peso_max=15
max_iteration=200
puts "Cambiar peso:\n\t"+
      "Actualmente el peso maximo es #{peso_max}"
peso_max=gets.chomp.to_i
puts "Cambiar iteraciones\n\t"+
      "Actualmente el programa cuenta con un limite de iteraciones de #{max_iteration}"
max_iteration=gets.chomp.to_i
files=read_file(".")
puts "archivos encontrados de configuraciones:"

files.each_with_index{|i,ind|
  puts "[#{ind+1}]\t#{i}"
}
puts "indice del archivo"
index_file=gets.chomp.to_i
file=File.open(files[index_file-1])
data=file.read
data=data.split("\n")
file.close
knapsack=RMHC.new(max_iteration,peso_max)
data.each{|j|
  a=j.split(",").map(&:to_i)
  knapsack.agregar_obj(a[0],a[1])
}
puts "Muestra de objetos de la mochila\n#{knapsack.mochila.obtener_lista}"
puts knapsack.algorithm
