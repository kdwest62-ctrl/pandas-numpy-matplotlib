import pandas as pd
import numpy as np

path = input("CSV path: ")
df = pd.read_csv(path)
print("Options")
options = ["1. Statistics",
           "2. Championship Points Progression",
           "3. Grid Position & Final Position Correlation",
           "4. Tire Degradation Curves",
           "5. Weather Impact Analysis",
           "6. Performance Comparison Between Teammates",
           "7. Exit"]
for option in options:
    print(option)

drivers = []
driver_list = df['driver_code'].tolist()
for item in driver_list:
    if item not in drivers:
        drivers.append(item)
while True:
    select = input("Select option (number): ")
    if select == '1':
        print(df.to_string())
    elif select == '2':
        for driver in drivers:
            driver_column = df[df['driver_code'] == driver]
            driver_points = driver_column['points_awarded'].tolist()
            cum_points = np.cumsum(np.array(driver_points))
            print(f"{driver} | {cum_points}")
    elif select == '3':
        for driver in drivers:
            driver_column = df[df['driver_code'] == driver]
            grid_pos = driver_column['starting_grid_position'].tolist()
            final_pos = driver_column['final_position'].tolist()
            print(driver)
            print(f"Grid positions: {grid_pos}")
            print(f"Final positions: {final_pos}")
            correlation = np.corrcoef(grid_pos, final_pos)
            print(correlation)
            print('-' * 8)
    elif select == '4':
        pass
    elif select == '5':
        pass
    elif select == '6':
        pass
    elif select == '7':
        break
    else:
        print("Option unavailable")
