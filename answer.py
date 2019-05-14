import numpy
import threading

A = numpy.array([[1,1],[2,2]])
B = numpy.array([[1,1],[2,2]]) 
C = numpy.array([[0,0],[0,0]])

def Matrix(a,b,i):
    for j in range (len(A)):
        C[i][j] = sum(map(lambda x,y: x*y, a[i], b[j]))

for i in range (len(A)):
     threading.Thread(target=matrix, args=(A,B,i)).start()
        
print("Результат:")
print(C)
