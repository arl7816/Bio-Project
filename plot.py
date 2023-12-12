import data
from classes import Data

def display_results() -> None:
  fetched = data.fetch_data()

  days = len(fetched["days"])

  producers = []
  consumers = []
  secondary = []
  for day in range(days):
    total = 0
    for spec in fetched["days"][day]["levels"][0]["species"]:
      total += spec["total"]
    producers.append(total)
    total = 0
    for spec in fetched["days"][day]["levels"][1]["species"]:
      total += spec["total"]
    consumers.append(total)
    total = 0
    for spec in fetched["days"][day]["levels"][2]["species"]:
      total += spec["total"]
    secondary.append(total)

  n = [i for i in range(days)]
  producer_totals = Data((n, producers))
  consumer_totals = Data((n, consumers))
  secondary_totals = Data((n, secondary))

  data.plot((1,1,1), producer_totals, "green")
  data.plot((1,1,1), consumer_totals, "red")
  data.plot((1,1,1), secondary_totals, "cyan")

  data.show()

  return