import tkinter 
from tkinter import messagebox
import re
from firebase import firebase as fb


class Registro:

    def __init__(self, login):
        self.login = login

    def transicion_login(self, ventana):
        ventana.destroy()
        ventana.quit()
        self.login.start()

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
        ventana.geometry("460x500")
        ventana.title("Registrarse")
        ventana.resizable(False,False)
        ventana.config(background = color_ventana)
        self.center(ventana)

        titulo_principal = tkinter.Label(ventana, text="Wing Gundam Zero || Registrase", font=(familia_fuente,15), bg=color_titulo_principal, fg=color_texto)
        titulo_principal.pack(fill = tkinter.X)

        advertencia = tkinter.StringVar()
        label_advertencia = tkinter.Label(ventana, textvariable=advertencia, bg=color_ventana, fg="yellow")
        label_advertencia.pack()

        label_nombre = tkinter.Label(ventana, text="Nombre: ", font=(familia_fuente,tamanio_fuente), bg=color_ventana, fg=color_texto)
        label_nombre.place(x = 30, y = 70)

        label_nombre_usuario = tkinter.Label(ventana, text="Nombre de Usuario: ", font=(familia_fuente,tamanio_fuente), bg=color_ventana, fg=color_texto)
        label_nombre_usuario.place(x = 30, y = 120)

        label_contrasenia = tkinter.Label(ventana, text="Contraseña: ", font=(familia_fuente,tamanio_fuente), bg=color_ventana, fg=color_texto)
        label_contrasenia.place(x = 30, y = 170)

        label_repetir_contrasenia = tkinter.Label(ventana, text="Repetir Contraseña: ", font=(familia_fuente,tamanio_fuente), bg=color_ventana, fg=color_texto)
        label_repetir_contrasenia.place(x = 30, y = 220)

        label_correo_electronico = tkinter.Label(ventana, text="Correo Electronico: ", font=(familia_fuente,tamanio_fuente), bg=color_ventana, fg=color_texto)
        label_correo_electronico.place(x = 30, y = 270)

        label_fecha_nacimiento = tkinter.Label(ventana, text="Fecha de Nacimiento: ", font=(familia_fuente,tamanio_fuente), bg=color_ventana, fg=color_texto)
        label_fecha_nacimiento.place(x = 30, y = 320)

        label_pais = tkinter.Label(ventana, text="Pais: ", font=(familia_fuente,tamanio_fuente), bg=color_ventana, fg=color_texto)
        label_pais.place(x = 30, y = 370)

        nombre = tkinter.StringVar()
        nombre_usuario = tkinter.StringVar()
        contrasenia = tkinter.StringVar()
        repeticion_contrasenia = tkinter.StringVar()
        correo_electronico = tkinter.StringVar()
        fecha_nacimiento = tkinter.StringVar()
        pais = tkinter.StringVar()
        lista_paises = ["Afganistan", "Albania", "Alemania", "Andorra", "Angola", "Antigua y Barbuda", "Arabia Saudita", "Argelia", "Argentina", "Armenia", "Australia", "Austria", "Azerbaiyan", "Bahamas", "Banglades", "Barbados", "Barein", "Belgica", "Belice", "Benin", "Bielorrusia", "Birmania", "Bolivia", "Botsuana", "Brasil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Butan", "Cabo Verde", "Camboya", "Camerun", "Canada", "Catar", "Chad", "Chile", "China", "Chipre", "Ciudad del Vaticano", "Colombia", "Comoras", "Corea del Norte", "Corea del Sur", "Costa de Marfil", "Costa Rica", "Croacia", "Cuba", "Dinamarca", "Dominica", "Ecuador", "Egipto", "El Salvador", "Emiratos Arabes Unidos", "Eritrea", "Eslovaquia", "Eslovenia", "España", "Estados Unidos", "Estonia", "Etiopía", "Filipinas", "Finlandia", "Fiyi", "Francia", "Gabón", "Gambia", "Georgia", "Ghana", "Granada", "Grecia", "Guatemala", "Guyana", "Guinea", "Haiti", "Honduras", "Hungria", "India", "Indonesia", "Irak", "Iran", "Irlanda", "Islandia", "Isla de los Piratas", "Israel", "Italia", "Jamaica", "Japon", "Jordania", "Kazajistan", "Kenia", "Kirguistan", "Kiribati", "Kuwait", "Laos", "Lesoto", "Letonia", "Libano", "Liberia", "Libia", "Liechtenstein", "Lituania", "Luxemburgo", "Macedonia del Norte", "Madagascar", "Malasia", "Malaui", "Maldivas", "Mali", "Malta", "Marruecos", "Mauricio", "Mauritania", "Mexico", "Micronesia", "Moldavia", "Mordor", "Monaco", "Mongolia", "Montenegro", "Mozambique", "Namibia", "Nauru", "Nepal", "Nicaragua", "Níger", "Nigeria", "Noruega", "Nueva Zelanda", "Oman", "Paises Bajos", "Pakistan", "Palaos", "Panama", "Papua Nueva Guinea", "Paraguay", "Peru", "Polonia", "Portugal", "Reino Unido", "Republica Dominicana", "Ruanda", "Rumania", "Rusia", "Samoa", "San Marino", "Santa Lucia", "Senegal", "Serbia", "Seychelles", "Sierra Leona", "Singapur", "Siria", "Somalia", "Suazilandia", "Sudáfrica", "Sudán", "Sudán del Sur", "Suecia", "Suiza", "Surinam", "Tailandia", "Tanzania", "Takoshima", "Timor Oriental", "Togo", "Tonga", "Trinidad y Tobago", "Tunez", "Turkmenistán", "Turquía", "Tuvalu", "Ucrania", "Uganda", "Uruguay", "Uzbekistán", "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Yibuti", "Zambia", "Zimbabue"]
        

        entry_nombre = tkinter.Entry(ventana, textvariable=nombre, width="30")
        nombre.trace("w", lambda *args: self.limitador(nombre, 25))
        entry_nombre.place(x = 250, y = 70)

        entry_nombre_usuario = tkinter.Entry(ventana, textvariable=nombre_usuario, width="30")
        nombre_usuario.trace("w", lambda *args: self.limitador(nombre_usuario, 10))
        entry_nombre_usuario.place(x = 250, y = 120)

        entry_contrasenia = tkinter.Entry(ventana, textvariable=contrasenia, width="30", show="*")
        contrasenia.trace("w", lambda *args: self.limitador(contrasenia, 30))
        entry_contrasenia.place(x = 250, y = 170)

        entry_repetir_contrasenia = tkinter.Entry(ventana, textvariable=repeticion_contrasenia, width="30", show="*")
        repeticion_contrasenia.trace("w", lambda *args: self.limitador(repeticion_contrasenia, 30))
        entry_repetir_contrasenia.place(x = 250, y = 220)

        entry_correo_electronico = tkinter.Entry(ventana, textvariable=correo_electronico, width="30")
        entry_correo_electronico.place(x = 250, y = 270)

        entry_fecha_nacimiento = tkinter.Entry(ventana, textvariable=fecha_nacimiento, width="30")
        fecha_nacimiento.trace("w", lambda *args: self.limitador(fecha_nacimiento, 10))
        entry_fecha_nacimiento.place(x = 250, y = 320)

        options_paises = tkinter.OptionMenu(ventana, pais, *lista_paises)
        options_paises.place(x = 250, y = 370)

        boton_regresar = tkinter.Button(ventana, text="Regresar", font=(familia_fuente,tamanio_fuente), width="19", bg="#A74B94", fg=color_texto, command = lambda: self.transicion_login(ventana))
        boton_regresar.place(x = 30, y = 430)

        boton_registrarse = tkinter.Button(ventana, text="Registrarse", font=(familia_fuente,tamanio_fuente), width="19", bg=color_botones, fg=color_texto, command = lambda: self.registrarse(nombre.get(), nombre_usuario.get(), contrasenia.get(), repeticion_contrasenia.get(), correo_electronico.get(), fecha_nacimiento.get(), pais.get(), advertencia, ventana))
        boton_registrarse.place(x = 250, y = 430)

        ventana.mainloop()


    def limitador(self, entry_text, numero):
        if len(entry_text.get()) > 0:
            entry_text.set(entry_text.get()[:int(numero)])


    def registrarse(self, nombre, nombre_usuario, contrasenia, repeticion_contrasenia, correo, fecha_nacimiento, pais, advertencia, ventana):
        
        patternNombre = re.compile("[A-Za-z ]+")
        patternCorreo = re.compile("^[^@]+@[^@]+\.[a-zA-Z]{2,}$")
        patternFecha = re.compile("^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$")
        if (patternNombre.fullmatch(nombre) is not None):
            if(len(contrasenia) >= 5):
                if(contrasenia == repeticion_contrasenia):
                    if (patternCorreo.fullmatch(correo) is not None):
                        if (patternFecha.fullmatch(fecha_nacimiento) is not None):
                            try:
                                advertencia.set("")
                                firebase = fb.FirebaseApplication("https://proyectopython2020a-d2866.firebaseio.com/", None)
                                resultados_consulta = firebase.get('/proyectopython2020a-d2866/Usuario', '')
                                for documento in resultados_consulta:
                                    usuario = resultados_consulta[documento]
                                    if (nombre_usuario == usuario['nombre_usuario']):
                                        advertencia.set("Error: El nombre de usuario seleccionado ya existe")
                                        return
                                    if(correo == usuario['correo']):
                                        advertencia.set("Error: El correo seleccionado esta registrado por otro usuario")
                                        return
                                
                                data = {
                                    'nombre': nombre,
                                    'nombre_usuario': nombre_usuario,
                                    'contrasenia': contrasenia,
                                    'correo': correo,
                                    'fecha_nacimiento': fecha_nacimiento,
                                    'pais': pais
                                }
                                result = firebase.post("/proyectopython2020a-d2866/Usuario", data)
                                print(result)
                                messagebox.showinfo(message="El usuario ha sido creado exitosamente", title="Informacion")
                                ventana.destroy()
                                ventana.quit()
                                self.login.start()
                            except Exception as ex:
                                print(ex)
                                messagebox.showinfo(message="Error al conectar con la base de datos", title="ERROR")
                        else:
                            advertencia.set("Error: La fecha debe ser real y estar en el formato dd/mm/yyyy")
                    else:
                        advertencia.set("Error: El formato del correo electronico es invalido")
                else:
                    advertencia.set("Error: Las contraseñas no coinciden")
            else:
                advertencia.set("Error: La contraseña debe tener un minimo de 5 caracteres")
        else:
            advertencia.set("Error: El nombre solo puede contener letras, no numeros ni caracteres especiales")

        
