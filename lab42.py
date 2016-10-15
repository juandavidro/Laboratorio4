import random
import sys

n= int(sys.stdin.readline().strip())

refernce_string=[]
fifo = []
n_faults = 0

for i in range(n):
	num=random.randrange(10)
	refernce_string.append(num)
	
print (refernce_string)

for i in refernce_string:
	
	for x in fifo:
		if x == i:
			break	
	else:
		#print ("no esta")
		if len(fifo)<5:
			fifo.append(i)
		else:
			fifo.pop(0)
			fifo.append(i)
		n_faults += 1		


	print (fifo)
print ("numero de fallos: ", n_faults)
