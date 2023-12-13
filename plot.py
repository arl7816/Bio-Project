import data
from classes import Data

def plot_no_plastic(fetched: dict, days: int) -> None:
  producers = []
  consumers = []
  secondary = []
  for day in range(days):
    total = 0
    for spec in fetched["samples"][0]["years"][day]["levels"][0]["species"]:
      total += spec["total"]
    producers.append(total)
    total = 0
    for spec in fetched["samples"][0]["years"][day]["levels"][1]["species"]:
      total += spec["total"]
    consumers.append(total)
    total = 0
    for spec in fetched["samples"][0]["years"][day]["levels"][2]["species"]:
      total += spec["total"]
    secondary.append(total)

  n = [i for i in range(days)]
  producer_totals = Data(Data((n, producers)).smooth_data())
  consumer_totals = Data(Data((n, consumers)).smooth_data())
  secondary_totals = Data(Data((n, secondary)).smooth_data())

  data.plot((3,3,1), producer_totals, "green", key = "main", legend="producers")
  data.plot((3,3,1), consumer_totals, "red", legend="primary")
  data.plot((3,3,1), secondary_totals, "cyan", legend="secondary")

  data.plot((3,3,4), consumer_totals, "red", legend="primary", key = "main_sub")
  data.plot((3,3,4), secondary_totals, "cyan", legend="secondary")

  data.subplots["main"].grid()
  data.subplots["main_sub"].grid()
  data.set_labels("main", "Years", "Total population", "Totals populations over time (No plastic)")
  data.set_labels("main_sub", "Years", "Total Population", "")

  data.subplots["main"].legend()
  data.subplots["main_sub"].legend()

  return

def plot_continue_plastic(fetched: dict, days: int) -> None:
  producers = []
  plastic_producers_avgs = []
  consumers = []
  plastic_consumer_avgs = []
  secondary = []
  plastic_second_avgs = []
  for day in range(days):
    total = 0
    plastic_total = 0
    for spec in fetched["samples"][1]["years"][day]["levels"][0]["species"]:
      total += spec["total"]
      plastic_total += spec["plastic"]

    length = len(fetched["samples"][1]["years"][day]["levels"][0]["species"])
    plastic_producers_avgs.append((plastic_total / length)
                                  if length != 0 else 0)
    
    plastic_total = 0
    producers.append(total)
    total = 0
    for spec in fetched["samples"][1]["years"][day]["levels"][1]["species"]:
      total += spec["total"]
      plastic_total += spec["plastic"]

    length = len(fetched["samples"][1]["years"][day]["levels"][1]["species"])
    plastic_consumer_avgs.append((plastic_total / length)
                                 if length != 0 else 0)
    
    plastic_total = 0
    consumers.append(total)
    total = 0
    for spec in fetched["samples"][1]["years"][day]["levels"][2]["species"]:
      total += spec["total"]
      plastic_total += spec["plastic"]

    length = len(fetched["samples"][1]["years"][day]["levels"][2]["species"])
    plastic_second_avgs.append((plastic_total / length) 
                               if length != 0 else 0)
    
    plastic_total = 0
    secondary.append(total)

  n = [i for i in range(days)]
  producer_totals = Data(Data((n, producers)).smooth_data())
  consumer_totals = Data(Data((n, consumers)).smooth_data())
  secondary_totals = Data(Data((n, secondary)).smooth_data())
  producer_pl_avgs = Data(Data((n, plastic_producers_avgs)).smooth_data())
  consumer_pl_avgs = Data(Data((n, plastic_consumer_avgs)).smooth_data())
  secondary_pl_avgs = Data(Data((n, plastic_second_avgs)).smooth_data())

  data.plot((3,3,2), producer_totals, "green", key = "main", legend="producers")
  data.plot((3,3,2), consumer_totals, "red", legend="primary")
  data.plot((3,3,2), secondary_totals, "cyan", legend="secondary")

  data.plot((3,3,5), consumer_totals, "red", legend="primary", key = "main_sub")
  data.plot((3,3,5), secondary_totals, "cyan", legend="secondary")

  data.plot((3, 2, 5), producer_pl_avgs, "green", "producers", key = "averages", linestyle="--")
  data.plot((3, 2, 5), consumer_pl_avgs, "red", "consumers", linestyle="--")
  data.plot((3, 2, 5), secondary_pl_avgs, "cyan", "secondary", linestyle="--")

  data.subplots["main"].grid()
  data.subplots["main_sub"].grid()
  data.subplots["averages"].grid()
  data.set_labels("main", "Years", "Total population", "Totals populations over time with plastic (weak primary)")
  data.set_labels("main_sub", "Years", "Total Population", "")
  data.set_labels("averages", "years", "average plastic", "Average Amount of plastic for weak consumer")

  data.subplots["main"].legend()
  data.subplots["main_sub"].legend()
  data.subplots["averages"].legend()

  return

