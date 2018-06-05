# --------------------------Importacion de librerias---------------------------------
import glob
import math
import os
import random

import nltk
import tkinter.messagebox
import ManejoArchivos
import operator
import CosineSimilarity
from tkinter import *
from tkinter import filedialog

# --------------------------Declaracion de variables---------------------------------
global NomDatos
NomDatos = "ejemplos"
global resultados
global totalResultados


# --------------------------Declaracion de funciones---------------------------------
def ficherosEnDir(ruta):
    listado = []
    for raiz, subcarpetas, ficheros in os.walk(ruta):
        for fichero in ficheros:
            listado.append(os.path.join(raiz, fichero))
    return listado


def buscarPalabra(query):
    print("Buscando...")
    global resultados
    global NomDatos
    global totalResultados
    valores = {}
    resultados= []
    totalResultados=0
    #print(resultados)
    path="C:/Users/Armando/Documents/Primer Semestre 2018/Analisis/Progra#3/Datos/TF-IDF"
    archivos=ficherosEnDir(path)
    for x in archivos:
        busqueda=CosineSimilarity.function(x, query, archivos.__len__())
      #  print(busqueda)
        if busqueda[1] != 0.0:
            valores[busqueda[0]] = busqueda[1]
            totalResultados+=1
   #print(valores)
    sorted_d = sorted(valores.items(), key=operator.itemgetter(1))
    resultados=sorted_d
    #`print(resultados)

def mostrarResultado(ID):
    #print(ID)
    ventanaMos = Tk()
    ventanaMos.title(ID)
    ventanaMos.resizable(FALSE, FALSE)
    ventanaMos.geometry("1024x700+250+50")
    file=open(ID,'r')
    texto=file.readline()
    file.close()
    #print(texto)
    S = Scrollbar(ventanaMos)
    T = Text(ventanaMos, height=10, width=130)
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = texto
    T.insert(END, quote)


def cerrar(ventana):
    ventana.destroy()
    ventanaPrincipal()

def crearVentanaResultados(cantidad):
    # --------------------------VentanaAdministrador---------------------------------
    ventanaRes = Tk()
    ventanaRes.title("Resultados")
    ventanaRes.resizable(FALSE, FALSE)
    ventanaRes.geometry("1024x700+250+50")
    ventanaRes.configure(background='white')
    ventanaRes.protocol("WM_DELETE_WINDOW", lambda root=ventanaRes: cerrar(root))
    # Canvas
    scrollbar = Scrollbar(ventanaRes)
    canvas = Canvas(ventanaRes, yscrollcommand=scrollbar.set, height=768, width=1000)
    scrollbar.config(command=canvas.yview)
    scrollbar.grid(row=0, column=10, sticky=N + S + E + W)
    elframe = Frame(canvas)
    canvas.grid(row=0, column=0, sticky=N + S + E + W)
    canvas.create_window(0, 0, window=elframe)
    indice = 0
    pos = 0
    cont = 0
    bandera=True
    def crearBoton2(pos, cont, texto):
        nombre1 = Button(elframe, text=texto, state=DISABLED, relief="flat", borderwidth=5,compound=TOP, width=100, anchor="w",foreground="black",font=("Helvetica", 12, "underline")).grid(row=pos,
                                                                                                         column=cont,
                                                                                                         padx=10,
                                                                                                         pady=10)
    def crearBoton(pos, cont, texto, ID):
        nombre1 = Button(elframe, text=texto, relief="flat",anchor="w",borderwidth=5, command=lambda: (mostrarResultado(ID)),compound=TOP, width=100,foreground="blue",font=("Helvetica", 12, "underline")).grid(row=pos,
                                                                                                         column=cont,
                                                                                                         padx=10,
                                                                                                         pady=10)
    while indice < cantidad:
        try:
            if cont == 1:
                pos += 1
                cont = 0
            else:
                if bandera:
                    cant="Mostrando:"+str(cantidad)+" de un total de:"+str(totalResultados)
                    crearBoton2(pos, cont, cant)
                    cont += 1
                else:
                    crearBoton(pos, cont, resultados[indice][0], resultados[indice][0])
                    indice += 1
                    cont += 1
            bandera=False
        except:
            #print("error")
            crearBoton2(pos, cont, "No hay mas resultados")
            break
    ventanaRes.update()
    canvas.config(scrollregion=canvas.bbox("all"))


