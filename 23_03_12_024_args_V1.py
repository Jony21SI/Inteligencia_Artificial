# Jonatan Sanchez Ibarra 20310417

#¿Cuántos argumentos se utilizan en cada una de estas llamadas?
def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo') #4
colores('lila', 'negro', 'rojo') #3
colores('rosa') #1
colores('marrón', 'naranja') #2


#Completa el siguiente fragmento de código:
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores("azul","rojo")

#Crea una función que realice la suma de cinco números utilizando solo *args. Debes imprimir el resultado en la consola. La suma no se realizará directamente sobre el print().

def suma(*args):
    resultado=args[0]+args[1]+args[2]+args[3]+args[4]
    print ("El resultado de la suma es: ",resultado)

suma(2,12,70,5,43)
	