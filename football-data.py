import pandas as pd
import matplotlib.pyplot as plt

path = input("CSV path: ")
df = pd.read_csv(path)
print("1. Show CSV\n2. Statistical Analysis\n3. Charts\n4. Simulate remaining matches\n5. Exit")
df['Goals_For'] = df['Goals_For'].astype('Int64')
df['Goals_Against'] = df['Goals_Against'].astype('Int64')
while True:
    choice = input("Select option (input number):")
    if choice == '1':
        print(df.to_string())
    elif choice == '2':

    elif choice == '3':
        chart = input("a. Results\nb. Cumulative goal difference\nc. Home vs Away performance\nd. Season form guide\ne. Best win streak")
        if chart == 'a':
        elif chart == 'b':
        elif chart == 'c':
        elif chart == 'd':
        elif chart == 'e':
        else:
            print("Chart not available")
    elif choice == '4':

    elif choice == '5':
        break
    else:
        print("Option not available")

results = df['Result (W/L/D)'].tolist()
print(f"Team record [W: {results.count('W')} | L: {results.count('L')} | D: {results.count('D')}]")
print(f"Total points: {results.count('W')*3 + results.count('D')*1}")

scored = df['Goals_For'].sum()
conceded = df['Goals_Against'].sum()
played = df['Result (W/L/D)'].count()
remain = df['Result (W/L/D)'].isna().sum()
print(f"Matches played: {played} | remaining: {remain}")
print(f"Goals scored: {scored} | average: {scored / played}")
print(f"Goals conceded: {conceded} | average: {conceded / played}")
print(f"Goal difference: {scored - conceded}")

a = [results.count('W'), results.count('L'), results.count('D')]
labels = ['W', 'L', 'D']
plt.pie(a, labels=labels)
plt.show()

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
