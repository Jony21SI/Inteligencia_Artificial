# Jonatan Sanchez Ibarra 20310417
"""Haz una tupla que contenga cuatro colores de tu elección. Tendrás que poner una condición con el condicional if para cada color que 
le avise al usuario que el color está en la tupla 
con un mensaje como este: print('El color rojo está admitido') y una condición False para contemplar cualquier color que no esté en la tupla 
con un mensaje como este: print('Color no admitido'). No puedes utilizar el operador ==. Además tendrás que hacer esto con un input() que permita introducir un color al usuario."""

colores = ("rojo","verde","azul","rosa") #Tupla de 4 colores
color = input("Escriba un color: ").lower() #Se pide al usuario un color, se pasa a minusculas para compararlo posteriormente y se guarda en una variable
if color in colores: #Si el valor introducido por el usuario se encuentra en la tupla, la condicion se vuelve verdadera y se imprime el mensaje
    print("Este color si esta admitido") 
else: #En cambio, si no se encuenta en la tupla, se ejecuta la siguiente instruccion
    print("Este color no esta admitido")
