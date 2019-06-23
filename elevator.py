class Elevator():
  def __init__(self, env, name, curr_floor = 1):
    self.riders = []
    self.name = name
    self.curr_floor	= curr_floor
    self.stops = []
    self.going_up	= True
    self.still = True
    self.env = env

  def add_ride(self, to):
    if not to in self.stops:
      self.stops.append(to)
      self.riders.append(to)

    self.still = False

  def add_rider(self, rider):
    self.riders.append(rider) 

  def add_stop(self, stop):
    if not stop in self.stops:
      self.stops.append(stop)

  def remove_stop(self, stop):
    self.stops.remove(stop)

  def update(self):
    self.still = True
    
    if self.stops:
      curr_dest = None

      if self.going_up:
        curr_dest = max(self.stops)
      else:
        curr_dest = min(self.stops)

      if curr_dest > self.curr_floor:
        self.curr_floor += 1
        self.still = False
        self.going_up	= True
      elif curr_dest < self.curr_floor:
        self.curr_floor -= 1
        self.still = False
        self.going_up = False

      self.stops = [x for x in self.stops if x != self.curr_floor]
    
    print("[%i] %s is on floor %i" % (self.env.now, str(self), self.curr_floor))

    quitters = len([
      floor for floor in self.riders if floor == self.curr_floor
    ])
    self.riders = [
      floor for floor in self.riders if floor != self.curr_floor
    ]

    if quitters > 0:
      print("[%i] %i left %s on floor %i" % (self.env.now, quitters, str(self), self.curr_floor))

  def __repr__(self):
    return "Elevator(%i)" % self.name