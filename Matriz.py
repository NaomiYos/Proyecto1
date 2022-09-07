from graphviz import Digraph
class Celula:
   def __init__(self):
    self.estado=None
    self.f=None
    self.c=None
    self.derecha = None
    self.izquierda = None
    self.arriba = None
    self.abajo = None
class MatrizOrtogonal:
    def __init__(self):
        #Creamos el nodo raiz en 0,0
        self.raiz = Celula()
        self.raiz.c = 0
        self.raiz.f = 0

    def crearIndiceVertical(self, pos):
        # recorrer todos los nodos de manera vertical
        # creamos un temporal
        tmp = self.raiz
        while tmp != None:
            # no existe el indice; solo hay índices menores
            if tmp.abajo == None and tmp.c < pos:
                # ya no hay más nodos en vertical
                # se inserta al final
                nuevo = Celula()
                nuevo.f = 0
                nuevo.c = pos
                nuevo.arriba = tmp
                tmp.abajo = nuevo
                return tmp.abajo
            
            # indice actual es igual a el nuevo índice
            if tmp.c == pos :
                # no hacer nada
                return tmp

            # indice actual es menor, pero el siguiente es mayor
            if tmp.c < pos and tmp.abajo.c > pos:
                # insertar un nodo en medio del nodo actual y del nodo siguiente
                nuevo = Celula()
                nuevo.f = 0
                nuevo.c = pos

                # asignar abajo y arriba para el nodo nuevo
                nuevo.abajo = tmp.abajo
                nuevo.arriba = tmp
                
                tmp.abajo.arriba = nuevo # reasignar arriba para el nodo de abajo
                tmp.abajo = nuevo # reasignar abajo para el nodo actual
                return tmp.abajo

            # pasar al siguiente nodo abajo si no hubo un return
            tmp = tmp.abajo

    def crearIndiceHorizontal(self, pos):
        # recorrer todos los nodos de manera horizontal
        tmp = self.raiz
        while tmp != None:
            # no existe el indice; solo hay índices menores
            if tmp.derecha == None and tmp.f < pos:
                # ya no hay más nodos en horizontal
                # se inserta al final
                nuevo = Celula()
                nuevo.f = pos
                nuevo.c = 0
                nuevo.izquierda = tmp
                tmp.derecha = nuevo
                return tmp.derecha
            
            # indice actual es igual a el nuevo índice
            if tmp.f == pos :
                # no hacer nada
                return tmp

            # indice actual es menor, pero el siguiente es mayor
            if tmp.f < pos and tmp.derecha.f > pos:
                # insertar un nodo en medio del nodo actual y del nodo siguiente
                nuevo = Celula()
                nuevo.f = pos
                nuevo.c = 0

                # asignar derecha y arriba para el nodo nuevo
                nuevo.derecha = tmp.derecha
                nuevo.izquierda = tmp
                
                tmp.derecha.izquierda = nuevo # reasignar arriba para el nodo de derecha
                tmp.derecha = nuevo # reasignar derecha para el nodo actual
                return tmp.derecha
                
            # pasar al siguiente nodo derecha si es que no hubo return 
            tmp = tmp.derecha

    def insertarVertical(self, nodo, indiceHorizontal):
        # recorrer todos los nodos de manera horizontal para insertar los verticales
        tmp = indiceHorizontal
        while tmp != None:
            # no existe el indice; solo hay índices menores
            if tmp.abajo == None and tmp.c < nodo.c:
                # ya no hay más nodos en vertical
                # se inserta al final
                nodo.arriba = tmp
                tmp.abajo = nodo
                return tmp.abajo #nodo nuevo
            
            # indice actual es igual a el nuevo índice
            if tmp.c == nodo.c :
                # no hacer nada, el dato se sobre escribe
                tmp.estado = nodo.estado
                return tmp

            # indice actual es menor, pero el siguiente es mayor
            if tmp.c < nodo.c and tmp.abajo.c > nodo.c:
                # insertar un nodo en medio del nodo actual y del nodo siguiente

                # asignar abajo y arriba para el nodo nuevo
                nodo.abajo = tmp.abajo
                nodo.arriba = tmp
                
                tmp.abajo.arriba = nodo # reasignar arriba para el nodo de abajo
                tmp.abajo = nodo # reasignar abajo para el nodo actual
                return tmp.abajo

            # pasar al siguiente nodo abajo si no hubo return
            tmp = tmp.abajo
       
    def insertarHorizontal(self, nodo, indiceVertical):
        # recorrer todos los nodos en horizontal
        tmp = indiceVertical
        while tmp != None:
            # no existe el indice; solo hay índices menores
            if tmp.derecha == None and tmp.f < nodo.f:
                # ya no hay más nodos en horizontal
                # se inserta al final
                nodo.izquierda  = tmp
                tmp.derecha = nodo
                return tmp.derecha
            
            # indice actual es igual a el nuevo índice
            if tmp.f == nodo.f :
                # no hacer nada se sobre escribe
                tmp.estado = nodo.estado
                return tmp

            # indice actual es menor, pero el siguiente es mayor
            if tmp.f < nodo.f and tmp.derecha.f > nodo.f:
                # insertar un nodo en medio del nodo actual y del nodo siguiente
                # asignar derecha y arriba para el nodo nuevo
                nodo.derecha = tmp.derecha
                nodo.izquierda = tmp
                
                tmp.derecha.izquierda = nodo # reasignar arriba para el nodo de derecha
                tmp.derecha = nodo # reasignar derecha para el nodo actual
                return tmp.derecha
                
            # pasar al siguiente nodo derecha si esque no hubo return
            tmp = tmp.derecha

    def insertarDato(self, dato,  c, f):
        # validar que los índices existan en horizontal y vertical
        indiceVertical = self.crearIndiceVertical(c)
        indiceHorizontal = self.crearIndiceHorizontal(f)

        # crear el nodo valor
        nuevo = Celula()
        nuevo.f = f
        nuevo.c = c
        nuevo.estado = dato

        # indexar/apuntar nodo nuevo en indice vertical
        nuevo = self.insertarVertical(nuevo, indiceHorizontal) 
        nuevo = self.insertarHorizontal(nuevo, indiceVertical)
        #print("Nodo insertado...")
        pass
    
    def recorrerMatriz(self):
        print("Graficando lista...")
        
        dot = Digraph('G', filename='dot', engine='dot',format='svg')
        dot.node_attr.update(shape="box")
        dot.node_attr['style'] = 'filled'
        dot.attr(rankdir = "TB")
       # dot.attr(rankdir = "0.5")
       
        contSubgrap = 1
        
        #iniciamos en el nodo raiz
        tmpV = self.raiz

        #vamos bajando en vertical
        while tmpV != None:
            tmpH = tmpV

            #creamos subgrafos para alinearlos            
            c = Digraph('child'+str(contSubgrap))
            c.attr(rank='same')
            contSubgrap += 1

            #nos vamos a la derecha 
            while tmpH != None:
                self.graficarNodos(c, tmpH)
                tmpH = tmpH.derecha

            #se termino una fila, agregamos el subgrafo
            dot.subgraph(c)
            tmpV = tmpV.abajo


        #vuelvo a recorrer para mostrar las flechas
        tmpV = self.raiz
        #vamos bajando en vertical
        while tmpV != None:
            tmpH = tmpV

            #nos vamos a la derecha 
            while tmpH != None:
                self.graficarFlechas(dot, tmpH)
                tmpH = tmpH.derecha

            tmpV = tmpV.abajo
        dot.view()
        pass

    def graficarNodos(self, grafo, nodoE):
        
        nodo = nodoE
        id = str(nodo.c)+"_"+str(nodo.f)
        if nodo.estado==1:
            grafo.node(id," ",color="green",group=str(nodo.f))
        elif nodo.estado==0:
            grafo.node(id," ",fillcolor="white",group=str(nodo.f))
        
    def graficarFlechas(self, grafo, nodoE):
        nodo = nodoE
        id = str(nodo.c)+"_"+str(nodo.f)
        if nodo.c != 0 and nodo.f != 0:
            #Graficamos la flecha vertical
            idV1 = nodo.arriba.c
            idV2 = nodo.arriba.f
            idV = str(idV1)+"_"+str(idV2)
            grafo.edge(idV, id,color = "white")
            grafo.edge(id, idV,color = "white")
           


            #Ahora graficamos la flecha horizontal
            idH1 = nodo.izquierda.c
            idH2 = nodo.izquierda.f
            idH = str(idH1)+"_"+str(idH2)
            grafo.edge(idH,id,color = "white")
            grafo.edge(id,idH,color = "white")
        elif nodo.c == 0 and nodo.f != 0:
            #es una cabecera horizontal
            idAnterior = str(nodo.izquierda.c)+"_"+str(nodo.izquierda.f)
            grafo.edge(idAnterior, id,color = "white")   
        elif nodo.f == 0 and nodo.c != 0:
            #es una cabecera vertical
            idAnterior = str(nodo.arriba.c)+"_"+str(nodo.arriba.f)
            grafo.edge(idAnterior, id,color = "white")
        pass
