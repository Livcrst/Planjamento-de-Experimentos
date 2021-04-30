from scipy import stats
import matplotlib.pyplot as plt

Lenght = [128, 256, 384, 512, 640, 768, 896, 1024]

ob1 = [386, 850, 1544, 3035, 6650, 13887, 28059, 50916]
ob2 = [375, 805, 1644, 3123, 6839, 14567, 27439, 52129]
ob3 = [393, 824, 1553, 3235, 6768, 13456, 27659, 51360]

m1,b1,valueError1,valueP1,stdError1 = stats.linregress(Lenght,ob1) #49.33026413690476 -15248.357142857141
m2,b2,valueError2,valueP2,stdError2 = stats.linregress(Lenght,ob2)
m3,b3,valueError3,valueP3,stdError3 = stats.linregress(Lenght,ob3)

print(m1,b1)


# Calculo de m e b para a formula da linha de regressão
linregress1 = [m1*i+b1 for i in range(max(Lenght))]
linregress2 = [m2*i+b2 for i in range(max(Lenght))]
linregress3 = [m3*i+b3 for i in range(max(Lenght))]

#Letra a verificando se a regressão linear pode ser feita nas amostras.
plt.scatter(Lenght,ob1)
plt.show()
plt.scatter(Lenght,ob2)
plt.show()
plt.scatter(Lenght,ob3)
plt.xlabel('Length')
plt.ylabel('Observations')
plt.show()


#Calculando linhas de regressão
plt.scatter(Lenght,ob1)
plt.plot(linregress1,'r')
plt.show()
plt.scatter(Lenght,ob2)
plt.plot(linregress2,'r')
plt.show()
plt.scatter(Lenght,ob3)
plt.plot(linregress3,'r')
plt.xlabel('Length')
plt.ylabel('Observations')
plt.show()

#Porcentagem de variação explicada pela regressão
Percent = valueError1**2 # A porcentagem é 74%
# print(Percent)
#LEtra E 
Value = m1*(2**20)+b1
print('value',Value) #51711282.69047619