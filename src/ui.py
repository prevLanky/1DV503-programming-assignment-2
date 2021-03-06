# class keyword simply used as a namespace
import Debugger

class TextColor:
    PURPLE = '\033[95m'
    TEAL = '\033[96m'
    CLEAR = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'


def UserInput(message: str):
  while(True):
    try:
      data = input(message)
      return data
    except ValueError:
      Debugger.warningmsg("Invalid input")


def UserInputInt(message: str):
  while(True):
    try:
      data = int(input(message))
      return data
    except ValueError:
      Debugger.warningmsg("Invalid input")


# hack to clear the screen cross platform
def Clear():
  print("\n" * 50)


def PrintHeadline(headline: str):
  #Clear()
  print(TextColor.BOLD + TextColor.UNDERLINE + TextColor.PURPLE + headline + TextColor.CLEAR)


def Print(string: str):
  print(TextColor.TEAL + string + TextColor.CLEAR, end="")


def MainMenu() -> str:
  Clear()
  PrintHeadline("Main Menu")
  print(TextColor.TEAL + "0. Custom Search\n")
  print("1. Show all available games")
  print("2. Show basic info about a game") # show Title, year, publisher, avg price
  print("3. Show all info about a game")
  print("4. Show price and available stores for a given game")
  print("5. Show all games between given price range\n")
  # function calls are not new lines
  print("6. Show all games from a specific year")  
  print("7. Show all games from a specific publisher") 
  print("8. Show all games from a specific platform") 
  print("9. Show all games from a specific genre") 
  print("10. Show all games from a specific store\n") 
  print("Q. Quit" + TextColor.CLEAR)
  print(TextColor.BOLD + TextColor.PURPLE + "------------------------------------------------------------------" + TextColor.CLEAR)
  return input()

###################################
def PrintVertical(heading: list, data: list):
  for i in range(0, len(heading)):
    print(TextColor.PURPLE + TextColor.UNDERLINE + heading[i] + ":" + TextColor.CLEAR, end="")
    line = str()
    for result in data:
      line += " " + str(result[i])
    print(TextColor.TEAL + line + TextColor.CLEAR)


def PrintData(heading: str, data: list):
  PrintHeadline("\n\n" + heading)
  
  for tuple in data:
    line = str()
    for element in tuple:
      line += element + " : "
    line = line.removesuffix(": ")
    print(TextColor.TEAL + line + TextColor.CLEAR)
