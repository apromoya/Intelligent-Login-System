# src/hardware/cpu.py
from .alu import ALU
from .storage import Storage

class CPU:
    def __init__(self):
        self.alu = ALU()
        self.storage = Storage()

    def fetch_decode_execute(self, datos, memoria_ram):
        username = datos.get("user")
        password_intento = datos.get("pass")
        
        # 1. Verificación de intentos en RAM
        intentos = memoria_ram.leer_intentos(username)
        if intentos >= 3:
            return "ERROR: Usuario bloqueado por seguridad."

        # 2. Leer del Storage
        password_real = self.storage.leer_usuario(username)
        
        if password_real is None:
            memoria_ram.registrar_fallo(username)
            return "ERROR: Credenciales inválidas."

        # 3. Comparación directa en ALU
        self.alu.comparar(password_intento, password_real)

        if self.alu.zero_flag:
            memoria_ram.resetear_intentos(username)
            return "SUCCESS: Acceso concedido."
        else:
            nuevo_conteo = memoria_ram.registrar_fallo(username)
            return f"ERROR: Credenciales inválidas. (Intento {nuevo_conteo}/3)"