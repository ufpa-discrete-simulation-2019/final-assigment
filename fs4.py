class Fs4Simulation:
  def __init__(self, env, building):
    self.env = env
    self.awaiting = []
    self.building = building
    self.max_capacity = 4
    self.priority = {}

  def ask_ride(self, floor, to):
    self.awaiting.append({
      "floor": floor,
      "to": to
    })

  def run(self):
    self.init_sectors_priorities(self.building.sectors)
    while True:
      for person in self.awaiting:
        self.update_sectors_priorities(person['floor'], self.building.sectors)
        elevator = self.fs4(self.building.sectors, person["floor"])
        if (elevator 
          and elevator.curr_floor == person["floor"] 
          and len(elevator.riders) >= self.max_capacity):
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

  def init_sectors_priorities(self, sectors):
    for sector in sectors:
      self.priority[tuple(sector.floors)] = 1

  def update_sectors_priorities(self, floor, sectors):
    for sector in sectors:
      if sector.has_floor(floor):
        self.priority[tuple(sector.floors)] += 1
    return self.priority    

  def fs4(self, sectors, floor):
    # get free elevator cars -- at least one vacancy
    free_elevators = list(
      filter(lambda x: len(x.riders) < self.max_capacity,
        self.building.elevators)
    )

    # get highest-priority sector
    priorities = list(self.priority.items())
    hp_sector_floors = list(sorted(priorities, key=lambda x: x[1])[-1][0])
    hp_sector = None
    for sector in sectors:
      if sector.floors == hp_sector_floors:
        hp_sector = sector
    
    # get car with smallest distance from hp_sector 
    s = 1e10
    selected_car = None
    for elvt in free_elevators:
      dists = list(map(lambda x: abs(x - elvt.curr_floor),
        hp_sector.floors))
      min_dist = min(dists)
      if min_dist < s: 
        s = min_dist
        selected_car = elvt
    hp_sector.assigned_car = selected_car
    return selected_car