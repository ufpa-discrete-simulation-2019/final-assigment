import simpy
from building import Building
from fso import FsoSimulation

env = simpy.Environment()

floor_count = 10
elevator_count = 3
building = Building(env, floor_count, elevator_count)

simulation = FsoSimulation(env, building)

env.process(simulation.run())

simulation.ask_ride(1, 10)
env.run(until = 1)
simulation.ask_ride(1, 5)
env.run(until = 3)
simulation.ask_ride(7, 1)
env.run(until = 10)
simulation.ask_ride(1, 10)
env.run(until = 15)
simulation.ask_ride(1, 3)
env.run(until = 30)