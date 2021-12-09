print(" ")
print("calcula factorial o suma (F/S)") ##suma de naturales o factorial?

s = str(input())  #respuesta

## separamos casos

if s == "F":

	z = int(input("el factorial de: "))

### mientras x se multiplica con (x-1) yx-1 con (x-2)ya así..
	i=int(z)
	while i-1 != 0:
	  if z != 0: 
	   i = i-1  ## i empieza con el valor de x y reduce hasta cero
	   z = z*i 
	  else:
	   z = 1
	print(" ")
	print("   ",z)

elif s == "S": ##calcula la suma de los numeros de 0 -> y 
	j=0
	y = int(input("La suma de los naturales hasta... :"))
	start = 0
	stop = y	
	step = 1
	stop += step
	
	for x in range(start,stop,step):
		j += x
	print("     ",j)
print(" ")
print("      acabamos")

###este lenguaje comprende como miembros de un proceso dependientdo
###de las indentaciones




