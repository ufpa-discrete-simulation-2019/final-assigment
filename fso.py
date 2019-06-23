class FsoSimulation():
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
        elevator = self.fso(self.building.sectors, person["floor"])
        if elevator and elevator.curr_floor == person["floor"]:
          print(
            "[%i] Added rider to %s floor %i => %i" % 
            (self.env.now, elevator, person["floor"], person["to"])
          )
          
          elevator.add_ride(person["to"])
          self.awaiting.remove(person)
        elif elevator and elevator.curr_floor != person["floor"]:
          elevator.add_stop(person["floor"])

      self.building.update()

      yield self.env.timeout(1)
      print()

  def fso(self, sectors, floor):
    selected_car = None
    
    for sector in sectors:
      if sector.has_floor(floor):
        selected_car = sector.assigned_car

    lowest_sector = None

    for sector in sectors:
      if (not sector.is_vacant()) and sector.is_highest:
        sector_above = sector.sector_above

        if not sector_above.is_vacant() and sector_above.has_floor(floor):
          selected_car = sector.assigned_car
      
      if lowest_sector == None and (not sector.is_vacant()):
        if not sector.is_lowest:
          sector_below = sector.sector_below

          if sector_below.is_vacant() and sector_below.has_floor(floor):
            selected_car = sector.assigned_car
          
          lowest_sector = True
    if selected_car is None:
      print(selected_car,"ITS NONE")
    return selected_car
