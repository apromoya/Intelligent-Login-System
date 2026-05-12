from .alu import ALU
from .storage import Storage

class CPU:
    def __init__(self):
        self.alu = ALU()
        self.storage = Storage()

    def fetch_decode_execute(self, datos, memoria_ram):
        username = datos.get("user")
        password_intento = datos.get("pass")

        # REQUERIMIENTO 2: Contar intentos desde el inicio
        # No importa si el usuario existe o no, el intento se registra
        intentos = memoria_ram.leer_intentos(username)
        
        if intentos >= 3:
            return "BLOQUEADO: Seguridad activada por exceso de actividad."

        # Buscamos en el almacenamiento
        hash_real = self.storage.leer_usuario(username)
        
        # Si el usuario no existe, igual contamos el fallo para evitar rastreo
        if not hash_real:
            memoria_ram.registrar_fallo(username)
            return "ERROR: Credenciales inválidas."

        # REQUERIMIENTO 1: Validación real con la ALU
        es_valido = self.alu.comparar(password_intento, hash_real)

        if self.alu.zero_flag:
            memoria_ram.resetear_intentos(username)
            return "SUCCESS: Acceso concedido al sistema."
        else:
            nuevo_conteo = memoria_ram.registrar_fallo(username)
            return f"ERROR: Credenciales inválidas. (Intento {nuevo_conteo}/3)"