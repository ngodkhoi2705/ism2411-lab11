# Reflection
# 1. I would use .get() when a missing key is normal, like an optional email or phone field, so the program keeps going with a default. I would use bracket notation when the key must exist, so a KeyError tells me the data is broken. My rule: .get() for optional data, brackets for required.

# 2. This pattern reminds me of a PivotTable or SUMIF in Excel, where you total amounts by category. The Python version is more useful for large datasets because it runs the same way on a million rows, is repeatable, and does not slow down or require manual refreshing.

print("--- Exercise 1: One customer ---")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

print("--- Exercise 2: Update and add ---")
customer["phone"] = "555-5555"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)

print("--- Exercise 3: Safe lookup ---")
print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError as error:
    print("KeyError caught:", error)

print("--- Exercise 4: Iterate ---")
for key, value in customer.items():
    print(f"{key}: {value}")

# Looping without .items() gives only the keys, so I must look up each value myself with customer[key]. .items() gives key and value together.
for key in customer:
    print(key)

print("--- Exercise 5: Lookup table ---")
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15,
}
purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount rate: {discount_rate * 100:.0f}%")
print(f"Final price: ${final_price:.2f}")

print("--- Exercise 6: List of dicts ---")
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
]
for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} off a $300 purchase")

print("--- Exercise 7: Nested catalog ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product_name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product_name} - only {details['stock']} left")

print("--- Exercise 8: Sales by region ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + sale["amount"]

for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")