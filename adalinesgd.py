importar numpy como np 

de numpy. semilla de importación aleatoria

clase AdalineSGD(object):

	""" Clasificador ADAptive LInear NEuron.
 Parámetros
	-----------
 eta : flotador
 Tasa de aprendizaje (entre 0,0 y 1,0)
	n_iter : int
 Pasa por encima del conjunto de datos de entrenamiento.
 Atributos
	-----------
	w_ : 1d-array
 Pesas después del montaje.
 errors_ : lista
 Número de clasificaciones erróneas en cada época.
 shuffle : bool (sordo: Verdadero)
 Baraja los datos de entrenamiento en cada época si es verdadero 
 para prevenir ciclos.
 random_state : int (valor predeterminado: Ninguno)
 Establecer un estado aleatorio para barajar y 
 inicializando los pesos.
	"""

	def __init__(self, eta = 0.01, n_iter = 10, shuffle= True,
				random_state = Ninguno):

		yo mismo. eta = eta
		yo mismo. n_iter = n_iter
		yo mismo. w_initialization = Falso
		yo mismo. shuffle = shuffle

		si random_state:
			semilla(random_state)

	def fit(self, X, y):

		""" Datos de entrenamiento de ajuste.
 Parámetros
		------------
		X : {array-like}, shape = [n_samples, n_features]
 Vectores de entrenamiento, donde n_samples es el
 número de muestras y n_features es el número
 de características.
		y : array-like, shape = [n_samples]
 Valores objetivo.
 Devolución
		-------
 self : objeto
		"""

		yo mismo. _initialize_weights(X. forma[1])
		yo mismo. cost_ = []

		para i en rango(self. n_iter):

			si es uno mismo. barajar:
				X, y = yo. _shuffle(X, y)

			costar = []
			para xi, objetivo en zip(X, y):
				costo. apéndice (sí mismo. _update_weights(xi, objetivo))

			avg_cost = suma(costo) / len(y)
			yo mismo. cost_. apéndice(avg_cost)

		devolverse a sí mismo

	def partial_fit(self, X, y):

		""" Ajustar los datos de entrenamiento sin reinicializar los pesos """

		si no es uno mismo. w_initialized:
			yo mismo. _initialize_weights(X. forma[1])

		si es y. ravel(). forma[0] > 1:

			para xi, objetivo en zip(X, y):
				yo mismo. _update_weights(xi, objetivo)
		de lo contrario:
			yo mismo. _update_weights(X, y)

		devolverse a sí mismo

	def _shuffle(self, X, y):

		""" Mezclar datos de entrenamiento """

		r = np. aleatorio. permutación(len(y))

		return X[r], y[r]

	def _initialize_weights(self, m):

		""" Inicializar pesos a ceros """

		yo mismo. w_ = np. ceros (1 + m)
		yo mismo. w_initialized = Verdadero

	def _update_weights(self, xi, target):

		""" Aplicar la regla de aprendizaje Adaline para actualizar los pesos """

		output = yo. net_input(xi))
		error = (destino - salida)
		yo mismo. w_[1:] += yo. eta * xi. punto(error)
		yo mismo. w_[0] += yo. eta * error
		costo = 0.5 * (error ** 2)

		costo de devolución

	def net_input(self, X):

		""" Calcular la entrada neta """

		devolver np. punto(X, yo. w_[1:]) + yo. w_[0]

	activación def(self, X):

		""" Activar lineal de cómputo """

		volver a sí mismo. net_input(X)

	def predict(self, X):

		""" Etiqueta de clase de retorno después del paso de la unidad """

		devolver np. donde(sí mismo. activación(X) >= 0.0, 1, -1)
