class bcolors:
  """
  Changes the color of the terminal text.
  \n
  !!!WARNING will set all of terminal below to the color, make sure to reset color
  if desired at the end of the print statement and or string!!!
  """

  PINK = '\033[95m'
  BLUE = '\033[94m'
  CYAN = '\033[96m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  DEFAULT = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

  def generate_string(string: str, color: str, underline = False, bold = False, end_color = DEFAULT) -> str:
    return (bcolors.UNDERLINE if underline else "") + (bcolors.BOLD if bold else "") + color + string + end_color

  def print_color(string: str, color: str, underline = False, bold = False, end_color = DEFAULT) -> None:
    """
    Prints out a colored string in the command Line

    Args:
        string (str): The string to be printed
        color (str): The color of the string (recommend using the bcolors class)
        underline (bool, optional): Whether or not the text is underlined. Defaults to False.
        bold (bool, optional): whether or not the text is bold. Defaults to False.
        end_color (str, optional): The terminal color after the print statement. 
        Defaults to bcolors.DEFAULT.
    """
    print((bcolors.UNDERLINE if underline else "") + 
          (bcolors.BOLD if bold else "") + 
          color + string + end_color)