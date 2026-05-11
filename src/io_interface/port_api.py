class PortAPI:
    def receive_data(self):
        user = input("User: ")
        if user == "exit": return "SHUTDOWN"
        password = input("Pass: ")
        return {"user": user, "pass": password}

    def send_response(self, mensaje):
        print(f"[PORT]: Respuesta enviada -> {mensaje}")