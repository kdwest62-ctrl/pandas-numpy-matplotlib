import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = input("CSV path: ")
df = pd.read_csv(path)
df['Goals_For'] = df['Goals_For'].astype('Int64')
df['Goals_Against'] = df['Goals_Against'].astype('Int64')
scored = df['Goals_For'].sum()
conceded = df['Goals_Against'].sum()
played = df['Result (W/L/D)'].count()
results = df['Result (W/L/D)'].tolist()
print("Options")
print("1. Show CSV\n2. Statistical Analysis\n3. Charts\n4. Simulate remaining matches\n5. Exit")
while True:
    choice = input("Select option (num): ")
    if choice == '1':
        print(df.to_string())
    elif choice == '2':
        pass
    elif choice == '3':
        print("a. Results\nb. Cumulative goal difference\nc. Home vs Away performance\nd. Season form guide")
        chart = input("Select chart (letter): ")
        if chart == 'a':
            a = [results.count('W'), results.count('L'), results.count('D')]
            labels = ['W', 'L', 'D']
            plt.pie(a, labels=labels)
            plt.show()
        elif chart == 'b':
            x = df['Match_Number'].tolist()
            y1 = np.array(df['Goal_Difference'].tolist())
            y = np.cumsum(y1)
            plt.plot(x, y, color="orange", marker="+")
            plt.title("Cumulative Goal Difference")
            plt.xlabel("Match Number")
            plt.ylabel("Goal Difference")
            plt.show()
        elif chart == 'c':
            home_matches = df[df['Home/Away'] == 'H']
            home_results_list = home_matches['Result (W/L/D)'].tolist()
            away_matches = df[df['Home/Away'] == 'A']
            away_results_list = away_matches['Result (W/L/D)'].tolist()
            fig, (ax1, ax2) = plt.subplots(1, 2)
            ax1.bar(['W', 'L', 'D'],
                    [home_results_list.count('W'), home_results_list.count('L'), home_results_list.count('D')])
            ax1.set_title('First Plot')
            ax2.bar(['W', 'L', 'D'],
                    [away_results_list.count('W'), away_results_list.count('L'), away_results_list.count('D')])
            ax2.set_title('Second Plot')
            plt.ylim(top=max(home_results_list.count('W'), home_results_list.count('L'), home_results_list.count('D')))
            plt.tight_layout()
            plt.show()
        elif chart == 'd':
            y = df['Result (W/L/D)'].tolist()
            x = df['Match_Number'].tolist()
            plt.plot(x, y, color="blue", markersize=10,
                     marker=".", markerfacecolor="cyan")
            plt.title("Form Guide")
            plt.xlabel("Match Number")
            plt.ylabel("Result (W/L/D)")
            plt.gca().invert_yaxis()
            plt.show()
        else:
            print("Chart not available")
    elif choice == '4':
        pass
    elif choice == '5':
        break
    else:
        print("Option not available")
