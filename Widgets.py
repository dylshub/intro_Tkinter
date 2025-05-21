import tkinter as tk
#CREAR ventana
ventana = tk.Tk()
ventana.title("CREACION DE WIDGETS")
ventana.geometry("700x500")

#Crear Widgets
etiqueta = tk.Label(ventana, text = "LABEL 1", font= ("Consolas", 14) ).pack()
boton = tk.Button(ventana, text= " BOTON 1 ", font = ("Consolas", 14)).pack()
entrada = tk.Entry(ventana, font = ("Consolas", 14))
entrada.insert(0,"Ingrese un dato")
entrada.pack()
textBox = tk.Text(ventana).pack()
CheckButton = tk.Checkbutton(ventana, text = " activo ").pack()
RadioButton = tk.Radiobutton(ventana, text = "radio button").pack()
ListBox = tk.Listbox(ventana).pack()
canvas = tk.Canvas(ventana, width=150,height=100, bg = "blue"  ).pack()



ventana.mainloop()