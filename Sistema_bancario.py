login = False
inicio = True
usuarios = []
while login == False and inicio == True:
    intro = input('\nBienvenido al programa de transacciones bancarias\nQue deseas hacer?\n1. Registrarse\n2. Iniciar sesion\n3. Salir\n')
    while intro != "1" and intro != "2" and intro != "3":
        intro = input('Ingresa la opcion deseas hacer:\n1. Registrarse\n2. Iniciar Sesion\n3. Salir\n')

    if intro == "1":
        nombre = input("Ingresa tus nombres: ")
        apellido = input("Ingresa tus apellidos: ")
        dpi = input("Ingresa tu dpi: ")
        while len(dpi) != 13:
            dpi = input("Ingresa un dpi valido: ")
        pin = input("ingresa un pin de 4 digitos: ")
        while len(pin) != 4:
            pin = input("ingresa un pin valido: ")
        tipo_moneda = input("Ingresa tu tipo de moneda: Q o $: ")
        while tipo_moneda != "Q" and tipo_moneda != "$":
            tipo_moneda = input("Ingresa unicamente el tipo de moneda: Q o $: ")
        if tipo_moneda == "Q":
            monto_apertura = input("ingrese el numero del monto de apertura que desea agragar:\n1. Q100\n2. Q200\n3. Q500\n4. Q1000\n")
            while monto_apertura != "1" and monto_apertura != "2" and monto_apertura != "3" and monto_apertura != "4":
                monto_apertura = input("ingrese el numero del monto de apertura que desea agragar:\n1. Q100\n2. Q200\n3. Q500\n4. Q1000\n")
            if monto_apertura == "1":
                monto_apertura = 100
            elif monto_apertura == "2":
                monto_apertura = 200
            elif monto_apertura == "3":
                monto_apertura = 500 
            else:
                monto_apertura = 1000 
        elif tipo_moneda == "$":
            monto_apertura = input("ingrese el numero del monto de apertura que desea agragar:\n1. $15\n2. $25\n3. $75\n4. $125\n")
            while monto_apertura != "1" and monto_apertura != "2" and monto_apertura != "3" and monto_apertura != "4":
                monto_apertura = input("ingrese el numero del monto de apertura que desea agragar:\n1. $15\n2. $25\n3. $75\n4. $125\n")
            if monto_apertura == "1":
                monto_apertura = 15
            elif monto_apertura == "2":
                monto_apertura = 25
            elif monto_apertura == "3":
                monto_apertura = 75
            else:
                monto_apertura = 125
        tipo_cuenta = input("Ingresa el tipo de cuenta que deseas utilizar:\n1. Clasica\n2. Ahorro\n3. Preferente\n")
        while tipo_cuenta != "1" and tipo_cuenta != "2"and tipo_cuenta != "3":
            tipo_cuenta = input("Ingresa el tipo de cuenta que deseas utilizar:\n1. Clasica\n2. Ahorro\n3. Preferente\n")
        if tipo_cuenta == "1":
            tipo_cuenta = "Clasica"
        elif tipo_cuenta == "2":
            tipo_cuenta = "Ahorro"
        else:
            tipo_cuenta = "Preferente"
        confirm = input("Bienvenido "+nombre+" estas a punto de registrarte con la siguiente informacion:\nNombre: "+nombre+"\nApellido: "+apellido+"\nDPI: "+dpi+"\nPIN: "+pin+"\nTipo de cuenta: "+tipo_cuenta+"\nTipo de moneda: "+tipo_moneda+"\nMonto de apertura: "+str(monto_apertura)+"\n\nDeseas continuar con esta informacion?\n1.Si 2.No\n")
        while confirm != "1" and confirm != "2":
            confirm = input("Ingrese unicamente 1 para si y 2 para no: ")
        if confirm == "1":
            usuario = {}
            usuario[dpi] = dpi
            usuario[pin] = pin
            usuarios.append(usuario)
            login = True
        else:
            print("\nRegistro cancelado!")

        while login == True:
            menu = input("\nBienvenido al menu del sistema de facturacion "+nombre+"\nQue deseas hacer?\n\n1. Depositar\n2. Retirar\n3. Cambiar de moneda\n4. Cerrar Sesion\n")
            if menu == "1":
                validar_pin = input("Confirma tu PIN para continuar: ")
                if validar_pin == pin:
                    cant = int(input("Ingresa la cantidad de "+tipo_moneda+" que deseas depositar: "))
                    monto_apertura = monto_apertura + cant
                    print("\nTransaccion realizada!, tu saldo actual es de: "+tipo_moneda+"."+str(monto_apertura))
                else:
                    print("\nERROR El PIN ingresado no coincide!")
            elif menu == "2":
                validar_pin = input("Confirma tu PIN para continuar: ")
                if validar_pin == pin:
                    cant = int(input("Ingrese la cantidad que deseas Retirar: "))
                    if tipo_moneda == "Q":
                        if tipo_cuenta == "Clasica":
                            if cant <= 2000:
                                if cant < monto_apertura:
                                    monto_apertura = monto_apertura - cant
                                    print("\nTransaccion realizada!, tu saldo actual es de: "+tipo_moneda+"."+str(monto_apertura))
                                else:
                                    print("\nERROR No dispones del saldo suficiente")
                            else:
                                print("\nERROR No puedes retirar mas de Q.2,000 en una cuenta Clasica")
                        if tipo_cuenta == "Ahorro":
                            if cant <= 3000:
                                if cant < monto_apertura:
                                    monto_apertura = monto_apertura - cant
                                    print("\nTransaccion realizada!, tu saldo actual es de: "+tipo_moneda+"."+str(monto_apertura))
                                else:
                                    print("\nERROR No dispones del saldo suficiente")
                            else:
                                print("\nERROR No puedes retirar mas de Q.2,000 en una cuenta Ahorro")
                        if tipo_cuenta == "Preferente":
                            if cant < monto_apertura:
                                monto_apertura = monto_apertura - cant
                                print("\nTransaccion realizada!, tu saldo actual es de: "+tipo_moneda+"."+str(monto_apertura))
                            else:
                                print("\nERROR No dispones del saldo suficiente")
                    if tipo_moneda == "$":
                        if tipo_cuenta == "Clasica":
                            if cant <= 250:
                                if cant < monto_apertura:
                                    monto_apertura = monto_apertura - cant
                                    print("\nTransaccion realizada!, tu saldo actual es de: "+tipo_moneda+"."+str(monto_apertura))
                                else:
                                    print("\nERROR No dispones del saldo suficiente")
                            else:
                                print("\nERROR No puedes retirar mas de $.250 en una cuenta Clasica")
                        if tipo_cuenta == "Ahorro":
                            if cant <= 275:
                                if cant < monto_apertura:
                                    monto_apertura = monto_apertura - cant
                                    print("\nTransaccion realizada!, tu saldo actual es de: "+tipo_moneda+"."+str(monto_apertura))
                                else:
                                    print("\nERROR No dispones del saldo suficiente")
                            else:
                                print("\nERROR No puedes retirar mas de $.275 en una cuenta Ahorro")
                        if tipo_cuenta == "Preferente":
                            if cant < monto_apertura:
                                monto_apertura = monto_apertura - cant
                                print("\nTransaccion realizada!, tu saldo actual es de: "+tipo_moneda+"."+str(monto_apertura))
                            else:
                                print("\nERROR No dispones del saldo suficiente")
                else:
                    print("\nERROR El PIN ingresado no coincide!")
            elif menu == "3":
                validar_pin = input("Confirma tu PIN para continuar: ")
                if validar_pin == pin:
                    if tipo_moneda == "Q":
                        tipo_moneda = "$"
                        monto_apertura = monto_apertura/8
                        print("\nCambio de moneda exitoso! has cambiado de Quetzal a Dolar tu saldo actual en Dolar es de: "+tipo_moneda+"."+str(monto_apertura))
                    elif tipo_moneda == "$":
                        tipo_moneda = "Q"
                        monto_apertura = monto_apertura*8
                        print("\nCambio de moneda exitoso! has cambiado de Dolar a Quetzal tu saldo actual en Quetzales es de: "+tipo_moneda+"."+str(monto_apertura))
                    else:
                        print("\nERROR El PIN ingresado no coincide!")
            elif menu == "4":
                login = False
    elif intro == "2":
        dpi_login = input("Ingresa un DPI: ")
        pin_login = input("Ingresa tu PIN: ")
        if dpi_login == dpi and pin_login == pin:
            login = True
            while login == True:
                menu = input("\nBienvenido al menu del sistema de facturacion "+nombre+"\nQue deseas hacer?\n\n1. Depositar\n2. Retirar\n3. Cambiar de moneda\n4. Cerrar Sesion\n")
                if menu == "1":
                    validar_pin = input("Confirma tu PIN para continuar: ")
                    if validar_pin == pin:
                        cant = int(input("Ingresa la cantidad de "+tipo_moneda+" que deseas depositar: "))
                        monto_apertura = monto_apertura + cant
                        print("\nTransaccion realizada!, tu saldo actual es de: "+tipo_moneda+"."+str(monto_apertura))
                    else:
                        print("\nERROR El PIN ingresado no coincide!")
                elif menu == "2":
                    validar_pin = input("Confirma tu PIN para continuar: ")
                    if validar_pin == pin:
                        cant = int(input("Ingrese la cantidad que deseas Retirar: "))
                        if tipo_moneda == "Q":
                            if tipo_cuenta == "Clasica":
                                if cant <= 2000:
                                    if cant < monto_apertura:
                                        monto_apertura = monto_apertura - cant
                                        print("\nTransaccion realizada!, tu saldo actual es de: "+tipo_moneda+"."+str(monto_apertura))
                                    else:
                                        print("\nERROR No dispones del saldo suficiente")
                                else:
                                    print("\nERROR No puedes retirar mas de Q.2,000 en una cuenta Clasica")
                            if tipo_cuenta == "Ahorro":
                                if cant <= 3000:
                                    if cant < monto_apertura:
                                        monto_apertura = monto_apertura - cant
                                        print("\nTransaccion realizada!, tu saldo actual es de: "+tipo_moneda+"."+str(monto_apertura))
                                    else:
                                        print("\nERROR No dispones del saldo suficiente")
                                else:
                                    print("\nERROR No puedes retirar mas de Q.2,000 en una cuenta Ahorro")
                            if tipo_cuenta == "Preferente":
                                if cant < monto_apertura:
                                    monto_apertura = monto_apertura - cant
                                    print("\nTransaccion realizada!, tu saldo actual es de: "+tipo_moneda+"."+str(monto_apertura))
                                else:
                                    print("\nERROR No dispones del saldo suficiente")
                        if tipo_moneda == "$":
                            if tipo_cuenta == "Clasica":
                                if cant <= 250:
                                    if cant < monto_apertura:
                                        monto_apertura = monto_apertura - cant
                                        print("\nTransaccion realizada!, tu saldo actual es de: "+tipo_moneda+"."+str(monto_apertura))
                                    else:
                                        print("\nERROR No dispones del saldo suficiente")
                                else:
                                    print("\nERROR No puedes retirar mas de $.250 en una cuenta Clasica")
                            if tipo_cuenta == "Ahorro":
                                if cant <= 275:
                                    if cant < monto_apertura:
                                        monto_apertura = monto_apertura - cant
                                        print("\nTransaccion realizada!, tu saldo actual es de: "+tipo_moneda+"."+str(monto_apertura))
                                    else:
                                        print("\nERROR No dispones del saldo suficiente")
                                else:
                                    print("\nERROR No puedes retirar mas de $.275 en una cuenta Ahorro")
                            if tipo_cuenta == "Preferente":
                                if cant < monto_apertura:
                                    monto_apertura = monto_apertura - cant
                                    print("\nTransaccion realizada!, tu saldo actual es de: "+tipo_moneda+"."+str(monto_apertura))
                                else:
                                    print("\nERROR No dispones del saldo suficiente")
                    else:
                        print("\nERROR El PIN ingresado no coincide!")
                elif menu == "3":
                    validar_pin = input("Confirma tu PIN para continuar: ")
                    if validar_pin == pin:
                        if tipo_moneda == "Q":
                            tipo_moneda = "$"
                            monto_apertura = monto_apertura/8
                            print("\nCambio de moneda exitoso! has cambiado de Quetzal a Dolar tu saldo actual en Dolar es de: "+tipo_moneda+"."+str(monto_apertura))
                        elif tipo_moneda == "$":
                            tipo_moneda = "Q"
                            monto_apertura = monto_apertura*8
                            print("\nCambio de moneda exitoso! has cambiado de Dolar a Quetzal tu saldo actual en Quetzales es de: "+tipo_moneda+"."+str(monto_apertura))
                        else:
                            print("\nERROR El PIN ingresado no coincide!")
                elif menu == "4":
                    login = False
        else:
            print('Datos incorrectos')
    elif intro == "3":
        login = False
        inicio = False
        print("Vuelve pronto! :)")

