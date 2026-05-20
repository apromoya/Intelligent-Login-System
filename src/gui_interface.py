import customtkinter as ctk
from hardware.cpu import CPU
from hardware.memory import RAM

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

BG       = "#0d1117"
CARD     = "#161b22"
BORDER   = "#30363d"
SURFACE  = "#21262d"
ACCENT   = "#00d26a"
ACCENT_H = "#00b359"
TEXT     = "#e6edf3"
MUTED    = "#8b949e"
ERR      = "#f85149"
SUCCESS  = "#3fb950"
MEMBER_C = ["#58a6ff", "#f78166", "#ffa657", "#bc8cff"]

# ── Datos del equipo ──────────────────────────────────────────────
MEMBERS = ["Oscar", "Yeison", "Alvaro", "Wainer"]
ICONS   = ["💻", "⚙️", "🔧", "🛡️"]


# ── Helpers de UI ─────────────────────────────────────────────────
def _sep(parent, pady=(0, 0)):
    ctk.CTkFrame(parent, height=1, fg_color=BORDER).pack(fill="x", padx=28, pady=pady)


def _entry(parent, placeholder, show=None):
    kw = dict(
        placeholder_text=placeholder, height=44, corner_radius=10,
        font=("Arial", 12), fg_color=SURFACE, border_color=BORDER,
        text_color=TEXT, placeholder_text_color=MUTED,
    )
    if show:
        kw["show"] = show
    return ctk.CTkEntry(parent, **kw)


