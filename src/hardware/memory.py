# src/hardware/memory.py

class RAM:
    def __init__(self):
        # Nuestro banco de memoria volátil
        self.celdas_intentos = {}

    def leer_intentos(self, usuario):
        return self.celdas_intentos.get(usuario, 0)

    def registrar_fallo(self, usuario):
        actual = self.celdas_intentos.get(usuario, 0)
        self.celdas_intentos[usuario] = actual + 1
        return self.celdas_intentos[usuario]

    def resetear_intentos(self, usuario):
        if usuario in self.celdas_intentos:
            self.celdas_intentos[usuario] = 0