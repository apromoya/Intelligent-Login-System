# src/hardware/memory.py

class RAM:
    def __init__(self):
        """
        Inicializa los bancos de memoria volátil.
        En una arquitectura real, estos serían registros o celdas de memoria.
        """
        # Simulamos las celdas de memoria usando un diccionario
        # donde la llave es la dirección (usuario) y el valor es el dato (intentos).
        self.celdas_intentos = {}

    def leer_intentos(self, usuario):
        """
        Operación de LECTURA de memoria.
        La CPU pide el dato almacenado en la 'dirección' del usuario.
        """
        # Si el usuario no está en memoria, devolvemos 0 (dato por defecto)
        return self.celdas_intentos.get(usuario, 0)

    def registrar_fallo(self, usuario):
        """
        Operación de ESCRITURA/ACTUALIZACIÓN.
        Simula el incremento de un valor en un registro de memoria.
        """
        intentos_actuales = self.leer_intentos(usuario)
        nuevo_valor = intentos_actuales + 1
        self.celdas_intentos[usuario] = nuevo_valor
        
        print(f"[RAM]: Celda de memoria '{usuario}' actualizada a {nuevo_valor}.")
        return nuevo_valor

    def resetear_intentos(self, usuario):
        """
        Operación de LIMPIEZA (Clear).
        Se ejecuta cuando la CPU detecta un acceso exitoso (Zero Flag activo).
        """
        if usuario in self.celdas_intentos:
            self.celdas_intentos[usuario] = 0
            print(f"[RAM]: Celda de memoria '{usuario}' reseteada a 0.")