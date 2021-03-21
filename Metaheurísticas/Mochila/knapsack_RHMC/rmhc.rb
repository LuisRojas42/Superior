require "./mochila.rb"
class RMHC
  attr_accessor :max_iteraciones, :peso_max
  attr_reader :mochila
  def initialize(max_iteraciones=100,peso_max=10)
    @max_iteraciones=max_iteraciones
    @peso_max=peso_max
    @mochila=Mochila.new([],@peso_max)
  end

  def num_to_bin(num)
    str=[]
    if num==0
      @mochila.lista_objetos.length.times{|i|
        str.push(0)
      }
      return str
    end
    while num>0
      if num%2==0
        str.unshift(0)
      else
        str.unshift(1)
      end
      num/=2
    end
    dif=@mochila.lista_objetos.length-str.length
    puts str.to_s
    dif.times{|i|str.unshift(0)}
    puts str.to_s
    str
  end

  def agregar_obj(peso,beneficio)
    @mochila.agregar_objeto(peso,beneficio)
  end

  def algorithm()
    i=0
    best_solution=0
    bits=[]
    loop{
      # Se genera la solucion aleatoria
      gen=0
      # Se genera un numero de combinacion 2^(N)
      @mochila.lista_objetos.length.times{|i|gen+=2**i}
      solu=rand(1..(gen))
      bits=num_to_bin(solu)
      if @mochila.obtener_peso(bits)<=@peso_max and @mochila.obtener_beneficio(bits)>0
        break
      end
    }
    bits.each{|i|
      if i==1
        best_solution+=1
      end
    }

    print("bs ",best_solution,"\n")

    f_best=@mochila.obtener_beneficio(bits)
    str="Solucion inicial:\n#{@mochila.obtener_lista_sel(bits)}\n"+
      "Peso: #{@mochila.obtener_peso(bits)} & Beneficio: #{f_best}"

    while i<@max_iteraciones
      locus=rand(0..(best_solution-1)).to_i
      new_best=rand(locus..best_solution).to_i
      new_best.times{|i|
        bits[i]^=1
      }
      peso_n=@mochila.obtener_peso(bits)
      f_new=@mochila.obtener_beneficio(bits)
      if f_new>=f_best and peso_n<=@peso_max
        best_solution=new_best
        f_best=f_new
      else
        new_best.times{|i|
          bits[i]^=1
        }
      end
      i+=1
    end
    str+="\n\nSolucion final\n#{@mochila.obtener_lista_sel(bits)}\n"+
      "Peso: #{@mochila.obtener_peso(bits)} & Beneficio: #{f_best}\n"+
      "Peso maximo de #{@peso_max}"
    str
  end


end
