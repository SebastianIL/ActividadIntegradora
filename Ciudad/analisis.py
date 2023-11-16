import numpy as np
import matplotlib.pyplot as plt
from model import Ciudad
import gc

resultados = []
longitud = []

for num_coches in range(1, 17):
    pasos = []

    # Repite la simulación 100 veces
    for _ in range(100):
        # Crea una nueva instancia del modelo
        modelo = Ciudad(num_agents=num_coches, width=24, height=24)
        while modelo.running:
            modelo.step()
        pasos.append(modelo.schedule.steps)
        del modelo
    # Almacena el número promedio de pasos
    resultados.append(sum(pasos) / len(pasos))
    gc.collect()

resultados = np.array(resultados)

resultados_std = np.std(resultados)
# atropellados_std = np.std(atropellados)
# Grafica los resultados
plt.errorbar(range(1, 17), resultados, yerr=resultados_std)
plt.title('Pasos necesarios para que todo los coches lleguen a su destino')
plt.suptitle('(100 repeticiones)')
plt.xlabel('Número de coches')
plt.ylabel('Número promedio de pasos')
plt.show()

