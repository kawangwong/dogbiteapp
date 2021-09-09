import requests
dogBiteUrl = "https://data.cityofnewyork.us/resource/rsgh-akpg.json?$limit=11000"

formattedURLforJson = requests.get(f"{dogBiteUrl}")
prettyprint = formattedURLforJson.json()[1] #change the index number here.

'''this is a counter of how many times it appears in list'''

###testing function for print
def testerthing():
  print("hey, you have a working page!!")


def appearance(phrase):
  Male = 0
  Female = 0
  Unknown = 0
  x = 100 #change value for desired range
  for i in range(x):
    prettyprint = formattedURLforJson.json()[i]
    theGender = prettyprint.get(phrase, None)
    if theGender == "M":
      Male += 1
    if theGender == "M" and i == x-1:
      Male += 1
      statement1 =(f"There are {Male} male dogs that bit people in 2015.")
      statement2 = (f"There are {Female} female dogs that bit people in 2015.")
      statement3 = (f"There are {Unknown} unidentified gender of dogs that bit people in 2015.")
      allstatements = (f"{statement1} \n {statement2} \n {statement3}")
      return allstatements      
    if theGender == "F":
      Female += 1
    if theGender == "F" and i == x-1:
      Female += 1
      statement1 =(f"There are {Male} male dogs that bit people in 2015.")
      statement2 = (f"There are {Female} female dogs that bit people in 2015.")
      statement3 = (f"There are {Unknown} unidentified gender of dogs that bit people in 2015.")
      allstatements = (f"{statement1} \n {statement2} \n {statement3}")
      return allstatements
    if theGender == "U":
      Unknown += 1
    if theGender == "U" and i == x-1:
      Unknown += 1
      statement1 =(f"There are {Male} male dogs that bit people in 2015.")
      statement2 = (f"There are {Female} female dogs that bit people in 2015.")
      statement3 = (f"There are {Unknown} unidentified gender of dogs that bit people in 2015.")
      allstatements = (f"{statement1} \n {statement2} \n {statement3}")
      return allstatements

# appearance("gender")

