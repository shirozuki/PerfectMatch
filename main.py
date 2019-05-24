#-*- coding: utf-8 -*-

import networkx as nx
import random

random.seed()
G = nx.Graph()

attrList = ['książki', 'fotografia', 'paintball', 'wspinaczka', 'strzelnica', 'tenis', 'warcaby', 'fizyka', 'literatura', 'komiksy', 'kraje orientu', 'gry komputerowe', 'gry na instrumecie', 'filmy', 'muzyka', 'spacery', 'śpiew', 'gotowanie', 'pieczenie', 'majsterkowanie', 'pędzenie bimbru', 'uprawa roślin', 'zielarstwo', 'bieganie', 'gimnastyka', 'jazda konna', 'rower', 'pływanie', 'taniec', 'sporty walki', 'wędkarstwo', 'malowanie', 'rysowanie', 'programowanie', 'bilard', 'szachy', 'języki obce', 'puzzle', 'krzyżówki', 'astronomia', 'piłka nożna', 'koszykówka', 'podróże', 'biwakowanie', 'góry', 'morze', 'samochody', 'manga i anime', 'religia', 'filozofia']

print(len(attrList))
numOfMen = 10
numOfWomen = 10
numOfNodes = numOfMen + numOfWomen

i = 0

while i < numOfMen:
    nodeName = "M" + str(i + 1)
    j = 0
    k = 0
    selfAttrInUse = []
    partnerAttrInUse = []
    selfAttrList = []
    wantedAttrList = []

    while j < 10:
        x = random.randint(0, 49)
        if x in selfAttrInUse:
            continue
        else:
            selfAttrInUse.append(x)
            selfAttrList.append(attrList[x])
            j += 1

    while k < 10:
        x = random.randint(0, 49)
        if x in partnerAttrInUse:
            continue
        else:
            partnerAttrInUse.append(x)
            wantedAttrList.append(attrList[x])
            k += 1

    print("Mężczyzna nr " + str(i + 1) + " stworzony")
    print("Jego zainteresowania: ")
    for item in selfAttrList:
        print(item)
    print("Cechy interesujące u partnera: ")
    for item in wantedAttrList:
        print(item)
    
    
    G.add_node(i, id=i, gender='M', selfAttrs=selfAttrList, wantedAttrs=wantedAttrList)
    i += 1

while i < numOfNodes:
    nodeName = "K" + str(i + 1)
    j = 0
    k = 0
    selfAttrInUse = []
    partnerAttrInUse = []
    selfAttrList = []
    wantedAttrList = []

    while j < 10:
        x = random.randint(0, 49)
        if x in selfAttrInUse:
            continue
        else:
            selfAttrInUse.append(x)
            selfAttrList.append(attrList[x])
            j += 1

    while k < 10:
        x = random.randint(0, 49)
        if x in partnerAttrInUse:
            continue
        else:
            partnerAttrInUse.append(x)
            wantedAttrList.append(attrList[x])
            k += 1

    print("Kobieta nr " + str(i + 1) + " stworzona")
    print("Jej zainteresowania: ")
    for item in selfAttrList:
        print(item)
    print("Cechy interesujące u partnera: ")
    for item in wantedAttrList:
        print(item)
    
    G.add_node(i, id=i, gender='K', selfAttrs=selfAttrList, wantedAttrs=wantedAttrList)
    i += 1

i = 0
while i < G.number_of_nodes():
    print(G.nodes()[i])
    i += 1

i = 0
womenStartPoint = 0

while(G.node[womenStartPoint]['gender']) != 'K':
    womenStartPoint += 1

while (G.node[i]['gender']) == 'M':
    hiScore = 0
    j = womenStartPoint
    matches = 0
    print("Mężczyzna: " + str(G.node[i]['id']))
 
    while (j < G.number_of_nodes()):
        if (G.node[j]['gender'] == 'K'):
            print("M" + str(G.node[i]['id']) + " + K" + str(G.node[j]['id']))
            matches = (len(set(G.node[i]['selfAttrs']) & set(G.node[j]['wantedAttrs']))) + (len(set(G.node[i]['wantedAttrs']) & set(G.node[j]['selfAttrs'])))
            print("Dopasowanie: ", matches)
            thisScore = matches
            if thisScore >= hiScore:
                hiScore = thisScore
                bestCandidate = j
            G.add_edge(i, j, weight = matches)
        j += 1
    print("Dla M" + str(i) + " najlepszą kandydatką jest K" + str(bestCandidate) + " z wynikiem: " + str(hiScore))
    print("------------------------------------------------")
    i += 1
    

f = open("graph.xml","w+")
f.write('<?xml version="1.0" encoding="ISO-8859-1"?>\n'
'<!DOCTYPE gxl SYSTEM "http://www.gupro.de/GXL/gxl-1.0.dtd">\n'
'<gxl>\n'
'<graph>\n')

i = 0
while i < G.number_of_nodes():
    f.write('<node id="' + str(G.node[i]['id']) + '" gender="' + str(G.node[i]['gender']) + '" >\n')
    str1 = ', '.join(G.node[i]['selfAttrs'])
    f.write('<selfAttrs>' + str1 + '</selfAttrs>\n')
    str2 = ', '.join(G.node[i]['wantedAttrs'])
    f.write('<wantedAttrs>' + str2 + '</wantedAttrs>\n')
    f.write('</node>\n')
    
    i += 1

i = 0
while i < G.number_of_edges():
    currList = list(G.edges(data=True))[i]
    f.write('<edge id="' + str(i) + '" from="' + str(currList[0]) + '" to="' + str(currList[1]) + '" weight="' + str(currList[2]['weight']) + '" />\n')
    i += 1

f.write("</graph>\n</gxl>")