### caracteristicas de los datos strings

##que opciones tenemos? a ver...

Str = "dattosssss coon"

Str_2 = "ammorcito corazon, tengo tentacion..."

print(dir(Str))

print("")
print("")
 ## nos da opciones que podemos utilizar para modificar y

##trabajar con nuestra variable

print(Str.__add__("caca"))  ## escribe Str + el argumento = "datocaca" 

print(Str.upper()) ## todas mayus

print(Str.lower()) #todas minus

print(Str.replace("da","gati").upper()) # reemplaza "da" con "gati" y lo expresa en mayus

print(Str.count("s")) #cuenta numero de veces que aparece el caracter

print(Str.startswith("da")) #empieza ; termina .endswith("sssss")

print(Str.split()) ### separa elementos o grupos de una frase considerando el argumento

a = Str.split()

print(a) ##convierte Caracter en Lista!!!!!11

print(Str_2.split('a')) ## separa la frase entre las as

print(Str_2.find('o')) ##Ubica la posicion del caracter "o"

print(len(Str_2)) ##cuenta numero de letras en Str_2


print(Str_2.isalpha()) #Alfanumerico

print(Str_2.isdigit()) ##Responde TRUE O FALSE

print(Str_2[0] + Str_2[1] + Str_2[2])
print(Str_2[1])
print(Str_2[2])
print(Str_2[3])
print(Str_2[4])
print(Str_2[5])
print(Str_2[6])
print(Str_2[7])
print(Str_2[8])


print(Str_2[0] + Str_2[1] + Str_2[2] +Str_2[3] + Str_2[4]) ##concadenando caracteres

x = "Byron"

print("Mi nombre es {0}".format(x)) ##-Inserta x en el texto





