#Letters en waarden, tevens gecodeerd voor kleine letters

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letterscore = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters += [letter.lower() for letter in letters]
letterscore *= 2


#Samenvoegen van letters en letterscore in enkele 'dictionary', rekening houdend met blanke stenen

letters_letterscore = {letter: punten for letter, punten in zip(letters, letterscore)}
letters_letterscore[" "] = 0


#Score van woordinvoer bepalen

def woordscore(woord):
  punten = 0
  for letter in woord:
    punten += letters_letterscore.get(letter, 0)
  return punten


#Invoer spelvariabelen

spelers_en_woorden = {"speler1": ["ARGWAAN", "nochtans", "Antidiluviaans"], "speler2": ["slim", "Intelligent", "kunstmatig"], "speler3": ["licht", "doNKer", "race"], "speler4": ["voorstel", "kip", "EI"]}


#Toevoegen van woorden aan bestaande spelers

def nieuw_woord(speler, woord):
  spelers_en_woorden[speler].append(woord)
  
nieuw_woord("speler1", "Quixotte")


#Leaderboard en updates ervan

leaderboard = {}
def ldrboardupdate():
  for speler, woorden in spelers_en_woorden.items():
    punten = 0
    for woord in woorden:
      punten += woordscore(woord)
      leaderboard[speler] = punten
  return leaderboard

ldrboardupdate()
print(leaderboard)

