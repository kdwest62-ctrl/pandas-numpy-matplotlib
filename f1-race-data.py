import pandas as pd
import numpy as np
from pathlib import Path

path = Path(input("CSV path: "))
if 'f1_race_data' in path.name:
    df = pd.read_csv(path)
    print("Options")
    options = ["1. CSV",
               "2. Championship Points Progression",
               "3. Grid Position & Final Position Correlation",
               "4. Tire Degradation per Lap",
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
            column_data = df['round'].tolist()
            rounds = []
            for entry in column_data:
                if entry not in rounds:
                    rounds.append(entry)
            for rd in rounds:
                if column_data.count(rd) > 1:
                    race = df[df['round'] == rd]
                    drivers = race['driver_code'].tolist()
                    laps = race['race_laps'].tolist()
                    laps = laps[0]
                    stints = race['tyre_stints'].tolist()
                    circuit = race['circuit_name'].tolist()
                    circuit = circuit[0]
                    laps_per_stint = list(map(lambda x: laps / x, stints))
                    rounded_stints = list(map(round, laps_per_stint))
                    tyre_deg = list(map(lambda x: 100 / x, rounded_stints))
                    tyre_deg = list(map(lambda x: round(x, 2), tyre_deg))
                    print(f'Round: {rd}')
                    print(f'Circuit: {circuit}')
                    print(f'Race laps: {laps}')
                    data = {'driver_code': [i for i in drivers],
                            'tyre_stints': [i for i in stints],
                            'ave_tyre_deg_per_lap (%)': [i for i in tyre_deg]}
                    deg = pd.DataFrame(data)
                    print(deg.to_string())
                    print('-' * 8)
                elif column_data.count(rd) == 1:
                    driver = df[df['round'] == rd]['driver_code'].values[0]
                    laps = df[df['round'] == rd]['race_laps'].values[0]
                    stints = df[df['round'] == rd]['tyre_stints'].values[0]
                    circuit = df[df['round'] == rd]['circuit_name'].values[0]
                    rounded_stints = round(laps / stints)
                    tyre_deg = 100 / rounded_stints
                    tyre_deg = round(tyre_deg, 2)
                    data = {'round': rd,
                            'circuit_name': circuit,
                            'race_laps': laps,
                            'driver_code': driver,
                            'tyre_stints': stints,
                            'ave_tyre_deg_per_lap (%)': tyre_deg}
                    deg = pd.DataFrame(data)
                    print(deg.to_string())
                    print('-' * 8)
        elif select == '5':
            pass
        elif select == '6':
            pass
        elif select == '7':
            print("Program closed")
            break
        else:
            print("Option unavailable")
else:
    print("Wrong CSV")
