importar numpy como np
importar matplotlib. pyplot como plt 

de matplotlib. importar colores  ListadoColormap

""" Función para colorear las regiones de deciosión """

def plot_decision_regions(X, y, clasificador, resolución = 0.02):

	# generador de marcadores de configuración y mapa de color

	marcadores = ('s', 'x', 'o', '^', 'v')
	colores = ('rojo', 'azul', 'verde claro', 'gris', 'cian')
	cmap = ListedColormap(colors[ : len(np. único(y))])

	# trazar la superficie de decisión

	x1_min, x1_max = X[:, 0]. min() - 1, X[:, 0]. max() + 1
	x2_min, x2_max = X[:, 1]. min() - 1, X[:, 1]. max() + 1
	xx1, xx2 = np. meshgrid(np. arange(x1_min, x1_max, resolución),
		np. arange(x2_min, x2_max, resolución))

	z = clasificador. predecir(np. array([xx1. ravel(), xx2. ravel()]). T)
	Z = z. remodelación(xx1. forma)

	plt. contourf(xx1, xx2, Z, alfa = 0.4, cmap = cmap)
	plt. xlim(xx1. min(), xx1. máximo())
	plt. ylim(xx2. min(), xx2. máximo())

	# ejemplos de clase de parcela

	para idx, cl en enumerate(np. unique(y)):
		plt. scatter(x = X[y == cl, 0], y = X[y == cl, 1],
			alfa = 0,8, c = cmap(idx), marcador = marcadores[idx],
			etiqueta = cl)
