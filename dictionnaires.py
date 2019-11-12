mon_dictionnaires = {"Pierre":50, 'Jacques':50000, 'Paul':100}


for i in mon_dictionnaires:
	print(i)
	print(mon_dictionnaires[i])

for i in mon_dictionnaires.keys():
	print(i)

for i in mon_dictionnaires.values():
	print(i)

for key, value in mon_dictionnaires.items():
	print(key)
	print(value)

mon_dictionnaires = {}

mon_dictionnaires['Pierre'] = 50

print(mon_dictionnaires['Pierre'])
