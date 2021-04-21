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

def getcharXrang(cont):
    return model.charXrang(cont)
