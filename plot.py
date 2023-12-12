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

  data.plot((2,2,1), producer_totals, "green", key = "main", legend="producers")
  data.plot((2,2,1), consumer_totals, "red", legend="primary")
  data.plot((2,2,1), secondary_totals, "cyan", legend="secondary")

  data.plot((2,2,3), consumer_totals, "red", legend="primary", key = "main_sub")
  data.plot((2,2,3), secondary_totals, "cyan", legend="secondary")

  data.subplots["main"].grid()
  data.subplots["main_sub"].grid()
  data.set_labels("main", "Years", "Total population", "Totals populations over time (No plastic)")
  data.set_labels("main_sub", "Years", "Total Population", "")

  data.subplots["main"].legend()
  data.subplots["main_sub"].legend()

def plot_continue_plastic(fetched: dict, days: int) -> None:
  producers = []
  consumers = []
  secondary = []
  for day in range(days):
    total = 0
    for spec in fetched["samples"][1]["years"][day]["levels"][0]["species"]:
      total += spec["total"]
    producers.append(total)
    total = 0
    for spec in fetched["samples"][1]["years"][day]["levels"][1]["species"]:
      total += spec["total"]
    consumers.append(total)
    total = 0
    for spec in fetched["samples"][1]["years"][day]["levels"][2]["species"]:
      total += spec["total"]
    secondary.append(total)

  n = [i for i in range(days)]
  producer_totals = Data(Data((n, producers)).smooth_data())
  consumer_totals = Data(Data((n, consumers)).smooth_data())
  secondary_totals = Data(Data((n, secondary)).smooth_data())

  data.plot((2,2,2), producer_totals, "green", key = "main", legend="producers")
  data.plot((2,2,2), consumer_totals, "red", legend="primary")
  data.plot((2,2,2), secondary_totals, "cyan", legend="secondary")

  data.plot((2,2,4), consumer_totals, "red", legend="primary", key = "main_sub")
  data.plot((2,2,4), secondary_totals, "cyan", legend="secondary")

  data.subplots["main"].grid()
  data.subplots["main_sub"].grid()
  data.set_labels("main", "Years", "Total population", "Totals populations over time (with plastic)")
  data.set_labels("main_sub", "Years", "Total Population", "")

  data.subplots["main"].legend()
  data.subplots["main_sub"].legend()

def display_results() -> None:
  fetched = data.fetch_data()

  days = len(fetched["samples"][0]["years"])

  plot_no_plastic(fetched, days)

  plot_continue_plastic(fetched, days)

  data.show()

  return