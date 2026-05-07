import pandas as pd
import matplotlib.pyplot as plt

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
        print(f"Team record [W: {results.count('W')} | L: {results.count('L')} | D: {results.count('D')}]")
        print(f"Total points: {results.count('W') * 3 + results.count('D') * 1}")
        print(f"Matches played: {played} | remaining: {38 - played}")
        print(f"Goals scored: {scored} | average: {scored / played}")
        print(f"Goals conceded: {conceded} | average: {conceded / played}")
        print(f"Goal difference: {scored - conceded}")
    elif choice == '3':
        print("a. Results\nb. Cumulative goal difference\nc. Home vs Away performance\nd. Season form guide\ne. Best win streak")
        chart = input("Select chart (num): ")
        if chart == 'a':
            a = [results.count('W'), results.count('L'), results.count('D')]
            labels = ['W', 'L', 'D']
            plt.pie(a, labels=labels)
            plt.show()
        elif chart == 'b':
            pass
        elif chart == 'c':
            pass
        elif chart == 'd':
            y = df['Result (W/L/D)'].dropna().tolist()
            x = df['Match_Number'].tolist()
            while len(x) > len(y):
                del x[-1]
            plt.plot(x, y, color="blue", markersize=10,
                     marker=".", markerfacecolor="cyan")
            plt.title("Form Guide")
            plt.xlabel("Match Number")
            plt.ylabel("Result (W/L/D)")
            plt.gca().invert_yaxis()
            plt.show()
        elif chart == 'e':
            pass
        else:
            print("Chart not available")
    elif choice == '4':
        pass
    elif choice == '5':
        break
    else:
        print("Option not available")
