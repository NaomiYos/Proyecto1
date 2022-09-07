class Paciente:
    def __init__(self,id, nombre,edad) :
        self.id=id
        self.nombre=nombre
        self.edad=edad
        self.siguiente=None
   

class Listasimple:
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def CrearPaciente(self,xid,xnombre,xedad):
        nuevo=Paciente(xid,xnombre,xedad)

        if self.primero==None:
            self.primero=nuevo
            self.ultimo=nuevo
        else:
            self.ultimo.siguiente=nuevo
            self.ultimo=nuevo

    def Imprimir(self):
       # temp=Nodo("")
        cantidad=0
        temp=self.primero
        while temp!=None:
            cantidad+=1
            print("Paciente "+str(temp.nombre)+str(temp.edad),"id "+str(temp.id))
            temp=temp.siguiente
        #print("son "+temp+" elementos")
    
    def getPaciente(self,nombre):
        tmp=self.primero
        while tmp is not None:
            if tmp.nombre==nombre:
                return tmp
            tmp=tmp.siguiente
        return None
    
 