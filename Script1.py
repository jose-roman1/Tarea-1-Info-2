
class Persona():
    def __init__(self ):
        self.__nombre =""
        self.__cedula =0
        self.__genero = ""
#Propiedades
    # Setters
    def asignarNombre(self,h):
        self.__nombre = h
    def asignarCedula(self,h):
        self.__cedula = h
    def asignarGenero(self,h):
        self.__genero = h

    # getters 
    def verNombre(self): 
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verGenero(self):
        return self.__genero
    
    #deleters
    def borrarNombre(self):
        del self.__nombre
    def borrarCedula(self):
        del self.__cedula
    def borrarGenero(self):
        del self.__genero
        
# Métodos adicionales segun la abstracción hecha 
    def caminar(self):        
        print(input("ingrese direccion: "))
    def comer(self):
        print(input("Ingrese la comida que desea: "))

class Paciente(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.__servicio = ""

    def asignarServicio(self, servicio):
        self.__servicio = servicio
    def verServicio(self):
        return self.__servicio

class Empleado_Hospital(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.__turno = ''

    def asignarTurno(self, turno):
        self.__turno = turno

    def verTurno(self):
        return self.__turno

class Enfermera(Empleado_Hospital):
    def __init__(self):
        # Empleado_Hospital.__init__(self) # Invocando el constructor de la clase padre de la cual esta heredando 
        super().__init__() # Este metodo hace exactamente lo mismo que le anterior, invocar el constructor de la clase padre 
        self.__rango = ''

    def asignarRango(self, rango):
        self.__rango = rango
    def verRango(self):
        return self.__rango

class Medico(Empleado_Hospital):
    def __init__(self):
        Empleado_Hospital.__init__(self)
        
        self.__especialidad = ''
    
    def asignarEspecialidad(self, especialidad):
        self.__especialidad = ''
    def verEspecialidad(self):
        return self.__especialidad
LP = []
LM = []
LE = []
while True:
    x = int(input("Selecciones un menú: \n1) Paciente\n2) Médico\n3) Enfermera\n4) Ver Información\nR// "))
    if x == 1:
        N = input("Ingrese el nombre del paciente: ")
        C = int(input("Ingrese la cédula del paciente: "))
        G = input("Ingrese el género del paciente\nM - Masculino\nF - Femenino\nR// ")
        S = input("Ingrese el servicio del paciente: ")
        Pa = Paciente()
        Pa.asignarNombre(N)
        Pa.asignarCedula(C)
        Pa.asignarGenero(G)
        Pa.asignarServicio(S)

        LP.append(Pa)
    elif x == 2:
        N = input("Ingrese el nombre del médico: ")
        C = int(input("Ingrese la cédula del médico: "))
        G = input("Ingrese el género del médico\nM - Masculino\nF - Femenino\nR// ")
        T = input("Ingrese el turno del médico: ")
        E = input("Ingrese la especialidad del médico: ")
        Me = Medico()
        Me.asignarNombre(N)
        Me.asignarCedula(C)
        Me.asignarGenero(G)
        Me.asignarTurno(T)
        Me.asignarEspecialidad(E)

        LM.append(Me)

    elif x == 3:
        N = input("Ingrese el nombre de la Enfermera: ")
        C = int(input("Ingrese la cédula de la Enfermera: "))
        G = input("Ingrese el género de la Enfermera\nM - Masculino\nF - Femenino\nR// ")
        T = input("Ingrese el turno de la Enfermera: ")
        R = input("Ingrese el rango de la Enfermera: ")
        En = Enfermera()
        En.asignarNombre(N)
        En.asignarCedula(C)
        En.asignarGenero(G)
        En.asignarTurno(T)
        En.asignarRango(R)
    elif x == 4:
        o = int(input("Selecciones un menú: \n1) Paciente\n2) Médico\n3) Enfermera\n4) Ver Pacientes\nR// "))
        if o == 1:
            w = 0
            for i in LP:
                print(LP[w].verNombre())
                print(LP[w].verCedula())
                print(LP[w].verGenero())
                print(LP[w].verServicio())
                print("----------------------------")
                w = w + 1
        elif o == 2:
            w = 0
            for i in LM:
                print(LM[w].verNombre())
                print(LM[w].verCedula())
                print(LM[w].verGenero())
                print(LM[w].verTurno())
                print(LM[w].verEspecialidad())
                print("----------------------------")
                w = w + 1
        elif o == 3:
            w = 0
            for i in LP:
                print(LE[w].verNombre())
                print(LE[w].verCedula())
                print(LE[w].verGenero())
                print(LE[w].verTurno())
                print(LE[w].verRango())
                print("----------------------------")
                w = w + 1
print("Prueba de Git Número 2")
print("Prueba de Git Número 3")
print("Prueba de Git Número 4")