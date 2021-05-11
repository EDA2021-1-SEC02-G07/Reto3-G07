import config as cf
import model
import csv
import tracemalloc
import time

def init():
    analyzer = model.newAnalyzer()
    return analyzer

def loadData(analyzer, musicFile, userFile, sentFile):
    musicFile = cf.data_dir + musicFile
    inputFile = csv.DictReader(open(musicFile, encoding='utf-8'), delimiter=',')

    for x in inputFile:
        model.addSong(analyzer, x)

    userFile = cf.data_dir + userFile
    inputFile = csv.DictReader(open(userFile, encoding='utf-8'), delimiter=',')
    
    for x in inputFile:
        model.addUser(analyzer, x)

    sentFile = cf.data_dir + sentFile
    inputFile = csv.DictReader(open(sentFile, encoding='utf-8'), delimiter=',')
    
    for etiqueta in inputFile:
        model.addTag(analyzer, etiqueta)

    return analyzer

def getcharXrang(cont, char, ranlo, ranhi):
    if char == 1:
        charF = 'instrumentalness'
    elif char == 2:
        charF = 'liveness'
    elif char == 3:
        charF = 'speechiness'
    elif char == 4:
        charF = 'danceability'
    elif char == 5:
        charF = 'valence'
    elif char == 6:
        charF = 'tempo'
    elif char == 7:
        charF = 'acousticness'
    elif char == 8:
        charF = 'energy'
    ranlo = float(ranlo)
    ranhi = float(ranhi)
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    ans= model.charXrang(cont, charF, ranlo, ranhi)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    print('tiempo ',delta_time,' memoria: ', delta_memory )
    return ans
   

def getpartyBaby(cont, enlo, enhi, danlo, danhi):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    enlo = float(enlo)
    enhi = float(enhi)
    danlo = float(danlo)
    danhi = float(danhi)
    ans= model.partyBaby(cont, enlo, enhi, danlo, danhi)


    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    print('tiempo ',delta_time,' memoria: ', delta_memory )
   
    return ans 


def getgenxT(cont, generos):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    ans= model.genxT(cont, generos)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    print('tiempo ',delta_time,' memoria: ', delta_memory )
    return ans

def getMestudiar(cont, instmin, instmax, tempmin, tempmax):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    ans= model.Mestudiar(cont, instmin, instmax, tempmin, tempmax)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    print('tiempo ',delta_time,' memoria: ', delta_memory )
    return ans

def getGenXtiempo(cont, hmin, hmax):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    ans = model.GenxTiempo(cont,  hmin, hmax)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    print('tiempo ',delta_time,' memoria: ', delta_memory )
    return ans

def getdebug(cont):
    return model.debug(cont)

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
