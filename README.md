# 🟢 Lista Doblemente Enlazada en Python

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)]() 
[![Estado](https://img.shields.io/badge/Estado-Completado-brightgreen)]()

Este proyecto implementa una **lista doblemente enlazada** en Python, con **11 métodos** que permiten manejar nodos de manera completa.  
Cada nodo tiene un valor (`dato`) y apunta tanto al **siguiente nodo** como al **anterior**.  

---

## 📦 Diagrama conceptual de la clase

**Nodo**  
- `dato`: valor que almacena el nodo  
- `siguiente`: referencia al siguiente nodo  
- `anterior`: referencia al nodo anterior  

**ListaDoble**  
- `cabeza`: referencia al primer nodo de la lista  
- Métodos:  

### ➕ Métodos de inserción
- `insertar_inicio(dato)`  
- `insertar_final(dato)`  
- `insertar_posicion(dato, pos)`  
- `insertar_despues(dato, buscar)`  

### 🗑 Métodos de eliminación y modificación
- `eliminar(dato)`  
- `modificar_posicion(pos, nuevo_valor)`  

### 👀 Métodos de visualización
- `mostrar()`  
- `mostrar_inversa()`  

### 📊 Métodos de ordenamiento
- `ordenar_menor_mayor()`  
- `ordenar_mayor_menor()`  

### ➕ Métodos de cálculo
- `sumar_nodos()`  

---

## 🔗 Relación entre clases y nodos

```mermaid
classDiagram
class Nodo {
    +dato
    +siguiente
    +anterior
}

class ListaDoble {
    +cabeza
    +insertar_inicio(dato)
    +insertar_final(dato)
    +insertar_posicion(dato, pos)
    +insertar_despues(dato, buscar)
    +eliminar(dato)
    +modificar_posicion(pos, nuevo_valor)
    +mostrar()
    +mostrar_inversa()
    +ordenar_menor_mayor()
    +ordenar_mayor_menor()
    +sumar_nodos()
}

ListaDoble --> Nodo
