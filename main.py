# 
# Multi-Tarif Taximeter
km = 12

if km <= 3:  
    cost = 5.0  #Kurzstrecke
elif km <= 10:  
    cost = 5.0 * (km - 3) * 2.0  #Normaltarif
else:   
    cost = 19.0 * (km - 10) *1.5  #Langstrecke (Günstigerer KM-Preis)

print(f"Fahrpreis für {km} km: {cost} Euro")


# Eine Liste mit den Fahrpreisen der letzten Kunden
income = [8.5, 12.0, 5.0, 22.4]

# Zugriff auf ein Element (Zählung beginnt bei 0!)
print(f"Erste fahrt: {income}")

# Ein neues Element am Ende hinzufügen 
income.append(15.3)
print(f"Alle Einnahmen: {income}")
