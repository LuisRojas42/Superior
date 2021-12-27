import pandas as pd
import numpy as np
import sqlalchemy
from flask import *
from flask_cors import CORS, cross_origin

from Recomendador.No_Personalizado.Hot_Ranking import Hot_Ranking
from Recomendador.No_Personalizado.FP_Growth import FP_Growth
from Recomendador.No_Personalizado.Bayes import Bayes
from Recomendador.Personalizado.Basado_en_Contenido import Basado_en_Contenido
from Recomendador.Personalizado.Colaborativo_entre_Elementos import Colaborativo_entre_elementos

app = Flask(__name__)
CORS(app)
engine = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:8889/Restaurante')

##############################
@app.route('/get-ingredientes', methods=['GET'])
def get_ingredientes():    
    table_df = pd.read_sql_table('Ingrediente', con=engine)
    result = table_df.to_json(orient="records", date_format='iso')
    parsed = json.loads(result)
    return jsonify(parsed)

##############################
@app.route('/get-platillos', methods=['GET'])
def get_platillos():
    table_df = pd.read_sql_table('Platillo', con=engine)
    result = table_df.to_json(orient="records", date_format='iso')
    parsed = json.loads(result)
    return jsonify(parsed)

##############################
@app.route('/get-categorias', methods=['GET'])
def get_categorias():
    table_df = pd.read_sql_table('Categoria', con=engine)
    result = table_df.to_json(orient="records", date_format='iso')
    parsed = json.loads(result)
    return jsonify(parsed)

##############################
@app.route('/get-etiquetas', methods=['GET'])
def get_etiquetas():    
    table_df = pd.read_sql_table('Etiqueta', con=engine)
    result = table_df.to_json(orient="records", date_format='iso')
    parsed = json.loads(result)
    return jsonify(parsed)

##############################
@app.route('/get-rankings', methods=['GET'])
def get_rankings():    
    id_categoria = request.args.get('id_categoria')
    if not id_categoria:
        id_categoria = '0'
    with engine.connect() as con:
        result = con.execute("select Platillo.Nombre_platillo, Rankings.ranking, count(Rankings.ranking) as conteo, Platillo.id_Categoria from Rankings inner join Platillo on Platillo.id_Platillo = Rankings.id_Platillo where Platillo.id_Categoria  LIKE '"+id_categoria+"' group by Rankings.id_Platillo, Rankings.ranking;")
        columns = [col for col in result.keys()]
        rows = [dict(zip(columns, row)) for row in result]
        #print(rows)        
        items = Hot_Ranking.Hot_Raning(rows)
    return json.dumps(items)  

##############################
@app.route('/get-reglas', methods=['GET'])
def get_reglas():    
    with engine.connect() as con:
        result = con.execute("select Orden.id_Orden, Usuario.Nombre, Platillo.Nombre_Platillo from Orden inner join Usuario on Usuario.id_Usuario = Orden.id_Usuario inner join Orden_Platillo on Orden.id_Orden = Orden_Platillo.id_Orden inner join Platillo on Platillo.id_Platillo = Orden_Platillo.id_Platillo;")
        columns = [col for col in result.keys()]
        rows = [dict(zip(columns, row)) for row in result]
        #print(rows)        
        items = FP_Growth.FP_Growth(rows)
    return json.dumps(items)  

##############################
# BAYES
@app.route('/get-asociaciones', methods=['GET'])
def get_asociaciones():    
    id_platillo = request.args.get('id_platillo')
    if not id_platillo:
        id_platillo = '1'
    with engine.connect() as con:
        result = con.execute("select * from Rankings;")
        columns = [col for col in result.keys()]
        rows = [dict(zip(columns, row)) for row in result]
        #print(rows)        
        items = Bayes.Bayes(rows, int(id_platillo))
    return json.dumps(items)  

