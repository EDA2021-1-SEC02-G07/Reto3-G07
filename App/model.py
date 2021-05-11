import random
import config as cf
#from fuzzywuzzy import process
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
import datetime
from DISClib.DataStructures import listiterator as it
assert cf
import random
import operator

#CATÁLOGO#
def newAnalyzer():

    analyzer = {'lstSongs': None, 'artistID': None, 'trackID': None, 'instrumentalness': None,
    'liveness': None, "speechiness": None,"danceability": None, "valence": None, "tempo": None,
    "acousticness": None, "energy": None, 'horas': None}

    analyzer['lstSongs'] = lt.newList('SINGLE_LINKED', cmpTidList)
    analyzer['artistID'] = mp.newMap(69677, maptype='PROBING', loadfactor=0.693, comparefunction=cmpSTRmap)
    analyzer['trackID'] = mp.newMap(531547, maptype='PROBING', loadfactor=0.693, comparefunction=cmpSTRmap)
    analyzer['instrumentalness'] = om.newMap(omaptype='RBT', comparefunction=cmpINTtree)
    analyzer['liveness'] = om.newMap(omaptype='BST', comparefunction=cmpINTtree)
    analyzer['speechiness'] = om.newMap(omaptype='BST', comparefunction=cmpINTtree)
    analyzer['danceability'] = om.newMap(omaptype='RBT', comparefunction=cmpINTtree)
    analyzer['valence'] = om.newMap(omaptype='BST', comparefunction=cmpINTtree)
    analyzer['tempo'] = om.newMap(omaptype='RBT', comparefunction=cmpINTtree)
    analyzer['acousticness'] = om.newMap(omaptype='BST', comparefunction=cmpINTtree)
    analyzer['energy'] = om.newMap(omaptype='RBT', comparefunction=cmpINTtree)
    analyzer['horas'] = om.newMap(omaptype='RBT', comparefunction=cmpHRtree)
    analyzer['etiquetas'] = om.newMap(omaptype='RBT', comparefunction=cmpHRtree)
    analyzer['tagsSong'] = om.newMap(omaptype='RBT', comparefunction=cmpHRtree)

    

    return analyzer

