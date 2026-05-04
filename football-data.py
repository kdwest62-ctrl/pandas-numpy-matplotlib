import pandas as pd
import matplotlib.pyplot as plt

path = input("CSV path: ")
df = pd.read_csv(path)
print(df.to_string())
print('-'* 8)
results = df['Result (W/L/D)'].tolist()
win = []
lost = []
draw = []
for result in results:
    if result == 'W':
        win.append(result)
    elif result == 'L':
        lost.append(result)
    elif result == 'D':
        draw.append(result)
print(f"Team record [W: {len(win)} | L: {len(lost)} | D: {len(draw)}]")
print(f"Total points: {(len(win)*3) + (len(draw)*1)}")

scored = df['Goals_For'].sum()
conceded = df['Goals_Against'].sum()
played = df['Result (W/L/D)'].count()
remain = df['Result (W/L/D)'].isna().sum()
print(f"Matches played: {played} | remaining: {remain}")
print(f"Goals scored: {int(scored)} | average: {scored / played}")
print(f"Goals conceded: {int(conceded)} | average: {conceded / played}")
print(f"Goal difference: {int(scored - conceded)}")

y = df['Result (W/L/D)'].dropna().tolist()
x = df['Match_Number'].tolist()
while len(x) > len(y):
    del x[-1]
plt.plot(x, y)
plt.title("Form Guide")
plt.xlabel("Match Number")
plt.ylabel("Result (W/L/D)")
plt.gca().invert_yaxis()
plt.show()
