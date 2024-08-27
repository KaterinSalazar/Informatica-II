class Paciente:
    def __init__(self):
        self.__nombre=""
        self.__cedula=0
        self.__genero=""
        self.__servicio=""

    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula (self):
        return self.__cedula
    
    def asignarNombre(self,n):
        self.__nombre= n
    def asignarServicio(self,s):
        self.__servicio=s
    def asignarGenero(self,g):
        self.__genero=g
    def asignarCedula(self,c):
        self.__cedula = c
    def user(self,j):
        pass


class Sistema:
    def __init__(self):

        self.__lista_pacientes=[]
        self.__numero_pacientes=len(self.__lista_pacientes)

    def IngresarPaciente(self):

        nombre=input("Ingresar el nombre: ")
        cedula=int(input("Ingrese la cedula: "))
        genero=input("Ingrese el genero: ")
        servicio=input("Ingrese el servicio: ")

        p=Paciente()
        p.asignarNombre(nombre)
        p.asignarCedula(cedula)
        p.asignarGenero(genero)
        p.asignarServicio(servicio)

        self.__lista_pacientes.append(p)
        self.__numero_pacientes=len(self.__lista_pacientes)

    def verNumeroPacientes(self):
        return self.__numero_pacientes
    
    def verDatosPaciente(self):
        cedula=int(input("Ingrese la cedula a buscar: "))

        for paciente in self.__lista_pacientes:
    
            if cedula == paciente.verCedula():
                print("Nombre: "+str(paciente.verNombre()))
                print("Cedula: "+str(paciente.verGenero()))
                print("Servicio: "+str(paciente.verServicio()))
            else:
                print("no existe")

mi_sistema=Sistema()

while True:
    opcion=int(input("=========Menu=========\n1. Nuevo paciente\n2. Numero de Pacientes\n3. Datos Pacientes\n4.Salir"))
    if opcion ==1:
        mi_sistema.IngresarPaciente()
    elif opcion== 2:
        print("Ahora hay: "+str(mi_sistema.verNumeroPacientes()))
    elif opcion==3:
        mi_sistema.verDatosPaciente()
    elif opcion == 4:
        break
    else:
        print("Opcion invalida")