def addSong(analyzer, song):
    lt.addLast(analyzer['lstSongs'], song)

    if mp.contains(analyzer['artistID'], song['artist_id']):
        lt.addLast(me.getValue(mp.get(analyzer['artistID'], song['artist_id'])), (int(song['id']), song['artist_id'], song['track_id']))
    elif not mp.contains(analyzer['artistID'], song['artist_id']):
        mp.put(analyzer['artistID'], song['artist_id'], lt.newList(cmpfunction=cmpAidList))
        lt.addLast(me.getValue(mp.get(analyzer['artistID'], song['artist_id'])), (int(song['id']), song['artist_id'], song['track_id']))

    if mp.contains(analyzer['trackID'], song['track_id']):
        lt.addLast(me.getValue(mp.get(analyzer['trackID'], song['track_id'])), (int(song['id']), song['artist_id'], song['track_id'], song['energy'], song['danceability']))
    elif not mp.contains(analyzer['trackID'], song['track_id']):
        mp.put(analyzer['trackID'], song['track_id'], lt.newList(cmpfunction=cmpTidList))
        lt.addLast(me.getValue(mp.get(analyzer['trackID'], song['track_id'])), (int(song['id']), song['artist_id'], song['track_id'], song['energy'], song['danceability']))
    #CHARACTERISTICS#(int(song['id']), song['artist_id'], song['track_id'])
    if om.contains(analyzer['instrumentalness'], float(song['instrumentalness'])):
        lt.addLast(me.getValue(om.get(analyzer['instrumentalness'], float(song['instrumentalness']))), (int(song['id']), song['artist_id'], song['track_id']))
    elif not om.contains(analyzer['instrumentalness'], float(song['instrumentalness'])):
        om.put(analyzer['instrumentalness'], float(song['instrumentalness']), lt.newList(cmpfunction=cmpUidList))
        lt.addLast(me.getValue(om.get(analyzer['instrumentalness'], float(song['instrumentalness']))), (int(song['id']), song['artist_id'], song['track_id']))

    if om.contains(analyzer['liveness'], float(song['liveness'])):
        lt.addLast(me.getValue(om.get(analyzer['liveness'], float(song['liveness']))), (int(song['id']), song['artist_id'], song['track_id']))
    elif not om.contains(analyzer['liveness'], float(song['liveness'])):
        om.put(analyzer['liveness'], float(song['liveness']), lt.newList(cmpfunction=cmpUidList))
        lt.addLast(me.getValue(om.get(analyzer['liveness'], float(song['liveness']))), (int(song['id']), song['artist_id'], song['track_id']))

    if om.contains(analyzer['speechiness'], float(song['speechiness'])):
        lt.addLast(me.getValue(om.get(analyzer['speechiness'], float(song['speechiness']))), (int(song['id']), song['artist_id'], song['track_id']))
    elif not om.contains(analyzer['speechiness'], float(song['speechiness'])):
        om.put(analyzer['speechiness'], float(song['speechiness']), lt.newList(cmpfunction=cmpUidList))
        lt.addLast(me.getValue(om.get(analyzer['speechiness'], float(song['speechiness']))), (int(song['id']), song['artist_id'], song['track_id']))

    if om.contains(analyzer['danceability'], float(song['danceability'])):
        lt.addLast(me.getValue(om.get(analyzer['danceability'], float(song['danceability']))), (int(song['id']), song['artist_id'], song['track_id']))
    elif not om.contains(analyzer['danceability'], float(song['tempo'])):
        om.put(analyzer['danceability'], float(song['danceability']), lt.newList(cmpfunction=cmpUidList))
        lt.addLast(me.getValue(om.get(analyzer['danceability'], float(song['danceability']))), (int(song['id']), song['artist_id'], song['track_id']))

    if om.contains(analyzer['valence'], float(song['valence'])):
        lt.addLast(me.getValue(om.get(analyzer['valence'], float(song['valence']))), (int(song['id']), song['artist_id'], song['track_id']))
    elif not om.contains(analyzer['valence'], float(song['valence'])):
        om.put(analyzer['valence'], float(song['valence']), lt.newList(cmpfunction=cmpUidList))
        lt.addLast(me.getValue(om.get(analyzer['valence'], float(song['valence']))), (int(song['id']), song['artist_id'], song['track_id']))

    if om.contains(analyzer['tempo'], float(song['tempo'])):
        lt.addLast(me.getValue(om.get(analyzer['tempo'], float(song['tempo']))), (int(song['id']), song['artist_id'], song['track_id']))
    elif not om.contains(analyzer['tempo'], float(song['tempo'])):
        om.put(analyzer['tempo'], float(song['tempo']), lt.newList(cmpfunction=cmpUidList))
        lt.addLast(me.getValue(om.get(analyzer['tempo'], float(song['tempo']))), (int(song['id']), song['artist_id'], song['track_id']))

    if om.contains(analyzer['acousticness'], float(song['acousticness'])):
        lt.addLast(me.getValue(om.get(analyzer['acousticness'], float(song['acousticness']))), (int(song['id']), song['artist_id'], song['track_id']))
    elif not om.contains(analyzer['acousticness'], float(song['acousticness'])):
        om.put(analyzer['acousticness'], float(song['acousticness']), lt.newList(cmpfunction=cmpUidList))
        lt.addLast(me.getValue(om.get(analyzer['acousticness'], float(song['acousticness']))), (int(song['id']), song['artist_id'], song['track_id']))

    if om.contains(analyzer['energy'], float(song['energy'])):
        lt.addLast(me.getValue(om.get(analyzer['energy'], float(song['energy']))), (int(song['id']), song['artist_id'], song['track_id']))
    elif not om.contains(analyzer['energy'], float(song['energy'])):
        om.put(analyzer['energy'], float(song['energy']), lt.newList(cmpfunction=cmpUidList))
        lt.addLast(me.getValue(om.get(analyzer['energy'], float(song['energy']))), (int(song['id']), song['artist_id'], song['track_id']))
    
    return analyzer

