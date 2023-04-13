from typing import List
from datetime import date

class Cliente:
    def __init__(self, nombre: str, direccion: str):
        self.__nombre = nombre
        self.__direccion = direccion

    def get_nombre(self) -> str:
        return self.__nombre

    def set_nombre(self, nombre: str):
        self.__nombre = nombre

    def get_direccion(self) -> str:
        return self.__direccion

    def set_direccion(self, direccion: str):
        self.__direccion = direccion


class Producto:
    def __init__(self, nombre: str, precio: float):
        self.__nombre = nombre
        self.__precio = precio

    def get_nombre(self) -> str:
        return self.__nombre

    def set_nombre(self, nombre: str):
        self.__nombre = nombre

    def get_precio(self) -> float:
        return self.__precio

    def set_precio(self, precio: float):
        self.__precio = precio


class Factura:
    def __init__(self, cliente: Cliente, fecha: date, productos: List[Producto]):
        self.__cliente = cliente
        self.__fecha = fecha
        self.__productos = productos

    def get_cliente(self) -> Cliente:
        return self.__cliente

    def set_cliente(self, cliente: Cliente):
        self.__cliente = cliente

    def get_fecha(self) -> date:
        return self.__fecha

    def set_fecha(self, fecha: date):
        self.__fecha = fecha

    def get_productos(self) -> List[Producto]:
        return self.__productos

    def set_productos(self, productos: List[Producto]):
        self.__productos = productos

    def calcular_total(self) -> float:
        total = 0.0
        for producto in self.__productos:
            total += producto.get_precio()
        return total

    def imprimir_factura(self):
        print(f"Fecha: {self.__fecha}")
        print(f"Cliente: {self.__cliente.get_nombre()}")
        print("Productos:")
        for producto in self.__productos:
            print(f"- {producto.get_nombre()}: {producto.get_precio()}")
        print(f"Total: {self.calcular_total()}")

