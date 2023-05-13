import tkinter as tk

from IPython.utils import frame

from Programa import Tienda, Videojuego, Cliente, IRecibo, ReciboCompra, ReciboAlquiler


class ventana:

    def __init__(self):
        ventana = tk.Tk()
        ventana.geometry('600x600')
        ventana.title('TIENDA DE JUEGOS')

        botonregistrarcliente = tk.Button(ventana, text='REGISTRAR CLIENTE', padx=10, pady=10,
                                          command=self.ventanaregistarcliente)
        botonregistrarcliente.pack()

        botonbuscarcliente = tk.Button(ventana, text='BUSCAR CLIENTE', padx=10, pady=10,
                                       command=self.ventanabuscarcliente)
        botonbuscarcliente.pack()

        botonbuscarjuegopornombre = tk.Button(ventana, text='BUSCAR JUEGO POR NOMBRE', padx=10, pady=10,
                                              command=self.ventanabuscarjuegopornombre)
        botonbuscarjuegopornombre.pack()

        botonbuscarjuegoporcodigo = tk.Button(ventana, text='BUSCAR JUEGO POR CODIGO', padx=10, pady=10,
                                              command=self.ventanabuscarjuegoporcodigo)
        botonbuscarjuegoporcodigo.pack()

        botonregistarjuego = tk.Button(ventana, text='REGISTRAR JUEGO', padx=10, pady=10,
                                       command=self.ventanaregistrarjuego)
        botonregistarjuego.pack()

        botondevolvervideojuego = tk.Button(ventana, text='DEVOLVER VIDEOJUEGO', padx=10, pady=10)
        botondevolvervideojuego.pack()

        botoncomprarjuegoalcliente = tk.Button(ventana, text='COMPRAR JUEGO AL CLIENTE', padx=10, pady=10,
                                               command=self.ventanacomprarjuegoalcliente)
        botoncomprarjuegoalcliente.pack()

        botonvender = tk.Button(ventana, text='VENDER', padx=10, pady=10, command=self.vender)
        botonvender.pack()

        botonalquilar = tk.Button(ventana, text='ALQUILAR', padx=10, pady=10, command=self.alquilar)
        botonalquilar.pack()

        ventana.mainloop()

    def ventanaregistarcliente(self):
        ventana1()

    def ventanabuscarcliente(self):
        ventana2()

    def ventanabuscarjuegopornombre(self):
        ventana3()

    def ventanabuscarjuegoporcodigo(self):
        ventana4()

    def ventanaregistrarjuego(self):
        ventana5()

    def ventanacomprarjuegoalcliente(self):
        ventana6()

    def vender(self):
        ventana7()

    def alquilar(self):
        ventana8()


class ventana1:

    def __init__(self):
        self.ventanaregistarcliente = tk.Toplevel()
        self.ventanaregistarcliente.geometry('600x400')
        self.ventanaregistarcliente.title('REGISTRAR USUARIO')

        tk.Label(self.ventanaregistarcliente, text='INGRESE LA CEDULA DEL USUARIO', justify=tk.CENTER).pack()
        tk.Entry(self.ventanaregistarcliente, justify=tk.CENTER).pack()
        tk.Label(self.ventanaregistarcliente, text='INGRESE EL NOMBRE DEL USUARIO', justify=tk.CENTER).pack()
        tk.Entry(self.ventanaregistarcliente, justify=tk.CENTER).pack()
        tk.Label(self.ventanaregistarcliente, text='INGRESE LA DIRECCIÓN DEL USUARIO', justify=tk.CENTER).pack()
        tk.Entry(self.ventanaregistarcliente, justify=tk.CENTER).pack()
        tk.Label(self.ventanaregistarcliente, text='INGRESE EL TELEFONO DEL USUARIO', justify=tk.CENTER).pack()
        tk.Entry(self.ventanaregistarcliente, justify=tk.CENTER).pack()
        tk.Label(self.ventanaregistarcliente, text='INGRESE LA DIRECCIÓN DEL USUARIO', justify=tk.CENTER).pack()
        tk.Entry(self.ventanaregistarcliente, justify=tk.CENTER).pack()
        tk.Label(self.ventanaregistarcliente, text='POR FAVOR INICIALICE LAS COMRPAS DEL USUARIO EN 0',
                 justify=tk.CENTER).pack()
        tk.Entry(self.ventanaregistarcliente, justify=tk.CENTER).pack()
        tk.Label(self.ventanaregistarcliente, text='POR FAVOR INICIALICE EL ESTADO DEL USUARIO EN 0',
                 justify=tk.CENTER).pack()
        tk.Entry(self.ventanaregistarcliente, justify=tk.CENTER).pack()
        self.registro1 = tk.Button(self.ventanaregistarcliente, text='GUARDAR', padx=10, pady=10,
                                   command=self.volverventana)
        self.registro1.pack()

        if self.ventanaregistarcliente:
            ventana.withdraw()

        self.ventanaregistarcliente.mainloop()

    def volverventana(self):
        self.ventanaregistarcliente.destroy()


