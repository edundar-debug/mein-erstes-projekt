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
