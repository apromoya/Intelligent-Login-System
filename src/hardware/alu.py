# src/hardware/alu.py
import hashlib

class ALU:
    def __init__(self):
        """
        Inicializa los registros de estado (Flags) de la ALU.
        """
        # El Zero Flag (Z) se activa si el resultado de una operación es cero.
        # En comparaciones, si (A - B = 0), entonces son iguales.
        self.zero_flag = False
        
        # El Error Flag se activa si los operandos de entrada no son válidos.
        self.error_flag = False

    def comparar(self, password_plano, hash_referencia):
        """
        Operación lógica: VALIDAR_HASH.
        Recibe una señal de entrada (password) y la compara con un registro (hash).
        """
        # 1. Reset de Flags antes de la operación
        self.zero_flag = False
        self.error_flag = False

        if not password_plano or not hash_referencia:
            self.error_flag = True
            print("[ALU]: Error de operandos (Entrada nula).")
            return False

        # 2. PROCESAMIENTO: Transformación de la señal
        # Simulamos que la ALU realiza múltiples operaciones lógicas (XOR, AND, Rotaciones)
        # para generar el hash de la contraseña ingresada.
        try:
            hash_generado = hashlib.sha256(password_plano.encode()).hexdigest()
        except Exception:
            self.error_flag = True
            return False

        # 3. COMPARACIÓN: (Operación de resta lógica)
        # Si hash_generado == hash_referencia, el resultado lógico es "Cero" (igualdad).
        if hash_generado == hash_referencia:
            self.zero_flag = True
            print("[ALU]: Comparación exitosa. Zero Flag -> 1.")
            return True
        else:
            self.zero_flag = False
            print("[ALU]: Comparación fallida. Zero Flag -> 0.")
            return False