class CelulaLista:
   def __init__(self,id,estado,f,c):
    self.id=id
    self.estado=estado
    self.f=f
    self.c=c
   def __repr__(self):
        return str(self.__dict__)