import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
print(df.to_string())

print("Best seller")
best_seller = df[df['units_sold'] == max(df['units_sold'].to_list())]
print(best_seller.to_string())

a = set(df['product_name'].to_list())
items_sold = []
print(a)
for item in a:
    result = df.loc[df['product_name'] == item, 'units_sold']
    items_sold.append(sum(result))
b = dict(zip(a, items_sold))
print(b)

for k, v in b.items():
    if max(b.values()) == b[k]:
        print(f"Best seller: {k} with {v} units sold")
