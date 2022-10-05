import pdb
pdb.set_trace()

listado=[[2,4,1],[1,2,3,4,5,6,7,8],[100,250,43]]
print(f"Nuestra lista de listas es:\n{listado}\n")
maximos=list(map(lambda x: max(x), listado))
print (f"Los números mayores en cada lista de listas son: {maximos}\n")


lista= [3, 4, 8, 5, 5, 22, 13]
print(f"La lista que tenemos es: {lista}")
primos=list(filter(lambda x: x%2!=0, lista))
print(f"Los números primos de la lista son: {primos}")