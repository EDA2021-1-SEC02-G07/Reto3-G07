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
    print("\nBienvenido.")
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
def printGeneros():
    print('\nLista de géneros:')
    print('1. Reggae: 60-90bpm.')
    print('2. Down-tempo: 70-100bpm')
    print('3. Chill-out: 90-120bpm.')
    print('4. Hip-hop: 85-115bpm.')
    print('5. Jazz and Funk: 120-125bpm.')
    print('6. Pop: 100-130bpm.')
    print('7. R&B: 60-80bpm.')
    print('8. Rock: 110-140bpm.')
    print('9. Metal: 100-160bpm.')
    print('10. Crear nuevo género.')

def printChar():
    print('\nLista de características:')
    print('1. Instrumentalness')
    print('2. Liveness')
    print('3. Speechiness')
    print('4. Danceability')
    print('5. Valence')
    print('6. Tempo')
    print('7. Acousticness')
    print('8. Energy')

def singularity():
    genSel = True
    g = int(input('\nEscriba la opción del género que desea consultar: '))
    op = input('Si desea consultar otro género presione enter, de lo contrario presione 0: ')
    if op == '0':
        genSel = False
    return g, genSel

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
        print('Se cargaron', lt.size(cont['lstSongs']), 'elementos.')
        print('Se cargaron', mp.size(cont['artistID']), 'artistas únicos.')
        print('Se cargaron', mp.size(cont['trackID']), 'canciones únicas.\n')

    elif int(inputs[0]) == 2:
        printChar()
        char = int(input('Opción de la característica que desea consultar: '))
        ranlo = float(input('Valor inferior del rango en el que desea buscar: '))
        ranhi = float(input('Valor superior del rango en el que desea buscar: '))
        try:
            ans = controller.getcharXrang(cont, char, ranlo, ranhi)
            print('\n' + ans[2].capitalize(), 'entre', ranlo, 'y', ranhi)
            print('Reproducciones totales:', ans[0])
            print('Artistas únicos:', ans[1])
        except:
            print('\nSe ha producido un error.\n')

    elif int(inputs[0]) == 3:
        enlo = input('Valor inferior de energía en el que desea buscar: ')
        enhi = input('Valor superior de energía en el que desea buscar: ')
        danlo = input('Valor inferior de la bailabilidad en el que desea buscar: ')
        danhi = input('Valor superior de la bailabilidad en el que desea buscar: ')
        try:
            ans = controller.getpartyBaby(cont, enlo, enhi, danlo, danhi)
            print('Hay un total de', ans[0], 'canciones únicas.')
            print('Información de 5 canciones al azar:')
            for x in range(5):
                print('Canción ' + str(x+1) +': ', 'Track ID:', ans[1][x][2], 'Energía:', ans[1][x][3], 'Danceability:', ans[1][x][4])
        except:
            print('\nSe ha producido un error.\n')

    elif int(inputs[0]) == 4:
        pass
    elif int(inputs[0]) == 5:
        try:
            printGeneros()
            generos = []
            genSel = True
            while genSel and len(generos) < 6:
                sing = singularity()
                generos.append(sing[0])
                genSel = sing[1]
            ans = controller.getgenxT(cont, generos)
            print('\nEl total de reproducciones es: ', ans[0])
            for x in ans[1]:
                print('\n' + x.upper() + ':', ans[1][x][2], '-', str(ans[1][x][3]) + 'bpm')
                print('Reproducciones:', len(ans[1][x][0]))
                print('Algunos artistas: ')
                for y in range(1, 11):
                    print('Artista', str(y) + ':', ans[1][x][1][y])
        except:
            print('\nSe ha producido un error.\n')
    elif int(inputs[0]) == 6:
        pass
    elif int(inputs[0]) == 7:
        controller.getdebug(cont)
    else:
        sys.exit(0)