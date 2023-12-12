import classes
import json
from colors import bcolors
from matplotlib import pyplot as plt
from classes import Data

results = {}
subplots = {}
def print_stats(eco: classes.Ecosystem, day: int) -> None:
  bcolors.print_color("Day #" + str(day), bcolors.YELLOW)
  bcolors.print_color("Number of producing species:" + 
                      str(len(eco.trophic_layers[0])),
                      bcolors.YELLOW)
  bcolors.print_color("Number of consuming species:" + 
                      str(len(eco.trophic_layers[1])),
                      bcolors.YELLOW)
  bcolors.print_color("Number of secondary consuming species:" + 
                      str(len(eco.trophic_layers[2])),
                      bcolors.YELLOW)
  
  #producers
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
    print("Species:", producer.id , "Average plastic:", avg, "Pop:", len(producer.population))
  
  overall_avg /= total_orga
  print("Overall plastic:", overall_avg)

  # consumers
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
    print("Species:", consumer.id , "Average plastic:", avg, "Pop:", len(consumer.population))
  
  overall_avg /= total_orga
  print("Overall plastic:", overall_avg)

  # secondary consumers
  print(bcolors.CYAN + "Consumer plastic averages:")
  overall_avg = 0
  total_orga = 0
  for consumer in eco.trophic_layers[2]:
    avg = 0
    for animal in consumer.population:
      if animal.plastic > 0:
        print("Id:", animal.id, "Plastic:", animal.plastic)
        avg += animal.plastic
        overall_avg += animal.plastic
    avg /= len(consumer.population)
    total_orga += len(consumer.population)
    print("Species:", consumer.id , "Average plastic:", avg, "Pop:", len(consumer.population))
  
  overall_avg /= total_orga
  print("Overall plastic:", overall_avg)
  
  print(bcolors.DEFAULT)

  return

def init_data() -> None:
  results["days"] = []

def append_data(eco: classes.Ecosystem) -> None:
  results["days"].append({"levels": []})
  for level in eco.trophic_layers:
    arr = results["days"][-1]["levels"]
    arr.append({"species": []})
    results["days"][-1]["levels"] = arr
    for spec in level:
      total_plastic = 0
      for orga in spec.population:
        total_plastic += orga.plastic
      arr = results["days"][-1]["levels"][-1]["species"]
      arr.append({"id": spec.id, "total": len(spec.population), "plastic": total_plastic})
      results["days"][-1]["levels"][-1]["species"] = arr

def submit_data() -> None:
  with open("results.json", "w") as file:
    file.write(json.dumps(results, indent=4))

def fetch_data() -> dict:
  with open("results.json", "r") as file:
    data = json.load(file)
    return data

def plot(trt: tuple, data: Data, color, legend="", marker=None, key=None):
  if key == None:
    key = trt

  sub = plt.subplot(trt[0], trt[1], trt[2])
  subplots[key] = sub

  sub.plot(data.x, data.y, label=legend, color=color, marker=marker)
  return sub

def scatter(trt: tuple, data: Data, color: str, legend="", marker=None, key=None):
  if key == None:
    key = trt
  
  sub = plt.subplot(trt[0], trt[1], trt[2])
  subplots[key] = sub

  sub.scatter(data.x, data.y, label=legend, color=color, marker=marker)
  return sub

def bar(trt: tuple, data: Data, color, legend="", marker="o", key=None):
  if key == None:
    key = trt

  sub = plt.subplot(trt[0], trt[1], trt[2])
  subplots[key] = sub

  sub.bar(data.x, data.y, label=legend, color=color)
  return sub

def set_labels(key: str, xlabel: str, ylabel: str, title: str):
  subplots[key].set_title(title)
  subplots[key].set_xlabel(xlabel)
  subplots[key].set_ylabel(ylabel)

def show():
  plt.show()

if __name__ == "__main__":
  """with open("results.json", "r") as file:
    data = json.load(file)
    print(data["Days"])"""
  
  with open("results.json", "w") as file:
    x = {"Days": 5, "Plastic total": 2}
    y = json.dumps(x)
    file.write(y)

  pass