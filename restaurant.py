class Business:
  
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
  

class Franchise:
    
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return "This restaurant is located at " + self.address
  
  def available_menus(self, time):
    present_availability = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        present_availability.append(menu)
    return present_availability

  
class Menu:
  
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
    
  def __repr__(self):
    return self.name + ". This will be served from " + str(self.start_time) + " until " + str(self.end_time) + "." 
  
  def calculate_bill(self, purchased_items):
    total_price = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        total_price += self.items[purchased_item]
    return total_price

# MENUS
  
brunch = Menu("Brunch", {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 1100, 1600)

  
early_bird = Menu("Early Bird", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 1500, 1800)

dinner = Menu("Dinner", {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 1700, 2300)

kids = Menu("Kids", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 1100, 2100)

arepas = Menu("Take a'Arepa", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 1000, 2000)


# FRANCHISES

flagship_store = Franchise("1232 West End Road", [early_bird, kids, dinner, brunch])

new_installment = Franchise("12 East Mulberry Street", [early_bird, kids, dinner, brunch])

arepas_place = Franchise("189 Fitzgerald Avenue", arepas)

#BUSINESSES

basta = Business("Basta Fazoolin' with my heart", [flagship_store, new_installment])

arepabusiness = Business("Take a'Arepa", arepas_place)

