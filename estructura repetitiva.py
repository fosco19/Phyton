print("-----------Seleccione una opcicion------------------")
print("1. Tabla de multiplicaion")
print("2. listado de impares")
print("3. Mostrar los multiplos de un numero")
print("4. Salir del programa")
answ=int(input("Ingrese su opcion"))

while answ!=4:
    if answ==1:
        print("<<<<<HAS ELEGIDO LAS TABLAS DE MULTIPLICAION>>>>>")
        num=int(input("Ingrese una posicion inicial"))
        num2=int(input("Ingrese la posicion final"))
        num3=int(input("Ingrese el  numero que quiere multiplicar"))
        if num< 0:
            num *=-1
        if num2 <0:
            num2 *=-1
        if num3<0:
            num3*=-1
        print("<<La tabla de multiplicacion es el siguiente>>")
        for i in range(num,num2+1):
            print(num3, "*", i, " = ", num3 * i)


        print("-----------Seleccione una opcicion------------------")
        print("1. Tabla de multiplicaion")
        print("2. listado de impares")
        print("3. Mostrar los multiplos de un numero")
        print("4. Salir del programa")
        answ = int(input("Ingrese su opcion"))
    elif answ==2:
        print("<<<HAS ELEGIDO LA PCION DE LOS NUMEROS IMPARES>>>")
        resp=int(input("Ingrese hasta que numero maximo quiere que llegue: "))
        for j in range (1,resp,2):
            print("La lista de los numeros impares del numero ",resp," son ",j)


        print("-----------Seleccione una opcicion------------------")
        print("1. Tabla de multiplicaion")
        print("2. listado de impares")
        print("3. Mostrar los multiplos de un numero")
        print("4. Salir del programa")
        answ = int(input("Ingrese su opcion"))
    elif answ==3:
        print("<<Has elegido mostrar los multiplos de un numero rango(1-100>>")
        num=int(input("Ingrese el numero "))
        if num<0:
            num*=-1
        for i in range(1,100):
            if i%num==0:
                print("Los multiplos del ", num, " son  ",i);
        print("-----------Seleccione una opcicion------------------")
        print("1. Tabla de multiplicaion")
        print("2. listado de impares")
        print("3. Mostrar los multiplos de un numero")
        print("4. Salir del programa")
        answ = int(input("Ingrese su opcion"))
    else:
        print("-----------Vuelva a intentarlo otra vez------------------")
        print("1. Tabla de multiplicaion")
        print("2. listado de impares")
        print("3. Mostrar los multiplos de un numero")
        print("4. Salir del programa")
        answ = int(input("Ingrese su opcion"))





