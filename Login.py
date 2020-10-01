import tkinter 
from tkinter import messagebox
from Registro import Registro
from firebase import firebase as fb
from Game import Game

class Login:

    def __init__(self):
        self = self

    def transicion_registro(self, ventana):
        ventana.destroy()
        ventana.quit()
        Registro(self).start()

    def center(self, toplevel):
       toplevel.update_idletasks()
       w = toplevel.winfo_screenwidth()
       h = toplevel.winfo_screenheight()
       size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
       x = w/2 - size[0]/2
       y = h/2 - size[1]/2
       toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

    def start(self):
        familia_fuente = "Cambria"
        tamanio_fuente = 12
        color_botones = "#A74B94"
        color_ventana = "#4C2B64"
        color_titulo_principal = "#0F0D3E"
        color_texto = "#D8D5F4"

        ventana = tkinter.Tk()
        ventana.geometry("460x400")
        ventana.title("Ingresar al sistema")
        ventana.resizable(False,False)
        ventana.config(background = color_ventana)
        
        self.center(ventana)

        titulo_principal = tkinter.Label(ventana, text="Wing Gundam Zero || Ingresar", font=(familia_fuente,15), bg=color_titulo_principal, fg=color_texto)
        titulo_principal.pack(fill = tkinter.X)

        advertencia = tkinter.StringVar()
        label_advertencia = tkinter.Label(ventana, textvariable=advertencia, bg=color_ventana, fg="yellow")
        label_advertencia.pack()

        label_correo_electronico = tkinter.Label(ventana, text="Nombre de Usuario o Correo: ", font=(familia_fuente,tamanio_fuente), bg=color_ventana, fg=color_texto)
        label_correo_electronico.place(x = 30, y = 70)

        label_contrasenia = tkinter.Label(ventana, text="Contraseña: ", font=(familia_fuente,tamanio_fuente), bg=color_ventana, fg=color_texto)
        label_contrasenia.place(x = 30, y = 120)

        nombre_usuario = tkinter.StringVar()
        contrasenia = tkinter.StringVar()

        entry_nombre = tkinter.Entry(ventana, textvariable=nombre_usuario, width="30")
        entry_nombre.place(x = 250, y = 75)

        entry_contrasenia = tkinter.Entry(ventana, textvariable=contrasenia, width="30", show="*")
        entry_contrasenia.place(x = 250, y = 120)

        boton_ingresar = tkinter.Button(ventana, text="Ingresar", font=(familia_fuente,tamanio_fuente), width="25", bg=color_botones, fg=color_texto, command = lambda: self.loguearse(nombre_usuario.get(), contrasenia.get(), advertencia, ventana))
        boton_ingresar.place(x = 120, y = 220)

        boton_ir_a_registro = tkinter.Button(ventana, text="Registrarse", font=(familia_fuente,tamanio_fuente), width="25", bg=color_botones, fg=color_texto, command = lambda: self.transicion_registro(ventana))
        boton_ir_a_registro.place(x = 120, y = 270)

        ventana.mainloop()

    def loguearse(self, nombre_usuario, contrasenia, advertencia, ventana):
        #print("Ejecucion del boton loguearse: ")
        codigo_documento = ''
        try:
            firebase = fb.FirebaseApplication("https://proyectopython2020a-d2866.firebaseio.com/", None)
            resultados_consulta = firebase.get('/proyectopython2020a-d2866/Usuario', '')
            flag_credenciales = False
            for documento in resultados_consulta:
                usuario = resultados_consulta[documento]
                if(nombre_usuario == usuario['nombre_usuario'] or nombre_usuario == usuario['correo']):
                    if(contrasenia == usuario['contrasenia']):
                        flag_credenciales = True
                        datos_usuario = usuario
                        codigo_documento = documento


            if(flag_credenciales):
                menu = Game(codigo_documento, datos_usuario['nombre'], datos_usuario['nombre_usuario'], datos_usuario['correo'], datos_usuario['fecha_nacimiento'], datos_usuario['pais'], self)
                ventana.destroy()
                ventana.quit()
                menu.menu_principal()
            else:
                advertencia.set("Error: Las credenciales son incorrectas")
        except Exception as ex:
            print(ex)
            messagebox.showinfo(message="Ha ocurrido un error durante la ejecucion del juego", title="ERROR")