def addUser(analyzer, song):
    horas = song['created_at']
    horas = horas[11:16]
    #hora hasta min 16 otro [:]
    
    etiqueta = song['hashtag']

    if om.contains(analyzer['horas'], horas):
        lt.addLast(me.getValue(om.get(analyzer['horas'],horas )), (song['track_id'],song['hashtag']))
    elif not om.contains(analyzer['horas'], horas):
        om.put(analyzer['horas'], horas, lt.newList(cmpfunction=cmpUidList))
        lt.addLast(me.getValue(om.get(analyzer['horas'], horas)), (song['track_id'], song['hashtag']))

    cancion = song['track_id']
    if om.contains(analyzer['tagsSong'],cancion ):
        lt.addLast(me.getValue(om.get(analyzer['tagsSong'], cancion)), etiqueta)    
    elif not om.contains(analyzer['tagsSong'], cancion):
        om.put(analyzer['tagsSong'], cancion, lt.newList(cmpfunction=cmpUidList))    
        lt.addLast(me.getValue(om.get(analyzer['tagsSong'], cancion)), etiqueta)


def addTag(analyzer, etiqueta):
    
    avg = 'vader_avg'
    tag = etiqueta['hashtag']
    if  (etiqueta[avg]=='')==False:
        
        if om.contains(analyzer['etiquetas'], tag): 
            lt.addLast(me.getValue(om.get(analyzer['etiquetas'], tag)), (float(etiqueta['vader_avg'])))    
        elif not om.contains(analyzer['etiquetas'], tag):
            om.put(analyzer['etiquetas'], tag, lt.newList(cmpfunction=cmpUidList))    
            lt.addLast(me.getValue(om.get(analyzer['etiquetas'], tag)), (float(etiqueta['vader_avg'])))   
    
    
    
    

def updateHoras(map, song):
    horaRep = song['created_at']
    horaRep = datetime.datetime.strptime(horaRep, '%Y-%m-%d %H:%M:%S')
    horaRep = horaRep.replace(second=0)
    entry = om.get(map, horaRep.time())

    if entry is None:
        dataentry = newDataEntry(song)
        om.put(map, horaRep.time(), dataentry)
    else:
        dataentry = me.getValue(entry)
    addHoras(dataentry, song)
    
    return map

def addHoras(dataentry, song):
    pass

def newDataEntry(song):
    entry = {}


#FUNCIONES DE CONSULTA#
def charXrang(cont, char, ranlo, ranhi):
    artists = set()
    reps = om.values(cont[char], ranlo, ranhi)
    repsT = 0
    for x in lt.iterator(reps):
        repsT += lt.size(x)
        for y in lt.iterator(x):
            artists.add(y[1])
    return repsT, len(artists), char

def partyBaby(cont, enlo, enhi, danlo, danhi):
    tracksEn = set()
    tracksDa = set()
    energy = om.values(cont['energy'], enlo, enhi)
    dance = om.values(cont['danceability'], danlo, danhi)
    for x in lt.iterator(energy):
        for y in lt.iterator(x):
            tracksEn.add(y[2])
    for x in lt.iterator(dance):
        for y in lt.iterator(x):
            tracksDa.add(y[2])
    tracks = list(tracksEn.intersection(tracksDa))
    tot = len(tracks)
    rtracks = []
    r = random.sample(range(0, tot), 5)
    for x in r:
        track = me.getValue(mp.get(cont['trackID'], tracks[x]))
        rtracks.append(lt.firstElement(track))
    return tot, rtracks

