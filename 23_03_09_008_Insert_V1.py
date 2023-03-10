# Jonatan Sanchez Ibarra 20310417

#Añade a la siguiente lista los colores 'magenta' y 'turquesa' utilizando insert(). Tendrás que posicionar 'magenta' en la posición siguiente a la de 'lila' y 'turquesa' en la penúltima posición. Deberás hacer esto utilizando posiciones de lista negativas.

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #Lista de colores

colores.insert(-4,"magenta") #Se agrega el color magenta en la posicion 4, contando del final hacia el inicio
colores.insert(-1,"turquesa") #Se Agrega el color turquesa en la posicion penultima
print(colores) #Se imprime la lista de colores
