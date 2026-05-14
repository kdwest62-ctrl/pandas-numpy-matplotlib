import pandas as pd
import matplotlib.pyplot as plt

path = input("CSV path: ")
df = pd.read_csv(path)
print("Options")
options = ["1. Statistics",
           "2. Analysis",
           "3. Top 3 Products",
           "4. Customer Segmentation",
           "5. Moving Average",
           "6. Exit"]
for option in options:
    print(option)
while True:
    select = input("Select option (number): ")
    if select == '1':
        pass
    elif select == '2':
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
    elif select == '3':
        pass
    elif select == '4':
        customers = []
        for item in df['customer_id'].to_list():
            if item not in customers:
                customers.append(item)

        products_bought = []
        for customer in customers:
            result = df.loc[df['customer_id'] == customer, 'units_sold']
            products_bought.append(sum(result))
        print(customers)
        print(products_bought)

        plt.bar(customers, products_bought)
        plt.title("Products Sold per Customer")
        plt.xlabel("Customers")
        plt.ylabel("Products Bought")
        plt.tight_layout()
        plt.show()
    elif select == '5':
        pass
    elif select == '6':
        break
    else:
        print("Option not available")
