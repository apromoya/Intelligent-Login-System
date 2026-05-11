# src/main.py

from hardware.cpu import CPU
from hardware.memory import RAM
from io_interface.port_api import PortAPI

def bootstrap_system():
    """
    Función de arranque (BIOS/Boot) del sistema de login.
    Aquí se inicializan los componentes físicos.
    """
    print("--- Inicializando Sistema de Login Inteligente ---")
    
    # 1. Inicializar Hardware
    memoria_ram = RAM()      # Volátil (Contador de intentos)
    procesador = CPU()       # Unidad de Control
    puerto_entrada = PortAPI() # Interfaz E/S
    
    print("[BIOS]: Hardware detectado y operativo.")
    
    # 2. Ciclo de Ejecución (Main Loop)
    # Simulamos que el sistema está encendido y esperando interrupciones
    while True:
        print("\n[BUS]: Esperando señal de entrada en el puerto...")
        
        # Simulación de recepción de datos por el puerto (Input)
        datos_entrada = puerto_entrada.receive_data()
        
        if datos_entrada == "SHUTDOWN":
            print("[BIOS]: Apagando sistema...")
            break
            
        # 3. La CPU procesa la solicitud enviando las señales a los buses
        resultado = procesador.fetch_decode_execute(datos_entrada, memoria_ram)
        
        # 4. Respuesta del sistema (Output)
        puerto_entrada.send_response(resultado)

if __name__ == "__main__":
    bootstrap_system()