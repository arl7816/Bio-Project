import classes
import json
from colors import bcolors

def print_stats(eco: classes.Ecosystem) -> None:
  bcolors.print_color("Number of producing species:" + 
                      str(len(eco.trophic_layers[0])),
                      bcolors.YELLOW)
  bcolors.print_color("Number of consuming species:" + 
                      str(len(eco.trophic_layers[1])),
                      bcolors.YELLOW)
  
  print(bcolors.GREEN + "Producer plastic averages:")
  overall_avg = 0
  total_orga = 0
  for producer in eco.trophic_layers[0]:
    avg = 0
    for animal in producer.population:
      if animal.plastic > 0:
        print("Id:", animal.id, "Plastic:", animal.plastic)
        avg += animal.plastic
        overall_avg += animal.plastic
    avg /= len(producer.population)
    total_orga += len(producer.population)
    print("Species:", producer.id , "Average plastic:", avg)
  
  overall_avg /= total_orga
  print("Overall plastic:", overall_avg)

  print(bcolors.RED + "Consumer plastic averages:")
  overall_avg = 0
  total_orga = 0
  for consumer in eco.trophic_layers[1]:
    avg = 0
    for animal in consumer.population:
      if animal.plastic > 0:
        print("Id:", animal.id, "Plastic:", animal.plastic)
        avg += animal.plastic
        overall_avg += animal.plastic
    avg /= len(consumer.population)
    total_orga += len(consumer.population)
    print("Species:", consumer.id , "Average plastic:", avg)
  
  overall_avg /= total_orga
  print("Overall plastic:", overall_avg)
  
  print(bcolors.DEFAULT)

  return