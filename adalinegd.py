importar numpy como np 

clase AdalineGD(objeto):

	"""Clasificador ADAptive LInear NEuron.
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
	"""

	def __init__(self, eta = 0.01, n_iter = 50):
		yo mismo. eta = eta
		yo mismo. n_iter = n_iter

	def fit(self, X, y):

		""" Datos de entrenamiento de ajuste.
 Parámetros
		-----------
		X : {array-like}, shape = [n_samples, n_features]
 Vectores de entrenamiento,
 donde n_samples es el número de muestras y
 n_features es el número de características.
		y : array-like, shape = [n_samples]
 Valores objetivo.
 Devolución
		-------
 self : objeto
		"""

		yo mismo. w_ = np. ceros(1 + X. forma[1])
		yo mismo. cost_ = []

		para i en rango(self. n_iter):
			output = yo. net_input(X)
			errores = (y - salida)
			yo mismo. w_[1:] += yo. eta * X. T. dot(errores))
			yo mismo. w_[0] += yo. eta * errores. suma()
			costo = (errores ** 2). suma() / 2.0
			yo mismo. cost_. append(costo))

		devolverse a sí mismo

	def net_input(self, X):

		""" Calcular la entrada neta """

		devolver np. punto(X, yo. w_[1:]) + yo. w_[0]

	activación def(self, X):

		""" Activar lineal de cómputo """

		volver a sí mismo. net_input(X)

	def predict(self, X):

		""" Etiqueta de clase de retorno después del paso de la unidad """

		devolver np. donde(sí mismo. activación(X) >= 0.0, 1, -1)
