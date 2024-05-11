from multiprocessing import Process, Queue
from time import sleep, time

from .automatic_control import run_auto_car
from .generate_traffic import generate_traffic
from config import CarlaConf


def run():
    """
    Run the carla environment
    return: collision times
    """
    # Create a Queue instance
    q_1 = Queue()
    # q_2 = Queue()
    stop_msg = Queue()

    p_traffic = Process(target=generate_traffic, args=(
        CarlaConf.IP,
        CarlaConf.Port,
        CarlaConf.PortTM,
        CarlaConf.Client_Timeout,
        CarlaConf.VehicleNum,
        CarlaConf.WalkerNum,
        CarlaConf.Map,
        stop_msg,  # Pass the Queue instance to the generate_traffic function
    ))

    p_traffic.start()

    sleep(2)  # Wait for the traffic to be generated (important when changing the map)

    p_auto_car = Process(target=run_auto_car, args=(
        CarlaConf.IP,
        CarlaConf.Port,
        CarlaConf.ActorType,
        CarlaConf.AgentBehavior,
        CarlaConf.AgentType,
        CarlaConf.Map,
        q_1,  # Pass the Queue instance to the run_auto_car function
    ))

    # p_auto_car_1 = Process(target=run_auto_car, args=(
    #     CarlaConf.IP,
    #     CarlaConf.Port,
    #     CarlaConf.ActorType,
    #     CarlaConf.AgentBehavior,
    #     CarlaConf.AgentType,
    #     CarlaConf.Map,
    #     q_2,  # Pass the Queue instance to the run_auto_car function
    # ))

    p_auto_car.start()
    # sleep(2)
    # p_auto_car_1.start()

    result = dict()
    flag_1 = False
    flag_2 = not False
    while True:
        if not q_1.empty():
            result['auto_car_1'] = q_1.get()
            flag_1 = True
        # if not q_2.empty():
        #     result['auto_car_2'] = q_2.get()
        #     flag_2 = True
        if flag_1 and flag_2:
            break

    stop_msg.put('stop')

    while p_traffic.is_alive():
        sleep(1)

    return result
