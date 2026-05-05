import pandas as pd
import matplotlib.pyplot as plt

path = input("CSV path: ")
df = pd.read_csv(path)

print("1. Show CSV\n2. Totals\n3. Averages\n4. Simulation\n5. Graphs")
df['Goals_For'] = df['Goals_For'].astype('Int64')
df['Goals_Against'] = df['Goals_Against'].astype('Int64')
print(df.to_string())
print('-'* 8)
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

y = df['Result (W/L/D)'].dropna().tolist()
x = df['Match_Number'].tolist()
while len(x) > len(y):
    del x[-1]
plt.plot(x, y, color="red", markersize=10,
         marker=".", markerfacecolor="pink")
plt.title("Form Guide")
plt.xlabel("Match Number")
plt.ylabel("Result (W/L/D)")
plt.gca().invert_yaxis()
plt.show()
