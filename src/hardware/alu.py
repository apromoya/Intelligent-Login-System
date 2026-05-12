# src/hardware/alu.py

class ALU:
    def __init__(self):
        self.zero_flag = False  # True si son iguales, False si no

    def comparar(self, dato_a, dato_b):
        """
        Comparación simple de texto plano (Arquitectura básica).
        """
        if dato_a == dato_b:
            self.zero_flag = True
        else:
            self.zero_flag = False
        
        return self.zero_flag