##############################
@app.route('/get-mas_pedidos', methods=['GET'])
def get_mas_pedidos():    
    tiempo = request.args.get('tiempo')
    if not tiempo:
        tiempo = "10000"
    id_categoria = request.args.get('id_categoria')
    if not id_categoria:
        id_categoria = '1'
    with engine.connect() as con:
        #result = con.execute("call Mas_Pedido("+str(tiempo)+", '"+str(id_categoria)+"')")
        result = con.execute("select Platillo.Nombre_platillo, count(Orden_Platillo.id_Platillo) as pedidos, Platillo.id_Categoria from Orden_Platillo inner join Platillo on Platillo.id_Platillo = Orden_Platillo.id_Platillo inner join Orden on Orden.id_Orden = Orden_Platillo.id_Orden WHERE Orden.fecha >= CURRENT_DATE() - INTERVAL "+tiempo+" DAY and Platillo.id_Categoria  LIKE "+id_categoria+" group by Orden_Platillo.id_Platillo;")
        columns = [col for col in result.keys()]
        rows = [dict(zip(columns, row)) for row in result]
        #print(rows)        
    return json.dumps(rows)  

##############################
@app.route('/set-revisado', methods=['GET'])
def set_revisado():    
    id_Usuario = request.args.get('id_Usuario')
    id_Platillo = request.args.get('id_Platillo')
    if len(id_Usuario) > 0 and len(id_Platillo) > 0:
        with engine.connect() as con:
            id_Usuario = pd.read_sql_query("select id_Usuario from Usuario where nombre='"+id_Usuario+"';", con=engine)
            if not id_Usuario.empty:
                id_Usuario = id_Usuario.iloc[0]['id_Usuario']
                result = con.execute("insert into Revisados (id_Usuario, id_Platillo) values("+str(id_Usuario)+", "+str(id_Platillo)+");")                        
                return "Registro exitoso"
            else:
                return "No se encontro el Usuario"
    else:
        return "Parametros faltantes"    
         
##############################
@app.route('/set-usuario', methods=['GET'])
def set_usuario():    
    id_Usuario = request.args.get('id_Usuario')
    if len(id_Usuario) >= 1:
        with engine.connect() as con:
            result = con.execute("INSERT INTO Usuario (Nombre) SELECT * FROM (SELECT '"+str(id_Usuario)+"') AS tmp WHERE NOT EXISTS ( SELECT Nombre FROM Usuario WHERE Nombre = '"+str(id_Usuario)+"') LIMIT 1;")                        
            return "Registro exitoso"
    else:
        return "Registro fallido"    

##############################
@app.route('/get-ingredientes_platillo', methods=['GET'])
def get_ingredientes_platillo():    
    id_Platillo = request.args.get('id_Platillo')
    if len(id_Platillo) > 0:
        with engine.connect() as con:
            result = con.execute("select p.id_Platillo, Nombre_platillo, Nombre_ingrediente from Ingrediente_Platillo ip join Ingrediente i on i.id_Ingrediente = ip.id_Ingrediente join Platillo p on p.id_Platillo = ip.id_Platillo where ip.id_Platillo = "+str(id_Platillo)+";")                        
            columns = [col for col in result.keys()]
            rows = [dict(zip(columns, row)) for row in result]
            #print(rows)        
        return json.dumps(rows)  
    else:
        return "id_Ingrediente perdido"    

##############################
@app.route('/get-etiqueta_platillo', methods=['GET'])
def get_etiqueta_platillo():    
    id_Platillo = request.args.get('id_Platillo')
    if len(id_Platillo) > 0:
        with engine.connect() as con:
            result = con.execute("select p.id_Platillo, Nombre_platillo, Nombre_etiqueta, cantidad from Etiqueta_Platillo ep join Etiqueta e on e.id_Etiqueta = ep.id_Etiqueta join Platillo p on p.id_Platillo = ep.id_Platillo where ep.id_Platillo = "+str(id_Platillo)+";")                        
            columns = [col for col in result.keys()]
            rows = [dict(zip(columns, row)) for row in result]
            #print(rows)        
        return json.dumps(rows)  
    else:
        return "id_Ingrediente perdido"    

