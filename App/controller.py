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
    return model.charXrang(cont, charF, ranlo, ranhi)

def getpartyBaby(cont, enlo, enhi, danlo, danhi):
    enlo = float(enlo)
    enhi = float(enhi)
    danlo = float(danlo)
    danhi = float(danhi)
    return model.partyBaby(cont, enlo, enhi, danlo, danhi)

def getgenxT(cont, generos):
    return model.genxT(cont, generos)




def getdebug(cont):
    return model.debug(cont)
