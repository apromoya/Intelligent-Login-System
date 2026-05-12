# src/io_interface/port_api.py

class PortAPI:
    def __init__(self):
        """
        Inicializa los registros de entrada y salida (I/O Registers).
        """
        print("[PUERTO]: Inicializando registros de comunicación...")

    def recibir_peticion(self):
        """
        Simulación de interrupción de entrada (Input Interrupt).
        Captura los datos del periférico y los prepara para el Bus de Datos.
        """
        print("\n" + "="*30)
        print("  SISTEMA ESPERANDO ENTRADA  ")
        print("="*30)
        
        # Simulamos la captura de señales del teclado
        usuario = input(">> Ingrese Usuario (o 'exit' para apagar): ").strip()
        
        # Señal de apagado (Interrupt Signal)
        if usuario.lower() == "exit":
            return "OFF"
            
        password = input(">> Ingrese Password: ").strip()
        
        # Devolvemos un paquete de datos listo para la CPU
        return {
            "user": usuario,
            "pass": password
        }

    def enviar_respuesta(self, mensaje):
        """
        Simulación de señal de salida (Output Signal).
        Muestra el resultado del procesamiento en el monitor/periférico.
        """
        print("\n[PUERTO - SEÑAL DE SALIDA]:")
        print(f" > {mensaje}")
        print("-" * 30)