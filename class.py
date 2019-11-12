class MyClass:

	def __init__(self):
		self.name = "Pierre"
		self.taille = 50

  def exemple_docstring():
	  '''Ceci est ma ma premiere methode'''
	  pass

>>>help(exemple_docstring)

exemple_docstring.doc


class Bank:

	def __init__(self):
		''' Initialisation du nom et de la balance'''
		
		self.nom = ""
		self.balance = 0

client_01 = Bank()
client_01.nom = "Pierre"
client_01.balance = 10

print(client_01.nom)
print(client_01.balance)


class Bank:

	def __init__(self, nom, balance):
		''' Initialisation du nom et de la balance'''
		
		self.nom = nom
		self.balance = balance

client_01 = Bank("Arnold", 15)

print(client_01.nom)
print(client_01.balance)

class Bank:

	def __init__(self, nom, balance):
		''' Initialisation du nom et de la balance'''
		
		self.nom = nom
		self.balance = balance

client_01 = Bank("Arnold", 15)

print(client_01.nom)
print(client_01.balance)



class Bank:

	def __init__(self):
		''' Initialisation du nom et de la balance'''
		
		self.nom = ""
		self.balance = 0

	def ajouter_argent(self, montant):
		self.balance += montant 
		print(f"Vous avez ajouté {montant} au compte en banque de {self.nom}")


	def retirer_argent(self, montant):
		self.balance -= montant 
		print("Vous avez retiré {0} $ au compte en banque de {1}".format(montant, self.nom))


	def afficher_balance():
		print(f"{self.name} a {self.balance} $ dans son compte en banque")

client_01 = Bank()
client_01.nom = 'Pierre'
client_01.ajouter_argent(50)
client_01.afficher_balance()

client_02 = Bank()
client_02.nom = 'Paul'
client_02.ajouter_argent(100)

client_03 = Bank()
client_03.nom = 'Jacques'
client_03.ajouter_argent(50000)
