import config as cf
import sys
import time
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
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
        print("\nCargando información de los archivos ....")

        ini = time.time()
        cont = controller.init()
        controller.loadData(cont, musicFile)
        fini = time.time()

        print('\nTiempo de carga:', round((fini-ini), 3), 'segundos.')
        print('Se cargaron', om.size(cont['songs']), 'elementos.')
        print('Se cargaron', mp.size(cont['artistID']), 'artistas únicos.')
        print('Se cargaron', mp.size(cont['trackID']), 'canciones únicas.\n')

    elif int(inputs[0]) == 2:
        try:
            tempo = controller.getcharXrang(cont)
            print('\nLa altura del árbol es de', om.height(tempo), 'niveles.')
            print('El árbol tiene', om.size(tempo), 'elementos.\n')
        except:
            print('\nSe ha producido un error.\n')

    else:
        sys.exit(0)