print("-----------Seleccione una opcicion------------------")
print("1. Numero mayor o menor")
print("2. Verificar el mayor numero de tres numeros ")
print("3. Verificar si son multiplos de 7")
print("4. Tres numero pár o impar con su promedio")
print("5. Telefonia")
print("6. Salir")
opt=int(input("Ingrese la opcion que quiere realizar "))


    while opt != 6:
        if opt == 1:
            print("<<<<< Has elegido la opcion de quien es el  numero mayor o menor >>>>")
            num1 = int(input("Ingrese un numero"))
            num2 = int(input("Ingrese otro numero"))
            if num1 > num2:
                print("El mayor numero es ", num1)

            elif num2 > num1:
                print("El mayor numero es ", num2)
            else:
                print("Los numeros son iguales")

            print("-----------Seleccione una opcicion------------------")
            print("1. Numero mayor o menor")
            print("2. Verificar el mayor numero de tres numeros ")
            print("3. Verificar si son multiplos de 7")
            print("4. Tres numero pár o impar con su promedio")
            print("5. Telefonia")
            print("6. Salir")
            opt = int(input("Ingrese la opcion que quiere realizar "))

        elif opt == 2:
            print("<< Has elegido la opcionde verificar el mayor numero de tres numeros >>>>> ")
            num1 = int(input("Ingrese un numero"))
            num2 = int(input("Ingrese otro numero"))
            num3 = int(input("Ingrese otro numero"))

            if num1 > num2:
                if num1 > num3:
                    print("El mayor numero es ", num1)

            if num2 > num1:
                if num2 > num3:
                    print("El mayor numero es ", num2)

            if num3 > num1:
                if num3 > num2:
                    print("El mayor numero es ", num3)

            print("-----------Seleccione una opcicion------------------")
            print("1. Numero mayor o menor")
            print("2. Verificar el mayor numero de tres numeros ")
            print("3. Verificar si son multiplos de 7")
            print("4. Tres numero pár o impar con su promedio")
            print("5. Telefonia")
            print("6. Salir")
            opt = int(input("Ingrese la opcion que quiere realizar "))


        elif opt == 3:
            print("<<< Has elegido la opcion de verificar si son multiplos de 7 >>>")
            num1 = int(input("Ingrese un numero"))
            num2 = int(input("Ingrese otro numero"))
            num3 = int(input("Ingrese otro numero"))
            suma = num1 + num2 + num3
            if suma % 7 == 0:
                print("Es multiplo de 7 ,ya que la suma es ", suma)
            else:
                print("No es multiplo de 7 ya que la suma es", suma)
            print("-----------Seleccione una opcicion------------------")
            print("1. Numero mayor o menor")
            print("2. Verificar el mayor numero de tres numeros ")
            print("3. Verificar si son multiplos de 7")
            print("4. Tres numero pár o impar con su promedio")
            print("5. Telefonia")
            print("6. Salir")
            opt = int(input("Ingrese la opcion que quiere realizar "))

        elif opt == 4:
            print("<<<< Has elegido la opcion tres numero pár o impar con su promedio >>>>")
            num1 = int(input("Ingrese un numero"))
            num2 = int(input("Ingrese otro numero"))
            num3 = int(input("Ingrese otro numero"))
            prom = (num1 + num2 + num3) / 3
            if prom % 2 == 0:
                print("El promedio es par ,ya que el promedio es de", prom)
            else:
                print("El promedio es impar ,ya que el promedio es de", prom)
            print("-----------Seleccione una opcicion------------------")
            print("1. Numero mayor o menor")
            print("2. Verificar el mayor numero de tres numeros ")
            print("3. Verificar si son multiplos de 7")
            print("4. Tres numero pár o impar con su promedio")
            print("5. Telefonia")
            print("6. Salir")
            opt = int(input("Ingrese la opcion que quiere realizar "))
        elif opt == 5:
            print("<<< Has elegido la opcion de telefonia >>>")
            name = str(input("Ingrese su nombre"))
            mincosint = float(input("Minutos consumidos internacionalmente"))
            mincosnac = float(input("Minutos consumidos nacionales"))
            suma = int(mincosint + mincosnac)

            if suma < 26:
                print(name, 'sus minutos no se le cobrara ya que no exedio de lo establecido')
            elif suma > 25:
                if mincosnac > 25:
                    mincosnac -= 25
                    pago = float(name, " el pago es de Q", pago)
                else:
                    resto = mincosnac - 25
                    mincosint += resto
                    pago = float(mincosint * 2.5)
                    print(name, " el pago es de Q", pago)

            print("-----------Seleccione una opcicion------------------")
            print("1. Numero mayor o menor")
            print("2. Verificar el mayor numero de tres numeros ")
            print("3. Verificar si son multiplos de 7")
            print("4. Tres numero pár o impar con su promedio")
            print("5. Telefonia")
            print("6. Salir")
            opt = int(input("Ingrese la opcion que quiere realizar "))

        else:

            print("-----------Vuelva a intentarlo otra vez------------------")
            print("1. Numero mayor o menor")
            print("2. Verificar el mayor numero de tres numeros ")
            print("3. Verificar si son multiplos de 7")
            print("4. Tres numero pár o impar con su promedio")
            print("5. Telefonia")
            print("6. Salir")
            opt = int(input("Ingrese la opcion que quiere realizar "))
except:
    print("Vuelva a intentarlo otra vez")
    print("-----------Seleccione una opcicion------------------")
    print("1. Numero mayor o menor")
    print("2. Verificar el mayor numero de tres numeros ")
    print("3. Verificar si son multiplos de 7")
    print("4. Tres numero pár o impar con su promedio")
    print("5. Telefonia")
    print("6. Salir")
    opt = int(input("Ingrese la opcion que quiere realizar "))








