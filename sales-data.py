import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

path = Path(input("CSV path: "))
if 'sales_data' in path.name:
    df = pd.read_csv(path)
    print("Options")
    options = ["1. CSV",
               "2. Units Sold + Sales",
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
            print("a. Region | b. Product | c. Category")
            choice = input("Choose stat (letter): ")
            if choice == 'a':
                column_data = df['region'].tolist()
                regions = []
                for entry in column_data:
                    if entry not in regions:
                        regions.append(entry)
                sales = []
                units_sold = []
                for region in regions:
                    if column_data.count(region) > 1:
                        reg = df[df['region'] == region]
                        units = reg['units_sold'].tolist()
                        units_sold.append(sum(units))
                        sale = reg['sales'].tolist()
                        sales.append(round(sum(sale), 2))
                    elif column_data.count(region) == 1:
                        units = df[df['region'] == region]['units_sold'].values[0]
                        units_sold.append(units)
                        sale = df[df['region'] == region]['sales'].values[0]
                        sales.append(sale)
                data = {'region': [i for i in regions], 'units_sold': [i for i in units_sold],
                        'sales': [i for i in sales]}
                region_analysis = pd.DataFrame(data)
                print(region_analysis.to_string())
            elif choice == 'b':
                column_data = df['product_name'].tolist()
                products = []
                for item in column_data:
                    if item not in products:
                        products.append(item)
                sales = []
                units_sold = []
                for product in products:
                    if column_data.count(product) > 1:
                        prod = df[df['product_name'] == product]
                        units = prod['units_sold'].tolist()
                        units_sold.append(sum(units))
                        sale = prod['sales'].tolist()
                        sales.append(round(sum(sale), 2))
                    elif column_data.count(product) == 1:
                        units = df[df['product_name'] == product]['units_sold'].values[0]
                        units_sold.append(units)
                        sale = df[df['product_name'] == product]['sales'].values[0]
                        sales.append(sale)
                data = {'product_name': [i for i in products], 'units_sold': [i for i in units_sold],
                        'sales': [i for i in sales]}
                pr = pd.DataFrame(data)
                print(pr.to_string())
            elif choice == 'c':
                column_data = df['category'].tolist()
                categories = []
                for entry in column_data:
                    if entry not in categories:
                        categories.append(entry)
                sales = []
                units_sold = []
                for category in categories:
                    if column_data.count(category) > 1:
                        cat = df[df['category'] == category]
                        units = cat['units_sold'].tolist()
                        units_sold.append(sum(units))
                        sale = cat['sales'].tolist()
                        sales.append(round(sum(sale), 2))
                    elif column_data.count(category) == 1:
                        units = df[df['category'] == category]['units_sold'].values[0]
                        units_sold.append(units)
                        sale = df[df['category'] == category]['sales'].values[0]
                        sales.append(sale)
                data = {'category': [i for i in categories], 'units_sold': [i for i in units_sold],
                        'sales': [i for i in sales]}
                cat_analysis = pd.DataFrame(data)
                print(cat_analysis.to_string())
            else:
                print("Choice not available")
        elif select == '3':
            column_data = df['product_name'].tolist()
            products = []
            for entry in column_data:
                if entry not in products:
                    products.append(entry)
            sales = []
            units_sold = []
            for product in products:
                if column_data.count(product) > 1:
                    prod = df[df['product_name'] == product]
                    units = prod['units_sold'].tolist()
                    units_sold.append(sum(units))
                    sale = prod['sales'].tolist()
                    sales.append(round(sum(sale), 2))
                elif column_data.count(product) == 1:
                    units = df[df['product_name'] == product]['units_sold'].values[0]
                    units_sold.append(units)
                    sale = df[df['product_name'] == product]['sales'].values[0]
                    sales.append(sale)

            units_sold_ref = dict(zip(products, units_sold))
            units_sold_ref = dict(sorted(units_sold_ref.items(), key=lambda i: i[1], reverse=True))
            top_3_units_sold = dict(list(units_sold_ref.items())[:3])

            sales_ref = dict(zip(products, sales))
            sales_ref = dict(sorted(sales_ref.items(), key=lambda i: i[1], reverse=True))
            top_3_sales = dict(list(sales_ref.items())[:3])

            fig, axs = plt.subplots(1, 2, figsize=(10, 4))

            axs[0].bar([k for k in top_3_units_sold.keys()], [v for v in top_3_units_sold.values()])
            axs[0].set_title("Top 3")
            axs[0].set_xlabel("Products")
            axs[0].set_ylabel("Units Sold")

            axs[1].bar([k for k in top_3_sales.keys()], [v for v in top_3_sales.values()], color="orange")
            axs[1].set_title("Top 3")
            axs[1].set_xlabel("Products")
            axs[1].set_ylabel("Sales")

            plt.tight_layout()
            plt.show()
        elif select == '4':
            print("a. Region | b. Product | c. Category")
            choice = input("Choose stat (letter): ")
            if choice == 'a':
                column_data = df['region'].tolist()
                regions = []
                for entry in column_data:
                    if entry not in regions:
                        regions.append(entry)
                for region in regions:
                    if column_data.count(region) > 1:
                        reg = df[df['region'] == region]
                        customers = reg['customer_id'].tolist()
                        customers = set(customers)
                        print(f"Region: {region} | Customers: {customers}")
                    elif column_data.count(region) == 1:
                        customer = df[df['region'] == region]['customer_id'].values[0]
                        print(f"Region: {region} | Customer: {customer}")
            elif choice == 'b':
                column_data = df['product_name'].tolist()
                products = []
                for entry in column_data:
                    if entry not in products:
                        products.append(entry)
                for product in products:
                    if column_data.count(product) > 1:
                        prod = df[df['product_name'] == product]
                        customers = prod['customer_id'].tolist()
                        customers = set(customers)
                        print(f"Product: {product} | Customers: {customers}")
                    elif column_data.count(product) == 1:
                        customer = df[df['product_name'] == product]['customer_id'].values[0]
                        print(f"Product: {product} | Customer: {customer}")
            elif choice == 'c':
                column_data = df['category'].tolist()
                categories = []
                for entry in column_data:
                    if entry not in categories:
                        categories.append(entry)
                for category in categories:
                    if column_data.count(category) > 1:
                        cat = df[df['category'] == category]
                        customers = cat['customer_id'].tolist()
                        customers = set(customers)
                        print(f"Category: {category} | Customers: {customers}")
                    elif column_data.count(category) == 1:
                        customer = df[df['category'] == category]['customer_id'].values[0]
                        print(f"Category: {category} | Customer: {customer}")
            else:
                print("Choice not available")
        elif select == '5':
            def moving_average(d, window_size):
                weights = np.ones(window_size) / window_size
                return np.convolve(d, weights, mode='valid')
            column_data = df['units_sold'].tolist()
            print(f"Units sold (per transaction): {column_data}")
            data = np.array(column_data)
            try:
                window = int(input("Window size: "))
            except ValueError:
                print("Error! Input a number")
            else:
                print(moving_average(data, window))
        elif select == '6':
            print("Program closed")
            break
        else:
            print("Option not available")
else:
    print("Wrong CSV")
