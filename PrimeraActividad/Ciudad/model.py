import mesa
import random
import networkx as nx


class CalleNorte(mesa.Agent):  # noqa

    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id, model)

    def __str__(self):
        return "Calle Norte"

    def posiblesVecinos(self):
        vecindario = self.model.grid.get_neighborhood(self.pos, include_center=False, moore=False)
        vecindario = [(x, y) for x, y in vecindario if
                      0 <= x < self.model.grid.width and 0 <= y < self.model.grid.height]
        vecinos = self.model.grid.get_cell_list_contents(vecindario)
        vecinos_calle = [False, False, False, False]
        for vecino in vecinos:
            x, y = vecino.pos
            if x < 0 or y < 0 or x > 23 or y > 23:
                pass
            else:
                if (vecino.__str__() == "Calle Norte" or vecino.__str__() == "Calle Oeste" or vecino.__str__() == "Estacionamiento") and self.pos == (x + 1, y):
                    vecinos_calle[0] = True
                if (vecino.__str__() == "Calle Norte" or vecino.__str__() == "Calle Este" or vecino.__str__() == "Estacionamiento") and self.pos == (x - 1, y):
                    vecinos_calle[1] = True
                if (vecino.__str__() == "Calle Norte" or vecino.__str__() == "Calle Oeste" or vecino.__str__() == "Calle Este" or vecino.__str__() == "Estacionamiento") and self.pos == (x, y - 1):
                    vecinos_calle[3] = True
        return vecinos_calle

    def step(self):
        pass


