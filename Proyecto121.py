import pickle

class Evaluacion:
    def __init__(self, nom="", pat="", mat="", p1=0, p2=0, ef=0, aux=0, prac=0):
        self.nom = nom
        self.pat = pat
        self.mat = mat
        self.primer_parcial = p1
        self.segundo_parcial = p2
        self.examen_final = ef
        self.auxiliatura = aux
        self.practicas = prac

    def leer(self):
        self.nom = input("Nombre: ")
        self.pat = input("Apellido paterno: ")
        self.mat = input("Apellido materno: ")
        self.primer_parcial = int(input("Primer parcial: "))
        self.segundo_parcial = int(input("Segundo parcial: "))
        self.examen_final = int(input("Examen final: "))
        self.auxiliatura = int(input("Auxiliatura: "))
        self.practicas = int(input("Prácticas: "))

    def mostrar(self):
        print(f"{self.nom} {self.pat} {self.mat} - Nota total: {self.nota_total()}")

    def mostrar_nota_total(self):
        print(f"{self.nom} {self.pat} {self.mat} ---> {self.nota_total()}")

    def nota_total(self):
        return self.primer_parcial + self.segundo_parcial + self.examen_final + self.auxiliatura + self.practicas

    def esta_aprobado(self):
        return self.nota_total() >= 51


class Archivo:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def crear(self):
        try:
            with open(self.nombre_archivo, "wb") as archivo:
                pass
            print("Archivo creado correctamente.")
        except Exception as e:
            print(f"Error al crear el archivo: {e}")

    def adicionar(self):
        try:
            with open(self.nombre_archivo, "ab") as archivo:
                evaluacion = Evaluacion()
                evaluacion.leer()
                pickle.dump(evaluacion, archivo)
                print("Evaluación adicionada correctamente.")
        except Exception as e:
            print(f"Error al adicionar: {e}")

    def listar(self):
        try:
            with open(self.nombre_archivo, "rb") as archivo:
                lista = []
                while True:
                    try:
                        evaluacion = pickle.load(archivo)
                        lista.append(evaluacion)
                    except EOFError:
                        break
                return lista
        except Exception as e:
            print(f"Error al leer: {e}")
            return []


def main():
    archivo = Archivo("evaluaciones.dat")

    while True:
        print("1. Crear")
        print("2. Adicionar")
        print("3. Listar")
        print("4. Mostrar nota total")
        print("5. Mostrar cantidad de aprobados y reprobados")
        print("0. Salir")
        opc = input("Elegir una opción: ")

        if opc == "1":
            archivo.crear()
        elif opc == "2":
            archivo.adicionar()
        elif opc == "3":
            lista = archivo.listar()
            for evaluacion in lista:
                evaluacion.mostrar()
            print("Fin listado!!!")
        elif opc == "4":
            lista = archivo.listar()
            for evaluacion in lista:
                evaluacion.mostrar_nota_total()
        elif opc == "5":
            lista = archivo.listar()
            aprobados = sum(1 for evaluacion in lista if evaluacion.esta_aprobado())
            reprobados = len(lista) - aprobados
            print(f"Cantidad de aprobados: {aprobados}")
            print(f"Cantidad de reprobados: {reprobados}")
        elif opc == "0":
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")


if __name__ == "__main__":
    main()