class Dollar_in_Euro:
    
  waarde = 0.89
  
  def wisselkoers(self, euro):
    return euro * self.waarde
  
omzetting = Dollar_in_Euro()

voorbeeld5 = omzetting.wisselkoers(5)
print(voorbeeld5)
