class Clima:
    def __init__(self):
        self.codigo = []
        self.ciudad = []
        self.temp_minima = []
        self.temp_maxima = []
        self.zona = []
    
    def verificarNumero(self, dato):
        
        if dato.isdigit():
            return True
        else:
            return False

    def menu(self):
        opciones = """
        *******GESTION DEL CLIMA DE LOS DEPARTAMENTOS DE BOLIVIA*******
        1.- Registrar Clima
        2.- Ver Temperaturas
        3.- Promedio Minima Valle
        4.- Temperatura mas Baja Llano
        5.- Temperatura mas Alta Altiplano
        6.- Salir
        """
        print(opciones)
        dato = input("Elija una opcion: ")
        if self.verificarNumero(dato):
            eleccion = int(dato)
        else:
            print("Debe digitar solo numeros..!!")
            self.menu()
        self.opciones(eleccion)

    def opciones(self, eleccion):
        if (eleccion == 1):
            print(self.agregar())
            self.volverMenu()
        elif (eleccion == 2):
            self.mostrar()
            self.volverMenu()
        elif (eleccion == 3):
            self.promedioMin()
            self.volverMenu()
        elif (eleccion == 4):
            self.tempBajaLlano()
            self.volverMenu()
        elif (eleccion == 5):
            self.tempAltaAltiplano()
            self.volverMenu()
        elif (eleccion == 6):
            print("Gracias por Utilizar Nuestro Servicio")
        else:
            print("Elija una opcion del Menu")
            self.menu()

    def agregar(self):
        cod = input("Ingrese El numero Codigo: ")
        city = input("Ingrese La Ciudad: ")
        temp_min = int(input("Ingrese la Temp. Minima: "))
        temp_max = int(input("Ingrese la Temp. Maxima: "))
        zone = input("Ingrese la Zona: ")

        self.guardar(cod, city, temp_min, temp_max, zone)

        return "El Clima de la Ciudad de {} Registrado Exitosamente..!!".format(city)

    def guardar(self, codigo, ciudad, temp_minima, temp_maxima, zona):
        self.codigo.append(codigo)
        self.ciudad.append(ciudad)
        self.temp_minima.append(temp_minima)
        self.temp_maxima.append(temp_maxima)
        self.zona.append(zona)

    def mostrar(self):
        for i in range(len(self.ciudad)):
            self.detalle(i)
        pass

    def detalle(self, posicion):
        print("------------------------------------------------")
        print("TEMPERATURA DE {}".format(self.ciudad[posicion]))
        print("Minima: {}°".format(self.temp_minima[posicion]))
        print("Maxima: {}°".format(self.temp_maxima[posicion]))
        print("Zona: {}".format(self.zona[posicion]))
        pass
    
    def volverMenu(self):
        eleccion = input("Desea volver al Menu? y/n: ")
        if (eleccion == "y" or eleccion == "Y"):
            self.menu()
        else:
            return "--------QUE TENGA UN BUEN DIA--------"

    def promedioMin(self):
        prom = 0
        cont = 0
        for i in range(len(self.ciudad)):
            if(self.zona[i] == "Valle"):
                prom = prom + self.temp_minima[i]
                cont = cont + 1
        promTotal = int(prom/cont)
        return print("La Temperatura Minima Promedio de los Valles es {}°".format(promTotal))    

    def tempBajaLlano(self):
        tempbajaLl = []
        for i in range(len(self.ciudad)):
            if(self.zona[i] == "Llano"):
                tempbajaLl.append(self.temp_minima[i])
                if(self.temp_minima[i] == min(tempbajaLl)):
                    print("---------TEMPERATURA MAS BAJA DEL LLANO---------")
                    self.detalle(i)
        #for i in range(len(self.ciudad)):
            #if(self.zona[i] == "Llano"):
                
        return
    
    def tempAltaAltiplano(self):
        tempAltaAlt = []
        for i in range(len(self.ciudad)):
            if(self.zona[i] == "Altiplano"):
                tempAltaAlt.append(self.temp_maxima[i])
                if(self.temp_maxima[i] == max(tempAltaAlt)):
                    print("---------TEMPERATURA MAS ALTA DEL ALTIPLANO---------")
                    self.detalle(i)
        #for i in range(len(self.ciudad)):
            #if(self.zona[i] == "Altiplano"):
                
        return


clima = Clima()
clima.guardar(1, "SANTA CRUZ", 15, 29, "Llano")
clima.guardar(2, "BENI", 17, 31,"Llano")
clima.guardar(3, "PANDO", 18, 30,"Llano")
clima.guardar(4, "LA PAZ", 1, 13,"Altiplano")
clima.guardar(5, "ORURO", 2, 15,"Altiplano")
clima.guardar(6, "POTOSI", 2, 14,"Altiplano")
clima.guardar(7, "CBBA", 5, 18, "Valle")
clima.guardar(8, "SUCRE", 9, 23, "Valle")
clima.guardar(9, "TARIJA", 10, 25, "Valle")
clima.menu()