class ventana2:

    def __init__(self):
        self.ventanabuscarcliente = tk.Toplevel()
        self.ventanabuscarcliente.geometry('600x200')
        self.ventanabuscarcliente.title('BUSCAR CLIENTE')

        tk.Label(self.ventanabuscarcliente, text='INGRESE LA CEDULA DEL USUARIO', justify=tk.CENTER).pack()
        tk.Entry(self.ventanabuscarcliente, justify=tk.CENTER).pack()

        self.buscar = tk.Button(self.ventanabuscarcliente, text='BUSCAR', padx=10, pady=10)
        self.buscar.pack()

        self.volver = tk.Button(self.ventanabuscarcliente, text='VOLVER AL INICIO', padx=10, pady=10,
                                command=self.volverventana)
        self.volver.pack()

        if self.ventanabuscarcliente:
            ventana.withdraw()

        self.ventanabuscarcliente.mainloop()

    def volverventana(self):
        self.ventanabuscarcliente.destroy()


class ventana3:

    def __init__(self):
        self.ventanabuscarjuegopornombre = tk.Toplevel()
        self.ventanabuscarjuegopornombre.geometry('600x200')
        self.ventanabuscarjuegopornombre.title('BUSCAR JUEGO POR NOMBRE')

        tk.Label(self.ventanabuscarjuegopornombre, text='INGRESE EL NOMBRE DEL JUEGO', justify=tk.CENTER).pack()
        tk.Entry(self.ventanabuscarjuegopornombre, justify=tk.CENTER).pack()

        self.buscar = tk.Button(self.ventanabuscarjuegopornombre, text='BUSCAR', padx=10, pady=10)
        self.buscar.pack()

        self.volver = tk.Button(self.ventanabuscarjuegopornombre, text='VOLVER AL INICIO', padx=10, pady=10,
                                command=self.volverventana)
        self.volver.pack()

        if self.ventanabuscarjuegopornombre:
            ventana.withdraw()

        self.ventanabuscarjuegopornombre.mainloop()

    def volverventana(self):
        self.ventanabuscarjuegopornombre.destroy()


class ventana4:

    def __init__(self):
        self.ventanabuscarjuegoporcodigo = tk.Toplevel()
        self.ventanabuscarjuegoporcodigo.geometry('600x200')
        self.ventanabuscarjuegoporcodigo.title('BUSCAR JUEGO POR CODIGO')

        tk.Label(self.ventanabuscarjuegoporcodigo, text='INGRESE EL CODIGO DEL JUEGO', justify=tk.CENTER).pack()
        tk.Entry(self.ventanabuscarjuegoporcodigo, justify=tk.CENTER).pack()

        self.buscar = tk.Button(self.ventanabuscarjuegoporcodigo, text='BUSCAR', padx=10, pady=10)
        self.buscar.pack()

        self.volver = tk.Button(self.ventanabuscarjuegoporcodigo, text='VOLVER AL INICIO', padx=10, pady=10,
                                command=self.volverventana)
        self.volver.pack()

        if self.ventanabuscarjuegoporcodigo:
            ventana.withdraw()

        self.ventanabuscarjuegoporcodigo.mainloop()

    def volverventana(self):
        self.ventanabuscarjuegoporcodigo.destroy()


