import random
import sys

#n= int(sys.stdin.readline().strip())

refernce_string=[7,0,1,2,0,3,0,4,2,3,0,3,0,3,2,1,2,0,1,7,0,1]
lru = []
n_faults = 0
'''
for i in range(n):
	num=random.randrange(10)
	refernce_string.append(num)
'''
print (refernce_string)

for i in xrange(len(refernce_string)):

	quitados=[]
	for j in xrange(len(lru)):
		if refernce_string[i] == lru[j]:
			break
			
	else:
		if len(lru)<3:
			lru.append(refernce_string[i])
		else:
			for o in xrange(i+1,len(refernce_string)):
				if refernce_string[o] in lru and refernce_string[o] not in quitados:
					quitados.append(refernce_string[o])
				'''
				if len(aux)==1:
					break
				'''
			print quitados
			print
			if len(quitados)==0:
				lru[0]=refernce_string[i]
			
			elif len(quitados)<len(lru):
				for m in lru:
					if m not in quitados:
						victi=m
						break
				for m in xrange(len(lru)):
					if lru[m] ==victi:
						
						lru[m]=refernce_string[i]
			else:	
				for m in xrange(len(lru)):
					if lru[m] == quitados[len(quitados)-1]:
						lru[m]=refernce_string[i]
						break
		
		n_faults += 1	

	print (lru)
print ("numero de fallos: ", n_faults)	