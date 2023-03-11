# Jonatan Sanchez Ibarra 20310417

#Al siguiente código añádele un par de rangos de edad. Uno de 18 años hasta 45 y otro de más de 100 años hasta 120.
edad = int(input('¿Cuál es tu edad?\n')) #Se pregunta al usuario la edad y se guarda en una variable
if edad <= 0: #Si tiene menos o 0 anios, se ejecuta el if
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 18: #Si tiene 1 anio o mas, y 18 o menos se ejecuta el if
	print('Eres menor de edad.')
elif edad >18 and edad <=45: #Si tiene mas de 18 anios y menos o igual a 45, se ejecuta el if
	print("Estas en la juventud")
elif edad > 45 and edad <= 100: #Si tiene mas de 45 anios y menos o igual a 100, se ejecuta el if
	print('Eres un adulto.')
elif edad > 100 and edad <= 120:# Si tiene mas de 100 anios y menos o igual a 120, se ejecuta el if
	print("Has tenido una larga vida")
else:
	print('Edad no válida.') #Si no cumple con ninguna condicion, se ejecuta esta linea de codigo
	

    