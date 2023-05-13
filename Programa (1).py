from dataclasses import dataclass
import datetime
from abc import ABC

@dataclass
class Cliente:
    def __init__(self, id: str, nombre: str, apellido: str, direccion: str, email: str, contraseña: str, celular: int, fecha_nacimiento: datetime) -> None:
        self.id: str = id
        self.nombre: str = nombre
        self.apellido: str = apellido
        self.direccion: str = direccion
        self.email: str = email
        self.contrasena: str = contraseña
        self.celular: str = celular
        self.fecha_nacimiento: str = fecha_nacimiento
        self.alquiler: bool = False
        self.baneado: bool = False


class Videojuego:
    def __init__(self, nombre_juego, codigo_juego, precio_alquiler, precio_venta, cantidad):
        self.nombre_juego = nombre_juego
        self.codigo_juego = codigo_juego
        self.precio_alquiler = precio_alquiler
        self.precio_venta = precio_venta
        self.cantidad = cantidad

    def vender(self, codigo_juego: int, cedula: int):
        for juego in self.catalogo.values():
            if juego.codigo_juego == codigo_juego:
                for cliente in self.listaclientes.values():
                    if cliente.cedula == cedula:
                        Videojuego.cantidad -= 1

    def alquilar(self, nombre_juego: str, cedula: int):
        for juego in self.catalogo.values():
            if juego.nombre_juego == nombre_juego:
                for cliente in self.listaclientes.values():
                    if cliente.cedula == cedula:
                        cliente.estado = 1
                        Videojuego.cantidad -= 1


class Tienda:

    def __init__(self):
        self.listaclientes: dict[str, Cliente] = dict()
        self.cat: dict[str, Videojuego] = dict()


    def registrar_cliente(self, cedula: int, nombre: str, direccion: str, telefono: int, compras: int,
                          estado: int):
        if self.buscar_cliente(cedula) is None:
            cliente: Cliente = Cliente(cedula, nombre, direccion, telefono, compras, estado)
            self.listaclientes[cedula] = cliente


    def buscar_cliente(self, cedula: int):
        if cedula in self.listaclientes.keys():
            return self.listaclientes[cedula]
        else:
            return None

    def registrar_juego(self, nombre_juego: str, codigo_juego: int, precio_alquiler: int, precio_venta: int,
                        cantidad: int):
        if self.buscar_juego_por_codigo(codigo_juego) is None:
            juego: Videojuego = Videojuego(nombre_juego, codigo_juego, precio_alquiler, precio + venta, cantidad)
            self.catalogo[codigo_juego] = juego

    def buscar_juego_por_nombre(self, nombre_juego: str):
        for juego in self.catalogo.values():
            if juego.nombre_juego == nombre_juego:
                return juego
        return None

    def buscar_juego_por_codigo(self, codigo_juego: int):
        for juego in self.catalogo.values():
            if juego.codigo_juego == codigo_juego:
                return juego
        return None

    def devolver_videojuego(self, cedula: int):
        for cliente in self.listaclientes.values():
            if cliente.cedula == cedula:
                if cliente.estado == 1:
                    self.registrar_juego()
                elif cliente.estado == 0:
                    print("NO TIENES JUEGOS ALQUILADOS")

    def comprar_juego_al_cliente(self, cedula: int):
        for cliente in self.listaclientes.values():
            if cliente.cedula == cedula:
                self.registrar_juego()
            else:
                self.registrar_cliente()
                self.registrar_juego()


    def cliente_mayor_edad(self, cliente_mayor_edad):
        if cliente_mayor_edad.year < 18:
            return 'no se puede hacer compra'
        pass

class IRecibo(ABC):
    def __init__(self, id: str, cliente: str, informacion_video_juego: str) -> None:
        self.id: str = id
        self.cliente: str = cliente
        self.informacion_video_juego: str = informacion_video_juego

class ReciboCompra(IRecibo):
    def __init__(self, id: str, cliente: str, informacion_video_juego: str, valor_compra: float):
        super(ReciboCompra, self).__init__(id, cliente, informacion_video_juego)
        self.valor_compra = valor_compra

class ReciboAlquiler(IRecibo):
    def __init__(self, id: str, cliente: str, informacion_video_juego: str, valor_alquiler: float):
        super(ReciboCompra, self).__init__(id, cliente, informacion_video_juego)
        self.valor_alquiler = valor_alquiler
