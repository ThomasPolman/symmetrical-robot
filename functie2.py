# GROUND SHIPPING 

# 2 lb or less
# $1.50 * weight + $20.00

# Over 2 lb but less than or equal to 6 lb
# $3.00 * weight + $20.00

# Over 6 lb but less than or equal to 10 lb
# $4.00 * weight + $20.00

# Over 10 lb
# $4.75 * weight + $20.00


# DRONE SHIPPING

# 2 lb or less
# $4.50 * weight

# Over 2 lb but less than or equal to 6 lb
# $9.00 * weight

# Over 6 lb but less than or equal to 10 lb
# $12.00 * weight

# Over 10 lb
# $14.25 * weight


# PREMIUM GROUND SHIPPING
# Flat charge: $125.00


# OPGAVE
# Creeer een functie die voor ieder willekeurig gewicht
# de goedkoopste methode en daarbij behorende prijs signaleert


def ground_shipping(weight):
  if weight <= 2:
    return 1.5 * weight + 20
  elif weight > 2 and weight <= 6:
    return 3 * weight + 20
  elif weight > 6 and weight <= 10:
  	return 4 * weight + 20
  elif weight > 10:
    return 4.75 * weight + 20

def drone_shipping(weight):
   if weight <= 2:
     return 4.5 * weight
   elif weight > 2 and weight <= 6:
     return 9 * weight
   elif weight > 6 and weight <= 10:
     return weight * 12
   elif weight > 10:
     return weight * 14.5
  
premium_ground_shipping = 125.00

  
def cheapest_shipping(weight):
  if drone_shipping(weight) < premium_ground_shipping and drone_shipping(weight) < ground_shipping(weight):
    return "Drones zijn het goedkoopst! Het gaat u "+ str(drone_shipping(weight))+" kosten."
  elif ground_shipping(weight) < premium_ground_shipping and ground_shipping(weight) < drone_shipping(weight):
    return "U kunt het beste normaal landvervoer nemen. Dit gaat u "+ str(ground_shipping(weight))+ " kosten."
  else:
    return "Premium grondvervoer is uw beste optie. Dit kost u 125.00."

#Geef tussen de haakjes het gewicht aan
print(cheapest_shipping(5.0))
