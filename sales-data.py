import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
print(df.to_string())

print("Best seller")
best_seller = df[df['units_sold'] == max(df['units_sold'].to_list())]
print(best_seller.to_string())