##############################
@app.route('/rec_content_based', methods=['GET'])
def rec_content_based():    
    id_Usuario = request.args.get('id_Usuario')
    if len(id_Usuario) > 0:
        with engine.connect() as con:
            Rankings = pd.read_sql_query('select * from Rankings;', con=engine)
            Tags = pd.read_sql_query('call Platillo_etiquetas();', con=engine)
            id_Usuario = pd.read_sql_query("select id_Usuario from Usuario where nombre='"+id_Usuario+"';", con=engine)
            if not id_Usuario.empty:
                items = Basado_en_Contenido.Content_Based(Tags, Rankings, int(id_Usuario.values[0]))
                return items.to_json(orient = 'split')
            else:
                return "No se encontro el Usuario"
    else:
        return "Id_Usuario perdido"

##############################
@app.route('/set-orden', methods=['GET'])
def set_orden():    
    id_Usuario = request.args.get('id_Usuario')
    Platillos = request.args.get('Platillos')
    Fecha = request.args.get('Fecha')   
    Hora = request.args.get('Hora')
    qr = request.args.get('qr')
    try:
        if len(id_Usuario) > 0 and len(Platillos) > 0 and len(Fecha) > 0 and len(Hora) > 0 and len(qr) > 0:
            Platillos = Platillos.replace("_"," ").split(',')
            with engine.connect() as con:
                id_Usuario = pd.read_sql_query("select id_Usuario from Usuario where nombre='"+id_Usuario+"';", con=engine)
                if not id_Usuario.empty:
                    id_Usuario = id_Usuario.iloc[0]['id_Usuario']    
                    id_Orden = int(pd.read_sql_query('select max(id_Orden) from Orden;', con=engine).values[0]) + 1
                    insert_Orden = con.execute("insert into Orden(id_Orden, id_Usuario, fecha, Codigo_qr) values("+str(id_Orden)+", "+str(id_Usuario)+", '"+str(Fecha)+" "+str(Hora)+"', '"+str(qr)+"');")
                    for platillo in Platillos:
                        Orden_platillo = platillo.split('*')
                        if len(Orden_platillo) == 1:
                            insert_Orden_platillo = con.execute("insert into Orden_Platillo(id_Orden, id_Platillo, Cantidad) values("+str(id_Orden)+", (select id_Platillo from Platillo where Nombre_platillo = '"+Orden_platillo[0]+"'), 1);")                        
                        else:
                            insert_Orden_platillo = con.execute("insert into Orden_Platillo(id_Orden, id_Platillo, Cantidad) values("+str(id_Orden)+", (select id_Platillo from Platillo where Nombre_platillo = '"+Orden_platillo[0]+"'), "+Orden_platillo[1]+");")
                    return "Registro exitoso"
                else:
                    return "No se encontro el Usuario"
        else:
            return "Registro fallido"
    except:
        return "Registro fallido"

##############################
@app.route('/set-ranking', methods=['GET'])
def set_ranking():    
    id_Usuario = request.args.get('id_Usuario')
    id_Platillo = request.args.get('id_Platillo')
    if not id_Platillo:
        id_Platillo = 0
    ranking = request.args.get('ranking')
    if not ranking:
        ranking = -1
    if len(id_Usuario) > 0 and int(id_Platillo) > 0 and int(ranking) > -1:
        with engine.connect() as con:
            id_Usuario = pd.read_sql_query("select id_Usuario from Usuario where nombre='"+str(id_Usuario)+"';", con=engine)
            if not id_Usuario.empty:
                id_Usuario = id_Usuario.iloc[0]['id_Usuario']
                existe = pd.read_sql_query("select * from Rankings where id_Usuario = "+str(id_Usuario)+" and id_Platillo = "+str(id_Platillo)+";", con=engine)
                if not existe.empty:
                    result = con.execute("update Rankings set ranking="+str(ranking)+" where id_Usuario = "+str(id_Usuario)+" and id_Platillo = "+str(id_Platillo)+";")                        
                else:
                    result = con.execute("insert into Rankings (id_Usuario, id_Platillo, ranking) values("+str(id_Usuario)+", "+str(id_Platillo)+", "+str(ranking)+");")                        
                return "Registro exitoso"
            else:
                return "No se encontro el Usuario"
    else:
        return "Registro fallido"    

