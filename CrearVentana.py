import tkinter as tk

ventana = tk.Tk() #Crear ventana
ventana.title("Mi primera app")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text = "¡Hola Mundo!")
etiqueta.pack()

ventana.mainloop() #Mantener ventana en pantalla