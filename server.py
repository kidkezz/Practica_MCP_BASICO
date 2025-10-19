from mcp.server.fastmcp import FastMCP
import sqlite3
from database import init_db


init_db()

DB = "inventory.db"
mcp = FastMCP("InventarioDB")

@mcp.tool()
def crear_producto(nombre: str, categoria: str, cantidad: int, precio: float) -> str:
    """Crea un nuevo producto y lo guarda en la base de datos."""
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO productos (nombre, categoria, cantidad, precio) VALUES (?, ?, ?, ?)",
        (nombre, categoria, cantidad, precio)
    )
    conn.commit()
    conn.close()
    return "Producto creado exitosamente"

@mcp.tool()
def consultar_producto(id: int) -> dict:
    """Consulta un producto por su ID."""
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            "id": row[0],
            "nombre": row[1],
            "categoria": row[2],
            "cantidad": row[3],
            "precio": row[4]
        }
    return {"error": "Producto no encontrado"}

@mcp.tool()
def actualizar_producto(id: int, cantidad: int) -> str:
    """Actualiza únicamente la cantidad de un producto existente."""
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE productos SET cantidad = ? WHERE id = ?",
        (cantidad, id)
    )
    if cursor.rowcount == 0:
        conn.close()
        return "Producto no encontrado"
    conn.commit()
    conn.close()
    return "Producto actualizado correctamente"

@mcp.tool()
def eliminar_producto(id: int) -> str:
    """Elimina un producto por su ID."""
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
    if cursor.rowcount == 0:
        conn.close()
        return "Producto no encontrado"
    conn.commit()
    conn.close()
    return "Producto eliminado correctamente"

@mcp.resource("productos://listado")
def listar_productos() -> dict:
    """Devuelve un diccionario con todos los productos del inventario."""
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    rows = cursor.fetchall()
    conn.close()
    return {
        row[0]: {
            "nombre": row[1],
            "categoria": row[2],
            "cantidad": row[3],
            "precio": row[4]
        }
        for row in rows
    }

if __name__ == "__main__":
    mcp.serve()
