

# Generador congruencial mixto
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
        if periodo == self.mod:
            print("El periodo es completo: " + str(periodo))
        else:
            print("El periodo es incompleto: " + str(periodo))
        return num_gen


generador = Generador()
numeros_generados = generador.xn()
print(numeros_generados)


