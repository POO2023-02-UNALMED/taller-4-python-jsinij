from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=[]):
        self._grupo = grupo
        if asignaturas == None:
            self._asignaturas = []
        else:
            self._asignaturas = asignaturas
        if estudiantes == None:
            self.listadoAlumnos = []
        else:
            self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None: 
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self):
        return (f"Grupo de estudiantes: {self._grupo}")


    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        if nombre == None:
            cls.grado = "Grado 6"
            return
        cls.grado = nombre
        

