import random
import sys

n= int(sys.stdin.readline().strip())
n_frames=int(sys.stdin.readline().strip())

refernce_string=[]


lru_opti = []
n_faults_opti = 0

for i in range(n):
	num=random.randrange(10)
	refernce_string.append(num)

#print (refernce_string)


#Optimo
for i in xrange(len(refernce_string)):

	quitados=[]
	for j in xrange(len(lru_opti)):
		if refernce_string[i] == lru_opti[j]:
			break
			
	else:
		if len(lru_opti)<n_frames:
			lru_opti.append(refernce_string[i])
		else:
			for o in xrange(i+1,len(refernce_string)):
				if refernce_string[o] in lru_opti and refernce_string[o] not in quitados:
					quitados.append(refernce_string[o])


			if len(quitados)==0:
				lru_opti[0]=refernce_string[i]
			
			elif len(quitados)<len(lru_opti):
				for m in lru_opti:
					if m not in quitados:
						victi=m
						break
				for m in xrange(len(lru_opti)):
					if lru_opti[m] ==victi:
						lru_opti[m]=refernce_string[i]
			else:	
				for m in xrange(len(lru_opti)):
					if lru_opti[m] == quitados[len(quitados)-1]:
						lru_opti[m]=refernce_string[i]
						break
		
		n_faults_opti += 1	


#FIFO
fifo = []
n_faults_fifo = 0

for i in refernce_string:
	
	for x in fifo:
		if x == i:
			break	
	else:
		#print ("no esta")
		if len(fifo)<n_frames:
			fifo.append(i)
		else:
			fifo.pop(0)
			fifo.append(i)
		n_faults_fifo += 1		




#LRU

lru = []
n_faults_lru = 0

for i in refernce_string:
	for j in lru:
		if i == j:
			lru.remove(i)
			lru.append(i)
			break
	else:
		if len(lru)<n_frames:
			lru.append(i)
		else:
			lru.pop(0)
			lru.append(i)
		n_faults_lru += 1	

print "numero de fallos LRU: "+ str(n_faults_lru)	
print "numero de fallos FIFO: "+ str(n_faults_fifo)
print "numero de fallos Optimo: "+ str(n_faults_opti)
