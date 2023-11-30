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
            if x < 0 or y < 0 or x > 30 or y > 31:
                pass
            else:
                if (
                        vecino.__str__() == "Calle Norte" or vecino.__str__() == "Calle Oeste" or vecino.__str__() == "Estacionamiento" or vecino.__str__() == "Hospital") and self.pos == (
                x + 1, y):
                    vecinos_calle[0] = True
                if (
                        vecino.__str__() == "Calle Norte" or vecino.__str__() == "Calle Este" or vecino.__str__() == "Estacionamiento" or vecino.__str__() == "Hospital") and self.pos == (
                x - 1, y):
                    vecinos_calle[1] = True
                if (
                        vecino.__str__() == "Calle Norte" or vecino.__str__() == "Calle Oeste" or vecino.__str__() == "Calle Este" or vecino.__str__() == "Estacionamiento" or vecino.__str__() == "Hospital") and self.pos == (
                x, y - 1):
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
            if x < 0 or y < 0 or x > 30 or y > 31:
                pass
            else:
                if (
                        vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Oeste" or vecino.__str__() == "Estacionamiento" or vecino.__str__() == "Hospital") and self.pos == (
                x + 1, y):
                    vecinos_calle[0] = True
                if (
                        vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Este" or vecino.__str__() == "Estacionamiento" or vecino.__str__() == "Hospital") and self.pos == (
                x - 1, y):
                    vecinos_calle[1] = True
                if (
                        vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Este" or vecino.__str__() == "Calle Oeste" or vecino.__str__() == "Estacionamiento" or vecino.__str__() == "Hospital") and self.pos == (
                x, y + 1):
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
            if x < 0 or y < 0 or x > 30 or y > 31:
                pass
            else:
                if (
                        vecino.__str__() == "Calle Este" or vecino.__str__() == "Calle Norte" or vecino.__str__() == "Calle Sur" or vecino.__str__() == "Estacionamiento" or vecino.__str__() == "Hospital") and self.pos == (
                x - 1, y):
                    vecinos_calle[1] = True
                if (
                        vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Este" or vecino.__str__() == "Estacionamiento" or vecino.__str__() == "Hospital") and self.pos == (
                x, y + 1):
                    vecinos_calle[2] = True
                if (
                        vecino.__str__() == "Calle Norte" or vecino.__str__() == "Calle Este" or vecino.__str__() == "Estacionamiento" or vecino.__str__() == "Hospital") and self.pos == (
                x, y - 1):
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
            if x < 0 or y < 0 or x > 30 or y > 31:
                pass
            else:
                if (
                        vecino.__str__() == "Calle Oeste" or vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Norte" or vecino.__str__() == "Estacionamiento" or vecino.__str__() == "Hospital") and self.pos == (
                x + 1, y):
                    vecinos_calle[0] = True
                if (
                        vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Oeste" or vecino.__str__() == "Estacionamiento" or vecino.__str__() == "Hospital") and self.pos == (
                x, y + 1):
                    vecinos_calle[2] = True
                if (
                        vecino.__str__() == "Calle Norte" or vecino.__str__() == "Calle Oeste" or vecino.__str__() == "Estacionamiento" or vecino.__str__() == "Hospital") and self.pos == (
                x, y - 1):
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
            if x < 0 or y < 0 or x > 30 or y > 31:
                pass
            else:
                if ((
                        vecino.__str__() == "Calle Este" or vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Norte"
                        or vecino.__str__() == "Calle Oeste") and self.pos == (x + 1, y)):
                    vecinos_calle[0] = True
                if ((
                        vecino.__str__() == "Calle Este" or vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Norte"
                        or vecino.__str__() == "Calle Oeste") and self.pos == (x - 1, y)):
                    vecinos_calle[1] = True
                if ((
                        vecino.__str__() == "Calle Este" or vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Norte"
                        or vecino.__str__() == "Calle Oeste") and self.pos == (x, y + 1)):
                    vecinos_calle[2] = True
                if ((
                        vecino.__str__() == "Calle Este" or vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Norte"
                        or vecino.__str__() == "Calle Oeste") and self.pos == (x, y - 1)):
                    vecinos_calle[3] = True
        return vecinos_calle

    def step(self):
        pass


class Banqueta(mesa.Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id, model)

    def __str__(self):
        return "Banqueta"

    def posiblesVecinos(self):
        vecindario = self.model.grid.get_neighborhood(self.pos, include_center=False, moore=False)
        vecindario = [(x, y) for x, y in vecindario if
                      0 <= x < self.model.grid.width and 0 <= y < self.model.grid.height]
        vecinos = self.model.grid.get_cell_list_contents(vecindario)
        vecinos_calle = [False, False, False, False]
        for vecino in vecinos:
            x, y = vecino.pos
            if x < 0 or y < 0 or x > 30 or y > 31:
                pass
            else:
                # banqueta = self.model.grid.get_cell_list_contents((x , y))
                if (
                        vecino.__str__() == "Banqueta" or vecino.__str__() == "Estacionamiento" or vecino.__str__() == "Semaforo Rojo" or vecino.__str__() == "Semaforo Amarillo") and self.pos == (
                        x + 1, y):
                    vecinos_calle[0] = True
                if (
                        vecino.__str__() == "Banqueta" or vecino.__str__() == "Estacionamiento" or vecino.__str__() == "Semaforo Rojo" or vecino.__str__() == "Semaforo Amarillo") and self.pos == (
                        x - 1, y):
                    vecinos_calle[1] = True
                if (
                        vecino.__str__() == "Banqueta" or vecino.__str__() == "Estacionamiento" or vecino.__str__() == "Semaforo Rojo" or vecino.__str__() == "Semaforo Amarillo") and self.pos == (
                        x, y + 1):
                    vecinos_calle[2] = True
                if (
                        vecino.__str__() == "Banqueta" or vecino.__str__() == "Estacionamiento" or vecino.__str__() == "Semaforo Rojo") and self.pos == (
                        x, y - 1):
                    vecinos_calle[3] = True
        return vecinos_calle

    def step(self):
        pass


