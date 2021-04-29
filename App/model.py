import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

def newAnalyzer():

    analyzer = {'lstSongs': None, 'artistID': None, 'trackID': None, 'instrumentalness': None,
    'liveness': None, "speechiness": None,"danceability": None,"valence": None, "loudness": None,
    "tempo": None, "acousticness": None, "energy": None, "mode": None, 'key': None}

    analyzer['lstSongs'] = lt.newList('SINGLE_LINKED', cmpTidList)
    analyzer['artistID'] = mp.newMap(69677, maptype='PROBING', loadfactor=0.693, comparefunction=cmpSTRmap)
    analyzer['trackID'] = mp.newMap(531547, maptype='PROBING', loadfactor=0.693, comparefunction=cmpSTRmap)
    analyzer['instrumentalness'] = om.newMap(omaptype='RBT', comparefunction=cmpINTtree)
    analyzer['liveness'] = om.newMap(omaptype='BST', comparefunction=cmpINTtree)
    analyzer['speechiness'] = om.newMap(omaptype='BST', comparefunction=cmpINTtree)
    analyzer['danceability'] = om.newMap(omaptype='RBT', comparefunction=cmpINTtree)
    analyzer['valence'] = om.newMap(omaptype='BST', comparefunction=cmpINTtree)
    analyzer['loudness'] = om.newMap(omaptype='BST', comparefunction=cmpINTtree)
    analyzer['tempo'] = om.newMap(omaptype='RBT', comparefunction=cmpINTtree)
    analyzer['acousticness'] = om.newMap(omaptype='BST', comparefunction=cmpINTtree)
    analyzer['energy'] = om.newMap(omaptype='RBT', comparefunction=cmpINTtree)
    analyzer['mode'] = om.newMap(omaptype='BST', comparefunction=cmpINTtree)
    analyzer['key'] = om.newMap(omaptype='BST', comparefunction=cmpINTtree)
    

    return analyzer

def addSong(analyzer, song):
    lt.addLast(analyzer['lstSongs'], song)

    if mp.contains(analyzer['artistID'], song['artist_id']):
        lt.addLast(me.getValue(mp.get(analyzer['artistID'], song['artist_id'])), int(song['id']))
    elif not mp.contains(analyzer['artistID'], song['artist_id']):
        mp.put(analyzer['artistID'], song['artist_id'], lt.newList(cmpfunction=cmpAidList))
        lt.addLast(me.getValue(mp.get(analyzer['artistID'], song['artist_id'])), int(song['id']))

    if mp.contains(analyzer['trackID'], song['track_id']):
        lt.addLast(me.getValue(mp.get(analyzer['trackID'], song['track_id'])), int(song['id']))
    elif not mp.contains(analyzer['trackID'], song['track_id']):
        mp.put(analyzer['trackID'], song['track_id'], lt.newList(cmpfunction=cmpTidList))
        lt.addLast(me.getValue(mp.get(analyzer['trackID'], song['track_id'])), int(song['id']))
