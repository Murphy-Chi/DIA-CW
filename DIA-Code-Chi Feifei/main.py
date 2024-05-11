from time import sleep

import carla

import carla_env
from config import CarlaConf, EvalConf
from tqdm import trange

from utils.benchmark import benchmark_reward


def main():
    agent_1_results = []
    # agent_2_results = []

    for i in trange(EvalConf.Epochs):
        result = carla_env.run()
        agent_1_results.append(result['auto_car_1'])
        # agent_2_results.append(result['auto_car_2'])

    print('Agent 1 collision results:', agent_1_results)
    # print('Agent 2 collision results:', agent_2_results)

    print('Agent 1 reward:', benchmark_reward(agent_1_results))
    # print('Agent 2 reward:', benchmark_reward(agent_2_results))
    with open('./results.txt', 'a+') as f:
        f.write(f'Map: {CarlaConf.Map}\n')
        f.write(f'Vehicle number: {CarlaConf.VehicleNum}\n')
        f.write(f'Collision results: {agent_1_results}\n')
        f.write(f'Agent 1: {benchmark_reward(agent_1_results)}\n\n')
        # f.write(f'Agent 2: {benchmark_reward(agent_2_results)}\n')


if __name__ == '__main__':
    CarlaConf.Map = 'Town01'
    CarlaConf.VehicleNum = 0
    main()
    CarlaConf.VehicleNum = 100
    sleep(15)
    main()
    # CarlaConf.Map = 'Town10HD_Opt'
    # CarlaConf.VehicleNum = 0
    # sleep(30)
    # main()
    # CarlaConf.VehicleNum = 100
    # sleep(15)
    # main()
