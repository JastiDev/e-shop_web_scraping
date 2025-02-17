import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ebay_products.csv")


df["Price"] = df["Price"].replace('[^\d]', '', regex=True).astype(float)

print("Data Overview")
print(df.describe())

plt.figure(figsize=(10, 5))
plt.hist(df["Price"], bins=20, color='blue', edgecolor='black', alpha=0.7)
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.title("Price Overview")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