def buscar(palabra,cantidad):
    print("Buscando " + palabra + " y mostrando " +str(cantidad))
    buscarPalabra(palabra)
    crearVentanaResultados(cantidad)
    #Prueba
    #x=range(22000000)
    #lista=[]
    #for x in range(22000000):
        #   lista.append([])
    #for x in range(50):
        #   print(lista[x])
        #  lista[x]=[1,2,3,4,5,"asdasd"]
        # print (lista[x])


def onEnter():
    buscar()



def cambiarSetDatos(self):
    folder_selected = filedialog.askdirectory()
    print(folder_selected)
    global NomDatos
    NomDatos = folder_selected
    self.destroy()
    verificar("admin", "admin")


def abrirArchivoTxt():
    filename = "C:/Users/Armando/Documents/Primer Semestre 2018/Analisis/Progra#3/Datos/datos.txt"
    archivo = open(filename.encode('unicode-escape').replace("'", "\\'"), 'r')
    texto = archivo.readline()
    cont = 0
    while texto != "":
        texto = archivo.readline()
        name = "C:/Users/Armando/Documents/Primer Semestre 2018/Analisis/Progra#3/Datos/Txt/" + str(cont) + ".txt"
        file = open(name, "w")
        file.write(texto)
        file.close()
        cont = cont + 1


def indexarArchivos():
    cantidadDocumentos=22000000
    print("Entro a indexar")
    #folder_selected = filedialog.askdirectory()
    #ficheros = ficherosEnDir(folder_selected)
    print("Termino de sacar los files de los reviews")
    # locate = filedialog.askdirectory()
    cont = 0
    while cont<cantidadDocumentos:
        path = "C:/Users/Armando/Documents/Primer Semestre 2018/Analisis/Progra#3/Datos/Reviews/"+str(cont)+".txt"
        sacarTF(path, cont)
        cont= cont+1
    #for x in ficheros:
     #   sacarTF(x, cont)
      #  cont = cont + 1
    print("Termino de sacar TF")
    file_path="C:/Users/Armando/Documents/Primer Semestre 2018/Analisis/Progra#3/Datos/Diccionario/"
    print("Saco los files de los diccionarios")
    goal_path="C:/Users/Armando/Documents/Primer Semestre 2018/Analisis/Progra#3/Datos/TF-IDF"
    diccionario=ficherosEnDir(file_path)
    total_files=22000000
    for x in diccionario:
        calculateIDF(x, goal_path, total_files)
    print("Termino de sacar los TFIDF")
def separarJson():
    ManejoArchivos.jsonToTxt(
        "C:/Users/Armando/Documents/Primer Semestre 2018/Analisis/Progra#3/Datos/Datos/reviews_Books.json",
        "C:/Users/Armando/Documents/Primer Semestre 2018/Analisis/Progra#3/Datos/Reviews/")


def verificar(usu, cont):
    if usu == "admin" and cont == "admin":
        # --------------------------VentanaAdministrador---------------------------------
        ventanaAdm = Tk()
        ventanaAdm.title("Administrador")
        ventanaAdm.resizable(FALSE, FALSE)
        ventanaAdm.geometry("260x200+650+250")
        ventanaAdm.configure(background='white')
        # --------------------------Botones---------------------------------
        btnCambiarSet = Button(ventanaAdm, text="Cambiar", command=lambda: cambiarSetDatos(ventanaAdm)).place(x=160,
                                                                                                              y=40)
        btnIndexar = Button(ventanaAdm, text="Indexar", command=indexarArchivos).place(x=160, y=80)
        btnSepararJson = Button(ventanaAdm, text="Separar", command=separarJson).place(x=160, y=120)
        # --------------------------Etiquetas---------------------------------
        setDatos = Label(ventanaAdm, text="Set de datos").place(x=30, y=40)
        indexar = Label(ventanaAdm, text="Indexar nuevos datos").place(x=30, y=80)
        separar = Label(ventanaAdm, text="Separar Json").place(x=30, y=120)
        nombreSetDstos = Label(ventanaAdm, text="Set de datos actual:" + NomDatos).place(x=10, y=150)
    else:
        tkinter.messagebox.showerror("Error", "Error al iniciar")


