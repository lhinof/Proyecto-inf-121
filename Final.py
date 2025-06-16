import pickle
from datetime import date

class FeriaDeSalud:
    def __init__(self, nombre, fecha, lugar, tipo):
        self.nombre = nombre
        self.fecha = fecha
        self.lugar = lugar
        self.tipo = tipo
        self.usuarios = []

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def guardar_datos(self):
        with open("datos.dat", "wb") as archivo:
            pickle.dump(self.usuarios, archivo)

    def cargar_datos(self):
        try:
            with open("datos.dat", "rb") as archivo:
                self.usuarios = pickle.load(archivo)
        except FileNotFoundError:
            pass

    def mostrar_usuarios(self):
        print(f"\nLista de participantes registrados en '{self.nombre}':\n")
        for usuario in self.usuarios:
            usuario.mostrar_info()
            print("---")

class PuestoDeTrabajo:
    def __init__(self, nombre, tipo_de_enfermedades, numero_de_puesto, capacidad):
        self.nombre = nombre
        self.tipo_de_enfermedades = tipo_de_enfermedades
        self.numero_de_puesto = numero_de_puesto
        self.capacidad = capacidad
        self.personas_dentro = 0

    def mostrar_datos(self):
        print(f"\nPuesto de trabajo: {self.nombre}")
        print(f"Tipo de enfermedades: {self.tipo_de_enfermedades}")
        print(f"Número de puesto: {self.numero_de_puesto}")
        print(f"Capacidad: {self.capacidad}")

class Consulta:
    def __init__(self, diagnostico, descripcion, tratamientos, medico, usuario):
        self.diagnostico = diagnostico
        self.descripcion = descripcion
        self.tratamientos = tratamientos
        self.medico = medico
        self.usuario = usuario

class Tratamiento:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Género: {self.genero}")

class Usuario(Persona):
    def __init__(self, nombre, edad, genero, vacunas=None):
        super().__init__(nombre, edad, genero)
        self.vacunas = vacunas if vacunas else []

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Vacunas: {self.vacunas}")

class Paciente(Usuario):
    def __init__(self, nombre, edad, genero, vacunas=None, historial_medico=None):
        super().__init__(nombre, edad, genero, vacunas)
        self.historial_medico = historial_medico if historial_medico else []

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Historial médico: {self.historial_medico}")

class Medico(Usuario):
    def __init__(self, nombre, edad, genero, especialidad):
        super().__init__(nombre, edad, genero)
        self.especialidad = especialidad

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Especialidad: {self.especialidad}")


if __name__ == "__main__":
    feria = FeriaDeSalud("Feria de Salud La Paz", date(2025, 6, 11), "La Paz, Bolivia", "Salud Pública")
    feria.cargar_datos()

    while True:
        print("\n1. Registrar paciente")
        print("2. Registrar médico")
        print("3. Mostrar usuarios")
        print("4. Guardar datos")
        print("5. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            nombre = input("Ingrese nombre del paciente: ")
            edad = int(input("Ingrese edad del paciente: "))
            genero = input("Ingrese género del paciente: ")
            paciente = Paciente(nombre, edad, genero)
            feria.registrar_usuario(paciente)
        elif opcion == "2":
            nombre = input("Ingrese nombre del médico: ")
            edad = int(input("Ingrese edad del médico: "))
            genero = input("Ingrese género del médico: ")
            especialidad = input("Ingrese especialidad del médico: ")
            medico = Medico(nombre, edad, genero, especialidad)
            feria.registrar_usuario(medico)
        elif opcion == "3":
            feria.mostrar_usuarios()
        elif opcion == "4":
            feria.guardar_datos()
            print("Datos guardados correctamente")
        elif opcion == "5":
            break
        else:
            print("Opción inválida")