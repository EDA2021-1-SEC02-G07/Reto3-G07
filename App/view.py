import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
assert cf

musicFile = 'context_content_features-small.csv'
cont = None

def printMenu():
    print("Bienvenido.")
    print("1- Cargar información en el catálogo.")
    print("2- Consultar reproducciones por características en un rango. ")
    print("3- Canciones para fiesta según energía y bailabilidad.")
    print("4. Música para estudiar según según la instrumentalidad y el tempo.")
    print("5- Canciones por género musical.")
    print("6- Género musical más escuchado en un tiempo.")
    print("0- Salir.")

catalog = None
 
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        cont = controller.init()
        controller.loadData(cont, musicFile)

        print(mp.size(cont['songs']), mp.size(cont['artistID']), mp.size(cont['trackID']))

    elif int(inputs[0]) == 2:
        pass

    else:
        sys.exit(0)
sys.exit(0)

import config as cf
import model
import csv

def init():
    analyzer = model.newAnalyzer()
    return analyzer

def loadData(analyzer, musicFile):
    musicFile = cf.data_dir + musicFile
    inputFile = csv.DictReader(open(musicFile, encoding='utf-8'), delimiter=',')

    for x in inputFile:
        model.addSong(analyzer, x)
    return analyzer
