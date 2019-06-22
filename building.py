from sector import Sector
from elevator import Elevator

class Building():
  def __init__(self, env, floor_count, elevator_count):
    self.env = env
    self.floor_count = floor_count
    self.elevators = [
      Elevator(self.env, i) 
      for i in range(1, elevator_count + 1)
    ]
    self.sectors = self.make_sectors(floor_count)

  def elevator_in(self, floor):
    for elevator in self.elevators:
      if elevator.curr_floor == floor:
        return elevator

    return None

  def make_sectors(self, floor_count):
    floors = list(range(1, floor_count + 1))

    sector_size = floor_count // len(self.elevators)
    sector_count = floor_count // sector_size
    
    sectors = []
    for i in range(1, sector_count + 1):
      is_lowest = i == 1
      is_highest = i == sector_count
      assigned_elevator = self.elevators[i - 1]
      
      start = sector_size * (i - 1)
      count = sector_size if not is_highest else sector_size + 1
      assigned_floors = floors[start : start + count]

      sector_below = None if is_lowest else sectors[i - 2]
      sector_above = None

      sector = Sector(
        assigned_floors,
        assigned_elevator,
        is_lowest,
        is_highest,
        sector_below,
        sector_above
      )

      sectors.append(sector)

    for i in range(0, len(sectors) - 1):
      sectors[i].sector_above = sectors[i + 1]

    return sectors

  def update(self):
    for elevator in self.elevators:
      elevator.update()

  def __repr__ (self):
    return "Building(%s)" % str(self.sectors)