def administrador():
    # --------------------------VentanaAutenticar---------------------------------
    ventanaVer = Tk()
    ventanaVer.title("Verificacion")
    ventanaVer.resizable(FALSE, FALSE)
    ventanaVer.geometry("260x160+600+200")
    ventanaVer.configure(background='white')
    # --------------------------Entradas de texto---------------------------------
    usu = StringVar()
    cont = StringVar()
    txtUsuario = Entry(ventanaVer, textvariable=usu, width=20).place(x=100, y=20)
    txtContrasenna = Entry(ventanaVer, textvariable=cont, width=20, show="*").place(x=100, y=60)
    usu.set("admin")
    cont.set("admin")
    # --------------------------Botones---------------------------------
    btnVerificar = Button(ventanaVer, text="Verificar",
                          command=lambda: (verificar(usu.get(), cont.get()), ventanaVer.destroy())).place(x=120, y=100)

    # --------------------------Etiquetas---------------------------------
    usuario = Label(ventanaVer, text="Usuario").place(x=20, y=20)
    contrasenna = Label(ventanaVer, text="Contraseña").place(x=20, y=60)


# Funciones para quitar basura de los textos
def tokenizar(ruta, cont):
    lista = []
    path = ruta
    archivo = open(path, 'r')
    texto = archivo.readline().lower()
    prueba = nltk.word_tokenize(texto)
    for x in prueba:
        if x != "," and x != "reviewerID" and x != "reviewerName" and x != "reviewText" and x != "asin" and x != "helpful" and x != "overall" and x != "summary" and x != "unixReviewTime" and x != "reviewTime" and x != "{" and x != "``" and x != "''" and x != ":" and x != "@" and x != "[" and x != "]" and x != "(" and x != "." and x != "," and x != "..." and x != ";" and x != "&" and x != ")" and x != "}":
            lista.append(x.split(" "))
    texto = ""
    pos = 0
    for x in lista:
        for y in x:
            if pos == 0:
                texto = texto + y
                pos = 1
            else:
                texto = texto + "," + y
    name = "C:/Users/Armando/Documents/Primer Semestre 2018/Analisis/Progra#3/Datos/Tokenizar/" + str(cont) + ".txt"
    file = open(name, "w")
    file.write(texto)
    file.close()
    ruta = "C:/Users/Armando/Documents/Primer Semestre 2018/Analisis/Progra#3/Datos/Rutas/" + str(cont) + ".txt"
    file = open(ruta, "w")
    file.write(path)
    file.close()
    archivo.close()
def quitarCaracteres(lista):
    bandera = False
    listaSinCaracteres=[]
    listaCarac = ['/', '', '?', '<', '>', '-', '.', ',', '¿', '"', ')', '(', ';', ':', '*', '+', '-', ' ', '#', '!', '¿',
             '%', '&', '^', '`', "'", "]", "[", "{", "}", "$", "_", "@", "~", "=",'1','2','3','4','5','6','7','8','9','0']
    listaProhibida = ['\n', '', ' ', 'and', 'this','the']
    for x in lista:
        elemento = ""
        for w in x:
            if w not in listaCarac:
                elemento = elemento + w
        try:
            numero = int(elemento)
            elemento = ""
        except:
            pass
        if elemento.__len__()!=1 and elemento.__len__()!=2:
            if elemento not in listaProhibida:
                if bandera:
                    listaSinCaracteres.append(elemento)
                else:
                    bandera=True
    return listaSinCaracteres

def sacarTF(x, cont):
    locate = "C:/Users/Armando/Documents/Primer Semestre 2018/Analisis/Progra#3/Datos/Diccionario/"
    temp = []
    archivo = open(x, 'r')
    texto = archivo.readline().lower()
    texto = texto[1:].split(" ")
    lista=quitarCaracteres(texto)
    archivo.close()
    for y in lista:
        if temp.count(y) == 0:
            #print(y)
            temp.append(y)
            #print("Este es el len nuevo" + str(lista.__len__()))
            cantidad = lista.count(y) / lista.__len__()
            ubicacion=''
            ubicacion = locate + str(y) + ".txt"
            #print(ubicacion)
            if os.path.exists(ubicacion):
                try:
                    palabra = open(ubicacion, 'a')
                    palabra.write("\n" + str(cont) + "," + str(cantidad) + "," + x)
                    palabra.close()
                    ubicacion = ''
                except:
                    pass
            else:
                try:
                    palabra = open(ubicacion, 'a')
                    palabra.write(y)
                    palabra.write("\n" + str(cont) + "," + str(cantidad) + "," + x)
                    palabra.close()
                    ubicacion = ''
                except:
                    pass
