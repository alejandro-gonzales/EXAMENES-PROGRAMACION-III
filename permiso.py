from datetime import datetime
class Permiso:
    def __init__(self):
        self.codigo = []
        self.conductor = []
        self.modelo = []
        self.marca = []
        self.placa = []
        self.ciudad = []
        self.fecha_solicitud = []
        self.motivo = []
        self.habilitado = []
    
    def verificarNumero(self, dato):
        
        if dato.isdigit():
            return True
        else:
            return False

    def menu(self):
        opciones = """
        *******GESTION DE PERMISOS VEHICULARES*******
        1.- Registrar Permiso
        2.- Ver Permisos Solicitados
        3.- Habilitar Permisos Solicitados hasta el 31/05/2020
        4.- Ver Permisos Habilitados
        5.- Ver Permisos No Habilitados
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
            self.agregar()
            self.volverMenu()
        elif (eleccion == 2):
            self.mostrar()
            self.volverMenu()
        elif (eleccion == 3):
            self.habilitarPermisos()
            self.volverMenu()
        elif (eleccion == 4):
            self.detalleHabilitado()
            self.volverMenu()
        elif (eleccion == 5):
            self.detalleNoHabilitado()
            self.volverMenu()
        elif (eleccion == 6):
            print("--------GRACIAS POR UTILIZAR NUESTRO SISTEMA--------")
        else:
            print("Elija una opcion del Menu")
            self.menu()

    def volverMenu(self):
        eleccion = input("Desea volver al Menu? S/N: ")
        if (eleccion == "s" or eleccion == "S"):
            self.menu()
        else:
            return "--------GRACIAS POR UTILIZAR NUESTRO SISTEMA--------"

    def validarSiNo(self, mensaje):
        valor = input("{} s/n: ".format(mensaje))
        if (valor == "s" or valor == "S" or valor == "n" or valor == "N"):
            return valor
        else:
            print("Seleccione S para habilitado o N para No Habilitado...")
            return self.validarSiNo(mensaje)

    def obtenerHabilitado(self, datoHabilitado):
        if(datoHabilitado == "S" or datoHabilitado == "s"):
            return 1
        elif(datoHabilitado == "N" or datoHabilitado == "n"):
            return 0

    def agregar(self):
        codigo = int(input("Introduzca Codigo: "))
        conductor = input("Nombre del Solicitante: ")
        modelo = input("Modelo del Vehiculo: ")
        marca = input("Marca del Vehiculo: ")
        placa = input("Placa del Vehiculo: ")
        ciudad = input("Ciudad: ")
        fecha_solicitud = input("Fecha de solicitud: ")
        motivo = input("Motivo de Solicitud: ")
        datoHabilitado = input("Habilitado S/N?: ")

        habilitado = self.obtenerHabilitado(datoHabilitado)
        if(habilitado == 1):
            habilitado = 1
        elif(habilitado == 0):
            habilitado = 0  

        self.guardar(codigo, conductor, modelo, marca, placa, ciudad, fecha_solicitud, motivo, habilitado)

        return print("Permiso Registrado Correctamente..!!")

    def guardar(self, codigo, conductor, modelo, marca, placa, ciudad, fecha_solicitud, motivo, habilitado):
        self.codigo.append(codigo)
        self.conductor.append(conductor)
        self.modelo.append(modelo)
        self.marca.append(marca)
        self.placa.append(placa)
        self.ciudad.append(ciudad)
        self.fecha_solicitud.append(fecha_solicitud)
        self.motivo.append(motivo)
        self.habilitado.append(habilitado)

    def mostrar(self):
        for posicion in range(len(self.codigo)):
            self.detalle(posicion)
        pass    
    
    def detalle(self, posicion):
        print("*********************************************")
        print("Codigo: {}".format(self.codigo[posicion]))
        print("Conductor: {}".format(self.conductor[posicion]))
        print("Modelo y Marca: {} - {}".format(self.modelo[posicion], self.marca[posicion]))
        print("Placa: {}".format(self.placa[posicion]))
        print("Ciudad: {}".format(self.ciudad[posicion]))
        print("Fecha Solicitud: {}".format(self.fecha_solicitud[posicion]))
        print("Motivo: {}".format(self.motivo[posicion]))
        
        if self.habilitado[posicion] == 1:
            print("Habilitado: Si")

        elif self.habilitado[posicion] == 0:
            print("Habilitado: No")
        pass

    def detalleHabilitadoSiNo(self, habilitado):
        for posicion in range(len(self.codigo)):
            if (self.habilitado[posicion] == habilitado):
                self.detalle(posicion)

    def detalleHabilitado(self):
        habilitado = 1
        self.detalleHabilitadoSiNo(habilitado)

    def detalleNoHabilitado(self):
        habilitado = 0
        self.detalleHabilitadoSiNo(habilitado)
    
    def habilitarPermisos(self):
        for posicion in range(len(self.codigo)):
            fechaRegistroCap = self.fecha_solicitud[posicion]
            fechaRegistro = datetime.strptime(fechaRegistroCap, '%d/%m/%Y')
            fechaRegistroLimite = "31/05/2020"
            fechaRegistroLimiteConvert = datetime.strptime(fechaRegistroLimite, '%d/%m/%Y')

            self.imprimirhabilitarPermisos(fechaRegistro, fechaRegistroLimiteConvert, posicion)

        return print("Permisos Habilitados Correctamente")

    def imprimirhabilitarPermisos(self, fechaRegistro, fechaRegistroLimiteConvert, posicion):
        if fechaRegistro < fechaRegistroLimiteConvert:
            self.habilitado[posicion] = 1

        else:
            self.habilitado[posicion] = 0

permisos = Permiso()
permisos.guardar(1, 'JOSE MERCADO', 'COROLLA', 'TOYOTA', '2504TDA', 'SANTA CRUZ', '15/06/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardar(2, 'ALBERTO MERCADO', 'HILUX', 'TOYOTA', '2640SDA', 'TARIJA', '12/04/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardar(3, 'GABRIEL MELGAR', 'SENTRA', 'NISSAN', '3204NTS', 'BENI', '30/05/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardar(4, 'CARLA MEDINA', 'LANCER', 'MITSUBISHI', '2207SBA', 'CHUQUISACA', '02/05/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardar(5, 'PABLO AGUILAR', 'ACCORD', 'HONDA', '3504ATD', 'COCHABAMBA', '09/04/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardar(6, 'CARLOS MONTERO', 'CIVIC', 'HONDA', '2804STA', 'SANTA CRUZ', '10/06/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardar(7, 'PABLO ALEMAN', 'YARIS', 'TOYOTA', '2054PDA', 'LA PAZ', '22/06/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.menu()