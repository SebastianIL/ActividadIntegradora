from .model import Ciudad, CalleSur, Coche, CalleEste, CalleNorte, CalleOeste, Semaforo, Edificio, Estacionamiento, Banqueta  # noqa

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
        portrayal["Color"] = "Grey"
        portrayal["w"] = 1
        portrayal["h"] = 1

    elif isinstance(agent, Edificio):
        portrayal["Layer"] = 1
        portrayal["Color"] = "Blue"
        portrayal["w"] = 1
        portrayal["h"] = 1

    elif isinstance(agent, Coche):
        portrayal["Layer"] = 2
        portrayal["Color"] = "Blue"
        portrayal["w"] = 0.5
        portrayal["h"] = 0.5

    elif isinstance(agent, Semaforo):
        if agent.state == "Red":
            portrayal["Color"] = "Red"
            portrayal["w"] = 1
            portrayal["h"] = 1
        elif agent.state == "Green":
            portrayal["Color"] = "Green"
            portrayal["w"] = 1
            portrayal["h"] = 1
        elif agent.state == "Yellow":
            portrayal["Color"] = "Yellow"
            portrayal["w"] = 1
            portrayal["h"] = 1

    elif isinstance(agent, Estacionamiento):
        portrayal["Layer"] = 1
        portrayal["Color"] = "LightGreen"
        portrayal["w"] = 1
        portrayal["h"] = 1

    elif isinstance(agent, Banqueta):
        portrayal["Color"] = "Black"
        portrayal["w"] = 1
        portrayal["h"] = 1

    # elif isinstance(agent, peaton):
    #     portrayal["Color"] = "Green"
    #     portrayal["Layer"] = 2
    #     portrayal["Shape"] = "circle"
    #     portrayal["r"] = 0.3

    return portrayal


canvas_element = mesa.visualization.CanvasGrid(
    vista_general, 31, 32, 690, 690
)

model_kwargs = {"num_agents": 12, "width": 31, "height": 32}

server = mesa.visualization.ModularServer(
    Ciudad,
    [canvas_element],
    "trafico",
    model_kwargs,
)