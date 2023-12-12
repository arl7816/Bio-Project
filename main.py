import classes
from random import randint as ran
import data

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
  # producers
  producers = eco.trophic_layers[0]
  print("len of prod before:", len(producers[0].population))
  for i, producer in enumerate(producers):
    new_orgas = []
    for index, animal in enumerate(producer.population):
      animal.life += 1
      
      if animal.life % producer.reprodution_rate == 0:
        new_orgas.extend([classes.Organism(-1) for _ in range(producer.reprodution_amount)])
      
      if day_num % producer.death_rate == 0:
        producer.population.pop(index)
    producer.population.extend(new_orgas)
  print("len of prod after:", len(producers[0].population))

  # consumers
  consumers = eco.trophic_layers[1]
  for consumer in consumers:
    new_orgas = []
    for index, animal in enumerate(consumer.population):
      if day_num % consumer.reprodution_rate == 0:
        #consumer.population.append(classes.Organism())
        new_orgas.append(classes.Organism(50))

      if day_num % consumer.death_rate == 0:
        consumer.population.pop(index)
        continue
      
      for _ in range(consumer.eat_rate):
        spec_num = ran(0, len(producers)-1)
        #print(len(producers))
        orga_num = ran(0, len(producers[spec_num].population) - 1)

        animal.plastic += producers[spec_num].population[orga_num].plastic
        producers[spec_num].population.pop(orga_num)
        if len(producers[spec_num].population) == 0:
          producers.pop(spec_num)

      if animal.max_plastic <= animal.plastic:
        consumer.population.pop(index)
    consumer.population.extend(new_orgas)

  # secondary consumers

  return eco

def simulate(eco: classes.Ecosystem, days: int, start_plastic: int):
  # introduce the plastic into population
  eco = introduce_plastic(eco, start_plastic)

  """for level in eco.trophic_layers:
    for spec in level:
      for animal in spec.population:
        if animal.plastic > 0:
          print(animal.id , animal.plastic)"""

  # simulate the days
  data.print_stats(eco)
  for day in range(days):
    eco = simulate_day(eco, day)
    eco = introduce_plastic(eco, 10)
  data.print_stats(eco)

  return

def main() -> None:

  eco = generate_ecosystem()

  simulate(eco, 10, 20000)

  return

if __name__ == "__main__":
  main()