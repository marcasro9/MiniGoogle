import numpy as np
import math
import re
import os.path

def retornarTF_IDF(consulta,total_documentos):##realiza el tf-idf de la consulta, necesario para el cosine similarity
    consulta = consulta.strip(".")
    consulta = consulta.strip(",")
    consulta = consulta.strip(":")
    recorrer = consulta.split(" ")
    temp = []
    valores = []
    for i in recorrer:
        if i.lower() not in temp:
            tf = recorrer.count(i.lower()) / len(recorrer)
            temp.append(i.lower())
            tf_idf = tf * retornaIDF(i.lower(), total_documentos)
            valores.append(tf_idf)
    return valores

def correccionQuery(consulta):
    consulta = consulta.strip(".")
    consulta = consulta.strip(",")
    consulta = consulta.strip(":")
    recorrer = consulta.split(" ")
    temp = []
    for i in recorrer:
        if i.lower() not in temp:
            temp.append(i.lower())
    return temp


def retornaIDF(palabra,total_documentos):
    path = "C:/Users/Armando/Documents/Primer Semestre 2018/Analisis/Progra#3/Datos/Diccionario/"#busca en el diccionario de palabras y cuenta si en el dataset existen documentos con esa
    path += palabra +".txt"#palabra y aplica la fórmula del idf y retorna el valor
    if os.path.exists(path):
        count = 0
        archivo = open(path,"r")
        for i in archivo.readlines():
            if i != "\n":
                count += 1
        archivo.close()
        return -math.log(count / total_documentos)
    else:
        return -math.log(1/total_documentos)#si no existe esa palabra en el dataset se normaliza

def function(path,query,total_documentos):
    archivo1 = open(path, "r")#abre un text con los tf-idf de una review
    listaUnoP = []
    valoresArchivo =[]
    consulta = correccionQuery(query)
    valoresQuery = []
    valoresQuery = retornarTF_IDF(query, total_documentos)
    count = False
    path1 = ""
    for linea in archivo1.readlines():
        if (count):
            if(linea != '\n'):
                temp = linea.split(",")
                temp_tf_idf = float(re.search(r'\d+.\d+', temp[1][0:-1]).group())
                listaUnoP.append(temp[0])
                valoresArchivo.append(temp_tf_idf)
        else:
            path1 = linea
            count = True
    archivo1.close()
    queryNuevo=[]
    valoresQueryNuevo=[]
    posQuery=0
    for x in consulta:
        if x not in listaUnoP:
            listaUnoP.append(x)
            valoresArchivo.append(0)
            posQuery+=1
        posQuery += 1
    posQuery2=0
    for x in listaUnoP:
        if x not in queryNuevo and x not in consulta:
            queryNuevo.append(x)
            valoresQueryNuevo.append(0)
        else:
            for y in consulta:
                if x == y:
                    queryNuevo.append(y)
                    valoresQueryNuevo.append(valoresQuery[posQuery2])
                    posQuery2+=1

    a = np.array(valoresArchivo)
    b = np.array(valoresQueryNuevo)
    c = np.array(listaUnoP)
    d = np.array(queryNuevo)
    #print(a)
    #print(c)
    #print(b)
    #print(d)
    valor_punto = np.dot(a, b)
    sumA = sum(math.pow(i,2) for i in a)
    sumB = sum(math.pow(j,2) for j in b)
    resultado = valor_punto/((math.sqrt(sumA)) * math.sqrt(sumB))
    valor_resultado = []
    valor_resultado.append(path1[0:-1])
    valor_resultado.append(resultado)
    return valor_resultado