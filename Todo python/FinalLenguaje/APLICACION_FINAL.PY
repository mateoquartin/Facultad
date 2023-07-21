import tkinter as tk

class ListaTareas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Lista de tareas")

        self.tareas = []
        
        self.input_tarea = tk.Entry(ventana, font=("Arial", 14))
        self.input_tarea.pack(pady=7)
        
        self.agregar_btn = tk.Button(ventana, text="Agregar Tarea", command=self.agregar_tarea)
        self.agregar_btn.pack(pady=5)
        
        self.lista_tareas = tk.Listbox(ventana, width=70, height=20, font=("Arial", 12))
        self.lista_tareas.pack(pady=10)
        
        self.eliminar_btn = tk.Button(ventana, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.eliminar_btn.pack(pady=5)
        
        self.completar_btn = tk.Button(ventana, text="Marcar como Completado", command=self.completar_tarea)
        self.completar_btn.pack(pady=5)

        # Capturar el evento de cierre de la ventana
        self.ventana.protocol("cierre", self.cerrar_ventana)

        # Cargar tareas guardadas en la apertura de la ventana
        self.cargar_tareas()

    def agregar_tarea(self):
        tarea = self.input_tarea.get() # Toma el texto ingresado por el usuario 
        if tarea and not tarea.isdigit(): #evalua si no esta vacia la tarea y si no es solo numeros
            self.tareas.append(tarea)
            self.lista_tareas.insert(tk.END, tarea) # se agrega la tarea en el ultimo de la lista
            self.input_tarea.delete(0, tk.END) # se borra el contenido del cuadro de entrada mediante  
            self.guardar_tareas() 

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection() # crea una tupla con en indice seleccionado 
        if seleccion:
            indice = seleccion[0]
            self.lista_tareas.delete(indice)
            self.tareas.pop(indice) # elimina el elemento de la lista interna 
            self.guardar_tareas()

    def completar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            tarea = self.tareas[indice]
            tarea_completada = tarea + " (comletado)"
            self.lista_tareas.delete(indice)
            self.lista_tareas.insert(indice, tarea_completada)
            self.tareas[indice] = tarea_completada
            self.guardar_tareas()

    def guardar_tareas(self):
        with open("tareas.txt", "w") as archivo:
            for tarea in self.tareas:
                archivo.write(tarea + "\n")

    def cargar_tareas(self):
        try:
            with open("tareas.txt", "r") as archivo:
                tareas_guardadas = archivo.readlines()
                for tarea in tareas_guardadas:
                    self.tareas.append(tarea.strip())
                    self.lista_tareas.insert(tk.END, tarea.strip())
        except FileNotFoundError:
            pass

    def cerrar_ventana(self):
        self.guardar_tareas()
        self.ventana.destroy()

ventana = tk.Tk()
app = ListaTareas(ventana)
ventana.mainloop()
