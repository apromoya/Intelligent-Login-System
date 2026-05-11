# src/hardware/cpu.py

from .alu import ALU

class CPU:
    def __init__(self):
        self.alu = ALU()  # La CPU tiene su propia unidad aritmética
        self.registro_instruccion = None

    def fetch_decode_execute(self, datos, memoria_ram):
        """
        Ciclo de vida de la instrucción de Login.
        """
        # 1. FETCH & DECODE (Recibir y entender qué nos enviaron)
        username = datos.get("user")
        password_intento = datos.get("pass")
        self.registro_instruccion = "VALIDAR_ACCESO"

        print(f"[CPU]: Ejecutando {self.registro_instruccion} para el usuario: {username}")

        # 2. ACCESO A MEMORIA (RAM)
        # Verificamos si el usuario ya está en la RAM y si está bloqueado
        intentos = memoria_ram.leer_intentos(username)
        
        if intentos >= 3:
            return "ESTADO: BLOQUEADO (Demasiados intentos en RAM)"

        # 3. EXECUTE (Llamamos a la ALU para la comparación lógica)
        # Aquí la CPU le pasa los datos a la ALU para que ella haga el 'trabajo sucio'
        # Simulamos que traemos el hash real de la DB (esto lo haremos más adelante)
        hash_real = "hash_quemado_provisional" # Luego vendrá del archivo/disco
        
        # La ALU procesa y activa sus banderas (flags)
        es_valido = self.alu.comparar(password_intento, hash_real)

        if es_valido:
            memoria_ram.resetear_intentos(username)
            return "ESTADO: ACCESO CONCEDIDO"
        else:
            # Si falla, la CPU ordena a la RAM aumentar el contador
            nuevo_conteo = memoria_ram.registrar_fallo(username)
            return f"ESTADO: ACCESO DENEGADO (Intento {nuevo_conteo}/3)"