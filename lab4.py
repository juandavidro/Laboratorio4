import sys 
import math

tamano_p=int(sys.stdin.readline())
direccion=int(sys.stdin.readline())

cadena=bin(direccion)

n = int(float(math.log(tamano_p,2)))
m = int(math.ceil(math.log(direccion,2)))

num_p= m^n
pagina=""
num_pOut=""
corrimiento=""

for i in range(2,num_p+2):
	num_pOut+=cadena[i]
#print n
for i in range(2+len(num_pOut),n+2+len(num_pOut)):
	corrimiento+=cadena[i]

'''
print cadena	
print num_pOut
print corrimiento
print int(corrimiento,2)
'''

print ("La dirección " , str(direccion)," corresponde a:")
print ("número de página = ",str(int((num_pOut),2)))
print ("corrimiento = ",str(int(corrimiento,2)))