class CalleSur(mesa.Agent):  # noqa

    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id, model)

    def __str__(self):
        return "Calle Sur"

    def posiblesVecinos(self):
        vecindario = self.model.grid.get_neighborhood(self.pos, include_center=False, moore=False)
        vecindario = [(x, y) for x, y in vecindario if
                      0 <= x < self.model.grid.width and 0 <= y < self.model.grid.height]
        vecinos = self.model.grid.get_cell_list_contents(vecindario)
        vecinos_calle = [False, False, False, False]
        for vecino in vecinos:
            x, y = vecino.pos
            if x < 0 or y < 0 or x > 23 or y > 23:
                pass
            else:
                if (vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Oeste" or vecino.__str__() == "Estacionamiento") and self.pos == (x + 1, y):
                    vecinos_calle[0] = True
                if (vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Este" or vecino.__str__() == "Estacionamiento") and self.pos == (x - 1, y):
                    vecinos_calle[1] = True
                if (vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Este" or vecino.__str__() == "Calle Oeste" or vecino.__str__() == "Estacionamiento") and self.pos == (x, y + 1):
                    vecinos_calle[2] = True
        return vecinos_calle

    def step(self):
        pass


class CalleEste(mesa.Agent):  # noqa

    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id, model)

    def __str__(self):
        return "Calle Este"

    def posiblesVecinos(self):
        vecindario = self.model.grid.get_neighborhood(self.pos, include_center=False, moore=False)
        vecindario = [(x, y) for x, y in vecindario if
                      0 <= x < self.model.grid.width and 0 <= y < self.model.grid.height]
        vecinos = self.model.grid.get_cell_list_contents(vecindario)
        vecinos_calle = [False, False, False, False]
        for vecino in vecinos:
            x, y = vecino.pos
            if x < 0 or y < 0 or x > 23 or y > 23:
                pass
            else:
                if (vecino.__str__() == "Calle Este" or vecino.__str__() == "Calle Norte" or vecino.__str__() == "Calle Sur" or vecino.__str__() == "Estacionamiento") and self.pos == (x - 1, y):
                    vecinos_calle[1] = True
                if (vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Este" or vecino.__str__() == "Estacionamiento") and self.pos == (x, y + 1):
                    vecinos_calle[2] = True
                if (vecino.__str__() == "Calle Norte" or vecino.__str__() == "Calle Este" or vecino.__str__() == "Estacionamiento") and self.pos == (x, y - 1):
                    vecinos_calle[3] = True
        return vecinos_calle

    def step(self):
        pass


class CalleOeste(mesa.Agent):  # noqa
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id, model)

    def __str__(self):
        return "Calle Oeste"

    def posiblesVecinos(self):
        vecindario = self.model.grid.get_neighborhood(self.pos, include_center=False, moore=False)
        vecindario = [(x, y) for x, y in vecindario if
                      0 <= x < self.model.grid.width and 0 <= y < self.model.grid.height]
        vecinos = self.model.grid.get_cell_list_contents(vecindario)
        vecinos_calle = [False, False, False, False]
        for vecino in vecinos:
            x, y = vecino.pos
            if x < 0 or y < 0 or x > 23 or y > 23:
                pass
            else:
                if ((vecino.__str__() == "Calle Oeste" or vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Norte or vecino.__str__() == Estacionamiento"
                     and self.pos == (x + 1, y))):
                    vecinos_calle[0] = True
                if (vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Oeste" or vecino.__str__() == "Estacionamiento") and self.pos == (x, y + 1):
                    vecinos_calle[2] = True
                if (vecino.__str__() == "Calle Norte" or vecino.__str__() == "Calle Oeste" or vecino.__str__() == "Estacionamiento") and self.pos == (x, y - 1):
                    vecinos_calle[3] = True
        return vecinos_calle

    def step(self):
        pass


class Estacionamiento(mesa.Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id, model)

    def __str__(self):
        return "Estacionamiento"

    def posiblesVecinos(self):
        vecindario = self.model.grid.get_neighborhood(self.pos, include_center=False, moore=False)
        vecindario = [(x, y) for x, y in vecindario if
                      0 <= x < self.model.grid.width and 0 <= y < self.model.grid.height]
        vecinos = self.model.grid.get_cell_list_contents(vecindario)
        vecinos_calle = [False, False, False, False]
        for vecino in vecinos:
            x, y = vecino.pos
            if x < 0 or y < 0 or x > 23 or y > 23:
                pass
            else:
                if ((vecino.__str__() == "Calle Este" or vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Norte"
                     or vecino.__str__() == "Calle Oeste") and self.pos == (x + 1, y)):
                    vecinos_calle[0] = True
                if ((vecino.__str__() == "Calle Este" or vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Norte"
                     or vecino.__str__() == "Calle Oeste") and self.pos == (x - 1, y)):
                    vecinos_calle[1] = True
                if ((vecino.__str__() == "Calle Este" or vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Norte"
                     or vecino.__str__() == "Calle Oeste") and self.pos == (x, y + 1)):
                    vecinos_calle[2] = True
                if ((vecino.__str__() == "Calle Este" or vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Norte"
                     or vecino.__str__() == "Calle Oeste") and self.pos == (x, y - 1)):
                    vecinos_calle[3] = True
        return vecinos_calle

    def step(self):
        pass


class Edificio(mesa.Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id, model)

    def __str__(self):
        return "Edificio"

    def step(self):
        pass


class Rotonda(mesa.Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id, model)

    def __str__(self):
        return "Rotonda"

    def step(self):
        pass


class Semaforo(mesa.Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        self.state = ""
        super().__init__(unique_id, model)
        if self.unique_id == 23:
            self.state = "Red"
        elif self.unique_id == 24:
            self.state = "Green"

    def __str__(self):
        if self.state == "Red":
            return "Semaforo Rojo"
        if self.state == "Green":
            return "Semaforo Verde"

    def step(self):
        current_step = self.model.current_step
        if current_step % 5 == 0 and current_step != 0:
            if self.state == "Red":
                self.state = "Green"
            elif self.state == "Green":
                self.state = "Red"


class Coche(mesa.Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        self.prev_pos = None
        self.origen = None
        self.destino = None
        self.terminado = False
        self.contado = False
        self.ruta = []
        self.ruta_completa = []
        self.pasos_finales = 0
        super().__init__(unique_id, model)

    def __str__(self):
        return "Coche"

    def generar_ruta(self):
        # Crear un grafo dirigido para representar la red vial
        grafo = nx.DiGraph()
        posicion_previa = None
        # Agregar nodos y aristas al grafo según la red vial
        for x in range(self.model.grid.width):
            for y in range(self.model.grid.height):
                pos = (x, y)
                calle = self.model.grid.get_cell_list_contents(pos)
                if isinstance(calle[0], (CalleEste, CalleNorte, CalleOeste, CalleSur)):
                    caminos = calle[0].posiblesVecinos()
                    if caminos[0]:
                        grafo.add_edge(pos, (x - 1, y), weight=1)
                    if caminos[1]:
                        grafo.add_edge(pos, (x + 1, y), weight=1)
                    if caminos[2]:
                        grafo.add_edge(pos, (x, y - 1), weight=1)
                    if caminos[3]:
                        grafo.add_edge(pos, (x, y + 1), weight=1)
                elif len(calle) >= 2:
                    if isinstance(calle[1], Estacionamiento):
                        caminos = calle[1].posiblesVecinos()
                        if caminos[0]:
                            grafo.add_edge(pos, (x - 1, y), weight=1)
                        if caminos[1]:
                            grafo.add_edge(pos, (x + 1, y), weight=1)
                        if caminos[2]:
                            grafo.add_edge(pos, (x, y - 1), weight=1)
                        if caminos[3]:
                            grafo.add_edge(pos, (x, y + 1), weight=1)

        # Obtener la posición actual del coche y su destino
        origen = self.origen
        destino = self.destino

        # Calcular la ruta más corta utilizando el algoritmo de Dijkstra
        ruta_corta = nx.shortest_path(grafo, source=origen, target=destino, weight='weight')

        # Retornar el array de coordenadas de la ruta
        return ruta_corta

    def step(self):
        calle = self.model.grid.get_cell_list_contents(self.pos)
        if self.model.current_step == 0:
            self.ruta = self.generar_ruta()
            self.model.grid.move_agent(self, self.ruta[0])
            self.ruta.remove(self.ruta[0])
            self.ruta_completa = self.ruta
            self.model.grid.move_agent(self, self.ruta[0])
            self.ruta.remove(self.ruta[0])
        else:
            # ===================== CHECK DE SEMAFORO ==========================
            if self.ruta:
                calleSig = self.model.grid.get_cell_list_contents((self.ruta[0]))
                if len(calleSig) == 2:
                    if (isinstance(calleSig[1], Coche) or calleSig[1].__str__() == "Semaforo Rojo") and len(self.ruta) != 2:
                        pass
                    else:
                        if self.ruta[0] == self.destino and not self.terminado:
                            self.pasos_finales = self.model.current_step
                            self.terminado = True
                            self.prev_pos = self.pos
                            self.model.grid.move_agent(self, self.ruta[0])
                            self.ruta.remove(self.ruta[0])
                        elif not self.terminado:
                            self.prev_pos = self.pos
                            self.model.grid.move_agent(self, self.ruta[0])
                            self.ruta.remove(self.ruta[0])

                elif len(calleSig) >= 3:
                    if isinstance(calleSig[2], Coche):
                        pass
                    else:
                        if self.ruta[0] == self.destino and not self.terminado:
                            self.terminado = True
                            self.prev_pos = self.pos
                            self.model.grid.move_agent(self, self.ruta[0])
                            self.ruta.remove(self.ruta[0])
                        elif not self.terminado:
                            self.prev_pos = self.pos
                            self.model.grid.move_agent(self, self.ruta[0])
                            self.ruta.remove(self.ruta[0])

                elif self.ruta[0] == self.destino and not self.terminado:
                    self.terminado = True
                    self.prev_pos = self.pos
                    self.model.grid.move_agent(self, self.ruta[0])
                    self.ruta.remove(self.ruta[0])
                elif not self.terminado:
                    self.prev_pos = self.pos
                    self.model.grid.move_agent(self, self.ruta[0])
                    self.ruta.remove(self.ruta[0])


class Ciudad(mesa.Model):
    def __init__(self, num_agents, width, height):
        super().__init__()
        self.num_agents = num_agents
        self.promedios = None
        self.promediosReales = None
        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.MultiGrid(width=width, height=height, torus=False)
        self.current_step = 0
        self.lista_coches = []
        self.terminados = 0

        print(num_agents)

        estacionamiento1 = Estacionamiento(1, self)
        self.schedule.add(estacionamiento1)
        estacionamiento2 = Estacionamiento(2, self)
        self.schedule.add(estacionamiento2)
        estacionamiento3 = Estacionamiento(3, self)
        self.schedule.add(estacionamiento3)
        estacionamiento4 = Estacionamiento(4, self)
        self.schedule.add(estacionamiento4)
        estacionamiento5 = Estacionamiento(5, self)
        self.schedule.add(estacionamiento5)
        estacionamiento6 = Estacionamiento(6, self)
        self.schedule.add(estacionamiento6)
        estacionamiento7 = Estacionamiento(7, self)
        self.schedule.add(estacionamiento7)
        estacionamiento8 = Estacionamiento(8, self)
        self.schedule.add(estacionamiento8)
        estacionamiento9 = Estacionamiento(9, self)
        self.schedule.add(estacionamiento9)
        estacionamiento10 = Estacionamiento(10, self)
        self.schedule.add(estacionamiento10)
        estacionamiento11 = Estacionamiento(11, self)
        self.schedule.add(estacionamiento11)
        estacionamiento12 = Estacionamiento(12, self)
        self.schedule.add(estacionamiento12)
        estacionamiento13 = Estacionamiento(13, self)
        self.schedule.add(estacionamiento13)
        estacionamiento14 = Estacionamiento(14, self)
        self.schedule.add(estacionamiento14)
        estacionamiento15 = Estacionamiento(15, self)
        self.schedule.add(estacionamiento15)
        estacionamiento16 = Estacionamiento(16, self)
        self.schedule.add(estacionamiento16)
        estacionamiento17 = Estacionamiento(17, self)
        self.schedule.add(estacionamiento17)

        edificio = Edificio(22, self)
        self.schedule.add(edificio)

        semaforo1 = Semaforo(23, self)
        semaforo2 = Semaforo(24, self)
        self.schedule.add(semaforo1)
        self.schedule.add(semaforo2)

        rotonda = Rotonda(25, self)
        self.schedule.add(rotonda)

        # ==========Orilla Oeste==============

        for i in range(23):
            calle_sur = CalleSur(i + 26, self)
            self.schedule.add(calle_sur)
            self.grid.place_agent(calle_sur, (0, i + 1))

        for i in range(21):
            calle_sur = CalleSur(i + 49, self)
            self.schedule.add(calle_sur)
            self.grid.place_agent(calle_sur, (1, i + 2))

        self.grid.place_agent(semaforo1, (0, 12))
        self.grid.place_agent(semaforo1, (1, 12))

        # ============== Orilla Sur =======================

        for i in range(23):
            calle_este = CalleEste(70 + i, self)
            self.schedule.add(calle_este)
            self.grid.place_agent(calle_este, (i, 0))

        for i in range(21):
            calle_este = CalleEste(93 + i, self)
            self.schedule.add(calle_este)
            self.grid.place_agent(calle_este, (i + 1, 1))

        self.grid.place_agent(semaforo2, (11, 0))
        self.grid.place_agent(semaforo2, (11, 1))

        # ==========Orilla Este==============

        for i in range(23):
            calle_norte = CalleNorte(114 + i, self)
            self.schedule.add(calle_norte)
            self.grid.place_agent(calle_norte, (23, i))

        for i in range(21):
            calle_norte = CalleNorte(137 + i, self)
            self.schedule.add(calle_norte)
            self.grid.place_agent(calle_norte, (22, i + 1))

        self.grid.place_agent(semaforo1, (22, 7))
        self.grid.place_agent(semaforo1, (23, 7))

        # ==========Orilla Norte==============

        for i in range(23):
            calle_oeste = CalleOeste(158 + i, self)
            self.schedule.add(calle_oeste)
            self.grid.place_agent(calle_oeste, (i + 1, 23))

        for i in range(21):
            calle_oeste = CalleOeste(182 + i, self)
            self.schedule.add(calle_oeste)
            self.grid.place_agent(calle_oeste, (i + 2, 22))

        self.grid.place_agent(semaforo2, (16, 22))
        self.grid.place_agent(semaforo2, (16, 23))

        # ========== Edificios =============
        for i in range(6):
            for j in range(4):
                self.grid.place_agent(edificio, (j + 2, i + 2))

        for i in range(6):
            for j in range(4):
                self.grid.place_agent(edificio, (j + 8, i + 2))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 16, i + 6))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 16, i + 2))

        for i in range(4):
            for j in range(3):
                self.grid.place_agent(edificio, (j + 2, i + 12))

        for i in range(4):
            for j in range(5):
                self.grid.place_agent(edificio, (j + 7, i + 12))

        for i in range(4):
            for j in range(2):
                self.grid.place_agent(edificio, (j + 16, i + 12))

        for i in range(4):
            for j in range(2):
                self.grid.place_agent(edificio, (j + 20, i + 12))

        for i in range(4):
            for j in range(10):
                self.grid.place_agent(edificio, (j + 2, i + 18))

        for i in range(4):
            for j in range(2):
                self.grid.place_agent(edificio, (j + 16, i + 18))

        for i in range(4):
            for j in range(2):
                self.grid.place_agent(edificio, (j + 20, i + 18))

        # ============= FIN ========================
        # ============= Calles interiores Norte ========================
        it = 0
        for i in range(4):
            for j in range(2):
                calle_norte = CalleNorte(203 + it, self)
                self.schedule.add(calle_norte)
                self.grid.place_agent(calle_norte, (j + 5, i + 12))
                it += 1
        self.grid.place_agent(semaforo1, (5, 15))
        self.grid.place_agent(semaforo1, (6, 15))

        it = 0
        for i in range(6):
            for j in range(2):
                calle_norte = CalleNorte(211 + it, self)
                self.schedule.add(calle_norte)
                self.grid.place_agent(calle_norte, (j + 14, i + 2))
                it += 1
        self.grid.place_agent(semaforo1, (14, 3))
        self.grid.place_agent(semaforo1, (15, 3))

        it = 0
        for i in range(10):
            for j in range(2):
                calle_norte = CalleNorte(223 + it, self)
                self.schedule.add(calle_norte)
                self.grid.place_agent(calle_norte, (j + 14, i + 12))
                it += 1
        self.grid.place_agent(semaforo1, (14, 21))
        self.grid.place_agent(semaforo1, (15, 21))

        it = 0
        for i in range(4):
            for j in range(2):
                calle_norte = CalleNorte(243 + it, self)
                self.schedule.add(calle_norte)
                self.grid.place_agent(calle_norte, (j + 18, i + 12))
                it += 1

        # ================ Calles interiores Sur =======================
        it = 0
        for i in range(6):
            for j in range(2):
                calle_sur = CalleSur(251 + it, self)
                self.schedule.add(calle_sur)
                self.grid.place_agent(calle_sur, (j + 6, i + 2))
                it += 1

        it = 0
        for i in range(6):
            for j in range(2):
                calle_sur = CalleSur(263 + it, self)
                self.schedule.add(calle_sur)
                self.grid.place_agent(calle_sur, (j + 12, i + 2))
                it += 1
        self.grid.place_agent(semaforo1, (12, 2))
        self.grid.place_agent(semaforo1, (13, 2))

        it = 0
        for i in range(10):
            for j in range(2):
                calle_sur = CalleSur(275 + it, self)
                self.schedule.add(calle_sur)
                self.grid.place_agent(calle_sur, (j + 12, i + 12))
                it += 1

        it = 0
        for i in range(4):
            for j in range(2):
                calle_sur = CalleSur(295 + it, self)
                self.schedule.add(calle_sur)
                self.grid.place_agent(calle_sur, (j + 18, i + 18))
                it += 1

        # ================ Calles interiores Oeste =======================
        it = 0
        for i in range(2):
            for j in range(10):
                calle_oeste = CalleOeste(303 + it, self)
                self.schedule.add(calle_oeste)
                self.grid.place_agent(calle_oeste, (j + 2, i + 16))
                it += 1
        self.grid.place_agent(semaforo2, (7, 16))
        self.grid.place_agent(semaforo2, (7, 17))

        it = 0
        for i in range(2):
            for j in range(10):
                calle_oeste = CalleOeste(323 + it, self)
                self.schedule.add(calle_oeste)
                self.grid.place_agent(calle_oeste, (j + 2, i + 10))
                it += 1
        self.grid.place_agent(semaforo2, (2, 10))
        self.grid.place_agent(semaforo2, (2, 11))

        it = 0
        for i in range(2):
            for j in range(6):
                calle_oeste = CalleOeste(343 + it, self)
                self.schedule.add(calle_oeste)
                self.grid.place_agent(calle_oeste, (j + 16, i + 10))
                it += 1

        it = 0
        for i in range(2):
            for j in range(6):
                calle_oeste = CalleOeste(355 + it, self)
                self.schedule.add(calle_oeste)
                self.grid.place_agent(calle_oeste, (j + 16, i + 4))
                it += 1
        self.grid.place_agent(semaforo2, (16, 4))
        self.grid.place_agent(semaforo2, (16, 5))

        # ================ Calles interiores Este =======================
        it = 0
        for i in range(2):
            for j in range(10):
                calle_este = CalleEste(367 + it, self)
                self.schedule.add(calle_este)
                self.grid.place_agent(calle_este, (j + 2, i + 8))
                it += 1

        it = 0
        for i in range(2):
            for j in range(6):
                calle_este = CalleEste(387 + it, self)
                self.schedule.add(calle_este)
                self.grid.place_agent(calle_este, (j + 16, i + 8))
                it += 1
        self.grid.place_agent(semaforo2, (21, 8))
        self.grid.place_agent(semaforo2, (21, 9))

        # ================ ROTONDA =====================
        it = 0
        for i in range(2):
            for j in range(6):
                calle_este = CalleEste(399 + it, self)
                self.schedule.add(calle_este)
                self.grid.place_agent(calle_este, (j + 16, i + 16))
                it += 1

        for i in range(2):
            for j in range(2):
                self.grid.place_agent(rotonda, (j + 13, i + 9))

        for i in range(4):
            calle_norte = CalleNorte(411 + i, self)
            self.schedule.add(calle_norte)
            self.grid.place_agent(calle_norte, (15, i + 8))

        for i in range(4):
            calle_sur = CalleSur(i + 415, self)
            self.schedule.add(calle_sur)
            self.grid.place_agent(calle_sur, (12, i + 8))

        for i in range(2):
            calle_oeste = CalleOeste(419 + i, self)
            self.schedule.add(calle_oeste)
            self.grid.place_agent(calle_oeste, (13 + i, 11))

        for i in range(2):
            calle_este = CalleEste(421 + i, self)
            self.schedule.add(calle_este)
            self.grid.place_agent(calle_este, (13 + i, 8))

        # ================ ESTACIONAMIENTOS ===================

        self.grid.place_agent(estacionamiento1, (9, 21))
        self.grid.place_agent(estacionamiento2, (2, 20))
        self.grid.place_agent(estacionamiento3, (17, 20))
        self.grid.place_agent(estacionamiento4, (11, 19))
        self.grid.place_agent(estacionamiento5, (20, 19))
        self.grid.place_agent(estacionamiento6, (6, 18))
        self.grid.place_agent(estacionamiento7, (8, 15))
        self.grid.place_agent(estacionamiento8, (21, 14))
        self.grid.place_agent(estacionamiento9, (4, 13))
        self.grid.place_agent(estacionamiento10, (11, 13))
        self.grid.place_agent(estacionamiento11, (16, 13))
        self.grid.place_agent(estacionamiento12, (2, 6))
        self.grid.place_agent(estacionamiento13, (17, 6))
        self.grid.place_agent(estacionamiento14, (19, 6))
        self.grid.place_agent(estacionamiento15, (5, 3))
        self.grid.place_agent(estacionamiento16, (8, 3))
        self.grid.place_agent(estacionamiento17, (19, 3))

        # ================ VEHICULOS ===================
        estacionamiento = self.estacionamiento_position()
        destinos = self.estacionamiento_position()
        for i in range(num_agents):
            x, y = random.choice(estacionamiento)
            estacionamiento.remove((x, y))
            coche = Coche(i + 423, self)
            coche.origen = (x, y)
            self.schedule.add(coche)
            self.grid.place_agent(coche, (x, y))
            v, w = random.choice(destinos)
            coche.destino = (v, w)
            while coche.destino == coche.origen:
                del coche.destino
                v, w = random.choice(destinos)
                coche.destino = (v, w)

            destinos.remove((v, w))
            self.lista_coches.append(coche)

        # example data collector
        self.datacollector = mesa.datacollection.DataCollector(
            # model_reporters={
            #     "Coches": self.lista_coches,
            #     "Pasos restantes": self.lista_coches
            # }
        )
        self.running = True
        self.datacollector.collect(self)

    def pasos_Dijkstra(self):
        coches = self.lista_coches
        longitudes = []
        for coche in coches:
            longitudes.append(len(coche.ruta))
        return longitudes

    def estacionamiento_position(self):
        estacionamiento_cells = []

        for x in range(self.grid.width):
            for y in range(self.grid.height):
                cell_list = self.grid.get_cell_list_contents([(x, y)])
                if len(cell_list) == 2:
                    if cell_list[1].__str__() == "Estacionamiento":
                        estacionamiento_cells.append((x, y))

        if estacionamiento_cells:
            return estacionamiento_cells
        else:
            return None

    def get_pos(self):
        coches = []
        for x in range(self.grid.width):
            for y in range(self.grid.height):
                cell_list = self.grid.get_cell_list_contents([(x, y)])
                if len(cell_list) >= 2:
                    for i in range(self.num_agents):
                        if cell_list[1].unique_id == 423 + i:
                            coches.append((x, y))
                        elif len(cell_list) == 3:
                            if cell_list[2].unique_id == 423 + i:
                                coches.append((x, y))
                del cell_list
        return coches

    def estado_semaforo(self):
        semaforo1 = False
        semaforo2 = False
        estados = []
        for x in range(self.grid.width):
            for y in range(self.grid.height):
                cell_list = self.grid.get_cell_list_contents([(x, y)])
                if len(cell_list) >= 2:
                    if cell_list[1].unique_id == 23 and not semaforo1:
                        estados.append(cell_list[1].__str__())
                        semaforo1 = True
                    if cell_list[1].unique_id == 24 and not semaforo2:
                        estados.append(cell_list[1].__str__())
                        semaforo2 = True

        return estados

    def longitud_promedio(self):
        lista = []
        for coche in self.lista_coches:
            lista.append(len(coche.ruta_completa))
        promedio = (sum(lista)/len(lista))
        print(promedio)
        return promedio

    def pasos_finales(self):
        elementos = []
        for coche in self.lista_coches:
            elementos.append(coche.pasos_finales)
        promedio = (sum(elementos)/len(elementos))
        return promedio

    def step(self):
        if self.current_step == 1:
            self.promedios = self.longitud_promedio()
        self.datacollector.collect(self)
        self.schedule.step()
        self.current_step += 1

        for coche in self.lista_coches:
            if coche.terminado and not coche.contado:
                self.terminados += 1
                coche.contado = True
        if self.terminados == self.num_agents:
            self.promediosReales = self.pasos_finales()
            print(self.promediosReales)
            self.running = False
