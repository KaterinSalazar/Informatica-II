from utils import *
class Mascota:
    def __init__(self):
        self.__numerohistoria=0
        self.__nombre=" "
        self.__tipo=" "
        self.__peso=0
        self.__fechaingreso=""
        self.__medicamentos=[]
    
    def verNumHistoria(self):
        return self.__numerohistoria
    def verNombre(self):
        return self.__nombre
    def verTipo(self,tipo):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFechaIngreso(self):
        return self.__fechaingreso
    def verMedicamentos(self):
        return self.__medicamentos
    
    def asignarNumhistoria(self,numerohistoria):
        self.__numerohistoria=numerohistoria
    def asignarNombre(self,nombre):
        self.__nombre=nombre   
    def asignarTipo(self,tipo):
        self.__tipo=tipo   
    def asignarPeso(self,peso):
        self.__peso=peso
    def asignarFechaIngreso(self,fechaingreso):
        self.__numerohistoria=fechaingreso
    def asignarMedicamentos(self,medicamentos):
        self.__medicamentos=medicamentos

class Sistema:
    def __init__(self) :

       self.__lista_mascotas=[]
       self.__numero_mascotas=len(self.__lista_mascotas)
    
    def verListaMascotas(self):
        return self.__lista_mascotas
    def verNumeroMascotas(self):
        return self.__numero_mascotas
    def nuevoPaciente(self,val,p):
        if val==True:
            self.__lista_mascotas.append(p)
            self.__numero_mascotas=len(self.__lista_mascotas)
    def EliminarMascota(self,val,mascota):
        if val:
            self.__lista_mascotas.pop(mascota)

def main():

    sistema=Sistema()
    try:
        while True:
            opcion=int(input("==========MENU============\n1.Ingresar Mascota\n2.Ver decha de ingreso de la mascota\n3.Ver numero de mascotas en el servicio\n4.Ver Mediccamentos de la mascota\n5.Eliminar Mascota del servicio\n6.Salir\n"))
            if opcion==1:
                if sistema.verNumeroMascotas >=10:
                    print("el servicio esta lleno en el momento")
                else:
                    numerohistoria=int(input("Ingrese numero de historia de la mascota:\n"))
                    for mascota in sistema.__lista_mascotas:
                        if numerohistoria==mascota.verNumHistoria():
                            print ("La mascota ya se encuentra en el sericuvio")
                            continue
                        else:
                            nombre=input("Ingrese nombre de la mascota:  ")
                            tipomasc=int("Ingrese una de las siguientes opciones numericas de tipo de mascota:\n'1' -> si la mascota es un canino\n´2´->Si la mascota es un felino\n")
                            if tipomasc==1:
                                tipo="canino"
                            elif tipomasc==2:
                                tipo=="felino"
                            else:
                                print("la opcion ingresada no se encuentra en el menu...")
                            peso=float("Ingrese el peso de la mascota en kg: ")
                            fechaingreso=("Ingrese fecha de ingreso en formato dd/mm/yyyy")
                            val=validar_fecha(fechaingreso)
                            if val==False:
                                    print("Fecha inválida. Por favor, ingresa la fecha en formato dd/mm/yyyy.")
                                    continue
                            else:

                                nummedicamentos=int(input("Ingrese numero de medicamentos que se le administran a la mascota "))
                                medicamentos=[]
                                for i in range(0,nummedicamentos):
                                    medicamento= input("Ingrese nombre de medicamento: ")
                                    medicamentos.append(medicamento)
                                    i+=1

                                mascota=Mascota()
                                mascota.asignarNumhistoria(numerohistoria)
                                mascota.asignarNombre(nombre)
                                mascota.asignarTipo(tipo)
                                mascota.asignarPeso(peso)
                                mascota.asignarFechaIngreso(fechaingreso)
                                mascota.asignarMedicamentos(medicamento)





  

    
        