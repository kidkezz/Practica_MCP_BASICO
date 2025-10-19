import asyncio
from fastmcp import Client

async def test_inventario():
    
    from server import mcp
    
    async with Client(mcp) as client:
        # 1. Crear 5 productos
        print("=== Creando productos ===")
        productos = [
            {"nombre": "Laptop Dell", "categoria": "Electrónica", "cantidad": 10, "precio": 1500.0},
            {"nombre": "Mouse Logitech", "categoria": "Accesorios", "cantidad": 50, "precio": 25.0},
            {"nombre": "Teclado Mecánico", "categoria": "Accesorios", "cantidad": 30, "precio": 80.0},
            {"nombre": "Monitor LG 27\"", "categoria": "Electrónica", "cantidad": 15, "precio": 350.0},
            {"nombre": "Webcam HD", "categoria": "Accesorios", "cantidad": 20, "precio": 60.0}
        ]
        
        for prod in productos:
            result = await client.call_tool("crear_producto", prod)
            print(result)
        
        # 2. Consultar producto por ID
        print("\n=== Consultando producto ID 1 ===")
        result = await client.call_tool("consultar_producto", {"id": 1})
        print(result)
        
        # 3. Actualizar cantidad de producto
        print("\n=== Actualizando cantidad del producto 1 ===")
        result = await client.call_tool("actualizar_producto", {"id": 1, "cantidad": 15})
        print(result)
        
        # 4. Eliminar un producto
        print("\n=== Eliminando producto ID 5 ===")
        result = await client.call_tool("eliminar_producto", {"id": 5})
        print(result)
        
        # 5. Listar todos los productos
        print("\n=== Listando todos los productos ===")
        result = await client.read_resource("productos://listado")
        print(result)

if __name__ == "__main__":
    asyncio.run(test_inventario())
