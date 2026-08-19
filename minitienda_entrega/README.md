# MiniTienda - Sistema de Registro y Análisis de Ventas

**Curso:** Lógica de Programación - UIDE  
**Fecha:** 2026  
**Alumno:** Rafael Cambera

---

## 📋 Descripción

MiniTienda es un programa de consola que implementa un sistema completo de gestión de ventas con:
- Catálogo de productos (tuplas inmutables)
- Registro dinámico de ventas (listas)
- Almacenamiento persistente (CSV con Pandas)
- Análisis estadístico (NumPy)
- Visualización de datos (Matplotlib)
- Manejo robusto de errores (try/except/finally)

---

## ✅ Requisitos Cumplidos

### Estructuras de Datos
- ✓ **Tuplas**: Catálogo inmutable `catalogo = (('P001', 'Laptop'), ...)`
- ✓ **Diccionarios**: `precios = {'P001': 800.00, ...}`, `stock = {'P001': 5, ...}`
- ✓ **Listas**: `ventas_registro = [{'producto_id': 'P001', ...}, ...]`

### Funciones Modulares
- ✓ `obtener_nombre_producto()` - Búsqueda en tuplas
- ✓ `validar_producto()` - Verificación de catálogo
- ✓ `registrar_venta()` - Registro con descuento automático
- ✓ `guardar_csv()` / `cargar_csv()` - Persistencia con Pandas
- ✓ `calcular_metricas()` - Análisis con NumPy
- ✓ `graficar_ingresos()` - Visualización con Matplotlib
- ✓ `registrar_error()` - Logging en log.txt

### Control de Flujo
- ✓ `if/elif/else` en menú y validaciones
- ✓ `while True` para loop interactivo
- ✓ `for` para iteración sobre tuplas y diccionarios
- ✓ `break` para salir del menú
- ✓ `continue` en validaciones

### Manejo de Errores
- ✓ `try/except/else/finally` completo
- ✓ `ValueError` para inputs inválidos
- ✓ `FileNotFoundError` para archivos inexistentes
- ✓ `KeyError` para claves no encontradas
- ✓ `ZeroDivisionError` en cálculos seguros
- ✓ `KeyboardInterrupt` para interrupciones

### Pandas
- ✓ `DataFrame()` para tablas de ventas
- ✓ `.groupby()` para totales por producto
- ✓ `.to_csv()` para guardar datos
- ✓ `.read_csv()` para cargar datos

### NumPy
- ✓ `np.array()` para arreglos de datos
- ✓ `np.sum()` para totales
- ✓ `np.mean()` para promedios
- ✓ `np.std()` para desviación estándar
- ✓ `np.min()` / `np.max()` para extremos

### Matplotlib
- ✓ `.figure()` para crear gráficos
- ✓ `.bar()` para gráfico de barras
- ✓ `.xlabel()`, `.ylabel()`, `.title()` para etiquetas
- ✓ `.savefig()` para exportar a PNG

---

## 🎯 Retos Implementados

### Reto A: Agregar Producto al Catálogo
```python
def agregar_producto():
    # Convierte tupla a lista, agrega producto, reconvierte
    catalogo = tuple(list(catalogo) + [(producto_id, nombre)])
    precios[producto_id] = precio
    stock[producto_id] = stk
```
**Ubicación:** Función `agregar_producto()` - Menú opción 7

### Reto B: Exportar Gráfico a PNG
```python
def exportar_grafico():
    # ... código para generar gráfico ...
    plt.savefig('ingresos.png', dpi=300, bbox_inches='tight')
```
**Ubicación:** Función `exportar_grafico()` - Menú opción 6

### Reto C: Descuento si Cantidad >= 10
```python
def registrar_venta(producto_id, cantidad, precio_unitario):
    descuento = 0.05 if cantidad >= 10 else 0.0
    precio_final = precio_unitario * (1 - descuento)
    total = precio_final * cantidad
```
**Ubicación:** Función `registrar_venta()` - Se aplica automáticamente

### Reto D: Validar Producto y Registrar Intentos Fallidos
```python
def realizar_venta():
    if not validar_producto(producto_id):
        registrar_error(f"Intento de venta con producto_id inválido: {producto_id}")
        print(f"✗ Producto no existe")
```
**Ubicación:** Función `realizar_venta()` - Opción 2, con log en `log.txt`

---

## 📁 Archivos Generados

| Archivo | Descripción |
|---------|-------------|
| `minitienda.ipynb` | Código ejecutable con celdas de prueba |
| `ventas.csv` | Datos de ventas (10+ registros) |
| `ingresos.png` | Gráfico exportado de barras |
| `log.txt` | Registro de intentos fallidos |
| `README.md` | Este archivo |

