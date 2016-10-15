import random
import sys

n= int(sys.stdin.readline().strip())

refernce_string=[]
lru = []
n_faults = 0

for i in range(n):
	num=random.randrange(10)
	refernce_string.append(num)
	
print (refernce_string)

for i in refernce_string:
	for j in lru:
		if i == j:
			lru.remove(i)
			lru.append(i)
			break
	else:
		if len(lru)<5:
			lru.append(i)
		else:
			lru.pop(0)
			lru.append(i)
		n_faults += 1	
	#print (lru)
print ("numero de fallos: ", n_faults)	