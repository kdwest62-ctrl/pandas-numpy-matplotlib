import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
print(df.to_string())

products = []
for item in df['product_name'].to_list():
    if item not in products:
        products.append(item)

items_sold = []
for item in products:
    result = df.loc[df['product_name'] == item, 'units_sold']
    items_sold.append(sum(result))
b = dict(zip(products, items_sold))
print(b)

for k, v in b.items():
    if max(b.values()) == b[k]:
        print(f"Best seller: {k} with {v} units sold")
    elif min(b.values()) == b[k]:
        print(f"Low seller: {k} with {v} units sold")
