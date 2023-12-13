import numpy as np
from scipy.interpolate import make_interp_spline
from math import pow, sqrt
from scipy import stats
from random import randint as ran

class Organism:
  plastic: float
  max_plastic: float
  id: int
  life: int
  max_life: int

  instance = 0

  def __init__(self, max_plastic: int, max_life = 1, start_life = -1) -> None:
    self.plastic = 0
    self.max_life = max_life
    self.life = ran(0,max_life-1) if start_life == -1 else start_life
    self.max_plastic = max_plastic
    self.id = Organism.instance
    Organism.instance += 1

class Species:
  instance = 0

  def __init__(self, repro_rate: int, repro_amount: int, eat_rate: int, death_rate: int, max_plastic: int, start_amount: int) -> None:
    """[SUMMARY]

    Args:
        repro_rate (int): rate of reproduction in days
        repro_amount (int): the amount of babys they have 
        eat_rate (int): the amount of animals they eat a day (-1 means no eat)
        death_rate (int): how long until they die in days
        max_plastic (int): max plastic before death (-1 means no death) 
    """
    self.reprodution_rate = repro_rate
    self.reprodution_amount = repro_amount
    self.eat_rate = eat_rate
    self.death_rate = death_rate
    self.day_num = 1
    self.population = [Organism(max_plastic, death_rate) for _ in range(start_amount)]
    self.id = Species.instance
    Species.instance += 1


class Ecosystem:
  trophic_layers: list[list[Species]] # [producers, consumers, secondary consumers]

  def __init__(self, spec_count: tuple[int], *args: tuple[int, int, int, int, int, int]) -> None:
    self.trophic_layers = [None for _ in range(3)] 
    self.trophic_layers[0] = [Species(*args[0]) for _ in range(spec_count[0])]
    self.trophic_layers[1] = [Species(*args[1]) for _ in range(spec_count[1])]
    self.trophic_layers[2] = [Species(*args[2]) for _ in range(spec_count[2])]


class Data():
  """[summary]
  class used to keep track of two sets of data and manipulate them

  Raises:
    Exception: tuple must provie two arrays in the form of tuple
    Exception: both the x and y axis must have the same number of element
  """
  x = np.array([])
  y = np.array([])

  def __init__(self, data: tuple) -> None:
    """[summary]
    The constructor of the Data class

    Args:
      data (tuple): both the x and y axis of the initial data

    Raises:
      Exception: tuple must provie two arrays in the form of tuple
      Exception: both the x and y axis must have the same number of element
    """
    if len(data) != 2: raise Exception("the data must consist of two arrays")
    if len(data[0]) != len(data[1]):  raise Exception("x and y must be the same")
    self.x = np.array(data[0])
    self.y = np.array(data[1])
    self.size = len(self.x)

  def inverseX(self) -> None:
    """[summary]
      transforms each element of the xaxis into the reciprocal the element
    
    Returns:
      None
    """
    for i in range(len(self.x)):
      if (self.x[i] == 0): continue
      self.x[i] = 1/self.x[i]
  
  def insert(self, x, y, index=0) -> None:
    """[summary] not yet implemented

    Args:
        x (_type_): _description_
        y (_type_): _description_
        index (int, optional): _description_. Defaults to 0.
    """
    return

  def line_of_best_fit(self) -> list:
    """[summary] Gets the line of best fit for your data

    Preconditions:
      both x and y values are integers or floats

    Returns:
        list: an numpy array
    """
    a, b = np.polyfit(self.x, self.y, 1)

    return (self.x, a*self.x+b)

  def smooth_data(self, smoothness = 500) -> tuple:
    """[summary] Smooths out the data thats gets displayed

    Args:
      smoothness (int, optional): The amount of data points generated between x values (linear line is 50). Defaults to 500.

    Raises:
      Exception: smoothness of the line is less than 0

    Returns:
        tuple: your new data points, in the form of (x axis, y axis)
    """

    if (smoothness < 0):
      raise Exception("Smoothness of the data must be above or equal to 0")

    X_Y_Spline = make_interp_spline(self.x, self.y)
 
    # Returns evenly spaced numbers
    # over a specified interval.
    X_ = np.linspace(self.x.min(), self.x.max(), smoothness)
    Y_ = X_Y_Spline(X_)

    return (X_, Y_)

  def derivative(self) -> tuple:
    x = self.x
    y = self.y
    der = np.diff(y) / np.diff(x)
    x2 = (x[:-1] + x[1:]) / 2
    return (x2, der)
  
  def get_max(self) -> int:
    """[summary] Gets the max element from the y axis

    Returns:
        int: the max element within the y axis
    """
    return self.y.max()
  
  def get_min(self) -> float:
    return self.y.min()

  def remap(self, max = None) -> None:
    """[summary] stretches each of the data points on the y axis, so that the data fits more nicely between 
    a maximum number and 0

    Args:
      max (int, optional): The highest number the y should stretch to. Defaults to the max value of the object.

    Returns:
      None
    """
    if max == None: max = self.get_max()

    for index, element in enumerate(self.y):
      self.y[index] = max / element


  def get_averages(self, sort=False, x=None, y=None) -> tuple:
    """[summary] Gets the averages for every x value that repeats

    Args:
      sort (bool, optional): determines whether or not to sort the average x axis. Defaults to False
      x (list, optional): the x axis to get averages for. Defaults to the objects x axis
      y (list, optional): the y axis to get averages for. Defaults to the objects y axis 

    Returns:
        tuple(list, list): the x axis and the y axis representing the average of the given x element
    """
    averages = dict()
    xaxis = []
    yaxis = []
    if type(x) == type(None): x = self.x
    if type(y) == type(None): y = self.y

    for index in range(len(x)):
      if x[index] not in averages:
        averages[x[index]] = {
          "value": 0,
          "amount": 0
        }
      averages[x[index]]["value"] += y[index]
      averages[x[index]]["amount"] += 1
    
    for key in averages.keys():
      xaxis.append(key)
    
    if sort:
      xaxis.sort()

    for key in xaxis:
      yaxis.append(averages[key]["value"] / averages[key]["amount"])

    return xaxis, yaxis

  def mean(self, xaxis = False) -> float:
    sigma = 0
    if xaxis: sigma = sum(self.x)
    else: sigma = sum(self.y)

    return sigma / self.size
  
  def mode(self, xaxis = False):
    if xaxis:
      return stats.mode(self.x)[0]
    return stats.mode(self.y)[0]
  
  def median(self, xaxis = False):
    if xaxis: data = sorted(self.x)
    else: data = sorted(self.y)
    med = 0

    if self.size == 1:
      return data[0]

    if self.size % 2 == 1: 
      med = data[(self.size + 1) / 2 - 1]
    else:
      k = self.size / 2
      med = .5 * (data[k] + data[k - 1])

    return med
  
  def standard_deviation(self, xaxis = False):
    mean = 0
    if xaxis: mean = self.mean(True)
    else: mean = self.mean()

    sigma = 0
    if xaxis: sigma = sum([pow(n - mean, 2) for n in self.x])
    else: sigma = sum([pow(n - mean, 2) for n in self.y])

    varient = sigma / (self.size - 1)

    return sqrt(varient)
