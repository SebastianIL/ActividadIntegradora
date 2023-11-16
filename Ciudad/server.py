"""
Configure visualization elements and instantiate a server
"""

from .model import Ciudad, Coche, CalleSur, CalleEste, CalleNorte, CalleOeste, Semaforo, Edificio, Rotonda, Estacionamiento  # noqa

import mesa


def vista_general(agent):
    if agent is None:
        return

    portrayal = {
        "Shape": "rect",
        "Filled": "true",
        "Layer": 0,
        "w": 0.5,
        "h": 0.5,
        "Color": "Blue",
    }

    if (isinstance(agent, CalleSur) or isinstance(agent, CalleEste) or isinstance(agent, CalleOeste)
            or isinstance(agent, CalleNorte)):
        portrayal["Color"] = "LightGrey"
        portrayal["w"] = 1
        portrayal["h"] = 1

    elif isinstance(agent, Semaforo):
        if agent.state == "Red":
            portrayal["Color"] = "Red"
            portrayal["w"] = 1
            portrayal["h"] = 1
        if agent.state == "Green":
            portrayal["Color"] = "Green"
            portrayal["w"] = 1
            portrayal["h"] = 1

    elif isinstance(agent, Edificio):
        portrayal["Color"] = "SkyBlue"
        portrayal["w"] = 1
        portrayal["h"] = 1

    elif isinstance(agent, Rotonda):
        portrayal["Color"] = "Brown"
        portrayal["w"] = 1
        portrayal["h"] = 1

    elif isinstance(agent, Estacionamiento):
        portrayal["Color"] = "Yellow"
        portrayal["w"] = 1
        portrayal["h"] = 1

    elif isinstance(agent, Estacionamiento):
        portrayal["Color"] = "Orange"
        portrayal["w"] = 0.3
        portrayal["h"] = 0.3

    elif isinstance(agent, Coche):
        portrayal["Color"] = "Blue"
        portrayal["Shape"] = "circle"
        portrayal["r"] = "0.5"
        portrayal["Layer"] = 2

    # elif isinstance(agent, peaton):
    #     portrayal["Color"] = "Green"
    #     portrayal["Layer"] = 2
    #     portrayal["Shape"] = "circle"
    #     portrayal["r"] = 0.3

    return portrayal


canvas_element = mesa.visualization.CanvasGrid(
    vista_general, 24, 24, 700, 700
)

model_kwargs = {"num_agents": 17, "width": 24, "height": 24}

server = mesa.visualization.ModularServer(
    Ciudad,
    [canvas_element],
    "trafico",
    model_kwargs,
)