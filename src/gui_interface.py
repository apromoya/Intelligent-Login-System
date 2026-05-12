import tkinter as tk
from tkinter import messagebox
from hardware.cpu import CPU
from hardware.memory import RAM

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Login Inteligente - Arq. Hardware")
        self.root.geometry("400x300")
        
        # Inicializar Hardware
        self.cpu = CPU()
        self.ram = RAM()

        # UI Elements
        tk.Label(root, text="SISTEMA DE LOGUEO", font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Label(root, text="Usuario:").pack()
        self.entry_user = tk.Entry(root)
        self.entry_user.pack(pady=5)
        
        tk.Label(root, text="Contraseña:").pack()
        self.entry_pass = tk.Entry(root, show="*")
        self.entry_pass.pack(pady=5)
        
        self.btn_login = tk.Button(root, text="PROCESAR EN CPU", command=self.ejecutar_login, bg="#4CAF50", fg="white")
        self.btn_login.pack(pady=20)

    def ejecutar_login(self):
        datos = {
            "user": self.entry_user.get(),
            "pass": self.entry_pass.get()
        }
        
        # Enviamos los datos al "Bus" hacia la CPU
        resultado = self.cpu.fetch_decode_execute(datos, self.ram)
        
        # Manejo de respuestas visuales
        if "SUCCESS" in resultado:
            messagebox.showinfo("Bus de Datos", resultado)
            self.root.configure(bg="#d4edda")
        elif "BLOQUEADO" in resultado:
            messagebox.showerror("ALERTA DE HARDWARE", resultado)
            self.btn_login.config(state="disabled")
        else:
            messagebox.showwarning("Fallo de Validación", resultado)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()