# Sistema de Inventario con MCP (Model Context Protocol) Básico

Sistema de gestión de inventario construido con FastMCP y SQLite que permite crear, consultar, actualizar y eliminar productos mediante el protocolo MCP.

## Características

- Crear productos con nombre, categoría, cantidad y precio
- Consultar productos por ID
- Actualizar cantidad de productos
- Eliminar productos del inventario
- Listar todos los productos disponibles
- Base de datos SQLite persistente

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

### 1. Clonar o descargar el proyecto

git clone <tu-repositorio>
cd inventario-mcp


### 2. Instalar dependencias
pip install fastmcp

**Nota:** SQLite3 viene incluido con Python por defecto, solo se necesita verificar que  si este instalado y que este en el PATH

## Estructura del Proyecto
Practica_MCP_BASICO/
├── server.py # Servidor MCP con endpoints CRUD
├── database.py # Inicialización de base de datos
├── test_client.py # Script de pruebas básicas
├── inventory.db # Base de datos SQLite (se crea automáticamente)
└── README.md # Este archivo


## Uso
El servidor se iniciará y esperará conexiones MCP.

### Probar el sistema

Ejecuta el script de pruebas:

python test_simple.py

Este script:
1. Crea varios productos
2. Consulta un producto por ID
3. Actualiza la cantidad de un producto
4. Lista todos los productos


##  Herramientas (Tools) Disponibles

### `crear_producto(nombre, categoria, cantidad, precio)`
Crea un nuevo producto en el inventario.

**Parámetros:**
- `nombre` (str): Nombre del producto
- `categoria` (str): Categoría del producto
- `cantidad` (int): Cantidad disponible
- `precio` (float): Precio del producto

### `consultar_producto(id)`
Consulta un producto específico por su ID.

**Parámetros:**
- `id` (int): ID del producto a consultar

**Retorna:** Diccionario con los datos del producto o mensaje de error.

### `actualizar_producto(id, cantidad)`
Actualiza la cantidad de un producto existente.

**Parámetros:**
- `id` (int): ID del producto a actualizar
- `cantidad` (int): Nueva cantidad

### `eliminar_producto(id)`
Elimina un producto del inventario.

**Parámetros:**
- `id` (int): ID del producto a eliminar

### `listar_productos()`
Lista todos los productos del inventario como recurso MCP.

**URI del recurso:** `productos://listado`








