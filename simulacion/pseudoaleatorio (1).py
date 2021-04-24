#import matplotlib.pyplot as plt
#import numpy as np
#2import scipy.stats as stats
from math import sqrt

seeds = []
seeds2 = []
runs = 10000


def square(s):
    sqr = s * s
    if sqr < 1000000:
        sqr = (str(sqr)).zfill(8)
    return str(sqr)


def nextSeed(s):
    newSeed = square(s)
    return newSeed[2:6]


def normalizar(a):
    minimo = min(a)
    maximo = max(a)
    arreglo = []
    for i in a:
        valor = (i - minimo) / (maximo - minimo)
        arreglo.append(valor)
    return arreglo


def metodoCuadrados():
    cuad = []
    seed = ''
    while not (seed.isdecimal()):
        seed = input("Ingrese semilla de 4 digitos: ")
        if not (seed.isdecimal()):
            print("No es un numero, ingrese otra semilla")
    for n in range(runs):
        seed = nextSeed(int(seed))
        cuad.append(int(seed))
    cuad = normalizar(cuad)
    print(cuad)
    return cuad


def calcularGCL(mul, a, m, seed):
    return (mul * seed + a) % m


# GCL
def semillaGCL():
    gcl = []
    multiplicador = 25214903917
    incremento = 11
    m = 2 ** 48
    semilla = int(input("Introduce un numero de semilla menor a " + str(m) + ": "))
    for n in range(runs):
        semilla = calcularGCL(multiplicador, incremento, m, semilla)
        s = semilla / m
        gcl.append(s)
    return gcl


def clearArrays():
    seeds.clear()
    seeds2.clear()


def plot():
    plt.style.use('seaborn')
    plt.scatter(seeds, seeds2, s=20, edgecolor='black', linewidth=1, alpha=0.75)
    plt.show()


def chiCuadrado():
    sumRow = sum(seeds)
    sumRow2 = sum(seeds2)
    total = sumRow + sumRow2
    chi1 = []
    chi2 = []
    chiRes1 = chiRes2 = 0
    for i in range(runs):
        aux = seeds[i] + seeds2[i]
        chi1.append(aux * sumRow / total)
        chi2.append(aux * sumRow2 / total)
        chiRes1 += ((seeds[i] - chi1[i]) ** 2) / chi1[i]
        chiRes2 += ((seeds2[i] - chi2[i]) ** 2) / chi2[i]
    chiRes = chiRes1 + chiRes2
    crit = stats.chi2.ppf(q=0.99, df=runs - 1)
    if chiRes < crit:
        print("Independiente")
    else:
        print("Dependiente")

def pokerComparador(a,b,c):
    #1 - son iguales, 2 - son pares, 3 - son diferentes
    if (a == b and a == c):
        return 1;
    elif ((a == b) or (a == c) or (b == c)):
        return 2;
    else:
        return 3;

def pokerCalculator(FO, FE):
    return ((FE-FO)**2 / FE)
        
def pokerTest(seeds):
    #inicializo probabilidades de que 3 "cartas" sean todas iguales, dos iguales, o todas diferentes
    auxSeed = 0
    Xcal = 0;
    Chi = 13.2767;
    tamañoMuestra = len(seeds);
    FETrio = 0.01;
    FEPar = 0.27;
    FEDif = 0.72;
    FOTrio = FOPar = FODif = 0;
    seedStr = 'a'
    result = ''
    first = second = third = '';
    pokerSeeds = [];
    for seed in seeds:
        auxSeed  = seed * 1000
        pokerSeeds.append(auxSeed)
    for i in pokerSeeds:
        seedStr = str((i));
        first = seedStr[0];
        second = seedStr[1];
        third = seedStr[2];
        result = pokerComparador(first, second, third)
        if result == 1:
            FOTrio += 1;
        elif result == 2:
            FOPar += 1;
        elif result == 3:
            FODif += 1;
    if ((FODif+FOPar+FOTrio) == tamañoMuestra):
        print('todo bien hasta aca')
        Xcal += pokerCalculator(FODif, (FEDif * tamañoMuestra));
        Xcal += pokerCalculator(FOPar, (FEPar * tamañoMuestra));
        Xcal += pokerCalculator(FOTrio, (FETrio * tamañoMuestra));
    #aca meto el chi cuadrado conrrepondiente y lo compara a Xcal, si Xcal es mayor, no pása la prueba
    if (Xcal >= Chi):
        print('no pasa la prueba de independencia')
        print('Xcal: ' + str(Xcal))
    else:
        print('paso la prueba de independencia')

def valorEsperado(n0,n1,num):
    return (((2 * n0 * n1)/ num) + (0.5))

def varianzaCorridas(n0,n1,num):
    return (((2 * n0 * n1) * ((2 * n0 * n1) - num)) / ((num **2) * (num - 1) ))

def calcularCorridas(corridas):
    contador = 0;
    flag = -1;
    for c in corridas:
        if c != flag:
            contador += 1;
            flag = c;
    return contador;

def estadistico(c0 , ve, va):
    return ((c0 - ve) / va**0.5)
            
# con alfa 0.05 y 1000 corridas del seeds
#se aplica a GCL
def pruebaCorridas(seeds):
    corridaList = [];
    n1 = 0;
    n0 = 0;
    c0 = 0;
    num = 0;
    ve = 0;
    va = 0;
    z0 = 0;
    z = 1.962
    for s in seeds:
        if (s >= 0.5):
            n0 += 1;
            corridaList.append(0);
        else:
            n1 +=1;
            corridaList.append(1);
    num = n1 + n0;
    ve = valorEsperado(n0, n1, num);
    va = varianzaCorridas(n0, n1, num);
    c0 = calcularCorridas(corridaList);
    z0 = estadistico(c0, ve, va);
    if ((z0 < z) and (z0 > (-z))):
        print('el estadistico ' + str(z0) + ' pasa la prueba, es independiente')
    else :
        print('el estadistico ' + str(z0) + ' NO pasa la prueba, NO es independiente')
        


def menu():
    global seeds, seeds2
    opc = ''
    while opc != 0:
        print("1. Semilla GCL")
        print("2. Método Cuadrado")
        print("0. Salir")
        opc = int(input("Ingrese una opción: "))
        if opc == 1:
            seeds = semillaGCL()
            seeds2 = semillaGCL()
        elif opc == 2:
            seeds = metodoCuadrados()
            seeds2 = metodoCuadrados()
        elif opc == 0:
            break
        plot()
        chiCuadrado()
        clearArrays()


#menu()
seeds2 = semillaGCL();
#pokerTest(seeds2);
pruebaCorridas(seeds2);
