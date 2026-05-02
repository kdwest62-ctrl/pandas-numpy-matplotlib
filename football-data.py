import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
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
