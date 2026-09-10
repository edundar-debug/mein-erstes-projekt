# 
# Multi-Tarif Taximeter
km = 12

if km <= 3:  
    cost = 5.0  #Short distance frate
elif km <= 10:  
    cost = 5.0 + (km - 3) * 2.0  #Standard rate
else:   
    cost = 19.0 + (km - 10) *1.5  #Long distance rate

print(f"Fare for {km} km: {cost} euros")


# A list of the fares paid by the last customers
income = [8.5, 12.0, 5.0, 22.4]

# Access an element (indexing starts at 0!)
print(f"First drive: {income}")

# Add a new element at the end
income.append(15.3)
print(f"All income: {income}")


trips = [8.5, 12.0, 5.00, 22.40]
total_revenue = 0

# Go through each trip individually
for trip in trips:
     total_revenue = total_revenue + trip

print(f"Daily revenue: {total_revenue} euros")


# Function to calculate fare based on distance
def calculate_fare(km):
    if km <= 3:  
        cost = 5.0  #Short distance rate
    elif km <= 10:  
        cost = 5.0 + (km - 3) * 2.0  #Standard rate
    else:   
        cost = 19.0 + (km - 10) * 1.5  #Long distance rate
    return cost

# Example usage:
fare_1 = calculate_fare(12)
fare_2 = calculate_fare(2)

print(f"Fare 1: {fare_1} euros")
print(f"Fare 2: {fare_2} euros")
