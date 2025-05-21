import tkinter as tk

def Abrir_Ventana():
    ventana2 = tk.Toplevel()
    ventana2.title("Ventana secundaria")
    ventana2.geometry("200x100")
    tk.Label(ventana2, text = "VENTANA 2").pack()


ventana = tk.Tk()
ventana.title("VENTANA PRINCIPAL")
ventana.geometry("500x300")

boton = tk.Button(ventana, text ="Abrir ventana", command = Abrir_Ventana)
boton.pack()
ventana.mainloop()
