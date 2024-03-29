import simpy
import numpy
import scipy.stats as st
from building import Building
from fso import FsoSimulation
from nc import NcSimulation

numpy.random.seed(51)
env = simpy.Environment()

p = st.expon.rvs(size=10, loc=0,scale=2)

floor_count = 10
elevator_count = 3
building = Building(env, floor_count, elevator_count)

simulation = NcSimulation(env, building)

env.process(simulation.run())

time = 5
for x in range(50):
    from_floor = numpy.random.randint(0,10)
    to_floor = numpy.random.randint(0,10)
    print(from_floor,to_floor)
    simulation.ask_ride(from_floor,to_floor)
    #env.run(until=time)
    #time += 5


env.run(until=100)