class ventana5:

    def __init__(self):
        self.ventanaregistrarjuego = tk.Toplevel()
        self.ventanaregistrarjuego.geometry('600x400')
        self.ventanaregistrarjuego.title('REGISTRAR JUEGO')

        tk.Label(self.ventanaregistrarjuego, text='INGRESE EL NOMBRE DEL JUEGO', justify=tk.CENTER).pack()
        tk.Entry(self.ventanaregistrarjuego, justify=tk.CENTER).pack()
        tk.Label(self.ventanaregistrarjuego, text='INGRESE EL CODIGO DEL JUEGO', justify=tk.CENTER).pack()
        tk.Entry(self.ventanaregistrarjuego, justify=tk.CENTER).pack()
        tk.Label(self.ventanaregistrarjuego, text='INGRESE EL PRECIO DE ALQUILER', justify=tk.CENTER).pack()
        tk.Entry(self.ventanaregistrarjuego, justify=tk.CENTER).pack()
        tk.Label(self.ventanaregistrarjuego, text='INGRESE EL PRECIO DE VENTA', justify=tk.CENTER).pack()
        tk.Entry(self.ventanaregistrarjuego, justify=tk.CENTER).pack()
        tk.Label(self.ventanaregistrarjuego, text='INGRESE LA CANTIDAD DE UNIDADES DISPONIBLES',
                 justify=tk.CENTER).pack()
        tk.Entry(self.ventanaregistrarjuego, justify=tk.CENTER).pack()

        self.registro1 = tk.Button(self.ventanaregistrarjuego, text='GUARDAR', padx=10, pady=10,
                                   command=self.volverventana)
        self.registro1.pack()

        if self.ventanaregistrarjuego:
            ventana.withdraw()

        self.ventanaregistrarjuego.mainloop()

    def volverventana(self):
        self.ventanaregistrarjuego.destroy()


class ventana6:

    def __init__(self):
        self.venatanacomprarjuegoalcliente = tk.Toplevel()
        self.venatanacomprarjuegoalcliente.geometry('600x200')
        self.venatanacomprarjuegoalcliente.title('COMPRAR JUEGO AL CLIENTE')

        tk.Label(self.venatanacomprarjuegoalcliente, text='INGRESE LA CEDULA DEL USUARIO', justify=tk.CENTER).pack()
        tk.Entry(self.venatanacomprarjuegoalcliente, justify=tk.CENTER).pack()

        self.buscar = tk.Button(self.venatanacomprarjuegoalcliente, text='BUSCAR', padx=10, pady=10)
        self.buscar.pack()

        self.volver = tk.Button(self.venatanacomprarjuegoalcliente, text='VOLVER AL INICIO', padx=10, pady=10,
                                command=self.volverventana)
        self.volver.pack()

        if self.venatanacomprarjuegoalcliente:
            ventana.withdraw()

        self.venatanacomprarjuegoalcliente.mainloop()

    def volverventana(self):
        self.venatanacomprarjuegoalcliente.destroy()


class ventana7:

    def __init__(self):
        self.vender = tk.Toplevel()
        self.vender.geometry('600x200')
        self.vender.title('VENDER')

        tk.Label(self.vender, text='INGRESE EL CODIGO DEL JUEGO', justify=tk.CENTER).pack()
        tk.Entry(self.vender, justify=tk.CENTER).pack()

        tk.Label(self.vender, text='INGRESE LA CEDULA DEL USUARIO', justify=tk.CENTER).pack()
        tk.Entry(self.vender, justify=tk.CENTER).pack()

        self.buscar = tk.Button(self.vender, text='BUSCAR', padx=10, pady=10)
        self.buscar.pack()

        self.volver = tk.Button(self.vender, text='VOLVER AL INICIO', padx=10, pady=10,
                                command=self.volverventana)
        self.volver.pack()

        if self.vender:
            ventana.withdraw()

        self.vender.mainloop()

    def volverventana(self):
        self.vender.destroy()


class ventana8:

    def __init__(self):
        self.alquilar = tk.Toplevel()
        self.alquilar.geometry('600x200')
        self.alquilar.title('ALQUILAR')

        tk.Label(self.alquilar, text='INGRESE EL NOMBRE DEL JUEGO', justify=tk.CENTER).pack()
        tk.Entry(self.alquilar, justify=tk.CENTER).pack()

        tk.Label(self.alquilar, text='INGRESE LA CEDULA DEL USUARIO', justify=tk.CENTER).pack()
        tk.Entry(self.alquilar, justify=tk.CENTER).pack()

        self.buscar = tk.Button(self.alquilar, text='BUSCAR', padx=10, pady=10)
        self.buscar.pack()

        self.volver = tk.Button(self.alquilar, text='VOLVER AL INICIO', padx=10, pady=10,
                                command=self.volverventana)
        self.volver.pack()

        if self.alquilar:
            ventana.withdraw()

        self.alquilar.mainloop()

    def volverventana(self):
        self.alquilar.destroy()


if __name__ == "__main__":
    ventana()
