class Ticker:
  def __init__(self, env, start_tick, delta):
    self.env = env
    self.start_tick = start_tick
    self.delta = delta

  def run(self):
    while True:
      yield self.env.timeout