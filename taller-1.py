"""
@author: k-ami
"""
import numpy as np

vector1 =np.random.randint(1,10,10)
vector2 =np.random.randint(1,10,10)
print (vector1)

u1=sum(vector1)
u2=sum(vector2)
u3=u1+u2
print(u3)

u4=vector1+vector2
print(u4)

r= np.concatenate((vector1,vector2),0)
print(r)

#encontrar promedio de los valores
ab=np.mean(vector1)
ac=np.mean(vector2)
ad=np.mean(r)

#imprimir los numeros mayores que 

def mayora(list,int):
    return (i for i in list if i > 5);
numerosmayoresa5 = mayora(vector1,5)

print(numerosmayoresa5)

###-------------------------------------------###

def mayor(list,int):
    return(i for i in list if i > 5);
numerosmayoresa = mayor(vector2,5)

print(numerosmayoresa)

#determinar la poscicion de los numeros que son iguales en los arreglos

np.intersect1d(vector1, vector2)






