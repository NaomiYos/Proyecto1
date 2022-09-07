#from tkinter.tix import Tree
import xml.etree.cElementTree as ET
from listadatos import Listasimple
from Matriz import MatrizOrtogonal 
from colorama import Fore, Back, Style
x=Listasimple()
matrizOrtogonal = MatrizOrtogonal()
class CelulaLista:
   def __init__(self,id,estado,f,c):
    self.id=id
    self.estado=estado
    self.f=f
    self.c=c
   def __repr__(self):
        return str(self.__dict__)
lista=[]
lsize=[]
def cargarArchivo(ruta):
    archivo= ET.parse(ruta)
    raiz=archivo.getroot()
   
   # print(raiz)
    cont=0 
    for elem in raiz:
        for subelem in elem:
            for subsubelem in subelem.iter('datospersonales'):
               
               for subsubelem2 in subsubelem.iter('nombre'):
                nombre=subsubelem2.text
                
                #print(nombre)
               for age in subsubelem.iter('edad'):
                 varage=age.text
                # print(varage)
               x.CrearPaciente(cont,nombre,varage)


              
            for periodo in subelem.iter('periodos'):
                p=periodo.text
                print("periodos: "+ periodo.text)
            for m in subelem.iter('m'):
                matriz=m.text
                mat=int(matriz)
                if mat%10 !=0:
                 print("matriz no es múltiplo de 10, ingrese otra matriz")
                else:
                  lsize.append(mat)  
                  print("")
            for reja in subelem.iter('rejilla'):
                 for celda in reja.iter('celda'):
                    
                    f=celda.attrib['f']
                    c=celda.attrib['c']
                    print("filas "+f+"columnas "+c+"contador "+ str(cont))
                    tejido=CelulaLista(cont,1,int(f),int(c))
                    lista.append(tejido)

                   
                 cont+=1   
                 print("*********************")
    x.Imprimir()
def CrearMatriz(size):
 
    for i in range(0,size):
     for j in range(0,size):
      matrizOrtogonal.insertarDato(0,i,j)
   # matrizOrtogonal.recorrerMatriz()
    
def menu():
    while True:
        print(Fore.LIGHTBLACK_EX+"----MENU----")
        print(Fore.CYAN+'1. Cargar Archivo')
        print(Fore.CYAN+'2. Seleccionar Paciente')
        print(Fore.CYAN+'3. Graficar tejido del paciente ')
        print(Fore.CYAN+'. Salir')

        opcion=input(Fore.WHITE+'Ingrese una opcion ')
        if opcion=="1":
            Filename = input(Fore.BLUE+'Ingrese ruta del archivo: ')
            file =  Filename
            cargarArchivo(file)
        elif opcion=="2":
            nom = input(Fore.BLUE+'Ingrese nombre del paciente: ')
            paciente = x.getPaciente(nom)

            if paciente is None: 
                print(Fore.RED+'> Nombre incorrecto o no registrado')
            else:
                print(Fore.GREEN+'Paciente:', paciente.nombre,"edad: ",paciente.edad)
                print(Fore.GREEN+'Graficando Tejido inicial')
                index=paciente.id
                tam=lsize[index]
                print(str(tam))
                CrearMatriz(tam)
                size=len(lista)
                for i in range(0,size-1):
                    if paciente.id==lista[i].id :
                        
                        fx=lista[i].f
                        fila=int(fx)
                        cx=lista[i].c
                        columna=int(cx)
                        matrizOrtogonal.insertarDato(1,fila,columna)
                        
        elif opcion=="3":
            matrizOrtogonal.recorrerMatriz()
             
menu()

    