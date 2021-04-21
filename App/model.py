import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

def newAnalyzer():
    analyzer = {'lstSongs': None,'songs': None, 'artistID': None, 'trackID': None}

    analyzer['lstSongs'] = lt.newList('SINGLE_LINKED', cmpTidList)
    analyzer['songs'] = mp.newMap(107347, maptype='PROBING', loadfactor=0.693, comparefunction=cmpINTmap)
    analyzer['artistID'] = mp.newMap(17657, maptype='PROBING', loadfactor=0.693, comparefunction=cmpSTRmap)
    analyzer['trackID'] = mp.newMap(52859, maptype='PROBING', loadfactor=0.693, comparefunction=cmpSTRmap)

    return analyzer

def addSong(analyzer, song):
    mp.put(analyzer['songs'], int(song['id']), song)
    
    if mp.contains(analyzer['artistID'], song['artist_id']):
        lt.addLast(me.getValue(mp.get(analyzer['artistID'], song['artist_id'])), song)
    elif not mp.contains(analyzer['artistID'], song['artist_id']):
        mp.put(analyzer['artistID'], song['artist_id'], lt.newList(cmpfunction=cmpAidList))
        lt.addLast(me.getValue(mp.get(analyzer['artistID'], song['artist_id'])), song)

    if mp.contains(analyzer['trackID'], song['track_id']):
        lt.addLast(me.getValue(mp.get(analyzer['trackID'], song['track_id'])), song)
    elif not mp.contains(analyzer['trackID'], song['track_id']):
        mp.put(analyzer['trackID'], song['track_id'], lt.newList(cmpfunction=cmpTidList))
        lt.addLast(me.getValue(mp.get(analyzer['trackID'], song['track_id'])), song)

    return analyzer

def updateTrackID(map, song):
    trackID = song['id']
    entry = om.get(map, trackID)
    if entry is None:
        dataentry = newDataEntry(song)
        om.put(map, trackID, dataentry)
    else:
        dataentry = me.getValue(entry)
    addTrackID(dataentry, song)
    
    return map

def addTrackID(dataentry, song):
    pass

def newDataEntry(song):
    entry = {}

def cmpINTtree(int1, int2):
    if int(int1) == int(int2):
        return 0
    elif int(int1) > int(int2):
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