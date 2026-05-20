import json
import os
import bcrypt

class Storage:
    def __init__(self):
        """
        Inicializa el controlador de almacenamiento secundario.
        Define la ruta física hacia el disco (archivo JSON).
        """
        # Obtenemos la ruta absoluta de este archivo para localizar 'data/usuarios.json'
        # sin importar desde qué carpeta ejecutes el programa.
        base_dir = os.path.dirname(__file__)
        self.path = os.path.abspath(os.path.join(base_dir, '../../data/usuarios.json'))

    def leer_usuario(self, usuario):
        """
        Operación de lectura de sectores de disco.
        La CPU solicita el hash de un usuario específico.
        """
        try:
            # Simulamos el acceso al bus de E/S del disco
            with open(self.path, 'r') as archivo:
                # Cargamos la tabla de descriptores (Base de datos)
                base_datos = json.load(archivo)
                
                # Buscamos el dato en el almacenamiento persistente
                return base_datos.get(usuario)
        except FileNotFoundError:
            print(f"[ERROR DE HARDWARE]: Disco no detectado en la ruta: {self.path}")
            return None
        except json.JSONDecodeError:
            print("[ERROR DE HARDWARE]: Sectores de disco corruptos (JSON mal formado).")
            return None

    def escribir_usuario(self, usuario, hash_bcrypt):
        """
        Operación de escritura — almacena el hash bcrypt del usuario.
        """
        try:
            with open(self.path, 'r+') as archivo:
                datos = json.load(archivo)
                datos[usuario] = hash_bcrypt
                archivo.seek(0)
                json.dump(datos, archivo, indent=4)
                archivo.truncate()
                return True
        except Exception as e:
            print(f"[ERROR]: Fallo en la escritura de disco: {e}")
            return False

    def registrar_usuario(self, usuario, password_plano):
        """
        Hashea la contraseña con bcrypt (salt automático, 12 rondas)
        y la persiste en el almacenamiento.
        """
        hash_pwd = bcrypt.hashpw(password_plano.encode("utf-8"), bcrypt.gensalt(rounds=12))
        return self.escribir_usuario(usuario, hash_pwd.decode("utf-8"))