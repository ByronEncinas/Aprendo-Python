lista = [1,'yolo',False,[5,3,6]] ##puede contener diferentes tipos de datos

print(lista)

color = ["rojo","verde","amarillo"]

print(color[2]) ##elemento 2 de la lista

print("naranja" in color) ##existencia de cierto elemento en la lista

r = list(range(1,11)) ## funcion range ubica numeros enteros en un rango de [a,b-1]

print(r)

##las listas pueden ser cambiadas

r[4] = "caca"

print(r)

## print(dir(color))

color.append('cafe')

print(color)

color.extend(('azul','blanco'))

print(color)

color.insert(1,'negro') ##inserta en la posicion 1

print(color)

color.pop() ##remueve el ultimo elemento de la lista

print(color)

color.remove('rojo')##remueve elemento pedido

print(color)

color.pop(4) ## elimina el elemento numero 4

color.sort() ## en orden alfabetico A - Z

print(color)

color.sort(reverse=True) ## de Z-A

print(color)

color.insert(1,'rojo')
color.insert(1,'rojo')

print(color)

print(color.count('rojo'))