##############################
@app.route('/get-Ordenes', methods=['GET'])
def get_Ordenes():    
    id_Usuario = request.args.get('id_Usuario')
    if len(id_Usuario) > 0:
        with engine.connect() as con:
            id_Usuario = pd.read_sql_query("select id_Usuario from Usuario where nombre='"+id_Usuario+"';", con=engine)
            if not id_Usuario.empty:
                id_Usuario = id_Usuario.iloc[0]['id_Usuario']
                result = con.execute("select Orden_Platillo.id_Orden, Orden.id_Usuario, Orden_Platillo.id_Platillo, Platillo.Nombre_platillo, Orden_Platillo.Cantidad, Fecha, Codigo_qr from Orden_Platillo join Orden on Orden_Platillo.id_Orden = Orden.id_Orden join Platillo on Platillo.id_Platillo = Orden_Platillo.id_Platillo and Orden.id_Usuario = "+str(id_Usuario)+";")                        
                columns = [col for col in result.keys()]
                rows = [dict(zip(columns, row)) for row in result]
                return json.dumps(rows)  
            else:
                return "No se encontro el Usuario"
    else:
        return "Id_Usuario perdido"

##############################
@app.route('/rec_colab_item', methods=['GET'])
def rec_colab_item():    
    id_Usuario = request.args.get('id_Usuario')
    if len(id_Usuario) > 0:
        with engine.connect() as con:
            Rankings = pd.read_sql_query('select * from Rankings;', con=engine)            
            id_Usuario = pd.read_sql_query("select id_Usuario from Usuario where nombre='"+id_Usuario+"';", con=engine)            
            if not id_Usuario.empty:
                Rankings_usr = pd.read_sql_query('select * from Rankings where id_Usuario = '+str(id_Usuario.iloc[0]['id_Usuario'])+';', con=engine)            
                if not Rankings_usr.empty:
                    items = Colaborativo_entre_elementos.Colaborativo_Usuarios(Rankings, int(id_Usuario.values[0]))
                    return items.to_json(orient = 'split')
                else:
                    return "Usuario sin información suficiente"
            else:
                return "No se encontro el Usuario"
    else:
        return "Id_Usuario perdido"

##############################
@app.route('/ranking-usr', methods=['GET'])
def ranking_usr():    
    id_Usuario = request.args.get('id_Usuario')
    id_Platillo = request.args.get('id_Platillo')
    if not id_Usuario:
        id_Usuario = ""
    if not id_Platillo:
        id_Platillo = ""
    if len(id_Usuario) > 0 and int(id_Platillo) > 0:
        with engine.connect() as con:
            id_Usuario = pd.read_sql_query("select id_Usuario from Usuario where nombre='"+str(id_Usuario)+"';", con=engine)
            if not id_Usuario.empty:
                id_Usuario = id_Usuario.iloc[0]['id_Usuario']
                existe = pd.read_sql_query("select * from Rankings where id_Usuario = "+str(id_Usuario)+" and id_Platillo = "+str(id_Platillo)+";", con=engine)
                if not existe.empty:
                    ranking = existe.iloc[0]['ranking']
                    return str(ranking)
                else:
                    return "-1"
            else:
                return "No se encontro el Usuario"
    else:
        return "Registro fallido"  

##############################
@app.route('/get-platillos_saludables', methods=['GET'])
def get_platillos_saludables():    
    Etiqueta = request.args.get('Etiqueta')
    try:
        if len(Etiqueta) > 0:
            with engine.connect() as con:
                result = con.execute("select Platillo.id_Platillo, Platillo.Nombre_platillo, Platillo.Video_RA, Etiqueta.Nombre_etiqueta, Etiqueta_Platillo.Cantidad from Platillo join Etiqueta_Platillo on Etiqueta_Platillo.id_Platillo = Platillo.id_Platillo join Etiqueta on Etiqueta.id_Etiqueta = Etiqueta_Platillo.id_Etiqueta where Etiqueta.Nombre_etiqueta = '"+str(Etiqueta)+"' order by Cantidad;")                        
                columns = [col for col in result.keys()]
                rows = [dict(zip(columns, row)) for row in result]
                #print(rows)        
            return json.dumps(rows)  
        else:
            return "Etiqueta perdida"                
    except:
        return "Etiqueta perdida"

##############################
@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to my API'})

##############################
if __name__ == "__main__":
        app.run(debug=True)