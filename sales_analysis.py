import pandas as pd
data = {"prodoct": ["Laptop", "Mouse", "Keyboard", "Laptop", "Mouse"], "Sales": [50000, 2000, 3000, 60000,2500]}
df = pd.DataFrame(data)
total_sales = df["Sales"].sum()
print("Total Sales:",total_sales)