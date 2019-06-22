class Sector(object):
  floors = []
  assigned_car = None
  is_lowest = False
  is_highest = False
  sector_below = None
  sector_above = None

  def __init__(self, floors, assigned_car, is_lowest, is_highest, sector_below, sector_above):
    self.floors = floors
    self.assigned_car = assigned_car
    self.is_lowest = is_lowest
    self.is_highest = is_highest
    self.sector_below = sector_below
    self.sector_above = sector_above

  def is_vacant(self):
    return self.assigned_car != None

  def has_floor(self, floor):
    return floor in self.floors

  def __repr__ (self):
    return "Sector(%s, %s)" % (str(self.assigned_car), str(self.floors))