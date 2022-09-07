#from tkinter.tix import Tree
import xml.etree.cElementTree as ET
from listadatos import Listasimple
from Matriz import MatrizOrtogonal 
from CelulaLista import CelulaLista
from colorama import Fore, Back, Style
x=Listasimple()
lista=[]

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
               paciente=x.CrearPaciente(cont,nombre,varage)
               lista.append(paciente)

              
            for periodo in subelem.iter('periodos'):
                p=periodo.text
                print("periodos: "+ periodo.text)
            for m in subelem.iter('m'):
                matriz=m.text
                mat=int(matriz)
                if mat%10 !=0:
                 print("matriz no es múltiplo de 10, ingrese otra matriz")
               # else:
                #CrearMatriz(mat)
            for reja in subelem.iter('rejilla'):
                 for celda in reja.iter('celda'):
                    
                    f=celda.attrib['f']
                    c=celda.attrib['c']

                    #cl=CelulaLista()
                    print("filas "+f+"columnas "+c+"contador "+ str(cont))
                    tejido=CelulaLista(cont,1,f,c)
                    lista.append(tejido)
                    print("fila "+str(lista[cont]))
                 cont+=1   
                 print("*********************")
    x.Imprimir()
def CrearMatriz(size):
    matrizOrtogonal = MatrizOrtogonal()
    for i in range(0,size):
     for j in range(0,size):
      matrizOrtogonal.insertarDato(1,i,j)
  
    #matrizOrtogonal.insertarDato(0,0,1)
    matrizOrtogonal.recorrerMatriz()
def menu():
    while True:
        print(Fore.LIGHTBLACK_EX+"----MENU----")
        print(Fore.CYAN+'1. Cargar Archivo')
        print(Fore.CYAN+'2. Seleccionar Paciente')
        print(Fore.CYAN+'2. Graficar tejido del paciente ')
        print(Fore.CYAN+'2. Obtener diagnóstico ')
        print(Fore.CYAN+'2. Salir')

        opcion=input(Fore.YELLOW+'Ingrese una opcion ')
        if opcion=="1":
            Filename = input(Fore.BLUE+'Ingrese ruta del archivo: ')
            file =  Filename
            cargarArchivo(file)
        if opcion=="2":
            nom = input(Fore.BLUE+'Ingrese nombre del paciente: ')
            paciente = x.getPaciente(nom)

            if paciente is None: 
                print(Fore.RED+'> Nombre incorrecto o no registrado')
            else:
                print(Fore.GREEN+'Paciente:', paciente.nombre,"edad: ",paciente.edad, "id: "+ str(paciente.id))
                size=len(lista)
                print(size)
                for i in range(0,size-1):
                    if paciente.id==lista[i].id :
                        print("fila "+str(lista[i].f)+" columna "+str(lista[i].f))

menu()

    