#file_path is the path of the file which you are calculating the idf(is a word or element)
#goal_path is the path where do you will put the td-idf of all the words from a text file
#count represents a different file with all the td_idf
#total_files is the total number of documents
def calculateIDF(file_path, goal_path,total_files):
    print("Entro a calcular idf")
    file = open(file_path,"r")
    count = 0 #represents the total of txt files where the word is in
    bandera = False
    temporal_list = []
    palabra=""
    bandera=False
    line = file.readline()
    palabra = line[0:-1]
    while line !="":
        line = file.readline()
        if line != "":
            count += 1
    file.close()
    file = open(file_path, "r")
    line = file.readline()
    while line != "":
        line = file.readline()
        if line != "":
            temporal_list = line.split(",")
            file_name = temporal_list[0]
            temporal_tf = temporal_list[1]
            tf = float(temporal_tf)
            tf_idf = tf * -math.log((count + 1) / total_files)
            if os.path.exists(goal_path+"/"+file_name+".txt"):
                overwrite_file = open(goal_path+"/"+file_name+".txt", "a")
                overwrite_file.write("\n"+palabra+","+str(tf_idf))
                overwrite_file.close()
            else:
                write_file = open(goal_path + "/" + file_name + ".txt", "a")
                write_file.write(temporal_list[2])
                write_file.write("\n"+palabra+","+str(tf_idf))
                write_file.close()
    file.close()


def ventanaPrincipal():
    # --------------------------VentanaPrincipal---------------------------------
    ventana = Tk()
    ventana.title("Principal")
    ventana.resizable(FALSE, FALSE)
    #ventana.geometry("1200x600+250+100")
    ventana.config(bg="white")
    #ventana.attributes("-fullscreen", True)

    # --------------------------Imagenes---------------------------------
    imagen1 = PhotoImage(file="C:/Users/Armando/Documents/Primer Semestre 2018/Analisis/Progra#3/Imagenes/Google1.png")
    imagen2 = PhotoImage(file="C:/Users/Armando/Documents/Primer Semestre 2018/Analisis/Progra#3/Imagenes/Google2.png")
    imagen3 = PhotoImage(file="C:/Users/Armando/Documents/Primer Semestre 2018/Analisis/Progra#3/Imagenes/Google3.png")
    imagen4 = PhotoImage(file="C:/Users/Armando/Documents/Primer Semestre 2018/Analisis/Progra#3/Imagenes/Google4.png")
    imagen5 = PhotoImage(file="C:/Users/Armando/Documents/Primer Semestre 2018/Analisis/Progra#3/Imagenes/Google5.png")
    imagen6 = PhotoImage(file="C:/Users/Armando/Documents/Primer Semestre 2018/Analisis/Progra#3/Imagenes/Google6.png")
    imagen7 = PhotoImage(file="C:/Users/Armando/Documents/Primer Semestre 2018/Analisis/Progra#3/Imagenes/Google7.png")
    imagen8 = PhotoImage(file="C:/Users/Armando/Documents/Primer Semestre 2018/Analisis/Progra#3/Imagenes/Google8.png")
    # --------------------------Menu---------------------------------
    menubarra = Menu(ventana)
    menubarra.add_command(label="Administrador", command=administrador)
    menubarra.add_command(label="Salir", command=ventana.destroy)
    ventana.config(menu=menubarra)

    # --------------------------Etiquetas---------------------------------
    lista=[imagen1,imagen2,imagen3,imagen4,imagen5,imagen6,imagen7,imagen8]
    numero=random.randint(0, 7)
    etiqueta = Label(ventana, image=lista[numero]).pack()


    # --------------------------Entradas de texto---------------------------------
    entrada = StringVar()
    cantidad = IntVar()
    txtBuscar = Entry(ventana, textvariable=entrada, width=70).place(x=580, y=570)
    txtCantidad = Entry(ventana, textvariable=cantidad, width=4).place(x=820, y=620)
    ventana.bind("<Return>",lambda event: (ventana.destroy(),buscar(entrada.get(), cantidad.get())))

    # --------------------------Botones---------------------------------
    btnBuscar = Button(ventana, text="Buscar",command=lambda: (ventana.destroy(),buscar(entrada.get(), cantidad.get())), width=20).place(x=640, y=620)
    ventana.mainloop()
ventanaPrincipal()