
import abc  # Importamos el método para poder hacer una clase abstracta

# Creamos la clase abstracta
class Persona_Equipo(metaclass = abc.ABCMeta):	 

	# Creamos constructor de la clase abstracta
	def __init__(self, nombre):						
		self.nombre = nombre 					

	@abc.abstractmethod	# Con esta linea indicamos que el siguiente método es abstracto
	def entrenar(self):				
		pass

	# Método set del argumento nombre
	def agregar_nombre(self, nombre):				
		self.nombre = nombre

	# Método get del argumento nombre
	def obtener_nombre(self):						
		return self.nombre


# Clase hija
class Entrenador(Persona_Equipo):				

	# Creamos constructor
	def __init__(self,n):						
		super(Entrenador, self).__init__(n)			
		self.codigo_entrenador = ""			

	# Método set
	def agregar_codigo_entrenador(self, codigo_entrenador):
		self.codigo_entrenador = codigo_entrenador

	# Método get
	def obtener_codigo_entrenador(self):				
		return self.codigo_entrenador

	# Sobreescribimos el método abstracto de la clase padre
	def entrenar(self):						
		print("Yo %s, Entrenador, soy el director del entrenamiento " % (self.obtener_nombre()))


# Clase hija
class Futbolista(Persona_Equipo):			

	# Creamos constructor
	def __init__(self,n):					
		super(Futbolista, self).__init__(n)			
		self.posircion_campo = ""				

	# Método set
	def agregar_posicion_campo(self, posircion_campo):	
		self.posircion_campo = posircion_campo

	# Método get
	def obtner_posicion_campo(self):					
		return self.posircion_campo

	# Sobreescribimos el método abstracto de la clase padre
	def entrenar(self):						
		print("Yo %s, Futbolista, hago Practica en el entrenamiento " % (self.obtener_nombre()))


# Clase hija
class Presidente_Equipo(Persona_Equipo):				

	# Creamos constructor
	def __init__(self,n):					
		super(Presidente_Equipo, self).__init__(n)
		self.numero_propiedades = ""				

	# Método set
	def agregar_numero_propiedades(self, numero_propiedades):		
		self.numero_propiedades = numero_propiedades

	# Método get
	def obtener_numero_propiedades(self):			
		return self.numero_propiedades

	# Sobreescribimos el método abstracto de la clase padre
	def entrenar(self):					
		print("Yo %s, Presidente, Pongo dinero para el entrenamiento" % (self.obtener_nombre()))


# Clase hija
class Medico_Equipo(Persona_Equipo):		

	# Creamos constructor
	def __init__(self,n):											
		super(Medico_Equipo, self).__init__(n)		
		self.titulo = ""					

	# Método set
	def agregar_Titulo(self,titulo):
		self.titulo = titulo

	# Método get
	def obtener_titulo(self):					
		return self.titulo

	# Sobreescribimos el método abstracto de la clase padre
	def entrenar(self):						
		print("Yo %s, Medico, atiendo a los jugadores del entrenamiento " % (self.obtener_nombre()))


