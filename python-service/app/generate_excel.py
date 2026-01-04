import pandas as pd
import numpy as np
from faker import Faker
import uuid
import random
import os

fake = Faker()

# Liczba wierszy
NUM_ROWS = 2000

# Definicja departamentów i osób odpowiedzialnych
departments = ["Sales", "IT", "HR", "Finance", "Marketing"]
department_person = {
    "Sales": lambda: fake.name(),
    "IT": lambda: "IT Account",
    "HR": lambda: "HR Coordinator",
    "Finance": lambda: "Finance Manager",
    "Marketing": lambda: "Marketing Lead"
}

currencies = ["PLN", "EUR", "USD"]
payment_methods = ["Bank Transfer", "Credit Card", "Cash"]
categories = ["Software", "Consulting", "Support", "Training"]

data = []

for _ in range(NUM_ROWS):
    dept = random.choice(departments)

    # Quantity i UnitPrice zależnie od działu
    if dept == "Sales":
        quantity = random.randint(1, 20)
        unit_price = round(random.uniform(100, 5000), 2)
    else:
        quantity = random.randint(1, 5)
        unit_price = round(random.uniform(50, 1000), 2)

    amount = round(quantity * unit_price, 2)

    row = {
        "TransactionID": str(uuid.uuid4()),
        "TransactionDate": fake.date_between(start_date="-90d", end_date="today"),
        "Department": dept,
        "SalesPerson": department_person[dept](),
        "ClientID": f"C-{random.randint(1000,9999)}",
        "ClientName": fake.company(),
        "Product": fake.bs().title(),
        "Category": random.choice(categories),
        "Quantity": quantity,
        "UnitPrice": unit_price,
        "Amount": amount,
        "Currency": random.choice(currencies),
        "PaymentMethod": random.choice(payment_methods),
        "InvoiceNumber": f"INV-{random.randint(10000,99999)}",
        "Country": fake.country(),
        "Notes": fake.sentence()
    }

    data.append(row)

df = pd.DataFrame(data)

# Absolutna ścieżka do katalogu examples w repo
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
output_dir = os.path.join(repo_root, "examples")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "sales_data.xlsx")

# Zapis do Excel
df.to_excel(output_path, sheet_name="SalesData", index=False)

# Komunikat
print(f"Excel file generated: {output_path}")
