import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
        print(df.to_string())
    elif select == '2':
        data = df['product_name'].tolist()
        products = []
        for item in data:
            if item not in products:
                products.append(item)
        sales = []
        units_sold = []
        for item in products:
            product = df[df['product_name'] == item]
            units = product['units_sold'].tolist()
            units_sold.append(sum(units))
            sale = product['sales'].tolist()
            sales.append(round(sum(sale), 2))
        data = {'product_name': [i for i in products], 'units_sold': [i for i in units_sold],
                'sales': [i for i in sales]}
        df = pd.DataFrame(data)
        print(df.to_string())
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
        plt.ylabel("Products Sold")
        plt.tight_layout()
        plt.show()
    elif select == '5':
        def moving_average(d, window_size):
            weights = np.ones(window_size) / window_size
            return np.convolve(d, weights, mode='valid')
        column_data = df['units_sold'].tolist()
        print(f"Units sold (per transaction): {column_data}")
        data = np.array(column_data)
        window = int(input("Window size: "))
        print(moving_average(data, window))
    elif select == '6':
        break
    else:
        print("Option not available")
