# Jonatan Sanchez Ibarra 20310417

#Itera el diccionario teclado1 con un solo bucle for que muestre esto en la consola:
"""
Categoría = Teclados.
Modelo = HyperX Alloy FPS Pro.
Precio = 89,99.
"""

teclado1 = {            #Diccionario de Teclado
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

for x in teclado1: #Se va iterando todo el diccionario
    print(x,":",teclado1[x]) #Se imprime primero la clave del diccionario y despues el valor de esa clave
