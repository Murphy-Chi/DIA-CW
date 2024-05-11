# from carla.agent.agent import Agent
# from carla.client import VehicleControl
# from carla.agent_benchmark.experiment import Experiment
# from carla.sensor import Camera
# from carla.settings import CarlaSettings
# from .experiment_suite import ExperimentSuite
#
# class ForwardAgent(Agent):
#     def run_step(self, measurements, sensor_data, directions, target):
#             if current_speed < 20:  # speed limit can be adjusted
#         control.throttle = 0.9
#     else:
#         control.throttle = 0.0  # coasting or slight braking
#
#     if directions == "STRAIGHT":
#         control.steer = 0
#     elif directions == "LEFT":
#         control.steer = -0.5  # Adjust the steer value based on required sharpness of the turn
#     elif directions == "RIGHT":
#         control.steer = 0.5
#     else:
#         control.steer = 0  # if no direction is provided, continue straight
#
#     if target is not None and current_speed > 10:
#         distance_to_target = calculate_distance(measurements.position, target.position)  # Hypothetical function
#         if distance_to_target < 20:  # Close to target, start braking
#             control.brake = 0.5
#         else:
#             control.brake = 0.0
#
#     return control
#
#
# class BasicExperimentSuite(ExperimentSuite):
#     @property
#     def train_weathers(self):
#         return [1]
#
#     @property
#     def test_weathers(self):
#         return [1]
#
#
#
# if __name__ == "__main__":
#     run_benchmark()

def benchmark_reward(run_results: list):
    total_score = 0
    for i, result in enumerate(run_results):
        if result < 0:
            # the agent timeout
            total_score -= 10
        else:
            # finish the task
            total_score += 100
            # every collision will reduce the score
            total_score -= result * 5

    return total_score / len(run_results)
