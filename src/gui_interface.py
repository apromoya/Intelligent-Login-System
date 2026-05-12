import tkinter as tk
from tkinter import messagebox
from hardware.cpu import CPU
from hardware.memory import RAM

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Arquitectura de Hardware - Login")
        self.root.geometry("400x350")
        self.root.configure(bg="#f0f0f0")
        
        self.cpu = CPU()
        self.ram = RAM()

        # UI
        tk.Label(root, text="SISTEMA DE LOGUEO", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=20)
        
        tk.Label(root, text="Usuario:", bg="#f0f0f0").pack()
        self.entry_user = tk.Entry(root, font=("Arial", 12))
        self.entry_user.pack(pady=5)
        
        tk.Label(root, text="Contraseña:", bg="#f0f0f0").pack()
        self.entry_pass = tk.Entry(root, show="*", font=("Arial", 12))
        self.entry_pass.pack(pady=5)
        
        self.btn_login = tk.Button(root, text="PROCESAR EN CPU", command=self.ejecutar_login, 
                                bg="#2ecc71", fg="white", font=("Arial", 10, "bold"), width=20)
        self.btn_login.pack(pady=30)

    def abrir_bienvenida(self, usuario):
        # Creamos una nueva ventana (Toplevel)
        ventana_exito = tk.Toplevel(self.root)
        ventana_exito.title("Acceso Concedido")
        ventana_exito.geometry("300x200")
        ventana_exito.configure(bg="#d4edda")
        
        tk.Label(ventana_exito, text=f"¡Bienvenido, {usuario}!", font=("Arial", 14, "bold"), 
                bg="#d4edda", fg="#155724").pack(expand=True)
        
        tk.Button(ventana_exito, text="CERRAR SESIÓN", command=self.root.quit).pack(pady=10)
        
        # Ocultamos la ventana de login
        self.root.withdraw()

    def ejecutar_login(self):
        user = self.entry_user.get()
        password = self.entry_pass.get()
        
        resultado = self.cpu.fetch_decode_execute({"user": user, "pass": password}, self.ram)
        
        if "SUCCESS" in resultado:
            messagebox.showinfo("CPU: ALU OK", "Cotejo de Hash exitoso. Acceso permitido.")
            self.abrir_bienvenida(user)
        else:
            messagebox.showerror("CPU: Error de Seguridad", resultado)
            # Si el mensaje dice bloqueado, deshabilitamos el botón
            if "restringido" in resultado:
                self.btn_login.config(state="disabled", bg="#95a5a6")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()