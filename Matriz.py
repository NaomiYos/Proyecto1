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
    def __repr__(self):
        return str(self.__dict__)
class MatrizOrtogonal:
    def __init__(self):
       
        self.raiz = Celula()
        self.raiz.c = 0
        self.raiz.f = 0

    def crearIndiceVertical(self, pos):
        
        tmp = self.raiz
        while tmp != None:
          
            if tmp.abajo == None and tmp.c < pos:
               
                nuevo = Celula()
                nuevo.f = 0
                nuevo.c = pos
                nuevo.arriba = tmp
                tmp.abajo = nuevo
                return tmp.abajo
            
            if tmp.c == pos :
               
                return tmp

           
            if tmp.c < pos and tmp.abajo.c > pos:
                
                nuevo = Celula()
                nuevo.f = 0
                nuevo.c = pos

               
                nuevo.abajo = tmp.abajo
                nuevo.arriba = tmp
                
                tmp.abajo.arriba = nuevo 
                tmp.abajo = nuevo 
                return tmp.abajo

           
            tmp = tmp.abajo

    def crearIndiceHorizontal(self, pos):
        
        tmp = self.raiz
        while tmp != None:
            
            if tmp.derecha == None and tmp.f < pos:
                
                nuevo = Celula()
                nuevo.f = pos
                nuevo.c = 0
                nuevo.izquierda = tmp
                tmp.derecha = nuevo
                return tmp.derecha
            
           
            if tmp.f == pos :
                return tmp

            
            if tmp.f < pos and tmp.derecha.f > pos:
               
                nuevo = Celula()
                nuevo.f = pos
                nuevo.c = 0

               
                nuevo.derecha = tmp.derecha
                nuevo.izquierda = tmp
                
                tmp.derecha.izquierda = nuevo 
                tmp.derecha = nuevo 
                return tmp.derecha
                
           
            tmp = tmp.derecha

    def insertarVertical(self, nodo, indiceHorizontal):
      
        tmp = indiceHorizontal
        while tmp != None:
           
            if tmp.abajo == None and tmp.c < nodo.c:
                nodo.arriba = tmp
                tmp.abajo = nodo
                return tmp.abajo 
            if tmp.c == nodo.c :
                tmp.estado = nodo.estado
                return tmp

        
            if tmp.c < nodo.c and tmp.abajo.c > nodo.c:
              
                nodo.abajo = tmp.abajo
                nodo.arriba = tmp
                
                tmp.abajo.arriba = nodo 
                tmp.abajo = nodo 
                return tmp.abajo

            
            tmp = tmp.abajo
       
    def insertarHorizontal(self, nodo, indiceVertical):
        
        tmp = indiceVertical
        while tmp != None:
            if tmp.derecha == None and tmp.f < nodo.f:
              
                nodo.izquierda  = tmp
                tmp.derecha = nodo
                return tmp.derecha
            if tmp.f == nodo.f :
                tmp.estado = nodo.estado
                return tmp
            if tmp.f < nodo.f and tmp.derecha.f > nodo.f:
                nodo.izquierda = tmp
                
                tmp.derecha.izquierda = nodo 
                tmp.derecha = nodo 
                return tmp.derecha
                
          
            tmp = tmp.derecha

    def insertarDato(self, dato,  c, f):
        indiceVertical = self.crearIndiceVertical(c)
        indiceHorizontal = self.crearIndiceHorizontal(f)
        nuevo = Celula()
        nuevo.f = f
        nuevo.c = c
        nuevo.estado = dato
        nuevo = self.insertarVertical(nuevo, indiceHorizontal) 
        nuevo = self.insertarHorizontal(nuevo, indiceVertical)
        pass
    
    def recorrerMatriz(self):
        print("Graficando lista...")
        
        dot = Digraph('G', filename='dot', engine='dot',format='svg')
        dot.node_attr.update(shape="box")
        dot.attr(pad="0.05")
        dot.attr(nodesep="0.1")
        dot.attr(ranksep="0.1")
        dot.node_attr['style'] = 'filled'
        dot.attr(rankdir = "TB")
       
        contSubgrap = 1
        tmpV = self.raiz
        while tmpV != None:
            tmpH = tmpV        
            c = Digraph('child'+str(contSubgrap))
            c.attr(rank='same')
            contSubgrap += 1
            while tmpH != None:
                self.graficarNodos(c, tmpH)
                tmpH = tmpH.derecha
            dot.subgraph(c)
            tmpV = tmpV.abajo

        tmpV = self.raiz
        while tmpV != None:
            tmpH = tmpV
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
            idV1 = nodo.arriba.c
            idV2 = nodo.arriba.f
            idV = str(idV1)+"_"+str(idV2)
            grafo.edge(idV, id,color = "white")
            grafo.edge(id, idV,color = "white")
           
            idH1 = nodo.izquierda.c
            idH2 = nodo.izquierda.f
            idH = str(idH1)+"_"+str(idH2)
            grafo.edge(idH,id,color = "white")
            grafo.edge(id,idH,color = "white")
        elif nodo.c == 0 and nodo.f != 0:
            idAnterior = str(nodo.izquierda.c)+"_"+str(nodo.izquierda.f)
            grafo.edge(idAnterior, id,color = "white")   
        elif nodo.f == 0 and nodo.c != 0:
            idAnterior = str(nodo.arriba.c)+"_"+str(nodo.arriba.f)
            grafo.edge(idAnterior, id,color = "white")
        pass
    def búsqueda(self,size):
        contf=0
        contc=0
        self.raiz.estado=1
        tmpV = self.raiz
        while tmpV != None:
            tmpH = tmpV

            tmparri=tmpH
            tmpabajo=tmpH
            tmpder=tmpH
            tmpizq=tmpH
            while tmpH != None:
                cont=0
                if tmpH.f==0 and tmpH.c==0:
                    tmpabajo=tmpH.abajo
                    tmpder=tmpH.derecha
                    if tmpabajo.estado==1:
                         cont+=1
                    elif tmpder.estado==1:
                         cont+=1
                #fila 0 sin la ultima columna
                elif tmpH.f==0 and tmpH.c !=0 and tmpH.c!=size-1:
                    tmpabajo=tmpH.abajo
                    tmpder=tmpH.derecha
                    tmpizq=tmpH.izquierda
                    if tmpabajo.estado==1:
                         cont+=1
                    elif tmpder.estado==1:
                         cont+=1
                    elif tmpizq.estado==1:
                        cont+=1
                #columna 0 a excepción del nodo de la esquina
                elif tmpH.c==4 and tmpH.f==4 :
                    tmpabajo=tmpH.abajo
                    tmpizq=tmpH.izquierda
                    tmparri=tmpH.arriba

                    if tmpabajo.estado==1:
                         cont+=1
                    elif tmpizq.estado==1:
                         cont+=1
                    elif tmparri.estado==1:
                     cont+=1
                #ultima fila a excepcion de las esquinas
                elif tmpH.f==size-1 and tmpH.c!=0 and tmpH.c!=size-1:
                    tmpder=tmpH.derecha
                    tmparri=tmpH.arriba
                    tmpizq=tmpH.izquierda
                    if tmparri.estado==1:
                         cont+=1
                    elif tmpder.estado==1:
                         cont+=1
                  
                    elif tmpizq.estado==1:
                        cont+=1
                # ultima columna a excepcion de las esquinas
                elif tmpH.c==size-1 and tmpH.f!=0 and tmpH.f!=size-1:
                    tmpabajo=tmpH.abajo
                    tmparri=tmpH.arriba
                    tmpizq=tmpH.izquierda
                    if tmpabajo.estado==1:
                         cont+=1
                    elif tmpizq.estado==1:
                         cont+=1
                    elif tmparri.estado==1:
                     cont+=1
                # nodo esquina inferior izquierda
                elif tmpH.c==0 and  tmpH.f==size-1:
                    print(tmpH.estado)
                    tmparri=tmpH.arriba
                    tmpder=tmpH.derecha
                    if tmpder.estado==1:
                         cont+=1
                    elif tmparri.estado==1:
                        cont+=1
                # nodo esquina inferior derecha
                elif tmpH.c==size-1 and  tmpH.f==size-1:
                    tmparri=tmpH.arriba
                    tmpizq=tmpH.izquierda
                    if tmpizq.estado==1:
                         cont+=1
                    elif tmparri.estado==1:
                     cont+=1
                # nodo esquina superior derecha
                elif tmpH.c==size-1 and  tmpH.f==0:
                    tmpabajo=tmpH.abajo
                    tmpizq=tmpH.izquierda
                    if tmpizq.estado==1:
                         cont+=1
                    elif tmpabajo.estado==1:
                     cont+=1 
                #no bordes         
                else:
                    tmpder=tmpH.derecha
                    tmparri=tmpH.arriba
                    tmpabajo=tmpH.abajo
                    tmpizq=tmpH.izquierda
                    if tmpabajo.estado==1:
                         cont+=1
                    elif tmpizq.estado==1:
                         cont+=1
                    elif tmparri.estado==1:
                         cont+=1
                    elif tmpder.estado==1:
                         cont+=1 
                if tmpH.estado==1 and cont==2 or cont==3:
                    print("el nodo en la fila "+str(tmpH.f)+" y columna "+str(tmpH.c)+"seguirá contagiada")
                else:
                    print("el nodo en la fila "+str(tmpH.f)+" y columna "+str(tmpH.c)+"ya no seguirá contagiada")
                if tmpH.estado==0 and cont==3:
                 print("el nodo en la fila "+str(tmpH.f)+" y columna "+str(tmpH.c)+"será contagiada")
                else:
                    print("no se contagiará")
                tmpH = tmpH.derecha
               

            tmpV = tmpV.abajo
        print("terminó de analizar")
