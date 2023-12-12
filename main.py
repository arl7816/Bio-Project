import classes
from random import randint as ran
import data
import plot

def generate_ecosystem() -> classes.Ecosystem:
  return classes.Ecosystem()

def introduce_plastic(eco: classes.Ecosystem, plastic: int) -> classes.Ecosystem:
  producers = eco.trophic_layers[0]

  for molecule in range(plastic):
    spec_num = ran(0, len(producers)-1)
    orga_num = ran(0, len(producers[spec_num].population) - 1)

    producers[spec_num].population[orga_num].plastic += 1

  return eco

def simulate_day(eco: classes.Ecosystem, day_num: int) -> classes.Ecosystem:
  def simulate_layer(species: list[classes.Species], lower_level: list[classes.Species]) -> (list[classes.Species], list[classes.Species]):
    for spec_index, spec in enumerate(species):
      new_orgas = []
      for animal_index, animal in enumerate(spec.population):
        animal.life += 1

        # is the animal going to die
        if animal.life > spec.death_rate and spec.death_rate > -1:
          spec.population.pop(animal_index)
          if len(spec.population) == 0:
            species.pop(spec_index)
          continue

        # is the animal going to eat
        for _ in range(spec.eat_rate):
          if lower_level is None: break
          if len(lower_level) == 0:
            data.print_stats(eco, -1)
            raise IndexError("Went extinct on day " + str(day_num))
          spec_num = ran(0, len(lower_level)-1)
          #print(len(producers))
          orga_num = ran(0, len(lower_level[spec_num].population) - 1)

          animal.plastic += lower_level[spec_num].population[orga_num].plastic
          lower_level[spec_num].population.pop(orga_num)
          if len(lower_level[spec_num].population) == 0:
            lower_level.pop(spec_num)

          if animal.max_plastic <= animal.plastic and animal.max_plastic > -1:
            spec.population.pop(animal_index)
            if len(spec.population) == 0:
              species.pop(spec_index)
            continue

        # is the animal going to reproduce
        #print(animal.life)
        if animal.life % spec.reprodution_rate == 0:
          new_orgas.extend([classes.Organism(animal.max_plastic, animal.max_life, 1) for _ in range(ran(1, spec.reprodution_amount))])

      spec.population.extend(new_orgas)
    return species, lower_level
  x = None
  eco.trophic_layers[0], x = simulate_layer(eco.trophic_layers[0], None)
  for layer_index in range(1,len(eco.trophic_layers)):
    eco.trophic_layers[layer_index], eco.trophic_layers[layer_index-1] = simulate_layer(eco.trophic_layers[layer_index], eco.trophic_layers[layer_index-1])

  return eco

def simulate(eco: classes.Ecosystem, days: int, start_plastic: int, daily_plastic: int, show_stats = False):
  # introduce the plastic into population
  eco = introduce_plastic(eco, start_plastic)

  for day in range(days):
    data.append_data(eco)
    if show_stats: data.print_stats(eco, day)
    eco = simulate_day(eco, day)
    eco = introduce_plastic(eco, daily_plastic)
    print("Year", day, "complete")
  data.append_data(eco)

  return

def main() -> None:

  print("Generating ecosystem sample")
  
  data.init_data()

  eco = generate_ecosystem()
  
  print("Starting simulation (no plastic)")

  data.init_sample()
  simulate(eco, 30, 0, 100, False)

  print("complete")

  eco = generate_ecosystem()

  print("Starting simulation (with plastic)")
  data.init_sample()
  simulate(eco, 30, 1000, 100000, False)

  print("complete")

  data.submit_data()
  plot.display_results()

  return

if __name__ == "__main__":
  main()