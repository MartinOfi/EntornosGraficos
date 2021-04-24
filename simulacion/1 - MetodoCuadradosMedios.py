
#Metodo de los Cuadrados Medios

numerosGenerados=[]
numerosCuadrados=[]
semilla = int(input("Ingresa la semilla de 4 digitos: ")) #Pedimos la semilla
pedida = int(input("Cantidad de numeros: ")) #Pedimos la cantidad de numeros a generar
contador = 0
print('{:^10}{:^10}{:^10}'.format('i','Zi','Zi^2'))
while (contador < pedida):
    #Elevamos la semila al cuadrado
    #zfill me permite determinar cuantos digitos quiero
    #ademas de no llegar a los digitos que necesito
    #rellena de ceros a la izquierda hasta completar
    #[2:6] me dice que quiero mostrar apartir de la posicion
    #2 hasta la posicion 6
    numerosGenerados.append(semilla)
    X2=(semilla*semilla)
    numerosCuadrados.append(X2)
    print('{:^10}{:^10}{:^10}'.format(contador,str(semilla).zfill(4),X2))
    semilla = int(str(X2).zfill(8)[2:6])
    contador = contador + 1