#CHARACTERISTICS#
    if om.contains(analyzer['instrumentalness'], float(song['instrumentalness'])):
        lt.addLast(me.getValue(om.get(analyzer['instrumentalness'], float(song['instrumentalness']))), int(song['id']))
    elif not om.contains(analyzer['instrumentalness'], float(song['instrumentalness'])):
        om.put(analyzer['instrumentalness'], float(song['instrumentalness']), lt.newList(cmpfunction=cmpUidList))
        lt.addLast(me.getValue(om.get(analyzer['instrumentalness'], float(song['instrumentalness']))), int(song['id']))

    if om.contains(analyzer['liveness'], float(song['liveness'])):
        lt.addLast(me.getValue(om.get(analyzer['liveness'], float(song['liveness']))), int(song['id']))
    elif not om.contains(analyzer['liveness'], float(song['liveness'])):
        om.put(analyzer['liveness'], float(song['liveness']), lt.newList(cmpfunction=cmpUidList))
        lt.addLast(me.getValue(om.get(analyzer['liveness'], float(song['liveness']))), int(song['id']))

    if om.contains(analyzer['speechiness'], float(song['speechiness'])):
        lt.addLast(me.getValue(om.get(analyzer['speechiness'], float(song['speechiness']))), int(song['id']))
    elif not om.contains(analyzer['speechiness'], float(song['speechiness'])):
        om.put(analyzer['speechiness'], float(song['speechiness']), lt.newList(cmpfunction=cmpUidList))
        lt.addLast(me.getValue(om.get(analyzer['speechiness'], float(song['speechiness']))), int(song['id']))

    if om.contains(analyzer['danceability'], float(song['danceability'])):
        lt.addLast(me.getValue(om.get(analyzer['danceability'], float(song['danceability']))), int(song['id']))
    elif not om.contains(analyzer['danceability'], float(song['tempo'])):
        om.put(analyzer['danceability'], float(song['danceability']), lt.newList(cmpfunction=cmpUidList))
        lt.addLast(me.getValue(om.get(analyzer['danceability'], float(song['danceability']))), int(song['id']))

    if om.contains(analyzer['valence'], float(song['valence'])):
        lt.addLast(me.getValue(om.get(analyzer['valence'], float(song['valence']))), int(song['id']))
    elif not om.contains(analyzer['valence'], float(song['valence'])):
        om.put(analyzer['valence'], float(song['valence']), lt.newList(cmpfunction=cmpUidList))
        lt.addLast(me.getValue(om.get(analyzer['valence'], float(song['valence']))), int(song['id']))

    if om.contains(analyzer['loudness'], float(song['loudness'])):
        lt.addLast(me.getValue(om.get(analyzer['loudness'], float(song['loudness']))), int(song['id']))
    elif not om.contains(analyzer['loudness'], float(song['loudness'])):
        om.put(analyzer['loudness'], float(song['loudness']), lt.newList(cmpfunction=cmpUidList))
        lt.addLast(me.getValue(om.get(analyzer['loudness'], float(song['loudness']))), int(song['id']))

    if om.contains(analyzer['tempo'], float(song['tempo'])):
        lt.addLast(me.getValue(om.get(analyzer['tempo'], float(song['tempo']))), int(song['id']))
    elif not om.contains(analyzer['tempo'], float(song['tempo'])):
        om.put(analyzer['tempo'], float(song['tempo']), lt.newList(cmpfunction=cmpUidList))
        lt.addLast(me.getValue(om.get(analyzer['tempo'], float(song['tempo']))), int(song['id']))

    if om.contains(analyzer['acousticness'], float(song['acousticness'])):
        lt.addLast(me.getValue(om.get(analyzer['acousticness'], float(song['acousticness']))), int(song['id']))
    elif not om.contains(analyzer['acousticness'], float(song['acousticness'])):
        om.put(analyzer['acousticness'], float(song['acousticness']), lt.newList(cmpfunction=cmpUidList))
        lt.addLast(me.getValue(om.get(analyzer['acousticness'], float(song['acousticness']))), int(song['id']))

    if om.contains(analyzer['energy'], float(song['energy'])):
        lt.addLast(me.getValue(om.get(analyzer['energy'], float(song['energy']))), int(song['id']))
    elif not om.contains(analyzer['energy'], float(song['energy'])):
        om.put(analyzer['energy'], float(song['energy']), lt.newList(cmpfunction=cmpUidList))
        lt.addLast(me.getValue(om.get(analyzer['energy'], float(song['energy']))), int(song['id']))

    if om.contains(analyzer['mode'], float(song['mode'])):
        lt.addLast(me.getValue(om.get(analyzer['mode'], float(song['mode']))), int(song['id']))
    elif not om.contains(analyzer['mode'], float(song['mode'])):
        om.put(analyzer['mode'], float(song['mode']), lt.newList(cmpfunction=cmpUidList))
        lt.addLast(me.getValue(om.get(analyzer['mode'], float(song['mode']))), int(song['id']))

    if om.contains(analyzer['key'], float(song['key'])):
        lt.addLast(me.getValue(om.get(analyzer['key'], float(song['key']))), int(song['id']))
    elif not om.contains(analyzer['key'], float(song['key'])):
        om.put(analyzer['key'], float(song['key']), lt.newList(cmpfunction=cmpUidList))
        lt.addLast(me.getValue(om.get(analyzer['key'], float(song['key']))), int(song['id']))
    
    return analyzer

def updateSongID(map, song):
    trackID = int(song['id'])
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

def charXrang(analyzer):
    return analyzer['tempo']







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

def cmpUidList(name, track):
    if name in track['id']:
        return 0
    return -1