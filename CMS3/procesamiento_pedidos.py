from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json

# ACLARACIÓN: El tipo de "pedidos" debería ser: pedidos: Queue[Dict[str, Union[int, str, Dict[str, int]]]]
# Por no ser soportado por la versión de CMS, usamos simplemente "pedidos: Queue"


def hayStockSuficiente(nombre, cantidad, stock) -> bool:
    res: bool = stock[nombre] >= cantidad
    return res


def procesamiento_pedidos(pedidos: Queue,
                          stock_productos: Dict[str, int],
                          precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
    res: List[Dict[str, Union[int, str, float, Dict[str, int]]]] = []
    while (not pedidos.empty()):

        curr_pedido = pedidos.get()
        curr_client = {
            'id': curr_pedido['id'], 'cliente': curr_pedido['cliente'], 'productos': {}, 'precio_total': 0.0, 'estado': 'completo'}
        productos = curr_pedido['productos']
        for producto in productos:

            if (hayStockSuficiente(producto, productos[producto], stock_productos)):

                curr_client['precio_total'] += precios_productos[producto] * \
                    productos[producto]
                curr_client['productos'][producto] = productos[producto]
                stock_productos[producto] -= productos[producto]
            else:

                curr_client['estado'] = 'incompleto'
                curr_client['productos'][producto] = stock_productos[producto]
                curr_client['precio_total'] += precios_productos[producto] * \
                    stock_productos[producto]
                stock_productos[producto] = 0
        res.append(curr_client)

    return res


if __name__ == '__main__':
    pedidos: Queue = Queue()
    list_pedidos = json.loads(input())
    [pedidos.put(p) for p in list_pedidos]
    stock_productos = json.loads(input())
    precios_productos = json.loads(input())
    print("{} {}".format(procesamiento_pedidos(
        pedidos, stock_productos, precios_productos), stock_productos))

# Ejemplo input
# pedidos: [{"id":21,"cliente":"Gabriela", "productos":{"Manzana":2}}, {"id":1,"cliente":"Juan","productos":{"Manzana":2,"Pan":4,"Factura":6}}]
# stock_productos: {"Manzana":10, "Leche":5, "Pan":3, "Factura":0}
# precios_productos: {"Manzana":3.5, "Leche":5.5, "Pan":3.5, "Factura":5}
