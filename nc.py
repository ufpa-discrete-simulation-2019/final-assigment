class NcSimulation():
  def __init__(self, env, building):
    self.env = env
    self.awaiting = []
    self.building = building

  def ask_ride(self, floor, to):
    self.awaiting.append({
      "floor": floor,
      "to": to
    })

  def run(self):
    while True:
      for person in self.awaiting:
        elevator = self.nc(self.building.sectors, person["floor"], person["to"])

        if elevator and elevator.curr_floor == person["floor"]:
          print(
            "[%i] Added rider to %s floor %i => %i" % 
            (self.env.now, elevator, person["floor"], person["to"])
          )
          
          elevator.add_ride(person["to"])
          self.awaiting.remove(person)
        elif elevator.curr_floor != person["floor"]:
          elevator.add_stop(person["floor"])

      self.building.update()

      yield self.env.timeout(1)
      print()

  def nc(self, sectors, floor, to_floor):
    fs = 1
    n = self.building.floor_count
    selected_car = self.building.elevators[0]

    for elevator in self.building.elevators:
      d = abs(elevator.curr_floor - floor)

      newFs = 0
      if elevator.still:
        newFs = n + 1 - d
      elif not elevator.going_up:
        same_direction = (floor - to_floor) > 0

        if floor > elevator.curr_floor:
          newFs = 1
        elif floor < elevator.curr_floor and same_direction:
          newFs = n + 2 - d
        elif floor < elevator.curr_floor and not same_direction:
          newFs = n + 1 - d
      elif elevator.going_up:
        same_direction = (floor - to_floor) < 0

        if floor < elevator.curr_floor:
          newFs = 1
        elif floor > elevator.curr_floor and same_direction:
          newFs = n + 2 - d
        elif floor > elevator.curr_floor and not same_direction:
          newFs = n + 1 - d
      
      if newFs > fs:
        selected_car = elevator
        fs = newFs
    
    return selected_car