def genxT(cont, generos):
    tempo = cont['tempo']
    genD = {1: ('Reggae', 60, 90), 2: ('Down-tempo', 70, 100), 3: ('Chill-out', 90, 120), 4: ('Hip-hop', 85, 115), 5: ('Jazz and Funk', 120, 125),
    6: ('Pop', 100, 130), 7: ('R&B', 60, 80 ), 8: ('Rock', 110, 140 ), 9: ('Metal', 100, 160)}
    genR = {}
    total = []
    nuevo =  True
    nuevos = []
    while nuevo:
        if 10 in generos:
            nuevos.append(Ngenero(generos))
        else:
            nuevo = False
    if len(nuevos) != 0:
        for x in nuevos:
            songs = om.values(tempo, x[1], x[2])
            reps = []
            artists = set()
            for y in lt.iterator(songs):
                for z in lt.iterator(y):
                    total.append(z[0])
                    reps.append(z[0])
                    artists.add(z[1])
                genR[x[0]] = (reps, list(artists), x[1], x[2])
    if len(generos) != 0:
        for x in generos:
            gen = genD[x]
            songs = om.values(tempo, gen[1], gen[2])
            reps = []
            artists = set()
            for y in lt.iterator(songs):
                for z in lt.iterator(y):
                    total.append(z[0])
                    reps.append(z[0])
                    artists.add(z[1])
                genR[gen[0]] = (reps, list(artists), gen[1], gen[2])
    return len(total), genR

def Ngenero(generos):
    nombre = input('\nEscriba el nombre del nuevo género: ')
    inf = int(input('Escriba el valor inferior del tempo: '))
    sup = int(input('Escriba el valor superior para el tempo: '))
    nuevoG = (nombre, inf, sup)
    generos.remove(10)
    return nuevoG

def Mestudiar(cont, instmin, instmax, tempmin, tempmax):
    tempo = om.keys(cont['tempo'], tempmin, tempmax)
    lista = lt.newList()
    final = {}
    contador = 0
    #recorre el tempo que tiene solo el rango, busca que tengan el inst requerido
    for x in lt.iterator(tempo): 
        r = om.get(cont['tempo'], x)
        valor = r['value']
        real = valor['first']['info']
       
        for i in real:
           
            if type(i)==str:
                pos = lt.isPresent(cont['lstSongs'],i )
                cancion = lt.getElement(cont['lstSongs'], pos)
                inst = cancion['instrumentalness']
               
                if float(inst)>= instmin and float(inst)<= instmax:
                    final[i] = (inst, x )
                    contador+= 1
                    lt.addLast(lista, i)
    #recorre genera 5 numeros aletorios y retorna la info de esas canciones
    print('Total de canciones únicas: ', contador)
    contador = 0
    lista_numeros = []
    while contador<5:
        numero = random.randint(0,lt.size(lista))
        if numero not in lista_numeros:
            contador+=1
            lista_numeros.append(numero)
            cancion = lt.getElement(lista, numero)
            info = final[cancion]
            print('\n Track', contador, ': ', cancion, 'con una instumentalidad de ',info[0], 'y un tempo de ', info[1] )

        