---

## 🚀 Cómo Ejecutar

### En Jupyter/Colab:
1. Abrir `minitienda.ipynb`
2. Ejecutar celdas en orden
3. Para menú interactivo: descomenta `menu()` en última celda

### En terminal Python:
```bash
python minitienda.py
```

---

## 📊 Respuestas a Preguntas Conceptuales

### ¿Qué parte la hizo Pandas? ¿Qué parte NumPy?

**Pandas:**
- Creación de `DataFrame()` para mostrar tabla de ventas con formato
- `.groupby('nombre')['total'].sum()` para agrupar ventas por producto
- `.to_csv('ventas.csv')` para guardar datos estructurados
- `.read_csv()` para cargar datos desde archivo

**NumPy:**
- `np.array()` para convertir listas a arreglos eficientes
- `np.sum()` para calcular total de ingresos
- `np.mean()` para obtener promedio de ventas
- `np.std()` para desviación estándar (variabilidad)
- `np.min()` / `np.max()` para valores extremos

---

### ¿Dónde usaste try/except y por qué?

| Ubicación | Excepción | Razón |
|-----------|-----------|-------|
| `realizar_venta()` | `ValueError` | El usuario puede ingresar texto en lugar de número |
| `realizar_venta()` | `KeyError` | El producto_id podría no existir en diccionarios |
| `cargar_csv()` | `FileNotFoundError` | El archivo ventas.csv podría no existir |
| `guardar_csv()` | `Exception` | Permisos insuficientes o disco lleno |
| `calcular_metricas()` | `ZeroDivisionError` | Evitar división por cero en promedios |
| `menu()` | `KeyboardInterrupt` | Capturar Ctrl+C del usuario |

---

### ¿Qué estructuras son tuplas, listas y diccionarios en el código?

**TUPLAS (Inmutables):**
```python
catalogo = (('P001', 'Laptop'), ('P002', 'Mouse'), ...)
# - No se pueden modificar
# - Ideal para catálogo fijo de productos
```

**LISTAS (Mutables):**
```python
ventas_registro = [
    {'producto_id': 'P001', 'cantidad': 1, 'total': 800.00},
    {'producto_id': 'P002', 'cantidad': 15, 'total': 356.25},
    ...
]
# - Crecen dinámicamente con cada venta
# - Se pueden agregar, eliminar, modificar
```

**DICCIONARIOS (Clave-Valor):**
```python
precios = {'P001': 800.00, 'P002': 25.00, 'P003': 75.00, ...}
stock = {'P001': 5, 'P002': 50, 'P003': 40, ...}

venta = {
    'producto_id': 'P001',
    'nombre': 'Laptop',
    'cantidad': 1,
    'precio_unitario': 800.00,
    'descuento_pct': 0,
    'total': 800.00,
    'fecha': '2024-01-15 14:30:00'
}
# - Acceso rápido por clave (O(1))
# - Flexibilidad en campos
```

---

## 🔄 Flujo del Programa

```
INICIO
  ↓
[Inicializar estructuras: Tuplas, Diccionarios, Listas]
  ↓
┌─────────────────────────────────┐
│   MENÚ PRINCIPAL (while True)   │
├─────────────────────────────────┤
│ 1) Ver catálogo (tuplas)        │
│ 2) Registrar venta              │
│    ├─ Validar producto          │
│    ├─ Verificar stock           │
│    ├─ Aplicar descuento (Reto C)│
│    └─ Guardar en lista          │
│ 3) Resumen (Pandas DataFrame)   │
│ 4) Métricas (NumPy)             │
│ 5) Graficar (Matplotlib)        │
│ 6) Exportar PNG (Reto B)        │
│ 7) Agregar producto (Reto A)    │
│ 8) Cargar CSV                   │
│ 9) Salir                        │
└─────────────────────────────────┘
  ↓
[Guardar CSV con Pandas]
  ↓
FIN
```

---

## 📝 Notas de Implementación

- **Validación robusta:** Cada operación verifica entrada antes de procesar
- **Logging completo:** Todos los errores se registran en `log.txt` con timestamp
- **Modularidad:** Cada función tiene una responsabilidad clara
- **Descuentos automáticos:** Se aplican sin intervención del usuario (Reto C)
- **Datos persistentes:** Las ventas se guardan automáticamente al salir

---

## 📧 Contacto

Para preguntas sobre la implementación, revisar el código en el notebook `minitienda.ipynb` con comentarios detallados en cada sección.
