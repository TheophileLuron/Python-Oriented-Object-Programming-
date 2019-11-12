First python files  / mon_script.py
Second python files / mon_modules.py
Third python files / __init__.py 

mon_modules.py 

def table_de_multiplication(nombre):
	return nombre * 5
  
  

mon_script.py


import mon_modules

ma_variable = mon_modules.table_de_multiplication(3)

print(ma_variable)


import mon_modules as mod

ma_variable = mod.table_de_multiplication(3)

print(ma_variable)


from mon_modules import table_de_multiplication as tm

ma_variable = tm(3)

print(ma_variable)
