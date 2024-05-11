import os

import torch


class GlobalConf:
    OS = os.name
    Project_Path = os.path.dirname(os.path.abspath(__file__))
    Device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


class CarlaConf:
    IP = '127.0.0.1'
    Port = 2000
    PortTM = 8000
    Client_Timeout = 20.0
    ActorType = ['vehicle.tesla.cybertruck', 'vehicle.vespa.zx125'][0]
    VehicleNum = 0
    WalkerNum = 59
    AgentBehavior = ['cautious', 'normal', 'aggressive'][0]
    AgentType = ["Behavior", "Basic", "Constant"][0]
    Map = ['Town01', 'Town02', 'Town03', 'Town04', 'Town05', 'Town06', 'Town07', 'Town10HD', 'Town10HD_Opt'][6]


class EvalConf:
    Timeout = 150
    Epochs = 50
