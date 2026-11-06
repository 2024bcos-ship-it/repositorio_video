import tkinter as tk
from time import strftime

# --- FUNCIONES DE CONTROL continuar---
def encender_led():
    # Cambia el color del círculo del LED a amarillo brillante
    canvas_led.itemconfig(led, fill="#FFFF00", outline="#FFCC00")
    label_estado.config(text="Estado: ENCENDIDO", fg="#FFCC00")

def apagar_led():
    # Cambia el color del círculo del LED a un amarillo oscuro/apagado
    canvas_led.itemconfig(led, fill="#555500", outline="#333300")
    label_estado.config(text="Estado: APAGADO", fg="#888888")

def actualizar_reloj():
    # Obtiene la fecha y hora actual en tiempo real
    fecha_hora_actual = strftime("%d/%m/%Y   %H:%M:%S")
    display_reloj.config(text=fecha_hora_actual)
    # Se ejecuta a sí misma cada 1000 milisegundos (1 segundo)
    display_reloj.after(1000, actualizar_reloj)

# --- VENTANA PRINCIPAL ---
ventana = tk.Tk()
ventana.title("Panel de Control - LED & Sensores")
ventana.geometry("450x500")
ventana.configure(bg="#1E1E1E")  # Fondo oscuro estilo VS Code
ventana.resizable(False, False)

# --- SECCIÓN 1: RELOJ (FECHA Y HORA) ---
frame_reloj = tk.LabelFrame(ventana, text=" FECHA Y HORA ", fg="#00FF00", bg="#1E1E1E", font=("Arial", 10, "bold"), padx=10, pady=10)
frame_reloj.pack(fill="x", padx=20, pady=15)

display_reloj = tk.Label(frame_reloj, text="", font=("Consolas", 18, "bold"), fg="#00FF00", bg="#000000", bd=5, relief="sunken", width=22)
display_reloj.pack(pady=5)

# --- SECCIÓN 2: CONTROL DEL LED ---
frame_led = tk.LabelFrame(ventana, text=" CONTROL DE LED ", fg="#FFFFFF", bg="#1E1E1E", font=("Arial", 10, "bold"), padx=10, pady=10)
frame_led.pack(fill="x", padx=20, pady=15)

# Interfaz visual del LED (Canvas)
canvas_led = tk.Canvas(frame_led, width=60, height=60, bg="#1E1E1E", highlightthickness=0)
canvas_led.pack(pady=5)
# Inicializa el LED apagado (amarillo oscuro)
led = canvas_led.create_oval(10, 10, 50, 50, fill="#555500", outline="#333300", width=2)

label_estado = tk.Label(frame_led, text="Estado: APAGADO", font=("Arial", 10, "bold"), fg="#888888", bg="#1E1E1E")
label_estado.pack()

# Contenedor para alinear los botones de lado a lado
frame_botones = tk.Frame(frame_led, bg="#1E1E1E")
frame_botones.pack(pady=10)

btn_encender = tk.Button(frame_botones, text="ENCENDER", font=("Arial", 11, "bold"), bg="#2ECC71", fg="white", activebackground="#27AE60", width=12, command=encender_led)
btn_encender.pack(side="left", padx=10)

btn_apagar = tk.Button(frame_botones, text="APAGAR", font=("Arial", 11, "bold"), bg="#E74C3C", fg="white", activebackground="#C0392B", width=12, command=apagar_led)
btn_apagar.pack(side="right", padx=10)

# --- SECCIÓN 3: DISPLAY DE TEMPERATURA ---
frame_temp = tk.LabelFrame(ventana, text=" MONITOR DE TEMPERATURA ", fg="#3498DB", bg="#1E1E1E", font=("Arial", 10, "bold"), padx=10, pady=10)
frame_temp.pack(fill="x", padx=20, pady=15)

# Entrada de texto para simular o ingresar el dato del sensor
label_instruccion = tk.Label(frame_temp, text="Ingresa la temperatura (°C):", fg="#FFFFFF", bg="#1E1E1E")
label_instruccion.pack(side="left", padx=5)

entrada_temp = tk.Entry(frame_temp, font=("Arial", 12), width=8, justify="center")
entrada_temp.pack(side="left", padx=5)
entrada_temp.insert(0, "24.5")  # Valor inicial por defecto

# Display digital para mostrar el valor final
display_temp = tk.Label(frame_temp, text="24.5 °C", font=("Consolas", 18, "bold"), fg="#3498DB", bg="#000000", bd=5, relief="sunken", width=8)
display_temp.pack(side="right", padx=10)

# Función para actualizar el display cuando el usuario escribe en la entrada
def actualizar_temp(*args):
    valor = entrada_temp.get()
    if valor:
        display_temp.config(text=f"{valor} °C")
    else:
        display_temp.config(text="--.- °C")

# Vincula la escritura del teclado para que el display cambie automáticamente
entrada_temp.bind("<KeyRelease>", actualizar_temp)

# --- INICIAR PROCESOS ---
actualizar_reloj()  # Activa el bucle del reloj de fondo
ventana.mainloop()  # Muestra la interfaz en pantalla
