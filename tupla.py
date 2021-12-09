x =(1,2,3) ##las tuplas no se pueden reasignar, son inmutables

y = tuple((1,2,3)) ##tuplas de un solo elemento son de tipo int

print(y)

## print(dir(x)) 

print(x[2])

##podemos eliminar una tupla con la funcion del

del y

# print(y) -> error

#podemos agrupar datos

P = {
	(1,2): "coordenadas cartesianas",
	(2.23,60): "coordenadas polares"
}
print(P)





