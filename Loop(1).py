### hagamos

x = int(input("el factorial de: "))

### mientras x se multiplica con (x-1) yx-1 con (x-2)ya así..
i=int(x)

while i-1 != 0:
  if x != 0: 
   print('The count is:', x)
   i = i-1  ## i empieza con el valor de x y reduce hasta cero
   x = x*i 
  else:
   x = 1
   print('The count is:', x)
	
print("acabamos")

###este lenguaje comprende como miembros de un proceso dependientdo
###de las indentaciones




