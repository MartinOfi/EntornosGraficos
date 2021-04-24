

#Test de corridas
#Prueba de corridas Arriba y Abajo

A = [ [ 4529.4, 9044.9, 13568, 18091, 22615, 27892], [ 9044.9, 18097, 27139, 36187, 45234, 55789], [13568, 27139, 40721, 54281, 67852, 83685], [18091, 36187, 54281, 72414, 90470, 111580], [22615, 45234, 67852, 90470, 113262, 139476], [27892, 55789, 83685, 111580, 139476, 172860] ]

b = [1/6, 5/24, 11/120, 19/720, 29/5040, 1/840]

X = 0

r = [0, 0, 0, 0, 0, 0]

class Generador:
    semilla = (2**20)
    multi = (5**15)
    conAdi = 10000
    mod = (2**35)

    def value(self, axi):
        return (((self.multi * axi) + self.conAdi) % self.mod)

    def xn(self):
        periodo = 0
        num_gen = []
        num = 0
        axi = self.value(self.semilla)
        print(str(axi))
        while periodo < 5000:
            axi = self.value(axi)
            num = axi / self.mod
            num_gen.append(num)
            periodo = periodo + 1
        return num_gen


def Chi2Indep (X):
    valorChi = 1.653
    #Valor de Chi-Cuadrado con 6 grados de libertad y 95% de confianza
    if (X > valorChi):
        print ("Los numeros aleatorios generados NO son Independientes")
    else:
        print ("Los numeros aleatorios generados son Independientes")

R = [ 0, 0, 0, 0, 0, 0]

generador = Generador()
numeros_generados = generador.xn()
cont = 0
i = 0
n = len(numeros_generados)
while (i < n-1):
    if (numeros_generados[i] < numeros_generados [i+1]):
        cont += 1
    elif (cont < 5):
        r [cont] = r [cont +1]
        cont = 0
    else:
        r [5] += 1
        cont = 0
    i += 1
i = 0
while (i < 6):
    R [i] = r [i] / r [5]
    i += 1
print ("R: ", R)
j = 0
k = 0
while (j < 6):
    while (k < 6):
        X = X + (R [j] - n * b [j]) * (R [k] - n * b [k]) * A [j][k]
        k += 1
    k = 0
    j += 1
X = X / n
print ("X: ", X)
Chi2Indep(X)


