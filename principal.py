#principal

from paquete.modelado import *		# Importamos el achivo .py dónde se encuentran todas las clases creadas	
import msvcrt   # Importamos una clase que la usaremos al final del código

# Creamos los diferentes objetos enviándoles como argumentro el 'nombre'
futbolista = Futbolista("Antonio")			
medico = Medico_Equipo("Ramon")				
presidente = Presidente_Equipo("Francisco") 	
entrenador = Entrenador("Jose")				

# Los metemos dentro de una lista
lista = [futbolista, medico, presidente, entrenador]	

# Presentamos la lista				
for i in lista:						
	i.entrenar()			


msvcrt.getch() # Simulamos el 'pause' antes de finalizar el programa 