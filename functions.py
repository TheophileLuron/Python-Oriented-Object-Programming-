def printer_0(texte, nombre):
	print(texte)
	print(nombre)

printer_0("Bonjour", 0)
printer_0("Bonsoir", 1)
printer_0("Au revoir", 2)


def printer(texte="Bonjour", nombre=3):
	print(texte)
	print(nombre)

printer()


def table_de_multiplication(nombre):
	for i in range(10):
		print("{0} * {1} = {2}".format(i, nombre, i * nombre))

table_de_multiplication(5)


def table_de_multiplication(nombre):
	return nombre * 5

ma_variable = table_de_multiplication(5)
print(ma_variable)