def location(spot):
  Queens = 0
  Bronx = 0
  Brooklyn = 0
  Manhattan = 0
  Staten_Island = 0
  Other = 0
  x = 100 #change value for desired range
  for i in range(x):
    prettyprint = formattedURLforJson.json()[i]
    theSpot = prettyprint.get(spot, "Other")
    if theSpot == "Queens":
      Queens += 1
    if theSpot == "Queens" and i == x-1:
      Queens += 1
      bstatement1 = (f"In Queens, there were {Queens} dog bites in 2015")
      bstatement2 = (f"In the Bronx, there were {Bronx} dog bites in 2015")
      bstatement3 = (f"In Brooklyn, there were {Brooklyn} dog bites in 2015")
      bstatement4 = (f"In Manhattan, there were {Manhattan} dog bites in 2015")
      bstatement5 = (f"In Staten Island, there were {Staten_Island} dog bites in 2015")
      bstatement6 = (f"We have no idea where there were {Other} dog bites in 2015")
      ballstatements = (f"{bstatement1}\n{bstatement2}\n{bstatement3}\n{bstatement4}\n{bstatement5}")
      print(ballstatements)
      return ballstatements
    if theSpot == "Bronx":
      Bronx += 1
    if theSpot == "Bronx" and i == x-1:
      Bronx += 1
      bstatement1 = (f"In Queens, there were {Queens} dog bites in 2015")
      bstatement2 = (f"In the Bronx, there were {Bronx} dog bites in 2015")
      bstatement3 = (f"In Brooklyn, there were {Brooklyn} dog bites in 2015")
      bstatement4 = (f"In Manhattan, there were {Manhattan} dog bites in 2015")
      bstatement5 = (f"In Staten Island, there were {Staten_Island} dog bites in 2015")
      bstatement6 = (f"We have no idea where there were {Other} dog bites in 2015")
      ballstatements = (f"{bstatement1}\n{bstatement2}\n{bstatement3}\n{bstatement4}\n{bstatement5}\n{bstatement6}")
      print(ballstatements)
      return ballstatements
    if theSpot == "Brooklyn":
      Brooklyn += 1
    if theSpot == "Brooklyn" and i == x-1:
      Brooklyn += 1
      bstatement1 = (f"In Queens, there were {Queens} dog bites in 2015")
      bstatement2 = (f"In the Bronx, there were {Bronx} dog bites in 2015")
      bstatement3 = (f"In Brooklyn, there were {Brooklyn} dog bites in 2015")
      bstatement4 = (f"In Manhattan, there were {Manhattan} dog bites in 2015")
      bstatement5 = (f"In Staten Island, there were {Staten_Island} dog bites in 2015")
      bstatement3 = (f"We have no idea where there were {Other} dog bites in 2015")
      ballstatements = (f"{bstatement1}\n{bstatement2}\n{bstatement3}\n{bstatement4}\n{bstatement5}\n{bstatement6}")
      print(ballstatements)
      return ballstatements
    if theSpot == "Manhattan":
      Manhattan += 1
    if theSpot == "Manhattan" and i == x-1:
      Manhattan += 1
      bstatement1 = (f"In Queens, there were {Queens} dog bites in 2015")
      bstatement2 = (f"In the Bronx, there were {Bronx} dog bites in 2015")
      bstatement3 = (f"In Brooklyn, there were {Brooklyn} dog bites in 2015")
      bstatement4 = (f"In Manhattan, there were {Manhattan} dog bites in 2015")
      bstatement5 = (f"In Staten Island, there were {Staten_Island} dog bites in 2015")
      bstatement6 = (f"We have no idea where there were {Other} dog bites in 2015")
      ballstatements = (f"{bstatement1}\n{bstatement2}\n{bstatement3}\n{bstatement4}\n{bstatement5}\n{bstatement6}")
      print(ballstatements)
      return ballstatements
    if theSpot == "Staten Island":
      Staten_Island += 1
    if theSpot == "Staten Island" and i == x-1:
      Staten_Island += 1
      bstatement1 = (f"In Queens, there were {Queens} dog bites in 2015")
      bstatement2 = (f"In the Bronx, there were {Bronx} dog bites in 2015")
      bstatement3 = (f"In Brooklyn, there were {Brooklyn} dog bites in 2015")
      bstatement4 = (f"In Manhattan, there were {Manhattan} dog bites in 2015")
      bstatement5 = (f"In Staten Island, there were {Staten_Island} dog bites in 2015")
      bstatement6 = (f"We have no idea where there were {Other} dog bites in 2015")
      ballstatements = (f"{bstatement1}\n{bstatement2}\n{bstatement3}\n{bstatement4}\n{bstatement5}\n{bstatement6}")
      print(ballstatements)
      return ballstatements
    if theSpot == "Other" and i == x-1:
      Other += 1
    if theSpot == "Other" and i == x-1:
      Other += 1
      bstatement1 = (f"In Queens, there were {Queens} dog bites in 2015")
      bstatement2 = (f"In the Bronx, there were {Bronx} dog bites in 2015")
      bstatement3 = (f"In Brooklyn, there were {Brooklyn} dog bites in 2015")
      bstatement4 = (f"In Manhattan, there were {Manhattan} dog bites in 2015")
      bstatement5 = (f"In Staten Island, there were {Staten_Island} dog bites in 2015")
      bstatement6 = (f"We have no idea where there were {Other} dog bites in 2015")
      ballstatements = (f"{bstatement1}\n{bstatement2}\n{bstatement3}\n{bstatement4}\n{bstatement5}\n{bstatement6}")
      print(ballstatements)
      return ballstatements

location("borough")


# prettyprint.get("breed", None)