def plot_weak_secondary(fetched: dict, days: int) -> None:
  producers = []
  plastic_producers_avgs = []
  consumers = []
  plastic_consumer_avgs = []
  secondary = []
  plastic_second_avgs = []
  for day in range(days):
    total = 0
    plastic_total = 0
    for spec in fetched["samples"][2]["years"][day]["levels"][0]["species"]:
      total += spec["total"]
      plastic_total += spec["plastic"]
    
    length = len(fetched["samples"][2]["years"][day]["levels"][0]["species"])
    plastic_producers_avgs.append((plastic_total / length)
                                  if length != 0 else 0)
    plastic_total = 0
    producers.append(total)
    total = 0
    for spec in fetched["samples"][2]["years"][day]["levels"][1]["species"]:
      total += spec["total"]
      plastic_total += spec["plastic"]
    length = len(fetched["samples"][2]["years"][day]["levels"][1]["species"])
    plastic_consumer_avgs.append((plastic_total / length)
                                 if length != 0 else 0)
    plastic_total = 0
    consumers.append(total)
    total = 0
    for spec in fetched["samples"][2]["years"][day]["levels"][2]["species"]:
      total += spec["total"]
      plastic_total += spec["plastic"]
    length = len(fetched["samples"][2]["years"][day]["levels"][2]["species"])
    plastic_second_avgs.append((plastic_total / length)
                               if length != 0 else 0)
    plastic_total = 0
    secondary.append(total)

  n = [i for i in range(days)]
  producer_totals = Data(Data((n, producers)).smooth_data())
  consumer_totals = Data(Data((n, consumers)).smooth_data())
  secondary_totals = Data(Data((n, secondary)).smooth_data())
  producer_pl_avgs = Data(Data((n, plastic_producers_avgs)).smooth_data())
  consumer_pl_avgs = Data(Data((n, plastic_consumer_avgs)).smooth_data())
  secondary_pl_avgs = Data(Data((n, plastic_second_avgs)).smooth_data())

  data.plot((3,3,3), producer_totals, "green", key = "main", legend="producers")
  data.plot((3,3,3), consumer_totals, "red", legend="primary")
  data.plot((3,3,3), secondary_totals, "cyan", legend="secondary")

  data.plot((3,3,6), consumer_totals, "red", legend="primary", key = "main_sub")
  data.plot((3,3,6), secondary_totals, "cyan", legend="secondary")

  data.plot((3, 2, 6), producer_pl_avgs, "green", "producers", key = "averages", linestyle="--")
  data.plot((3, 2, 6), consumer_pl_avgs, "red", "consumers", linestyle="--")
  data.plot((3, 2, 6), secondary_pl_avgs, "cyan", "secondary", linestyle="--")

  data.subplots["main"].grid()
  data.subplots["main_sub"].grid()
  data.subplots["averages"].grid()
  data.set_labels("main", "Years", "Total population", "Totals populations over time with plastic (weak secondary)")
  data.set_labels("main_sub", "Years", "Total Population", "")
  data.set_labels("averages", "years", "average plastic", "Average Amount of plastic for weak secondary")

  data.subplots["main"].legend()
  data.subplots["main_sub"].legend()
  data.subplots["averages"].legend()

  return

def display_results() -> None:
  fetched = data.fetch_data()

  days = len(fetched["samples"][0]["years"])

  plot_no_plastic(fetched, days)

  plot_continue_plastic(fetched, days)

  plot_weak_secondary(fetched, days)

  data.show()

  return