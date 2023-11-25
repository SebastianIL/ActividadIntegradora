import numpy as np
import matplotlib.pyplot as plt
from model import Ciudad
import gc

resultados = []
longitudes = []
pasos_reales = []

for num_coches in range(1, 11):
    pasos = []
    longitud = []
    reales = []
    # Repite la simulación 100 veces
    for _ in range(100):
        # Crea una nueva instancia del modelo
        modelo = Ciudad(num_agents=num_coches, width=31, height=32)
        while modelo.running:
            modelo.step()
        pasos.append(modelo.schedule.steps)
        longitud.append(modelo.promedios)
        reales.append(modelo.promediosReales)
        del modelo
    # Almacena el número promedio de pasos
    resultados.append(sum(pasos) / len(pasos))
    longitudes.append((sum(longitud) / len(longitud)))
    pasos_reales.append((sum(reales) / len(reales)))
    gc.collect()

resultados = np.array(resultados)
longitudes = np.array(longitudes)
pasos_reales = np.array(pasos_reales)

resultados_std = np.std(resultados)
longitudes_std = np.std(longitudes)
pasos_reales_std = np.std(pasos_reales)
# atropellados_std = np.std(atropellados)
# Grafica los resultados
plt.figure()
plt.plot(range(1, 11), resultados)
plt.title('Pasos necesarios para que todo los coches lleguen a su destino')
plt.suptitle('(100 repeticiones | Semáforos inteligentes)')
plt.xlabel('Número de coches')
plt.ylabel('Número promedio de pasos')
plt.show()

plt.figure()
plt.plot(range(1, 11), longitudes, label="Pasos de Dijkstra", color='red')
plt.plot(range(1, 11), pasos_reales, label="Pasos Realizados", color='blue')
plt.title('Pasos optimos promedio (Dijkstra)')
plt.suptitle('(100 repeticiones | Semáforos Inteligentes)')
plt.xlabel('Número de coches')
plt.ylabel('Número promedio de pasos')
plt.legend()
plt.show()
