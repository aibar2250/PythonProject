
# Task B1 — Trip Category (if / elif / else)
driver=input("Enter driver name:")
destination=input("Enter destination:")
distance=float(input("Enter distance (km):"))
consumption=float(input("Enter fuel consumption (L/100km):"))
price=float(input("Enter fuel price (KZT/L):"))

fuel_cost=(distance/100) * consumption *price

if distance < 100:
    category="Short trip"
elif distance <500:
    category="Medium trip"
else:
    category="Long trip"


print("=========================")
print("driver:",driver)
print("destination:",destination.upper())
print("distance:",distance,"km")
print("fuel cost:",fuel_cost,"KZT")
print("category:",category)
print("=========================")


# Task B2 — Cost Breakdown (for loop)
print("cost breakdown:")
for km in range(100,int(distance),100):
    cost=(km/100) * consumption * price
    print(km, "km",cost,"KZT")

# Task B3 — Destination Analysis (strings)
print("destination uppercase:",destination.upper())
print("destination lowercase:",destination.lower())
print("Length:",len(destination))
print("letter 'a' count",destination.lower().count("a"))


