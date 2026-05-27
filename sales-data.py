import pandas as pd
import numpy as np

path = input("CSV path: ")
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
        print("a. Product\nb. Category\nc. Region")
        choice = input("Choose stat (letter): ")
        if choice == 'a':
            column_data = df['product_name'].tolist()
            products = []
            for item in column_data:
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
            pr = pd.DataFrame(data)
            print(pr.to_string())
        elif choice == 'b':
            pass
        elif choice == 'c':
            pass
        else:
            print("Choice not available")
    elif select == '3':
        pass
    elif select == '4':
        print("a. Region\nb. Product\nc. Category")
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
            pass
        elif choice == 'c':
            pass
        else:
            print("Choice not available")
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
        print("Program closed")
        break
    else:
        print("Option not available")
