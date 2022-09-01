class Paciente:
    def __init__(self, nombre,edad) :
        self.nombre=nombre
        self.edad=edad
    def __repr__(self):
        return str(self.__dict__)