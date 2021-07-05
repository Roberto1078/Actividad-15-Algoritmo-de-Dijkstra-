import math
from queue import PriorityQueue
from PySide2.QtGui import QPen,QColor
from pprint import pprint


def distancia_euclidiana(x_1, y_1 , x_2, y_2) :
    raiz = math.sqrt((x_2 - x_1)**2 + (y_2-y_1)**2)
    return raiz

def recorrido_profundidad(inicio, diccionario) :

    visitados = []
    pila = []
    recorrido = []

    visitados.append(inicio)
    pila.append(inicio)

    while len(pila) > 0 :

        ultimo = pila[-1]
        recorrido.append(ultimo)
      
        lista = list(diccionario[ultimo])
        adyacente = []
        for p in lista :
            adyacente.append(p[0])
        pila.pop()
        for p in adyacente :
            if not p in visitados :
                pila.append(p)
        
        for p in adyacente :
            if not p in visitados :
                visitados.append(p)
    return recorrido

def recorrido_amplitud(inicio, diccionario) :

    visitados = []
    pila = []
    recorrido = []

    visitados.append(inicio)
    pila.append(inicio)

    while len(pila) > 0 :

        ultimo = pila[0]
        recorrido.append(ultimo)
      
        lista = list(diccionario[ultimo])
        adyacente = []
        for p in lista :
            adyacente.append(p[0])
        pila.pop(0)
        for p in adyacente :
            if not p in visitados :
                pila.append(p)
        
        for p in adyacente :
            if not p in visitados :
                visitados.append(p)
    return recorrido

def recorrido_amplitud(inicio,diccionario) :
    visitados = []
    pila = []
    recorrido = []

    visitados.append(inicio)
    pila.append(inicio)

    while len(pila) > 0 :

        ultimo = pila[-1]
        recorrido.append(ultimo)
      
        lista = list(diccionario[ultimo])
        adyacente = []
        for p in lista :
            adyacente.append(p[0])
        pila.pop()
        for p in adyacente :
            if not p in visitados :
                pila.append(p)
        
        for p in adyacente :
            if not p in visitados :
                visitados.append(p)
    return recorrido


def algoritmo_prim(origen, diccionario, self) :

    visitados = []
    visitados.append(origen)
    pen = QPen()
    pen.setWidth(2)
    color = QColor(150,50,150)
    pen.setColor(color)
    pq = PriorityQueue()

    lista = list(diccionario[origen])

    for p in lista :
        aristas = (p[1],p[0]) #Posicion 0 = arista Posicion 1 = ponderacion
        pq.put(aristas)

    destino = pq.get()
    destino = destino[1]

    while not pq.empty() :
        
        if not destino in visitados :
            lista = list(diccionario[destino]) #Posicion 0 = arista Posicion 1 = podenracion
            visitados.append(destino)
            for p in lista :
                if p[0] not in visitados :
                    value = (p[1],p[0])
                    pq.put(value)

            destino1 = pq.get()
            destino = destino1[1]
            distancia = destino1[0]
            for value in self.particulas :
                if value.distancia == distancia :
                    destino_x = destino[0]
                    destino_y = destino[1]
                    self.scene.addLine(value.origen_x+3,value.origen_y+3,destino_x,destino_y,pen)
        else :
            pq.get()
            pq_copy = PriorityQueue()
            if not pq.empty() :
                while not pq.empty() :
                    value = pq.get()
                    pq_copy.put(value)
                pq = pq_copy
                destino = pq_copy.get()
                destino = destino[1]
    return visitados

def algoritmo_Kruskal(grafo) :
    aem = {}
    lista = []

    for key,value in grafo.items() :
        for ady in value :
            arista = ady[0], key, ady[1] # 0 = velocidad 1 = destino key = origen
            lista.append(arista)
    lista.sort(key=lambda arista:arista[0])

    dj = make_set(grafo)

    while len(lista) > 0:
        arista = lista[-1]
        lista.pop()
        velocidad = arista[0]
        origen = arista[1]
        destino = arista[2]

        if find_set(origen, dj) != find_set(destino, dj) :
            add_arista(origen, destino, velocidad, aem)
            union_set(origen, destino, dj)
            print(dj)
    return aem



def add_arista(origen, destino, velocidad, grafo) :

    if origen in grafo :
        grafo[origen].append((velocidad, destino))
    else :
        grafo[origen] = [(velocidad, destino)]

    if destino in grafo :
        grafo[destino].append((velocidad, origen))
    else :
        grafo[destino] = [(velocidad, origen)]

def make_set(grafo) :
    dj = []

    for key in grafo :
        dj.append([key])

    return dj

def find_set(vertice, dj) :
    
    a=0
    while a < len(dj) :
        if vertice in dj[a] :
            return a
        a+=1

def union_set(origen, destino, dj) :
    i = find_set(origen, dj)
    j = find_set(destino, dj)

    i_list = dj[i]
    j_list = dj[j]
    new_list = dj[i] + dj[j]

    dj.remove(i_list)
    dj.remove(j_list)
    dj.append(new_list)

def algoritmo_Dijkstra(grafo, dict_distancia, dict_camino, origen) :

    dict_distancia[origen] = 0
    pq = PriorityQueue()
    inicio = dict_distancia[origen], origen
    pq.put(inicio)

    while not pq.empty() :
        nodo = pq.get() # 0 = Distancia 1 = arista
        lista = list(grafo[nodo[1]])

        for value in lista : #Lista 0 = distancia 1 = arista
            distancia = 0
            distancia = value[0] + nodo[0]
            if distancia < dict_distancia[value[1]] :
                dict_distancia[value[1]] = distancia
                dict_camino[value[1]] = nodo[1]
                valor = distancia, value[1]
                pq.put(valor)

    pprint(dict_distancia)
    print('\n')
    pprint(dict_camino)