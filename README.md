# Simulación de Robot con Trayectorias Matemáticas

Ejercicio Integrador - Programación Básica PRIA  
**Autor:** Eduardo Martins  
**Fecha:** Octubre 2025

## 📋 Descripción

Proyecto que integra las librerías **NumPy** (clásica) y **PyBullet** (emergente) para simular un robot móvil siguiendo trayectorias matemáticas generadas algorítmicamente en un entorno 3D.

El robot sigue dos tipos de trayectorias:
- **Trayectoria circular** (línea roja)
- **Trayectoria en forma de figura 8** (línea azul)

## 🎯 Objetivos

- Generar trayectorias matemáticas usando funciones trigonométricas con NumPy
- Calcular métricas de movimiento (distancia total, número de puntos)
- Simular el movimiento del robot en un entorno 3D con PyBullet
- Visualizar las trayectorias mediante líneas de colores

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**
- **NumPy**: Cálculos matemáticos y operaciones vectoriales
- **PyBullet**: Simulación física 3D
- **PyBullet Data**: Modelos URDF de robots

## 📦 Instalación

### Requisitos previos

```bash
python --version  # Verificar que tienes Python 3.8 o superior
```

### Instalar dependencias

```bash
pip install numpy pybullet pybullet_data
```

O usando un entorno virtual:

```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
# En Windows:
.venv\Scripts\activate
# En Mac/Linux:
source .venv/bin/activate

# Instalar dependencias
pip install numpy pybullet pybullet_data
```

## 🚀 Uso

Ejecutar el script principal:

```bash
python src/roboTrayectoria.py
```

El programa:
1. Abrirá una ventana de simulación 3D
2. El robot seguirá primero una trayectoria circular (roja)
3. Luego seguirá una trayectoria en forma de 8 (azul)
4. Mostrará en consola las métricas calculadas
5. Mantendrá la ventana abierta para observar el resultado

Para cerrar: presiona `Ctrl+C` en la terminal.

## 📊 Resultados

### Trayectoria Circular
- Puntos: 100
- Radio: 3.0 m
- Distancia: ~18.85 m

### Trayectoria Figura 8
- Puntos: 100
- Radio: 2.5 m
- Distancia: ~14.52 m

### Total
- Distancia recorrida: ~33.37 m
- Puntos visitados: 200

## 📁 Estructura del Proyecto

```
Ej_Integrador_EduardoMartins/
├── src/
│   └── roboTrayectoria.py    # Script principal
├── .venv/                     # Entorno virtual (no incluido en repo)
├── README.md                  # Este archivo
└── .gitignore                # Archivos ignorados por git
```

## 🔧 Funciones Principales

### `generar_trayectoria_circular(num_puntos, radio, altura)`
Genera una trayectoria circular usando ecuaciones paramétricas.

### `generar_trayectoria_ocho(num_puntos, radio, altura)`
Genera una trayectoria en forma de 8 (curva de Lissajous).

### `calcular_distancia_total(posiciones)`
Calcula la distancia euclidiana total recorrida.

## 📸 Capturas

<img width="425" height="238" alt="image" src="https://github.com/user-attachments/assets/a8b455f3-84e7-4ac2-aefe-23dfaa0447e1" />

*Vista del entorno mostrando ambas trayectorias*

## 📚 Referencias

- [NumPy Documentation](https://numpy.org/doc/)
- [PyBullet Quickstart Guide](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/)
- [PyBullet GitHub](https://github.com/bulletphysics/bullet3)

## 👨‍💻 Autor

**Eduardo Martins**  
Estudiante de Programación Básica - PRIA  
UTEC Universidad Tecnológica

## 📄 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

## 🙏 Agradecimientos

- Prof. MSc. André Kelbouscas por la guía en el proyecto
- Comunidad de PyBullet por la documentación
- Comunidad de NumPy por las herramientas matemáticas

---

**Fecha de última actualización:** Octubre 2025
