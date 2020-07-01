class Persona:
    def __init__ (self):
        self.nombre = []
        self.apellido = []
        self.carnet = []
        self.celular = []
        self.estado = []

class Administrativo(Persona):
    def __init__ (self):
        Persona.__init__(self)
        self.cargo = []
        self.area = []
    
    def guardarAdministrativo(self, nombre, apellido, carnet, celular, estado, cargo, area):
        self.nombre.append(nombre)
        self.apellido.append(apellido)
        self.carnet.append(carnet)
        self.celular.append(celular)
        self.estado.append(estado)
        self.cargo.append(cargo)
        self.area.append(area)
    
    def mostrarAdministrativo(self, posicion):
        print("********************ADMINISTRATIVO********************")
        print("Nombre Completo: {} {}".format(self.nombre[posicion], self.apellido[posicion]))
        print("Carnet: {}".format(self.carnet[posicion]))
        print("Celular: {}".format(self.celular[posicion]))
        if self.estado[posicion] == 1:
            estado = "Habilitado"
        elif self.estado[posicion] == 0:
            estado = "Inhabilitado"
        print("Estado: {}".format(estado))
        print("Cargo: {}".format(self.cargo[posicion]))
        print("Area: {}".format(self.area[posicion]))
        pass

    def listarAdministrativo(self):
        if self.nombre:    
            for posicion in range(len(self.cargo)):
                if self.cargo:
                    self.mostrarAdministrativo(posicion)
        else:
            return print("No hay Administrativos Registrados en el Sistema..!!")

class Docente(Persona):
    def __init__ (self):
        Persona.__init__(self)
        self.materia = []
        self.carrera = []

    def guardarDocente(self, nombre, apellido, carnet, celular, estado, materia, carrera):
        self.nombre.append(nombre)
        self.apellido.append(apellido)
        self.carnet.append(carnet)
        self.celular.append(celular)
        self.estado.append(estado)
        self.materia.append(materia)
        self.carrera.append(carrera)
    
    def mostrarDocente(self, posicion):
        print("********************DOCENTE********************")
        print("Nombre Completo: {} {}".format(self.nombre[3 + posicion], self.apellido[3 + posicion]))
        print("Carnet: {}".format(self.carnet[3 + posicion]))
        print("Celular: {}".format(self.celular[3 + posicion]))
        if self.estado[3 + posicion] == 1:
            estado = "Habilitado"
        elif self.estado[3 + posicion] == 0:
            estado = "Inhabilitado"
        print("Estado: {}".format(estado))
        print("Materia: {}".format(self.materia[posicion]))
        print("Carrera: {}".format(self.carrera[posicion]))
        pass

    def listarDocente(self):
        if self.nombre:
            for posicion in range(len(self.materia)):
                self.mostrarDocente(posicion)
        else:
            return print("No hay Docentes Registrados en el Sistema..!!")

class Colegio(Administrativo, Docente):
    def __init__ (self):
        Administrativo.__init__(self)
        Docente.__init__(self)
    
    def menu(self):
        print("""
            ************** ****** ***** MENU ***** ****** **************
            1.- MOSTRAR LOS DOCENTES REGISTRADOS
            2.- MOSTRAR LOS ADMINISTRATIVOS REGISTRADOS
            3.- MOSTRAR TODOS LOS DATOS REGISTRADOS (DOCENTES Y ADMINISTRATIVOS)
            4.- SALIR
        """)

        opcion = int(input("Elija una opcion del Menu: "))

        if opcion == 1:
            self.listarDocente()
            self.volverMenu()
        elif opcion == 2:
            self.listarAdministrativo()
            self.volverMenu()
        elif opcion == 3:
            self.listarDocente()
            self.listarAdministrativo()
            self.volverMenu()
        elif opcion == 4:
            print("GRACIAS POR EL SISTEMA DE GESTION DEL COLEGIO NACIONAL LA GUARDIA..!!")
        else:
            print("Elija una opcion correcta del Menu..!!")        

    def volverMenu(self):
        opcion = input("Desea volver al MENU? S/N: ")

        if opcion == "S" or opcion == "s":
            self.menu()
        elif opcion == "N" or opcion == "n":
            print("GRACIAS POR EL SISTEMA DE GESTION DEL COLEGIO NACIONAL LA GUARDIA..!!")
        else:
            print("Elija una opcion correcta S/N..!!")
            self.volverMenu()


colegio = Colegio()

colegio.guardarAdministrativo('JOSE', 'MERCADO', '7723652', '76354210', 1, 'ADMINISTRADOR GENERAL', 'ADMINISTRACION')

colegio.guardarAdministrativo('ANTONIO', 'MELGAR', '11223652', '69354210', 1, 'EJECUTIVO DE VENTAS', 'MARKETING')

colegio.guardarAdministrativo('JUAN', 'MERCADO', '6323652', '69054210', 1, 'EJECUTIVO DE VENTAS', 'MARKETING')

colegio.guardarDocente('MARCO', 'MERCADO', '11023652', '77254210', 1, 'MICROECONOMIA', 'ADMINISTRACION DE EMPRESAS')

colegio.guardarDocente('MARIO', 'PEREZ', '11123652', '69054278', 1, 'MACROECONOMIA', 'INGENIERA COMERCIAL')

colegio.menu()