# ── Aplicación principal ──────────────────────────────────────────
class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.cpu = CPU()
        self.ram = RAM()
        self.title("Sistema de Login — Arquitectura de Hardware")
        self.geometry("460x570")
        self.resizable(False, False)
        self.configure(fg_color=BG)
        self._build_login()

    # ── PANTALLA DE LOGIN ─────────────────────────────────────────
    def _build_login(self):
        for w in self.winfo_children():
            w.destroy()

        card = ctk.CTkFrame(self, fg_color=CARD, corner_radius=20,
                            border_width=1, border_color=BORDER)
        card.place(relx=.5, rely=.5, anchor="center", relwidth=.88, relheight=.90)

        ctk.CTkLabel(card, text="🔐", font=("Arial", 46)).pack(pady=(32, 4))
        ctk.CTkLabel(card, text="SISTEMA DE LOGIN",
                     font=("Arial", 21, "bold"), text_color=TEXT).pack()
        ctk.CTkLabel(card, text="Arquitectura de Hardware",
                     font=("Arial", 11), text_color=MUTED).pack(pady=(2, 18))

        _sep(card)

        ctk.CTkLabel(card, text="Usuario", font=("Arial", 11, "bold"),
                     text_color=MUTED, anchor="w").pack(padx=36, fill="x", pady=(14, 0))
        self.entry_user = _entry(card, "Ingresa tu usuario")
        self.entry_user.pack(padx=36, fill="x", pady=(4, 12))

        ctk.CTkLabel(card, text="Contraseña", font=("Arial", 11, "bold"),
                     text_color=MUTED, anchor="w").pack(padx=36, fill="x")
        self.entry_pass = _entry(card, "Ingresa tu contraseña", show="*")
        self.entry_pass.pack(padx=36, fill="x", pady=(4, 20))

        self.btn_login = ctk.CTkButton(
            card, text="⚡  PROCESAR EN CPU", height=46, corner_radius=12,
            font=("Arial", 13, "bold"), fg_color=ACCENT, hover_color=ACCENT_H,
            text_color="#0d1117", command=self._on_login,
        )
        self.btn_login.pack(padx=36, fill="x")

        self.lbl_status = ctk.CTkLabel(card, text="", font=("Arial", 11), text_color=MUTED)
        self.lbl_status.pack(pady=(8, 0))

        _sep(card, pady=(14, 8))
        ctk.CTkLabel(card, text="Equipo desarrollador",
                     font=("Arial", 10), text_color=MUTED).pack()

        row = ctk.CTkFrame(card, fg_color="transparent")
        row.pack(pady=(6, 22))
        for i, name in enumerate(MEMBERS):
            ctk.CTkLabel(row, text=name, font=("Arial", 10, "bold"),
                         text_color=MEMBER_C[i], fg_color=SURFACE,
                         corner_radius=8, width=72, height=26).grid(row=0, column=i, padx=4)

        self.bind("<Return>", lambda _: self._on_login())
        self.entry_user.focus()

    def _on_login(self):
        user = self.entry_user.get().strip()
        pwd  = self.entry_pass.get()
        if not user or not pwd:
            self.lbl_status.configure(text="⚠  Completa todos los campos",
                                      text_color="#ffa657")
            return
        self.btn_login.configure(text="⏳  Procesando...", state="disabled")
        self.after(700, lambda: self._procesar(user, pwd))

    def _procesar(self, user, pwd):
        resultado = self.cpu.fetch_decode_execute({"user": user, "pass": pwd}, self.ram)
        if "SUCCESS" in resultado:
            self.lbl_status.configure(text="✔  Hash verificado — Acceso concedido",
                                      text_color=SUCCESS)
            self.after(900, lambda: self._abrir_bienvenida(user))
        else:
            self.btn_login.configure(text="⚡  PROCESAR EN CPU", state="normal")
            self.lbl_status.configure(
                text=f"✘  {resultado.replace('ERROR: ', '')}", text_color=ERR)
            self.entry_pass.delete(0, "end")
            # BUG FIX: se verifica "bloqueado" (antes buscaba "restringido" incorrectamente)
            if "bloqueado" in resultado:
                self.btn_login.configure(state="disabled", fg_color=SURFACE,
                                         hover_color=SURFACE,
                                         text="🔒  ACCESO BLOQUEADO", text_color=ERR)

    # ── PANTALLA DE BIENVENIDA ────────────────────────────────────
    def _abrir_bienvenida(self, usuario):
        self.withdraw()

        win = ctk.CTkToplevel()
        win.title("Acceso Concedido")
        win.geometry("500x600")
        win.resizable(False, False)
        win.configure(fg_color=BG)
        win.protocol("WM_DELETE_WINDOW", lambda: (win.destroy(), self.quit()))

        card = ctk.CTkFrame(win, fg_color=CARD, corner_radius=20,
                            border_width=1, border_color=BORDER)
        card.place(relx=.5, rely=.5, anchor="center", relwidth=.88, relheight=.92)

        # Badge de acceso concedido
        badge = ctk.CTkFrame(card, fg_color="#1a3a2a", corner_radius=16,
                             border_width=1, border_color=SUCCESS)
        badge.pack(pady=(28, 0), padx=70)
        ctk.CTkLabel(badge, text="✔  ACCESO CONCEDIDO", font=("Arial", 11, "bold"),
                     text_color=SUCCESS).pack(padx=16, pady=8)

        ctk.CTkLabel(card, text="👋", font=("Arial", 50)).pack(pady=(14, 0))
        ctk.CTkLabel(card, text="¡Bienvenido!", font=("Arial", 16),
                     text_color=MUTED).pack()
        ctk.CTkLabel(card, text=usuario.upper(), font=("Arial", 28, "bold"),
                     text_color=ACCENT).pack(pady=(2, 4))

        _sep(card, pady=(12, 12))

        ctk.CTkLabel(card, text="EQUIPO DE DESARROLLO",
                     font=("Arial", 11, "bold"), text_color=MUTED).pack()

        # Tarjetas del equipo en cuadrícula 2x2
        grid = ctk.CTkFrame(card, fg_color="transparent")
        grid.pack(pady=12, padx=22, fill="x")
        grid.columnconfigure((0, 1), weight=1)

        for i, (name, icon) in enumerate(zip(MEMBERS, ICONS)):
            r, c = divmod(i, 2)
            mc = ctk.CTkFrame(grid, fg_color=SURFACE, corner_radius=14,
                              border_width=1, border_color=MEMBER_C[i])
            mc.grid(row=r, column=c, padx=7, pady=7, sticky="ew")
            ctk.CTkLabel(mc, text=icon, font=("Arial", 26)).pack(pady=(14, 2))
            ctk.CTkLabel(mc, text=name, font=("Arial", 14, "bold"),
                         text_color=MEMBER_C[i]).pack()
            ctk.CTkLabel(mc, text="Desarrollador", font=("Arial", 10),
                         text_color=MUTED).pack(pady=(2, 14))

        _sep(card, pady=(10, 14))

        ctk.CTkButton(
            card, text="🚪  CERRAR SESIÓN", height=42, corner_radius=12,
            font=("Arial", 12, "bold"), fg_color="#2a1a1a",
            hover_color="#4a2020", text_color=ERR,
            border_width=1, border_color=ERR,
            command=lambda: (win.destroy(), self.quit()),
        ).pack(padx=36, fill="x", pady=(0, 22))


if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()