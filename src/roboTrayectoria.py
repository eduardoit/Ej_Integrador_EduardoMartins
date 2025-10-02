import numpy as np
import pybullet as p
import pybullet_data
import time


def generar_trayectoria_circular(num_puntos=50, radio=2, altura=1):
    """
    Genera una trayectoria circular usando NumPy

    Args:
        num_puntos: cantidad de puntos en el círculo
        radio: radio del círculo
        altura: altura sobre el suelo

    Returns:
        array de posiciones (x, y, z)
    """
    angulos = np.linspace(0, 2 * np.pi, num_puntos)

    # Calcular posiciones usando funciones trigonométricas
    x = radio * np.cos(angulos)
    y = radio * np.sin(angulos)
    z = np.ones(num_puntos) * altura  # Altura constante

    # Combinar en una matriz de posiciones
    posiciones = np.column_stack([x, y, z])

    return posiciones


def generar_trayectoria_ocho(num_puntos=100, radio=2, altura=1):
    """
    Genera una trayectoria en forma de 8 usando NumPy

    Args:
        num_puntos: cantidad de puntos en la figura
        radio: tamaño de la figura
        altura: altura sobre el suelo

    Returns:
        array de posiciones (x, y, z)
    """
    t = np.linspace(0, 2 * np.pi, num_puntos)

    # Ecuaciones paramétricas para figura de 8
    x = radio * np.sin(t)
    y = radio * np.sin(t) * np.cos(t)
    z = np.ones(num_puntos) * altura

    posiciones = np.column_stack([x, y, z])

    return posiciones


def calcular_distancia_total(posiciones):
    """
    Calcula la distancia total recorrida usando NumPy

    Args:
        posiciones: array de posiciones (N, 3)

    Returns:
        distancia total en metros
    """
    # Calcular diferencias entre puntos consecutivos
    diferencias = np.diff(posiciones, axis=0)

    # Calcular distancia euclidiana de cada segmento
    distancias = np.linalg.norm(diferencias, axis=1)

    # Sumar todas las distancias
    distancia_total = np.sum(distancias)

    return distancia_total


def main():
    # Inicializar PyBullet en modo GUI
    p.connect(p.GUI)

    # Añadir la ruta de datos de PyBullet
    p.setAdditionalSearchPath(pybullet_data.getDataPath())

    # Configurar la cámara para mejor visualización
    p.resetDebugVisualizerCamera(
        cameraDistance=6,
        cameraYaw=45,
        cameraPitch=-30,
        cameraTargetPosition=[0, 0, 1]
    )

    # Cargar un plano para que el robot tenga superficie
    p.loadURDF("plane.urdf")

    # Cargar el robot R2D2
    robot_id = p.loadURDF("r2d2.urdf", [0, 0, 1])

    # Configurar gravedad
    p.setGravity(0, 0, -10)

    # ===== TRAYECTORIA 1: CÍRCULO =====
    print("\n--- Generando trayectoria circular ---")
    posiciones_circulo = generar_trayectoria_circular(num_puntos=100, radio=3, altura=1)
    distancia_circulo = calcular_distancia_total(posiciones_circulo)
    print(f"Distancia del círculo: {distancia_circulo:.2f} metros")

    # Orientación fija
    orientacion = p.getQuaternionFromEuler([0, 0, 0])
    posicion_anterior = None

    print("Iniciando simulación del círculo...")
    for i, posicion in enumerate(posiciones_circulo):
        p.resetBasePositionAndOrientation(robot_id, posicion, orientacion)

        # Dibujar línea roja para el círculo
        if posicion_anterior is not None:
            p.addUserDebugLine(posicion_anterior, posicion,
                               lineColorRGB=[1, 0, 0], lineWidth=2, lifeTime=0)

        posicion_anterior = posicion

        for _ in range(10):
            p.stepSimulation()
            time.sleep(1. / 240.)

        if i % 20 == 0:
            print(f"  Progreso: {(i / len(posiciones_circulo)) * 100:.1f}%")

    print("✓ Círculo completado\n")
    time.sleep(1)

    # ===== TRAYECTORIA 2: FIGURA DE 8 =====
    print("--- Generando trayectoria en forma de 8 ---")
    posiciones_ocho = generar_trayectoria_ocho(num_puntos=100, radio=2.5, altura=1)
    distancia_ocho = calcular_distancia_total(posiciones_ocho)
    print(f"Distancia de la figura 8: {distancia_ocho:.2f} metros")

    # Mover el robot al inicio de la figura 8
    p.resetBasePositionAndOrientation(robot_id, posiciones_ocho[0], orientacion)

    # Simular unos frames para que se vea el movimiento
    for _ in range(50):
        p.stepSimulation()
        time.sleep(1. / 240.)

    posicion_anterior = None

    print("Iniciando simulación de la figura 8...")
    for i, posicion in enumerate(posiciones_ocho):
        p.resetBasePositionAndOrientation(robot_id, posicion, orientacion)

        # Dibujar línea azul para la figura 8
        if posicion_anterior is not None:
            p.addUserDebugLine(posicion_anterior, posicion,
                               lineColorRGB=[0, 0, 1], lineWidth=2, lifeTime=0)

        posicion_anterior = posicion

        for _ in range(10):
            p.stepSimulation()
            time.sleep(1. / 240.)

        if i % 20 == 0:
            print(f"  Progreso: {(i / len(posiciones_ocho)) * 100:.1f}%")

    print("✓ Figura 8 completada\n")

    # ===== RESUMEN =====
    print("=" * 40)
    print("RESUMEN")
    print("=" * 40)
    print(f"Distancia círculo: {distancia_circulo:.2f} m")
    print(f"Distancia figura 8: {distancia_ocho:.2f} m")
    print(f"Distancia total: {distancia_circulo + distancia_ocho:.2f} m")
    print(f"Total de puntos: {len(posiciones_circulo) + len(posiciones_ocho)}")

    # Mantener la ventana abierta
    print("\nPresiona Ctrl+C para cerrar la simulación...")
    try:
        while True:
            p.stepSimulation()
            time.sleep(1. / 240.)
    except KeyboardInterrupt:
        print("\nCerrando simulación...")

    # Cerrar PyBullet
    p.disconnect()


if __name__ == "__main__":
    main()