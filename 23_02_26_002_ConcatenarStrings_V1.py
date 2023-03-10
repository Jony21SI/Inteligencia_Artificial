""" Jonatan Sanchez Ibarra 20310417 """

mensaje = "Hola " + "mundo" #Se Concatenan las strings
print(mensaje) #Se imprimen las variables concatenadas

frase = "Hoy no " #Frase 1
frase2 = "me voy a bañar" #Frase 2
frase_final = frase + frase2 #Se concatenan las variables
print(frase_final) #Se imprimen las variables concatenadas

print("Hoy no,",frase2) #Dentro del print se pueden concatenar strings guardadas en variables y texto directo

nombre = "Jonatan " #Se guarda el nombre
apellido = "Sanchez " #Se guarda el apellido
apellido_2 = "Ibarra" #Se guarda el apellido
nombre_completo = nombre + apellido + apellido_2 #Se concatenan las 3 variables anteriores en una sola
print(nombre_completo) #Se imprimen las variables concatenadas

print("45"+"20") #Se concatenan los numeros (Al tener comillas, no se suman, solo se concatenan como string)
