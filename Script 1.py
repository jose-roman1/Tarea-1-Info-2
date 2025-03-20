class Paciente():
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
        self.__sevicio = ""
    
    #Asignar
    def asignarNombre(self, a):
        self.__nombre = a
    def asignarCedula(self, a):
        self.__cedula = a
    def asignarGenero(self, a):
        self.__genero = a
    def asignarServicio(self, a):
        self.__sevicio = a
    # getters 
    def getNombre(self): 
        return self.__nombre
    def getCedula(self):
        return self.__cedula
    def getGenero(self):
        return self.__genero
    def getServicio(self):
        return self.__sevicio
    
class Sistema:
    def __init__(self):
        self.__lista_pacientes = []
        self.__numero_pacientes = len(self.__lista_pacientes)

    #Ingresar
    def ingresarPaciente(self):
        nombre = input("Ingrese el nombre del paciente: ")
        cedula = int(input("Ingrese la cédula del paciente: "))
        genero = input("Ingrese el género del paciente: ")
        servicio = input("Ingrese el servicio del paciente: ")

        P = Paciente()
        P.asignarNombre(nombre)
        P.asignarCedula(cedula)
        P.asignarGenero(genero)
        P.asignarServicio(servicio)

        self.__lista_pacientes.append(P)
        self.__numero_pacientes = len(self.__lista_pacientes)
    
    #VerNumeroPacientes
    def getNumeroPacientes(self):
        return self.__numero_pacientes
    #VerDatosPacientes
    def getDatosPacientes(self):
        cedula = int(input("Ingrese la cédula del paciente: "))
        for i in self.__lista_pacientes:
            if cedula == Paciente.getCedula():
                print(f"""---------------------------
-Nombre: {Paciente.getNombre()}
-Cédula: {Paciente.getCedula()}
-Género: {Paciente.getGenero()}
-Servicio:  {Paciente.getServicio()}
---------------------------""")

sistema = Sistema()

while True:
    R = int(input("""---------------------------
Elija una opción:
1. Ingresar nuevo paciente
2. Ver datos de un paciente
3. Númmero de pacientes en el sistema
4. Salir
---------------------------"""))
    if R == 1:
        pass
    elif R == 2:
        pass
    elif R == 3:
        pass
    elif R == 4:
        break