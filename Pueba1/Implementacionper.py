import pickle
from datetime import date

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
        self.codigo = None

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Historial médico: {self.historial_medico}")
        print(f"Código: {self.codigo}")

class Medico(Usuario):
    def __init__(self, nombre, edad, genero, especialidad):
        super().__init__(nombre, edad, genero)
        self.especialidad = especialidad
        self.codigo = None

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Especialidad: {self.especialidad}")
        print(f"Código: {self.codigo}")

class Tratamiento:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

class Consulta:
    def __init__(self, diagnostico, descripcion, tratamientos, medico, usuario, fecha=None):
        self.diagnostico = diagnostico
        self.descripcion = descripcion
        self.tratamientos = tratamientos
        self.medico = medico
        self.usuario = usuario
        self.fecha = fecha

def guardar_pacientes(pacientes, archivo='pacientes.dat'):
    with open(archivo, 'wb') as f:
        datos = [(f"P{str(i+1).zfill(2)}", p.nombre) for i, p in enumerate(pacientes)]
        for i, p in enumerate(pacientes):
            p.codigo = f"P{str(i+1).zfill(2)}"
        pickle.dump(datos, f)

def cargar_pacientes(archivo='pacientes.dat'):
    pacientes = []
    try:
        with open(archivo, 'rb') as f:
            datos = pickle.load(f)
            for codigo, nombre in datos:
                paciente = Paciente(nombre, edad=0, genero='Desconocido')
                paciente.codigo = codigo
                pacientes.append(paciente)
    except FileNotFoundError:
        pass
    return pacientes

def guardar_medicos(medicos, archivo='medicos.dat'):
    with open(archivo, 'wb') as f:
        datos = [(f"Med{str(i+1)}", m.nombre, m.especialidad) for i, m in enumerate(medicos)]
        for i, m in enumerate(medicos):
            m.codigo = f"Med{str(i+1)}"
        pickle.dump(datos, f)

def cargar_medicos(archivo='medicos.dat'):
    medicos = []
    try:
        with open(archivo, 'rb') as f:
            datos = pickle.load(f)
            for codigo, nombre, especialidad in datos:
                medico = Medico(nombre, edad=0, genero='Desconocido', especialidad=especialidad)
                medico.codigo = codigo
                medicos.append(medico)
    except FileNotFoundError:
        pass
    return medicos

def guardar_consultas(consultas, archivo='consultas.dat'):
    with open(archivo, 'wb') as f:
        datos = []
        for c in consultas:
            fecha = c.fecha if c.fecha else 'Desconocida'
            codigo_paciente = c.usuario.codigo if hasattr(c.usuario, 'codigo') else 'P00'
            codigo_medico = c.medico.codigo if hasattr(c.medico, 'codigo') else 'Med0'
            diagnostico = c.diagnostico
            tratamiento = c.tratamientos[0].nombre if c.tratamientos else 'Sin tratamiento'
            datos.append((fecha, codigo_paciente, codigo_medico, diagnostico, tratamiento))
        pickle.dump(datos, f)

def cargar_consultas(archivo='consultas.dat'):
    consultas = []
    try:
        with open(archivo, 'rb') as f:
            datos = pickle.load(f)
            for fecha, codigo_paciente, codigo_medico, diagnostico, tratamiento in datos:
                paciente = Paciente("Desconocido", 0, "Desconocido")
                paciente.codigo = codigo_paciente
                medico = Medico("Desconocido", 0, "Desconocido", "Desconocida")
                medico.codigo = codigo_medico
                tratamiento_obj = Tratamiento(tratamiento, "Descripción no disponible")
                consulta = Consulta(diagnostico, "", [tratamiento_obj], medico, paciente, fecha=fecha)
                consultas.append(consulta)
    except FileNotFoundError:
        pass
    return consultas

class FeriaDeSalud:
    def __init__(self, nombre, fecha, lugar, tipo):
        self.nombre = nombre
        self.fecha = fecha
        self.lugar = lugar
        self.tipo = tipo
        self.usuarios = []
        self.medicos = []
        self.consultas = []

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def mostrar_usuarios(self):
        print(f"\nLista de participantes registrados en '{self.nombre}':\n")
        for usuario in self.usuarios:
            usuario.mostrar_info()
            print("---")

    def guardar_todo(self):
        guardar_pacientes(self.usuarios)
        guardar_medicos(self.medicos)
        guardar_consultas(self.consultas)

def casos_de_ejemplo():
    feria = FeriaDeSalud("Feria de Salud La Paz", date(2025, 6, 11), "La Paz, Bolivia", "Salud Pública")

    p1 = Paciente("Ana", 30, "Femenino", vacunas=["COVID-19", "Influenza"])
    p2 = Paciente("Pedro", 45, "Masculino", vacunas=["Hepatitis B"])
    p3 = Paciente("Luis", 60, "Masculino")
    p4 = Paciente("Maria", 25, "Femenino", vacunas=["COVID-19"])
    p5 = Paciente("Carlos", 50, "Masculino")

    m1 = Medico("Jorge", 40, "Masculino", "Pediatría")
    m2 = Medico("Rocío", 38, "Femenino", "Cardiología")

    t1 = Tratamiento("Antibióticos", "Tratamiento con antibióticos para infecciones")
    t2 = Tratamiento("Terapia Física", "Sesiones de terapia para recuperación")
    t3 = Tratamiento("Control de presión", "Monitoreo y medicación para hipertensión")
    t4 = Tratamiento("Vacunación", "Aplicación de vacunas preventivas")
    t5 = Tratamiento("Consejería nutricional", "Asesoría sobre alimentación saludable")

    c1 = Consulta("Infección Respiratoria", "Paciente con tos y fiebre", [t1], m1, p1, fecha=date(2025, 6, 10))
    c2 = Consulta("Hipertensión", "Paciente con presión alta", [t3], m2, p2, fecha=date(2025, 6, 9))
    c3 = Consulta("Chequeo General", "Revisión anual", [t5], m1, p3, fecha=date(2025, 6, 8))
    c4 = Consulta("Vacunación COVID-19", "Aplicación de refuerzo", [t4], m1, p4, fecha=date(2025, 6, 7))
    c5 = Consulta("Dolor muscular", "Paciente con dolor lumbar", [t2], m2, p5, fecha=date(2025, 6, 6))

    for paciente in [p1, p2, p3, p4, p5]:
        feria.registrar_usuario(paciente)
    for medico in [m1, m2]:
        feria.medicos.append(medico)
    for consulta in [c1, c2, c3, c4, c5]:
        feria.consultas.append(consulta)

    feria.guardar_todo()

    print("\n--- Feria de Salud La Paz - Participantes ---")
    feria.mostrar_usuarios()

    print("\n--- Médicos Registrados ---")
    for medico in feria.medicos:
        medico.mostrar_info()
        print("---")
    print("\n--- Consultas Registradas ---")
    for consulta in feria.consultas:
        print(f"Fecha: {consulta.fecha}")
        print(f"Paciente: {consulta.usuario.nombre} (Código: {consulta.usuario.codigo})")
        print(f"Médico: {consulta.medico.nombre} (Código: {consulta.medico.codigo})")
        print(f"Diagnóstico: {consulta.diagnostico}")
        print(f"Tratamiento: {consulta.tratamientos[0].nombre if consulta.tratamientos else 'Ninguno'}")
        print("---")

if __name__ == "__main__":
    casos_de_ejemplo()
