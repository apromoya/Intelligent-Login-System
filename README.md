# Sistema Inteligente de Logueo (Intelligent Login System)
### Simulación de Arquitectura de Computadores - Von Neumann

Este proyecto implementa y simula los componentes principales de la arquitectura de hardware de una computadora (CPU, ALU, RAM, y Storage) aplicados a un sistema de validación de credenciales con interfaz gráfica moderna.

---

## 👥 Integrantes del Proyecto
* **Oscar Alexander Moya López**
* **Yeison Stiven Gómez Cano**
* **Álvaro Palacio Rojas**
* **Wainer Andrey Loaiza**

---

## 🏛️ Arquitectura del Sistema y Componentes

El sistema está diseñado emulando el modelo clásico de **Von Neumann**, donde los datos viajan a través de buses de comunicación entre diferentes componentes de hardware simulados:

### 1. 🧠 Unidad Central de Procesamiento (CPU)
* **Archivo:** `src/hardware/cpu.py`
* **Función:** Es el cerebro del sistema. Orquesta el ciclo **Fetch-Decode-Execute** (Buscar-Decodificar-Ejecutar). Recibe las instrucciones del periférico de entrada, consulta el estado de seguridad en la memoria RAM y coordina la lógica con la ALU y el controlador de almacenamiento.

### 2. ⚡ Unidad Aritmético-Lógica (ALU)
* **Archivo:** `src/hardware/alu.py`
* **Función:** Se encarga de la comparación lógica de los datos. Recibe la información procesada por la CPU, valida si los datos coinciden y activa la **Zero Flag** (Bandera lógica) en `True` o `False` para reportar el éxito o fallo de la operación de cotejo.

### 3. 💾 Memoria de Acceso Aleatorio (RAM)
* **Archivo:** `src/hardware/memory.py`
* **Función:** Memoria volátil del sistema. Almacena en tiempo de ejecución el registro temporal de intentos fallidos por usuario. Implementa políticas de seguridad bloqueando solicitudes si se detectan más de 3 fallos consecutivos en el ciclo de reloj actual. Los datos se limpian al reiniciar el proceso.

### 4. 🗄️ Controlador de Almacenamiento (Storage)
* **Archivo:** `src/hardware/storage.py`
* **Función:** Actúa como el puente o interfaz de entrada/salida entre la CPU y el almacenamiento no volátil. Se encarga de leer el archivo físico en el disco para extraer los registros solicitados.

### 5. 📀 Disco Duro / Base de Datos (JSON)
* **Archivo:** `data/usuarios.json`
* **Función:** Almacenamiento persistente (no volátil). Contiene los registros oficiales de los usuarios del sistema y sus credenciales en texto plano para asegurar una trazabilidad directa del flujo de datos en el bus de sistema.

### 6. 🖥️ Periférico de Entrada/Salida (GUI)
* **Archivo:** `src/gui_interface.py`
* **Función:** Representa la consola moderna y los componentes de hardware visuales. Diseñado con **CustomTkinter**, maneja de forma asíncrona un hilo dedicado a la renderización gráfica (`Main UI Thread`) para mantener la interfaz fluida, interactuando con la lógica de hardware a través de eventos de interrupción (clic del usuario).

---

## 🚀 Requisitos e Instalación

Para ejecutar este simulador en tu máquina local, necesitas tener instalado **Python 3** y la librería gráfica moderna:

```bash
# Instalar la librería gráfica requerida
pip install customtkinter


Ejecución del Sistema
Ubícate en la raíz del proyecto y ejecuta el periférico de interfaz gráfica:
Bash
python src/gui_interface.py
