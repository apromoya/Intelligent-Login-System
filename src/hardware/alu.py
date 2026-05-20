# src/hardware/alu.py
import bcrypt

class ALU:
    def __init__(self):
        self.zero_flag = False  # True si son iguales, False si no

    def comparar(self, dato_a, dato_b):
        """
        Verificación segura mediante bcrypt.checkpw.
        dato_a: contraseña ingresada (texto plano)
        dato_b: hash bcrypt almacenado en disco
        """
        try:
            self.zero_flag = bcrypt.checkpw(
                dato_a.encode("utf-8"),
                dato_b.encode("utf-8")
            )
        except Exception:
            self.zero_flag = False

        return self.zero_flag