def GenxTiempo(cont, hmin, hmax):

    #da el promedio de sentimiento en las canciones 

    #entrada de canciones por hora de escucha
    canciones_h = om.values(cont['horas'], hmin, hmax)
    dicc = {'R & B':0,'Reggae':0,'Down-tempo':0,'Hip-Hop':0, 'Chill-Out': 0,'Pop':0, 'Rock':0, 'Jazz and Funk':0 , 'Metal':0}
    dicc2 = {'R & B':[],'Reggae':[],'Down-tempo':[],'Hip-Hop':[], 'Chill-Out': [],'Pop':[], 'Rock':[], 'Jazz and Funk':[] , 'Metal':[]}
    for i in lt.iterator(canciones_h):
        for r in lt.iterator(i):    
            generos = generosS(cont, r[0])
            for i in generos:
                dicc[i]+= 1
                dicc2[i]= dicc2[i]+ [r[0]]
    print('\n Géneros ordenados por número de reproducciones\n')
       
    contador = 1
    dicc_sort = sorted(dicc.items(), key=operator.itemgetter(1), reverse=True)
    for x in enumerate(dicc_sort):
        print('Top ', contador, ': ', x[1][0], ' con ', dicc[x[1][0]], 'reps.')
        contador+=1
     
    print('\nEl género más escuchado es ', dicc_sort[0][0], ' con ', dicc_sort[0][1], 'reproducciones\n')
    print('------------------------',dicc_sort[0][0], 'analisis de sentimiento--------------------------' )

    dit_av = {}
    dit_list={}
    unique = 0
    for cancion in dicc2[dicc_sort[0][0]]:
        et = om.get(cont['tagsSong'], cancion)
        eti = et['value']['first']['info']
        eti = eti.lower()
        if cancion not in dit_av and om.get(cont['etiquetas'],eti):
            #contador, suma, lista
            avr = om.get(cont['etiquetas'], eti)
            avr = avr['value']['first']['info']
            dit_av[cancion]= float(avr)
            dit_list[cancion]= [eti]
            contador+=1
        if cancion in dit_av and om.get(cont['etiquetas'],eti):
            avr = om.get(cont['etiquetas'], eti)
            avr = avr['value']['first']['info']
            dit_av[cancion] += float(avr)
            dit_list[cancion]+= [eti]
    
    for i in dit_av:
        num = len(dit_list[i])
        dit_av[i]= dit_av[i]/num
    
    contador = 1
    dicc_sort = sorted(dit_av.items(), key=operator.itemgetter(1), reverse=True)

    for x in dicc_sort:
     
        print('Top ', contador, ' track: ', x[0], ' con ',len(dit_list[x[0]]), ' etiquetas y un VADER =  ',x[1])
        contador+=1
        if contador>10:
            break

 
def generosS(cont, cancion):
    tempo = cont['lstSongs']
    pos = lt.isPresent(tempo, cancion)
    tempo = lt.getElement(tempo, pos)
    tempo = tempo['tempo']
    dicc ={(60,80):'R & B', (60,90):'Reggae', (879,100):'Down-tempo', (85,115):'Hip-Hop', (90,120):'Chill-Out', (100,130):'Pop', (110,140):'Rock', (120,125):'Jazz and Funk', (100,160):'Metal'}
    lista = []
    for i in dicc:
        mini = i[0]
        maxi = i[1]
        if float(tempo)>=mini and float(tempo)<=maxi:
            lista = lista +[dicc[i]]
    return lista

    
    
    
#FUNCIONES DE COMPARACIÓN

def cmpINTtree(int1, int2):
    if float(int1) == float(int2):
        return 0
    elif float(int1) > float(int2):
        return 1
    else:
        return -1

def cmpSTRtree(str1, str2):
    if str1 == str2:
        return 0
    elif str1 > str2:
        return 1
    else:
        return -1

def cmpHRtree(hr1, hr2):
    if (hr1 == hr2):
        return 0
    elif (hr1 > hr2):
        return 1
    else:
        return -1

def cmpINTmap(name, int1):
    entry = me.getKey(int1)
    if int(name) == int(entry):
        return 0
    elif int(name) > int(entry):
        return 1
    else:
        return -1

def cmpSTRmap(name, str1):
    entry = me.getKey(str1)
    if name == entry:
        return 0
    elif name > entry:
        return 1
    else:
        return -1

def cmpAidList(name, artist):
    if name in artist['artist_id']:
        return 0
    return -1

def cmpTidList(name, track):
    if name in track['track_id']:
        return 0
    return -1

def cmpUidList(name, track):
    if name in track['id']:
        return 0
    return -1

#DEBUG#
def debug(analyzer):
    print(om.size(analyzer['tempo']))