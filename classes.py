class Organism:
  plastic: float
  max_plastic: float
  id: int
  life: int

  instance = 0

  def __init__(self, max_plastic: int) -> None:
    self.plastic = 0
    self.life = 0
    self.max_plastic = max_plastic
    self.id = Organism.instance
    Organism.instance += 1

class Species:
  instance = 0

  def __init__(self, repro_rate: int, repro_amount: int, eat_rate: int, death_rate: int, max_plastic: int) -> None:
    self.reprodution_rate = repro_rate
    self.reprodution_amount = repro_amount
    self.eat_rate = eat_rate
    self.death_rate = death_rate
    self.day_num = 1
    self.population = [Organism(max_plastic) for _ in range(2)]
    self.id = Species.instance
    Species.instance += 1


class Ecosystem:
  trophic_layers: list[list[Species]] # [producers, consumers, secondary consumers]

  def __init__(self) -> None:
    self.trophic_layers = [None for _ in range(5)] 
    #self.trophic_layers = [[Species() for _ in range(5)] for _ in range(3)]
    self.trophic_layers[0] = [Species(50, 50, -1, 90, -1) for _ in range(5)]
    self.trophic_layers[1] = [Species(90, 2, 20, 60, 50) for _ in range(5)]
