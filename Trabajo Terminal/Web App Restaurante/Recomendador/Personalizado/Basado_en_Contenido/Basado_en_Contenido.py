from warnings import catch_warnings
import pandas as pd
import numpy as np
import math

def Content_Based(Tags, Rankings, id_Usuario):
    #a = Rankings[Rankings['id_Usuario'] == 3]
    #a[a['id_Platillo'] == 33]

    #b = Tags[Tags['id_Usuario'] == 320]
    #b[b['id_Platillo'] == 2762]
    
    TF = Tags.groupby(['id_Platillo','etiqueta'], as_index = False, sort = False).count().rename(columns = {'id_Usuario': 'tag_count_TF'})[['id_Platillo','etiqueta','tag_count_TF']]
    #print(TF) 
    
    Tag_distinct = Tags[['etiqueta','id_Platillo']].drop_duplicates()
    DF = Tag_distinct.groupby(['etiqueta'], as_index = False, sort = False).count().rename(columns = {'id_Platillo': 'tag_count_DF'})[['etiqueta','tag_count_DF']]
    #print(DF) 

    a = math.log10(len(np.unique(Tags['id_Platillo']))) 
    DF['IDF'] = a - np.log10(DF['tag_count_DF']) # Peso a cada etiqueta
    TF = pd.merge(TF,DF,on = 'etiqueta', how = 'left', sort = False)
    TF['TF-IDF']=TF['tag_count_TF']*TF['IDF'] 
    #print(TF.head())

    Vect_len=TF[['id_Platillo','TF-IDF']]
    Vect_len['TF-IDF-Sq']=Vect_len['TF-IDF']**2
    Vect_len =Vect_len.groupby(['id_Platillo'], as_index = False, sort = False).sum().rename(columns = {'TF-IDF-Sq': 'TF-IDF-Sq-sum'})[['id_Platillo','TF-IDF-Sq-sum']]
    Vect_len['vect_len'] = np.sqrt(Vect_len[['TF-IDF-Sq-sum']].sum(axis=1))
    TF = pd.merge(TF,Vect_len,on = 'id_Platillo', how = 'left', sort = False)
    TF['TAG_WT']=TF['TF-IDF']/TF['vect_len']
    #print(TF.head())

    Ratings_filter=Rankings[Rankings['ranking']>=3.5] 
    distinct_users=np.unique(Rankings['id_Usuario']) 
    user_tag_pref=pd.DataFrame()
    i=1

    #enter user ID for analysis
    #userID = 320

    tag_merge_all=pd.DataFrame()
    try:    
        user_index = distinct_users.tolist().index(id_Usuario)         

        for user in distinct_users[user_index:user_index+1]:
            
            if i%30==0:
                print ("Usuario: ", i , "fuera de: ", len(distinct_users))
                    
            user_data=  Ratings_filter[Ratings_filter['id_Usuario']==user]
            user_data = pd.merge(TF,user_data,on = 'id_Platillo', how = 'inner', sort = False)
            user_data1 = user_data.groupby(['etiqueta'], as_index = False, sort = False).sum().rename(columns = {'TAG_WT': 'tag_pref'})[['etiqueta','tag_pref']]
            user_data1['Usuario']=user
            user_tag_pref = user_tag_pref.append(user_data1, ignore_index=True)
            i=i+1

        #print(user_tag_pref)

        distinct_users=np.unique(Ratings_filter['id_Usuario'])        

        i=1

        #enter user ID for analysis
        #userID = 320

        user_index = distinct_users.tolist().index(id_Usuario)

        for user in distinct_users[user_index:user_index+1]:

            
            user_tag_pref_all =  user_tag_pref[user_tag_pref['Usuario']==user]
            distinct_movies = np.unique(TF['id_Platillo'])
            j=1
            for movie in distinct_movies:
                
                if j%300==0:
                    
                    print ("Platillo: ", j , "fuera de: ", len(distinct_movies) , "con usuario: ", i , "fuera de: ", len(distinct_users))
                
                TF_Movie =  TF[TF['id_Platillo']==movie]
                tag_merge = pd.merge(TF_Movie,user_tag_pref_all,on = 'etiqueta', how = 'left', sort = False)
                tag_merge['tag_pref']=tag_merge['tag_pref'].fillna(0)
                tag_merge['tag_value']=tag_merge['TAG_WT']*tag_merge['tag_pref']
                
                TAG_WT_val=np.sqrt(np.sum(np.square(tag_merge['TAG_WT']), axis=0))
                tag_pref_val=np.sqrt(np.sum(np.square(user_tag_pref_all['tag_pref']), axis=0))
                
                tag_merge_final = tag_merge.groupby(['Usuario','id_Platillo'])[['tag_value']].sum().rename(columns = {'tag_value': 'Rating'}).reset_index()
                
                tag_merge_final['Rating']=tag_merge_final['Rating']/(TAG_WT_val*tag_pref_val)
                
                tag_merge_all = tag_merge_all.append(tag_merge_final, ignore_index=True)
                j=j+1
            i=i+1
        tag_merge_all = tag_merge_all.sort_values(['Usuario','Rating'], ascending=False)

        # Removing movies already rated by user

        movies_rated = Rankings[Rankings['id_Usuario']==id_Usuario]['id_Platillo']
        #tag_merge_all = tag_merge_all[~tag_merge_all['id_Platillo'].isin(movies_rated)]

        #print("###")
        #print(tag_merge_all)

        return tag_merge_all['id_Platillo']

    except:
        #tag_merge_all.append("Usuario sin rankings")
        return tag_merge_all