class Semaforo(mesa.Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        self.state = "Yellow"
        self.steps = 0
        self.coche = False
        super().__init__(unique_id, model)

    def __str__(self):
        if self.state == "Red":
            return "Semaforo Rojo"
        elif self.state == "Green":
            return "Semaforo Verde"
        elif self.state == "Yellow":
            return "Semaforo Amarillo"

    def Conteo(self):
        celda = self.model.grid.get_cell_list_contents(self.pos)
        x, y = self.pos
        vecinos = []

        if self.pos is not None:
            if isinstance(celda[0], CalleNorte):
                vecinos = [(x, y), (x, y - 1), (x, y - 2), (x, y - 3),
                           (x + 1, y - 1), (x + 1, y - 2), (x + 1, y - 3)]
            elif isinstance(celda[0], CalleSur):
                vecinos = [(x, y), (x - 1, y), (x, y + 1), (x, y + 2), (x, y + 3),
                           (x - 1, y + 1), (x - 1, y + 2), (x - 1, y + 3)]
            elif isinstance(celda[0], CalleEste):
                vecinos = [(x, y), (x, y - 1), (x - 1, y), (x - 2, y), (x - 3, y),
                           (x - 1, y - 1), (x - 2, y - 1), (x - 3, y - 1)]
            elif isinstance(celda[0], CalleOeste) and (x + 3) < 31:
                vecinos = [(x, y), (x, y + 1), (x + 1, y), (x + 2, y), (x + 3, y),
                           (x + 1, y + 1), (x + 2, y + 1), (x + 3, y + 1),
                           (x, y - 1), (x + 1, y - 1), (x + 2, y - 1), (x + 3, y - 1)]
            elif isinstance(celda[0], CalleOeste) and (x + 3) >= 31:
                vecinos = [(x, y), (x, y + 1), (x + 1, y), (x + 2, y),
                           (x + 1, y + 1), (x + 2, y + 1)]
        it = 0
        conteo = 0
        coords = [False, False, False, False,
                  False, False, False, False,
                  False, False, False, False]
        for vecino in vecinos:
            checar = self.model.grid.get_cell_list_contents(vecino)
            if len(checar) == 2:
                if isinstance(checar[1], Coche):
                    coords[it] = True
            if len(checar) == 3:
                if isinstance(checar[2], Coche) and not isinstance(checar[0], Estacionamiento):
                    coords[it] = True
            it += 1
        for coord in coords:
            if coord:
                conteo += 1

        return conteo

    def ConteoEmergencia(self):
        celda = self.model.grid.get_cell_list_contents(self.pos)
        x, y = self.pos
        vecinos = []

        if self.pos is not None:
            if isinstance(celda[0], CalleNorte):
                vecinos = [(x, y), (x, y - 1), (x, y - 2), (x, y - 3),
                           (x + 1, y - 1), (x + 1, y - 2), (x + 1, y - 3)]
            elif isinstance(celda[0], CalleSur):
                vecinos = [(x, y), (x - 1, y), (x, y + 1), (x, y + 2), (x, y + 3),
                           (x - 1, y + 1), (x - 1, y + 2), (x - 1, y + 3)]
            elif isinstance(celda[0], CalleEste):
                vecinos = [(x, y), (x, y - 1), (x - 1, y), (x - 2, y), (x - 3, y),
                           (x - 1, y - 1), (x - 2, y - 1), (x - 3, y - 1)]
            elif isinstance(celda[0], CalleOeste) and (x + 3) < 31:
                vecinos = [(x, y), (x, y + 1), (x + 1, y), (x + 2, y), (x + 3, y),
                           (x + 1, y + 1), (x + 2, y + 1), (x + 3, y + 1),
                           (x, y - 1), (x + 1, y - 1), (x + 2, y - 1), (x + 3, y - 1)]
            elif isinstance(celda[0], CalleOeste) and (x + 3) >= 31:
                vecinos = [(x, y), (x, y + 1), (x + 1, y), (x + 2, y),
                           (x + 1, y + 1), (x + 2, y + 1)]
        it = 0
        conteo = 0
        coords = [False, False, False, False,
                  False, False, False, False,
                  False, False, False, False]
        for vecino in vecinos:
            checar = self.model.grid.get_cell_list_contents(vecino)
            if len(checar) == 2:
                if isinstance(checar[1], Ambulancia):
                    coords[it] = True
            if len(checar) == 3:
                if isinstance(checar[2], Ambulancia) and not isinstance(checar[0], Estacionamiento):
                    coords[it] = True
            it += 1
        for coord in coords:
            if coord:
                conteo += 1

        return conteo

    def posiblesVecinos(self):
        vecindario = self.model.grid.get_neighborhood(self.pos, include_center=False, moore=False)
        vecindario = [(x, y) for x, y in vecindario if
                      0 <= x < self.model.grid.width and 0 <= y < self.model.grid.height]
        vecinos = self.model.grid.get_cell_list_contents(vecindario)
        vecinos_calle = [False, False, False, False]
        for vecino in vecinos:
            x, y = vecino.pos
            if x < 0 or y < 0 or x > 30 or y > 31:
                pass
            else:
                # banqueta = self.model.grid.get_cell_list_contents((x , y))
                if (
                        vecino.__str__() == "Banqueta" or vecino.__str__() == "Semaforo Amarillo" or vecino.__str__() == "Semaforo Rojo") and self.pos == (
                        x + 1, y):
                    vecinos_calle[0] = True
                if (
                        vecino.__str__() == "Banqueta" or vecino.__str__() == "Semaforo Amarillo" or vecino.__str__() == "Semaforo Rojo") and self.pos == (
                        x - 1, y):
                    vecinos_calle[1] = True
                if (
                        vecino.__str__() == "Banqueta" or vecino.__str__() == "Semaforo Amarillo" or vecino.__str__() == "Semaforo Rojo") and self.pos == (
                        x, y + 1):
                    vecinos_calle[2] = True
                if (
                        vecino.__str__() == "Banqueta" or vecino.__str__() == "Estacionamiento" or vecino.__str__() == "Semaforo Rojo") and self.pos == (
                        x, y - 1):
                    vecinos_calle[3] = True
        return vecinos_calle

    def semaforo_opuesto(self):
        x, y = self.pos
        semaforo = None
        if self.pos is not None:
            vecinos = self.model.grid.get_neighborhood((x, y), include_center=False, moore=True)
            for vecino in vecinos:
                vecino = self.model.grid.get_cell_list_contents(vecino)
                if len(vecino) >= 2:
                    if isinstance(vecino[1], Semaforo) and vecino[1].pos is not None and vecino[1].pos != self.pos:
                        semaforo = vecino[1]

            vecinos = self.model.grid.get_neighborhood((x + 1, y + 1), include_center=False, moore=True)
            for vecino in vecinos:
                vecino = self.model.grid.get_cell_list_contents(vecino)
                if len(vecino) >= 2:
                    if isinstance(vecino[1], Semaforo) and vecino[1].pos is not None and vecino[1].pos != self.pos:
                        semaforo = vecino[1]

            vecinos = self.model.grid.get_neighborhood((x - 1, y - 1), include_center=False, moore=True)
            for vecino in vecinos:
                vecino = self.model.grid.get_cell_list_contents(vecino)
                if len(vecino) >= 2:
                    if isinstance(vecino[1], Semaforo) and vecino[1].pos is not None and vecino[1].pos != self.pos:
                        semaforo = vecino[1]

            vecinos = self.model.grid.get_neighborhood((x - 1, y + 1), include_center=False, moore=True)
            for vecino in vecinos:
                vecino = self.model.grid.get_cell_list_contents(vecino)
                if len(vecino) >= 2:
                    if isinstance(vecino[1], Semaforo) and vecino[1].pos is not None and vecino[1].pos != self.pos:
                        semaforo = vecino[1]

            vecinos = self.model.grid.get_neighborhood((x + 1, y - 1), include_center=False, moore=True)
            for vecino in vecinos:
                vecino = self.model.grid.get_cell_list_contents(vecino)
                if len(vecino) >= 2:
                    if isinstance(vecino[1], Semaforo) and vecino[1].pos is not None and vecino[1].pos != self.pos:
                        semaforo = vecino[1]

        if semaforo is None:
            pass
        else:
            return semaforo

    def step(self):
        if isinstance(self.semaforo_opuesto(), Semaforo):
            opuesto = self.semaforo_opuesto()
            if self.ConteoEmergencia() == 0 and opuesto.ConteoEmergencia() == 0:
                if self.Conteo() == 0 and opuesto.Conteo() == 0:
                    self.state = "Yellow"
                    opuesto.state = "Yellow"
                elif self.Conteo() > opuesto.Conteo():
                    opuesto.state = "Red"
                    self.state = "Green"
                    self.steps += 1
                elif self.Conteo() < opuesto.Conteo():
                    opuesto.state = "Green"
                    self.state = "Red"
                    self.steps += 1
                    if self.steps != 0 and self.steps % 5 == 0:
                        if self.Conteo() > opuesto.Conteo() and self.steps % 5 == 0:
                            opuesto.state = "Red"
                            self.state = "Green"
                            self.steps += 1
                        elif self.Conteo() < opuesto.Conteo():
                            opuesto.state = "Green"
                            self.state = "Red"
                            self.steps += 1
            elif self.ConteoEmergencia() > opuesto.ConteoEmergencia():
                opuesto.state = "Red"
                self.state = "Green"
                self.steps += 1
            elif self.ConteoEmergencia() < opuesto.ConteoEmergencia():
                self.state = "Red"
                opuesto.state = "Green"
                self.steps += 1
        else:
            if self.Conteo() > 0:
                self.state = "Green"
            else:
                self.state = "Yellow"


class Edificio(mesa.Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id, model)

    def __str__(self):
        return "Edificio"

    def step(self):
        pass


class Hospital(mesa.Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id, model)

    def __str__(self):
        return "Hospital"

    def posiblesVecinos(self):
        vecindario = self.model.grid.get_neighborhood(self.pos, include_center=False, moore=False)
        vecindario = [(x, y) for x, y in vecindario if
                      0 <= x < self.model.grid.width and 0 <= y < self.model.grid.height]
        vecinos = self.model.grid.get_cell_list_contents(vecindario)
        vecinos_calle = [False, False, False, False]
        for vecino in vecinos:
            x, y = vecino.pos
            if x < 0 or y < 0 or x > 30 or y > 31:
                pass
            else:
                if ((
                        vecino.__str__() == "Calle Este" or vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Norte"
                        or vecino.__str__() == "Calle Oeste") and self.pos == (x + 1, y)):
                    vecinos_calle[0] = True
                if ((
                        vecino.__str__() == "Calle Este" or vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Norte"
                        or vecino.__str__() == "Calle Oeste") and self.pos == (x - 1, y)):
                    vecinos_calle[1] = True
                if ((
                        vecino.__str__() == "Calle Este" or vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Norte"
                        or vecino.__str__() == "Calle Oeste") and self.pos == (x, y + 1)):
                    vecinos_calle[2] = True
                if ((
                        vecino.__str__() == "Calle Este" or vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Norte"
                        or vecino.__str__() == "Calle Oeste") and self.pos == (x, y - 1)):
                    vecinos_calle[3] = True
        return vecinos_calle

    def step(self):
        pass


class Peaton(mesa.Agent):
    def __init__(self, unique_id, model):
        self.origen = None
        self.unique_id = unique_id
        self.prev_pos = None

        super().__init__(unique_id, model)

    def __str__(self):
        return "Peaton"

    def step(self):
        pasos = []
        x, y = self.pos
        calle = self.model.grid.get_cell_list_contents(self.pos)
        if x < 0 or y < 0 or x > 30 or y > 31:
            pass
        else:
            if isinstance(calle[0], Banqueta) and not isinstance(calle[0], Edificio) and len(calle) >= 1:
                caminos = calle[0].posiblesVecinos()
                siguiente = self.model.grid.get_cell_list_contents((x - 1, y))
                if caminos[0] and not isinstance(siguiente[0], Edificio) and (x-1) >= 0:
                    pasos.append((x - 1, y))
                if (x+1) < 30:
                    siguiente = self.model.grid.get_cell_list_contents((x + 1, y))
                    if caminos[1] and not isinstance(siguiente[0], Edificio):
                        pasos.append((x + 1, y))
                siguiente = self.model.grid.get_cell_list_contents((x, y - 1))
                if caminos[2] and not isinstance(siguiente[0], Edificio) and (y-1) >= 0:
                    pasos.append((x, y - 1))
                siguiente = self.model.grid.get_cell_list_contents((x, y + 1))
                if caminos[3] and not isinstance(siguiente[0], Edificio) and (y+1) < 31:
                    pasos.append((x, y + 1))

            elif len(calle) >= 3:
                if isinstance(calle[1], Banqueta) and isinstance(calle[0], (Estacionamiento, Hospital)):
                    caminos = calle[1].posiblesVecinos()
                    siguiente = self.model.grid.get_cell_list_contents((x - 1, y))
                    if caminos[0] and not isinstance(siguiente[0], Edificio) and (x-1) >= 0:
                        pasos.append((x - 1, y))
                    if (x + 1) < 30:
                        siguiente = self.model.grid.get_cell_list_contents((x + 1, y))
                        if caminos[1] and not isinstance(siguiente[0], Edificio):
                            pasos.append((x + 1, y))
                    siguiente = self.model.grid.get_cell_list_contents((x, y - 1))
                    if caminos[2] and not isinstance(siguiente[0], Edificio) and (y-1) >= 0:
                        pasos.append((x, y - 1))
                    siguiente = self.model.grid.get_cell_list_contents((x, y + 1))
                    if caminos[3] and not isinstance(siguiente[0], Edificio) and (y+1) < 31:
                        pasos.append((x, y + 1))
                elif isinstance(calle[1], Semaforo):
                    caminos = calle[1].posiblesVecinos()
                    siguiente = self.model.grid.get_cell_list_contents((x - 1, y))
                    if caminos[0] and not isinstance(siguiente[0], Edificio) and (x - 1) >= 0:
                        pasos.append((x - 1, y))
                    if (x + 1) < 30:
                        siguiente = self.model.grid.get_cell_list_contents((x + 1, y))
                        if caminos[1] and not isinstance(siguiente[0], Edificio):
                            pasos.append((x + 1, y))
                    siguiente = self.model.grid.get_cell_list_contents((x, y - 1))
                    if caminos[2] and not isinstance(siguiente[0], Edificio) and (y - 1) >= 0:
                        pasos.append((x, y - 1))
                    siguiente = self.model.grid.get_cell_list_contents((x, y + 1))
                    if caminos[3] and not isinstance(siguiente[0], Edificio) and (y + 1) < 31:
                        pasos.append((x, y + 1))
                elif isinstance(calle[0], Banqueta):
                    caminos = calle[0].posiblesVecinos()
                    siguiente = self.model.grid.get_cell_list_contents((x - 1, y))
                    if caminos[0] and not isinstance(siguiente[0], Edificio) and (x-1) >= 0:
                        pasos.append((x - 1, y))
                    if (x + 1) < 30:
                        siguiente = self.model.grid.get_cell_list_contents((x + 1, y))
                        if caminos[1] and not isinstance(siguiente[0], Edificio):
                            pasos.append((x + 1, y))
                    siguiente = self.model.grid.get_cell_list_contents((x, y - 1))
                    if caminos[2] and not isinstance(siguiente[0], Edificio) and (y-1) >= 0:
                        pasos.append((x, y - 1))
                    siguiente = self.model.grid.get_cell_list_contents((x, y + 1))
                    if caminos[3] and not isinstance(siguiente[0], Edificio) and (y+1) < 31:
                        pasos.append((x, y + 1))

        if pasos:
            movimiento = random.choice(pasos)
            self.prev_pos = self.pos
            self.model.grid.move_agent(self, movimiento)


class Coche(mesa.Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        self.prev_pos = None
        self.origen = None
        self.destino = None
        self.terminado = False
        self.chocado = False
        self.encamino = False
        self.ruta = []
        self.ruta_completa = []
        self.pasos_finales = 0
        super().__init__(unique_id, model)

    def __str__(self):
        return "Coche"

    def generar_ruta(self):
        # Crear un grafo dirigido para representar la red vial
        grafo = nx.DiGraph()
        # Obtener la posición actual del coche y su destino
        origen = self.origen
        destino = self.destino
        # Agregar nodos y aristas al grafo según la red vial
        for x in range(self.model.grid.width):
            for y in range(self.model.grid.height):
                pos = (x, y)
                calle = self.model.grid.get_cell_list_contents(pos)

                if isinstance(calle[0], (CalleEste, CalleNorte, CalleOeste, CalleSur, Estacionamiento, Banqueta)):
                    caminos = calle[0].posiblesVecinos()
                    if caminos[0]:
                        calleSig = self.model.grid.get_cell_list_contents((x - 1, y))
                        coche_chocado = False
                        if len(calleSig) >= 2:
                            if isinstance(calleSig[1], Coche):
                                if calleSig[1].chocado:
                                    coche_chocado = True
                        if not coche_chocado:
                            grafo.add_edge(pos, (x - 1, y), weight=1)
                    if caminos[1]:
                        calleSig = self.model.grid.get_cell_list_contents((x + 1, y))
                        coche_chocado = False
                        if len(calleSig) >= 2:
                            if isinstance(calleSig[1], Coche):
                                if calleSig[1].chocado:
                                    coche_chocado = True
                        if not coche_chocado:
                            grafo.add_edge(pos, (x + 1, y), weight=1)
                    if caminos[2]:
                        calleSig = self.model.grid.get_cell_list_contents((x, y - 1))
                        coche_chocado = False
                        if len(calleSig) >= 2:
                            if isinstance(calleSig[1], Coche):
                                if calleSig[1].chocado:
                                    coche_chocado = True
                        if not coche_chocado:
                            grafo.add_edge(pos, (x, y - 1), weight=1)
                    if caminos[3]:
                        calleSig = self.model.grid.get_cell_list_contents((x, y + 1))
                        coche_chocado = False
                        if len(calleSig) >= 2:
                            if isinstance(calleSig[1], Coche):
                                if calleSig[1].chocado:
                                    coche_chocado = True
                        if not coche_chocado:
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

        # Calcular la ruta más corta utilizando el algoritmo de Dijkstra
        try:
            ruta_corta = nx.shortest_path(grafo, source=origen, target=destino, weight='weight')
        except nx.NetworkXNoPath:
            ruta_corta = []

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

        elif not self.chocado and self.ruta:
            if len(calle) == 3:
                if isinstance(calle[2], Coche) and not isinstance(calle[1], Semaforo):
                    self.chocado = True
                elif len(calle) == 4:
                    if isinstance(calle[3], Coche):
                        self.chocado = True
            # ===================== CHECK DE SEMAFORO ==========================
            choice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                      0, 1, 2, 3, 3, 5, 6, 7, 8, 9,
                      0, 1, 2, 3, 3, 5, 6, 7, 8, 9,
                      0, 1, 2, 3, 3, 5, 6, 7, 8, 9,
                      0, 1, 2, 3, 3, 5, 6, 7, 8, 9,
                      0, 1, 2, 3, 3, 5, 6, 7, 8, 9,
                      0, 1, 2, 3, 3, 5, 6, 7, 8, 9,
                      0, 1, 2, 3, 3, 5, 6, 7, 8, 9,
                      0, 1, 2, 3, 3, 5, 6, 7, 8, 9,
                      0, 1, 2, 3, 3, 5, 6, 7, 8, 9]
            if self.ruta and not self.chocado:
                calleSig = self.model.grid.get_cell_list_contents((self.ruta[0]))
                coche_chocado = False
                if len(calleSig) >= 2:
                    if isinstance(calleSig[1], Coche):
                        if calleSig[1].chocado:
                            coche_chocado = True
                if len(calleSig) == 1:
                    if self.ruta[0] == self.destino and not self.terminado:
                        self.terminado = True
                        self.prev_pos = self.pos
                        self.model.grid.move_agent(self, self.ruta[0])
                        self.ruta.remove(self.ruta[0])
                    elif not self.terminado:
                        self.prev_pos = self.pos
                        self.model.grid.move_agent(self, self.ruta[0])
                        self.ruta.remove(self.ruta[0])

                elif len(calleSig) == 2:
                    if isinstance(calleSig[1], Ambulancia):
                        pass
                    elif ((isinstance(calleSig[1], (Coche, Ambulancia, Peaton)) or calleSig[1].__str__() == "Semaforo Rojo") and len(
                            self.ruta) != 2) and random.choice(choice) != 4 and not coche_chocado:
                        pass
                    elif random.choice(choice) == 4 and isinstance(calleSig[1], Coche) and not coche_chocado:
                        self.prev_pos = self.pos
                        self.model.grid.move_agent(self, self.ruta[0])
                        self.ruta.remove(self.ruta[0])
                    else:
                        if self.ruta[0] == self.destino and not self.terminado:
                            self.pasos_finales = self.model.current_step
                            self.terminado = True
                            self.prev_pos = self.pos
                            self.model.grid.move_agent(self, self.ruta[0])
                            self.ruta.remove(self.ruta[0])
                        elif coche_chocado:
                            self.origen = self.pos
                            self.ruta = self.generar_ruta()
                            if self.ruta:
                                self.model.grid.move_agent(self, self.ruta[0])
                                self.ruta.remove(self.ruta[0])

                        elif not self.terminado:
                            self.prev_pos = self.pos
                            self.model.grid.move_agent(self, self.ruta[0])
                            self.ruta.remove(self.ruta[0])
                elif len(calleSig) >= 3:
                    if isinstance(calleSig[2], Coche) and not coche_chocado:
                        pass
                    elif coche_chocado:
                        self.origen = self.pos
                        self.ruta = self.generar_ruta()
                        if self.ruta:
                            self.model.grid.move_agent(self, self.ruta[0])
                            self.ruta.remove(self.ruta[0])
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
        elif not self.ruta:
            self.origen = self.pos
            self.ruta = self.generar_ruta()


class Ambulancia(mesa.Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        self.prev_pos = None
        self.origen = None
        self.destino = None
        self.terminado = False
        self.emergencia = False
        self.pasos = 0
        self.ruta = []
        self.ruta_completa = []
        self.pasos_finales = 0
        super().__init__(unique_id, model)

    def __str__(self):
        return "Ambulancia"

    def generar_ruta(self):
        # Crear un grafo dirigido para representar la red vial
        grafo = nx.DiGraph()
        # Agregar nodos y aristas al grafo según la red vial
        for x in range(self.model.grid.width):
            for y in range(self.model.grid.height):
                pos = (x, y)
                calle = self.model.grid.get_cell_list_contents(pos)

                if isinstance(calle[0], (CalleEste, CalleNorte, CalleOeste, CalleSur, Estacionamiento, Hospital, Banqueta)):
                    caminos = calle[0].posiblesVecinos()
                    if caminos[0]:
                        calleSig = self.model.grid.get_cell_list_contents((x - 1, y))
                        coche_chocado = False
                        if len(calleSig) >= 2 and self.destino != (x - 1, y):
                            if isinstance(calleSig[1], Coche):
                                if calleSig[1].chocado:
                                    coche_chocado = True
                        if not coche_chocado:
                            grafo.add_edge(pos, (x - 1, y), weight=1)
                    if caminos[1]:
                        calleSig = self.model.grid.get_cell_list_contents((x + 1, y))
                        coche_chocado = False
                        if len(calleSig) >= 2 and self.destino != (x + 1, y):
                            if isinstance(calleSig[1], Coche):
                                if calleSig[1].chocado:
                                    coche_chocado = True
                        if not coche_chocado:
                            grafo.add_edge(pos, (x + 1, y), weight=1)
                    if caminos[2]:
                        calleSig = self.model.grid.get_cell_list_contents((x, y - 1))
                        coche_chocado = False
                        if len(calleSig) >= 2 and self.destino != (x, y - 1):
                            if isinstance(calleSig[1], Coche):
                                if calleSig[1].chocado:
                                    coche_chocado = True
                        if not coche_chocado:
                            grafo.add_edge(pos, (x, y - 1), weight=1)
                    if caminos[3]:
                        calleSig = self.model.grid.get_cell_list_contents((x, y + 1))
                        coche_chocado = False
                        if len(calleSig) >= 2 and self.destino != (x, y + 1):
                            if isinstance(calleSig[1], Coche):
                                if calleSig[1].chocado:
                                    coche_chocado = True
                        if not coche_chocado:
                            grafo.add_edge(pos, (x, y + 1), weight=1)
                elif len(calle) >= 2:

                    if isinstance(calle[1], Hospital):
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
        try:
            ruta_corta = nx.shortest_path(grafo, source=origen, target=destino, weight='weight')
        except nx.NetworkXNoPath:
            ruta_corta = []

        # Retornar el array de coordenadas de la ruta
        return ruta_corta

    def step(self):
        calle = self.model.grid.get_cell_list_contents(self.pos)
        if self.pasos == 0:
            self.ruta = self.generar_ruta()
            if self.ruta:
                self.model.grid.move_agent(self, self.ruta[0])
                self.ruta.remove(self.ruta[0])
                self.ruta_completa = self.ruta
                self.model.grid.move_agent(self, self.ruta[0])
                self.ruta.remove(self.ruta[0])

        elif self.ruta:
            # ===================== CHECK DE SEMAFORO ==========================
            choice = [0, 1, 2, 3, 3, 5, 6, 7, 8, 9,
                      0, 1, 2, 3, 3, 5, 6, 7, 8, 9,
                      0, 1, 2, 3, 3, 5, 6, 7, 8, 9,
                      0, 1, 2, 3, 3, 5, 6, 7, 8, 9,
                      0, 1, 2, 3, 3, 5, 6, 7, 8, 9,
                      0, 1, 2, 3, 3, 5, 6, 7, 8, 9,
                      0, 1, 2, 3, 3, 5, 6, 7, 8, 9,
                      0, 1, 2, 3, 3, 5, 6, 7, 8, 9,
                      0, 1, 2, 3, 3, 5, 6, 7, 8, 9,
                      0, 1, 2, 3, 3, 5, 6, 7, 8, 9]
            if self.ruta:
                calleSig = self.model.grid.get_cell_list_contents((self.ruta[0]))
                coche_chocado = False
                if len(calleSig) >= 2:
                    if isinstance(calleSig[1], Coche):
                        if calleSig[1].chocado:
                            coche_chocado = True
                if len(calleSig) == 1:
                    if self.ruta[0] == self.destino and not self.terminado:
                        self.terminado = True
                        self.prev_pos = self.pos
                        self.model.grid.move_agent(self, self.ruta[0])
                        self.ruta.remove(self.ruta[0])
                        self.origen = self.pos
                        self.destino = (2, 4)
                        self.ruta = self.generar_ruta()
                    elif not self.terminado:
                        self.prev_pos = self.pos
                        self.model.grid.move_agent(self, self.ruta[0])
                        self.ruta.remove(self.ruta[0])

                elif len(calleSig) == 2:
                    if (((isinstance(calleSig[1],  Peaton) or calleSig[1].__str__() == "Semaforo Rojo") and len(
                            self.ruta) != 2) and random.choice(choice) != 4 and not coche_chocado) and calleSig[1].pos != self.destino:
                        pass
                    else:
                        if self.ruta[0] == self.destino and not self.terminado:
                            self.pasos_finales = self.model.current_step
                            self.terminado = True
                            self.prev_pos = self.pos
                            self.model.grid.move_agent(self, self.ruta[0])
                            self.ruta.remove(self.ruta[0])
                            self.origen = self.pos
                            self.destino = (2, 4)
                            self.ruta = self.generar_ruta()
                        elif coche_chocado:
                            self.origen = self.pos
                            self.ruta = self.generar_ruta()
                            self.model.grid.move_agent(self, self.ruta[0])
                            self.ruta.remove(self.ruta[0])
                        elif not self.terminado:
                            self.prev_pos = self.pos
                            self.model.grid.move_agent(self, self.ruta[0])
                            self.ruta.remove(self.ruta[0])
                elif len(calleSig) >= 3:
                    if self.ruta[0] == self.destino:
                        self.terminado = True
                        self.prev_pos = self.pos
                        self.model.grid.move_agent(self, self.ruta[0])
                        self.ruta.remove(self.ruta[0])
                        self.origen = self.pos
                        self.destino = (2, 4)
                        self.ruta = self.generar_ruta()
                    elif coche_chocado:
                        self.origen = self.pos
                        self.ruta = self.generar_ruta()
                        if self.ruta:
                            self.model.grid.move_agent(self, self.ruta[0])
                            self.ruta.remove(self.ruta[0])
                    else:
                        if self.ruta[0] == self.destino and not self.terminado:
                            self.terminado = True
                            self.prev_pos = self.pos
                            self.model.grid.move_agent(self, self.ruta[0])
                            self.ruta.remove(self.ruta[0])
                            self.origen = self.pos
                            self.destino = (2, 4)
                            self.ruta = self.generar_ruta()
                        elif not self.terminado:
                            self.prev_pos = self.pos
                            self.model.grid.move_agent(self, self.ruta[0])
                            self.ruta.remove(self.ruta[0])

                elif self.ruta[0] == self.destino and not self.terminado:
                    self.terminado = True
                    self.prev_pos = self.pos
                    self.model.grid.move_agent(self, self.ruta[0])
                    self.ruta.remove(self.ruta[0])
                    self.origen = self.pos
                    self.destino = (2, 4)
                    self.ruta = self.generar_ruta()
                elif not self.terminado:
                    self.prev_pos = self.pos
                    self.model.grid.move_agent(self, self.ruta[0])
                    self.ruta.remove(self.ruta[0])
        elif not self.ruta:
            self.origen = self.pos
            self.ruta = self.generar_ruta()
        self.pasos += 1


class Ciudad(mesa.Model):
    def __init__(self, num_agents, num_peatones, width, height):
        super().__init__()
        self.num_agents = num_agents
        self.num_peatones = num_peatones
        self.promedios = None
        self.promediosReales = None
        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.MultiGrid(width=width, height=height, torus=False)
        self.current_step = 0
        self.lista_coches = []
        self.lista_peatones = []
        self.coches_chocados = []
        self.reportados = []
        self.lista_ambulancias = []
        self.n_ambulancias = 0
        self.terminados = 0
        print(self.num_agents)

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
        hospital = Hospital(13, self)
        self.schedule.add(hospital)

        banqueta = Banqueta(21, self)
        self.schedule.add(banqueta)

        edificio = Edificio(22, self)
        self.schedule.add(edificio)

        # ============================Orilla Oeste ========================
        for i in range(31):
            calle_sur = CalleSur(i + 23, self)
            self.schedule.add(calle_sur)
            self.grid.place_agent(calle_sur, (0, i + 1))

        for i in range(29):
            calle_sur = CalleSur(i + 54, self)
            self.schedule.add(calle_sur)
            self.grid.place_agent(calle_sur, (1, i + 2))

        # ============================Orilla Sur ========================
        for i in range(30):
            calle_este = CalleEste(85 + i, self)
            self.schedule.add(calle_este)
            self.grid.place_agent(calle_este, (i, 0))

        for i in range(28):
            calle_este = CalleEste(116 + i, self)
            self.schedule.add(calle_este)
            self.grid.place_agent(calle_este, (i + 1, 1))

        # ============================Orilla Este ========================
        for i in range(20):
            calle_norte = CalleNorte(146 + i, self)
            self.schedule.add(calle_norte)
            self.grid.place_agent(calle_norte, (30, i))

        for i in range(6):
            calle_norte = CalleNorte(166 + i, self)
            self.schedule.add(calle_norte)
            self.grid.place_agent(calle_norte, (29, i + 24))

        for i in range(6):
            calle_norte = CalleNorte(173 + i, self)
            self.schedule.add(calle_norte)
            self.grid.place_agent(calle_norte, (30, i + 24))

        for i in range(19):
            calle_norte = CalleNorte(180 + i, self)
            self.schedule.add(calle_norte)
            self.grid.place_agent(calle_norte, (29, i + 1))

        # ============================Orilla Norte ========================
        for i in range(30):
            calle_oeste = CalleOeste(206 + i, self)
            self.schedule.add(calle_oeste)
            self.grid.place_agent(calle_oeste, (i + 1, 31))

        for i in range(29):
            calle_oeste = CalleOeste(236 + i, self)
            self.schedule.add(calle_oeste)
            self.grid.place_agent(calle_oeste, (i + 2, 30))

        # ============================ Edificios ========================

        for i in range(2):
            for j in range(7):
                self.grid.place_agent(edificio, (j + 3, i + 27))

        for i in range(2):
            for j in range(7):
                self.grid.place_agent(edificio, (j + 11, i + 27))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 22, i + 27))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 3, i + 21))

        for i in range(3):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 12, i + 20))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 22, i + 21))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 3, i + 15))

        for i in range(4):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 12, i + 15))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 22, i + 15))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 3, i + 9))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 12, i + 9))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 22, i + 9))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 3, i + 3))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 12, i + 3))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 22, i + 3))

        # =======================Estacionamientos=======================

        self.grid.place_agent(estacionamiento1, (6, 20))
        self.grid.place_agent(estacionamiento2, (5, 26))
        self.grid.place_agent(estacionamiento3, (26, 17))
        self.grid.place_agent(estacionamiento4, (23, 14))
        self.grid.place_agent(estacionamiento5, (24, 11))
        self.grid.place_agent(estacionamiento6, (25, 23))
        self.grid.place_agent(estacionamiento7, (24, 26))
        self.grid.place_agent(estacionamiento8, (22, 29))
        self.grid.place_agent(estacionamiento9, (26, 29))
        self.grid.place_agent(estacionamiento10, (18, 27))
        self.grid.place_agent(estacionamiento11, (9, 29))
        self.grid.place_agent(estacionamiento12, (15, 29))
        self.grid.place_agent(hospital, (2, 4))

        # ============================Banquetas ========================
        it = 0
        for i in range(4):
            for j in range(17):
                banqueta = Banqueta(1000 + it, self)
                self.schedule.add(banqueta)
                self.grid.place_agent(banqueta, (j + 2, i + 26))
                it += 1

        it = 0
        for i in range(4):
            for j in range(8):
                banqueta = Banqueta(1069 + it, self)
                self.schedule.add(banqueta)
                self.grid.place_agent(banqueta, (j + 2, i + 20))
                it += 1
        it = 0
        for i in range(4):
            for j in range(8):
                banqueta = Banqueta(1102 + it, self)
                self.schedule.add(banqueta)
                self.grid.place_agent(banqueta, (j + 2, i + 14))
                it += 1

        it = 0
        for i in range(4):
            for j in range(8):
                banqueta = Banqueta(1134 + it, self)
                self.schedule.add(banqueta)
                self.grid.place_agent(banqueta, (j + 2, i + 8))
                it += 1

        it = 0
        for i in range(4):
            for j in range(8):
                banqueta = Banqueta(1167 + it, self)
                self.schedule.add(banqueta)
                self.grid.place_agent(banqueta, (j + 11, i + 8))
                it += 1

        it = 0
        for i in range(4):
            for j in range(8):
                banqueta = Banqueta(1199 + it, self)
                self.schedule.add(banqueta)
                self.grid.place_agent(banqueta, (j + 21, i + 8))
                it += 1

        it = 0
        for i in range(4):
            for j in range(8):
                banqueta = Banqueta(1231 + it, self)
                self.schedule.add(banqueta)
                self.grid.place_agent(banqueta, (j + 2, i + 2))
                it += 1

        it = 0
        for i in range(4):
            for j in range(8):
                banqueta = Banqueta(1263 + it, self)
                self.schedule.add(banqueta)
                self.grid.place_agent(banqueta, (j + 11, i + 2))
                it += 1

        it = 0
        for i in range(4):
            for j in range(8):
                banqueta = Banqueta(1295 + it, self)
                self.schedule.add(banqueta)
                self.grid.place_agent(banqueta, (j + 21, i + 2))
                it += 1

        it = 0
        for i in range(4):
            for j in range(8):
                banqueta = Banqueta(1327 + it, self)
                self.schedule.add(banqueta)
                self.grid.place_agent(banqueta, (j + 21, i + 14))
                it += 1

        it = 0
        for i in range(4):
            for j in range(10):
                banqueta = Banqueta(1367 + it, self)
                self.schedule.add(banqueta)
                self.grid.place_agent(banqueta, (j + 21, i + 20))
                it += 1

        it = 0
        for i in range(4):
            for j in range(8):
                banqueta = Banqueta(1410 + it, self)
                self.schedule.add(banqueta)
                self.grid.place_agent(banqueta, (j + 21, i + 26))
                it += 1

        it = 0
        for i in range(10):
            for j in range(8):
                banqueta = Banqueta(1495 + it, self)
                self.schedule.add(banqueta)
                self.grid.place_agent(banqueta, (j + 11, i + 14))
                it += 1

        # ===================== Calles interiores =============================
        it = 0
        for i in range(2):
            for j in range(17):
                calle_este = CalleEste(265 + it, self)
                self.schedule.add(calle_este)
                self.grid.place_agent(calle_este, (j + 2, i + 24))
                it += 1
        it = 0
        for i in range(2):
            for j in range(8):
                calle_este = CalleEste(299 + it, self)
                self.schedule.add(calle_este)
                self.grid.place_agent(calle_este, (j + 21, i + 24))
                it += 1

        it = 0
        for i in range(2):
            for j in range(17):
                calle_este = CalleEste(320 + it, self)
                self.schedule.add(calle_este)
                self.grid.place_agent(calle_este, (j + 2, i + 12))
                it += 1

        it = 0
        for i in range(2):
            for j in range(8):
                calle_este = CalleEste(355 + it, self)
                self.schedule.add(calle_este)
                self.grid.place_agent(calle_este, (j + 21, i + 12))
                it += 1

        it = 0
        for i in range(2):
            for j in range(17):
                calle_oeste = CalleOeste(376 + it, self)
                self.schedule.add(calle_oeste)
                self.grid.place_agent(calle_oeste, (j + 2, i + 6))
                it += 1

        it = 0
        for i in range(2):
            for j in range(8):
                calle_oeste = CalleOeste(410 + it, self)
                self.schedule.add(calle_oeste)
                self.grid.place_agent(calle_oeste, (j + 21, i + 6))
                it += 1

        it = 0
        for i in range(2):
            for j in range(8):
                calle_oeste = CalleOeste(431 + it, self)
                self.schedule.add(calle_oeste)
                self.grid.place_agent(calle_oeste, (j + 2, i + 18))
                it += 1

        it = 0
        for i in range(4):
            calle_norte = CalleNorte(449 + it, self)
            self.schedule.add(calle_norte)
            self.grid.place_agent(calle_norte, (10, i + 2))
            it += 1

        it = 0
        for i in range(4):
            calle_norte = CalleNorte(454 + it, self)
            self.schedule.add(calle_norte)
            self.grid.place_agent(calle_norte, (10, i + 8))
            it += 1

        it = 0
        for i in range(10):
            calle_norte = CalleNorte(458 + it, self)
            self.schedule.add(calle_norte)
            self.grid.place_agent(calle_norte, (10, i + 14))
            it += 1

        it = 0
        for i in range(28):
            for j in range(2):
                calle_sur = CalleSur(473 + it, self)
                self.schedule.add(calle_sur)
                self.grid.place_agent(calle_sur, (j + 19, i + 2))
                it += 1

        it = 0
        for i in range(2):
            for j in range(8):
                calle_oeste = CalleOeste(529 + it, self)
                self.schedule.add(calle_oeste)
                self.grid.place_agent(calle_oeste, (j + 21, i + 18))
                it += 1

        '''
        =========================== SEMAFOROS =================================
        '''

        # ================ SEMÁFOROS ORILLA NORTE ===================
        semaforo1 = Semaforo(600, self)
        self.schedule.add(semaforo1)
        self.grid.place_agent(semaforo1, (2, 31))
        self.grid.place_agent(semaforo1, (2, 30))

        semaforo2 = Semaforo(601, self)
        self.schedule.add(semaforo2)
        self.grid.place_agent(semaforo2, (11, 31))
        self.grid.place_agent(semaforo2, (11, 30))

        semaforo2 = Semaforo(602, self)
        self.schedule.add(semaforo2)
        self.grid.place_agent(semaforo2, (21, 31))
        self.grid.place_agent(semaforo2, (21, 30))

        # ================ SEMÁFOROS ORILLA OESTE ===================
        semaforo2 = Semaforo(605, self)
        self.schedule.add(semaforo2)
        self.grid.place_agent(semaforo2, (0, 2))
        self.grid.place_agent(semaforo2, (1, 2))

        semaforo1 = Semaforo(631, self)
        self.schedule.add(semaforo1)
        self.grid.place_agent(semaforo1, (0, 8))
        self.grid.place_agent(semaforo1, (1, 8))
        # !!!!!!!!!!!!!!!!!!! Opuestos !!!!!!!!!!!!!!!!!!!!!!!
        semaforo2 = Semaforo(606, self)
        self.schedule.add(semaforo2)
        self.grid.place_agent(semaforo2, (2, 6))
        self.grid.place_agent(semaforo2, (2, 7))

        semaforo2 = Semaforo(607, self)
        self.schedule.add(semaforo2)
        self.grid.place_agent(semaforo2, (0, 14))
        self.grid.place_agent(semaforo2, (1, 14))

        semaforo1 = Semaforo(608, self)
        self.schedule.add(semaforo1)
        self.grid.place_agent(semaforo1, (0, 20))
        self.grid.place_agent(semaforo1, (1, 20))

        semaforo2 = Semaforo(609, self)
        self.schedule.add(semaforo2)
        self.grid.place_agent(semaforo2, (0, 26))
        self.grid.place_agent(semaforo2, (1, 26))

        # ================ SEMÁFOROS ORILLA SUR ===================
        semaforo2 = Semaforo(610, self)
        self.schedule.add(semaforo2)
        self.grid.place_agent(semaforo2, (9, 0))
        self.grid.place_agent(semaforo2, (9, 1))

        semaforo2 = Semaforo(611, self)
        self.schedule.add(semaforo2)
        self.grid.place_agent(semaforo2, (18, 0))
        self.grid.place_agent(semaforo2, (18, 1))
        # !!!!!!!!!!!!! Opuestos !!!!!!!!!!!!!!!!!!!!
        semaforo2 = Semaforo(612, self)
        self.schedule.add(semaforo2)
        self.grid.place_agent(semaforo2, (19, 2))
        self.grid.place_agent(semaforo2, (20, 2))

        semaforo1 = Semaforo(613, self)
        self.schedule.add(semaforo1)
        self.grid.place_agent(semaforo1, (28, 0))
        self.grid.place_agent(semaforo1, (28, 1))

        # ================ SEMÁFOROS ORILLA ESTE ===================
        semaforo1 = Semaforo(614, self)
        self.schedule.add(semaforo1)
        self.grid.place_agent(semaforo1, (30, 11))
        self.grid.place_agent(semaforo1, (29, 11))
        # !!!!!!!!!!!!! Opuestos !!!!!!!!!!!!!!!!!!!!
        semaforo2 = Semaforo(615, self)
        self.schedule.add(semaforo2)
        self.grid.place_agent(semaforo2, (28, 12))
        self.grid.place_agent(semaforo2, (28, 13))

        # ================= INTERIOR OESTE =========================
        semaforo2 = Semaforo(616, self)
        self.schedule.add(semaforo2)
        self.grid.place_agent(semaforo2, (21, 6))
        self.grid.place_agent(semaforo2, (21, 7))
        # !!!!!!!!!!!!! Opuestos !!!!!!!!!!!!!!!!!!!!
        semaforo1 = Semaforo(617, self)
        self.schedule.add(semaforo1)
        self.grid.place_agent(semaforo1, (19, 8))
        self.grid.place_agent(semaforo1, (20, 8))

        semaforo2 = Semaforo(618, self)
        self.schedule.add(semaforo2)
        self.grid.place_agent(semaforo2, (11, 6))
        self.grid.place_agent(semaforo2, (11, 7))
        # !!!!!!!!!!!!! Opuestos !!!!!!!!!!!!!!!!!!!!
        semaforo1 = Semaforo(619, self)
        self.schedule.add(semaforo1)
        self.grid.place_agent(semaforo1, (10, 5))

        # =============== INTERIOR ESTE ABAJO ======================

        semaforo1 = Semaforo(620, self)
        self.schedule.add(semaforo1)
        self.grid.place_agent(semaforo1, (18, 12))
        self.grid.place_agent(semaforo1, (18, 13))
        # !!!!!!!!!!!!! Opuestos !!!!!!!!!!!!!!!!!!!!
        semaforo2 = Semaforo(621, self)
        self.schedule.add(semaforo2)
        self.grid.place_agent(semaforo2, (19, 14))
        self.grid.place_agent(semaforo2, (20, 14))

        semaforo1 = Semaforo(622, self)
        self.schedule.add(semaforo1)
        self.grid.place_agent(semaforo1, (9, 12))
        self.grid.place_agent(semaforo1, (9, 13))
        # !!!!!!!!!!!!! Opuestos !!!!!!!!!!!!!!!!!!!!
        semaforo2 = Semaforo(623, self)
        self.schedule.add(semaforo2)
        self.grid.place_agent(semaforo2, (10, 11))

        # =============== INTERIOR OESTE MEDIA =====================
        semaforo2 = Semaforo(624, self)
        self.schedule.add(semaforo2)
        self.grid.place_agent(semaforo2, (21, 18))
        self.grid.place_agent(semaforo2, (21, 19))
        # !!!!!!!!!!!!! Opuestos !!!!!!!!!!!!!!!!!!!!
        semaforo1 = Semaforo(625, self)
        self.schedule.add(semaforo1)
        self.grid.place_agent(semaforo1, (19, 20))
        self.grid.place_agent(semaforo1, (20, 20))

        # =============== INTERIOR ESTE ARRIBA ======================
        semaforo2 = Semaforo(626, self)
        self.schedule.add(semaforo2)
        self.grid.place_agent(semaforo2, (9, 24))
        self.grid.place_agent(semaforo2, (9, 25))
        # !!!!!!!!!!!!! Opuestos !!!!!!!!!!!!!!!!!!!!
        semaforo1 = Semaforo(627, self)
        self.schedule.add(semaforo1)
        self.grid.place_agent(semaforo1, (10, 23))

        semaforo2 = Semaforo(628, self)
        self.schedule.add(semaforo2)
        self.grid.place_agent(semaforo2, (18, 24))
        self.grid.place_agent(semaforo2, (18, 25))
        # !!!!!!!!!!!!! Opuestos !!!!!!!!!!!!!!!!!!!!
        semaforo1 = Semaforo(629, self)
        self.schedule.add(semaforo1)
        self.grid.place_agent(semaforo1, (19, 26))
        self.grid.place_agent(semaforo1, (20, 26))

        semaforo2 = Semaforo(630, self)
        self.schedule.add(semaforo2)
        self.grid.place_agent(semaforo2, (28, 24))
        self.grid.place_agent(semaforo2, (28, 25))

        # ================ VEHICULOS ===================
        comienzo = self.calle_position()
        destinos = self.estacionamiento_position()
        for i in range(num_agents):
            x, y = random.choice(comienzo)
            comienzo.remove((x, y))
            coche = Coche(i + 700, self)
            coche.origen = (x, y)
            self.schedule.add(coche)
            self.grid.place_agent(coche, (x, y))
            v, w = random.choice(destinos)
            coche.destino = (v, w)
            self.lista_coches.append(coche)

        banquetas = self.banqueta_position()
        for i in range(num_peatones):
            x, y = random.choice(banquetas)
            peaton = Peaton(i + 1600, self)
            peaton.origen = (x, y)
            self.schedule.add(peaton)
            self.grid.place_agent(peaton, (x, y))
            self.lista_peatones.append(peaton)

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
                if cell_list[0].__str__() == "Estacionamiento":
                    estacionamiento_cells.append((x, y))

        if estacionamiento_cells:
            return estacionamiento_cells
        else:
            return None

    def calle_position(self):
        calle_cells = []

        for x in range(self.grid.width):
            for y in range(self.grid.height):
                cell_list = self.grid.get_cell_list_contents([(x, y)])
                if isinstance(cell_list[0], (CalleEste, CalleNorte, CalleOeste, CalleSur)):
                    calle_cells.append((x, y))

        if calle_cells:
            return calle_cells
        else:
            return None

    def banqueta_position(self):
        banqueta_cells = []

        for x in range(self.grid.width):
            for y in range(self.grid.height):
                cell_list = self.grid.get_cell_list_contents([(x, y)])
                if cell_list[0].__str__() == "Banqueta":
                    banqueta_cells.append((x, y))

        if banqueta_cells:
            return banqueta_cells
        else:
            return None

    def get_pos_coches(self):
        coches = []
        for coche in self.lista_coches:
            coches.append(coche.pos)
        return coches

    def get_pos_Peaton(self):
        peaton = []
        for persona in self.lista_peatones:
            peaton.append(persona.pos)
        return peaton

    def estado_semaforo(self):
        estados = []
        for x in range(self.grid.width):
            for y in range(self.grid.height):
                cell_list = self.grid.get_cell_list_contents([(x, y)])
                if len(cell_list) >= 2:
                    if isinstance(cell_list[1], Semaforo):
                        if cell_list[1].__str__() == "Semaforo Rojo":
                            estados.append((0, cell_list[1].unique_id))
                        elif cell_list[1].__str__() == "Semaforo Amarillo":
                            estados.append((1, cell_list[1].unique_id))
                        elif cell_list[1].__str__() == "Semaforo Verde":
                            estados.append((2, cell_list[1].unique_id))
        estados = list(dict.fromkeys(estados))
        return estados

    def longitud_promedio(self):
        lista = []
        for coche in self.lista_coches:
            lista.append(len(coche.ruta_completa))
        promedio = (sum(lista) / len(lista))
        return promedio

    def pasos_finales(self):
        elementos = []
        for coche in self.lista_coches:
            elementos.append(coche.pasos_finales)
        promedio = (sum(elementos) / len(elementos))
        return promedio

    def step(self):
        if self.current_step == 1:
            self.promedios = self.longitud_promedio()
        self.datacollector.collect(self)
        self.schedule.step()
        self.current_step += 1

        for coche in self.lista_coches:
            if coche.chocado and not coche.encamino:
                if coche.pos not in self.reportados:
                    ambulancia = Ambulancia(2000 + self.n_ambulancias, self)
                    self.schedule.add(ambulancia)
                    ambulancia.origen = (2, 4)
                    ambulancia.destino = coche.pos
                    self.lista_ambulancias.append(ambulancia)
                    self.grid.place_agent(ambulancia, (2, 4))
                    self.n_ambulancias += 1
                    coche.encamino = True
                    self.reportados.append(coche.pos)

            if coche.terminado:
                self.lista_coches.remove(coche)
                self.grid.remove_agent(coche)
                self.schedule.remove(coche)

        for ambulancia in self.lista_ambulancias:
            cells = self.grid.get_cell_list_contents(ambulancia.pos)
            if ambulancia.terminado:
                for cell in cells:
                    if isinstance(cell, Coche):
                        if cell.chocado:
                            self.lista_coches.remove(cell)
                            self.grid.remove_agent(cell)
                            self.schedule.remove(cell)
                            print("borrado")
            ambulancia.terminado = False

        if not self.lista_coches or self.current_step >= 300:
            self.running = False
