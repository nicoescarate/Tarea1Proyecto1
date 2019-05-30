#Tarea
#definicion de variables
a=5 #hipotenusa
b=3 #cateto
c=2 #catetp
r=4 #radio
listaPeriodismo=[]
listaIngenieria=[]
lista = [['Analia',0],['Joaquin',1]] 

def nombre():                                           #definicion de la funcion 
    print('Mi nombre es:','Joaquin Araya Santander')    #funcion predeterminada para escribir en consola de python 
    

def areaTriangulo(x,y,z):                   #definicion de la funcion
    area=(z+y)                              #formula para calcular area de un traingulo rectangulo ((cateto1+cateto2)/2)
    if (z+y)>x and (x+y)>z and (z+x)>y :    #desigualdad triangular
        print('El area del triangulo es:')  #funcioon predeterminada para escribir en la consola de python
        return area                         #lo que entrega la funcion
    else:                                   
        print('El trinagulo no es viable')  #funcion predeterminada para escribir en la consolade pythonare

def areaCirculo(x):                    #definicion de la funcion
    areaC=x^2*3,14/2                   #formula para calcular el area de un circulo
    print('El area del circulo es:')   #funcion predeterminada para escrinbir en la consola de python
    return areaC                       #lo que entrega la funcion 


def separacionListas(x):
    for i in lista:
        if i[1] == 1:
            listaPeriodismo.append(i)
        if i[1] == 0:
            listaIngenieria.append(i)
        return listaPeriodismo
        return listaIngenieria
            
